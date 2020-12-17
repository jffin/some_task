from typing import List, Dict

import nltk
import scipy
from sentence_transformers import SentenceTransformer

from text_api.models import Text


class SentenceEmbedding:
    top_amount_results: int = 20

    def __init__(self, sentence: str, slug: str):
        # sentence to compare with
        self.sentence: str = sentence
        # slug of sentence text
        self.slug: str = slug
        self.texts: List[Text] = self._get_texts()
        # Sentence Embedding used with SentenceBERT model
        self.model: SentenceTransformer = SentenceTransformer('bert-base-nli-mean-tokens')
        self.results: List[Dict[str, str]] = []

    @classmethod
    def run(cls, sentence: str, slug: str) -> List[Dict[str, str]]:
        # starting point
        obj = cls(sentence, slug)
        obj.search()
        obj.sort_results()

        return obj.results

    def _get_texts(self) -> List[Text]:
        # find all texts except current
        return Text.query.filter(Text.slug != self.slug).all()

    @staticmethod
    def _convert_text_sentences(text: str) -> List[str]:
        # convert text to sentences
        return nltk.tokenize.sent_tokenize(text)

    def search(self) -> None:
        # define search query and embed into vector
        query = self.model.encode(self.sentence)
        # iterate through texts
        for text in self.texts:
            self._calculate_text_result(text, query)

    def _calculate_text_result(self, text: Text, query: List):
        # create vector from sentence we try to compare with needed
        corpus = self._convert_text_sentences(text.content)
        corpus_embeddings = self.model.encode(corpus)
        # compute the cosine similarity with scipy
        distances = scipy.spatial.distance.cdist([query], corpus_embeddings, 'cosine')[0]

        # merge distances with ids and sort
        results = zip(range(len(distances)), distances)
        results = sorted(results, key=lambda x: x[1])

        # create result's dictionary with top distance
        for idx, distance in results[:self.top_amount_results]:
            self.results.append({
                'sentence': corpus[idx].strip(),
                'distance': 1 - distance,
                'slug': text.slug,
            })

    def sort_results(self) -> None:
        # sort reverse results
        self.results = sorted(self.results, key=lambda r: r['distance'], reverse=True)
