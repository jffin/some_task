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
        self.texts: List[Text] = self.get_texts()
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

    def get_texts(self) -> List[Text]:
        # find all texts except current
        return Text.query.filter(Text.slug != self.slug).all()

    @staticmethod
    def convert_text_sentences(text: str) -> List[str]:
        # convert text to sentences
        return nltk.tokenize.sent_tokenize(text)

    def search(self) -> None:
        # query is
        query = self.model.encode(self.sentence)
        for text in self.texts:
            self.calculate_text_result(text, query)

    def calculate_text_result(self, text: Text, query: List):
        corpus = self.convert_text_sentences(text.content)
        corpus_embeddings = self.model.encode(corpus)
        distances = scipy.spatial.distance.cdist([query], corpus_embeddings, 'cosine')[0]
        results = zip(range(len(distances)), distances)
        results = sorted(results, key=lambda x: x[1])
        for idx, distance in results[:self.top_amount_results]:
            self.results.append({
                'sentence': corpus[idx].strip(),
                'distance': 1 - distance,
                'slug': text.slug,
            })

    def sort_results(self) -> None:
        self.results = sorted(self.results, key=lambda r: r['distance'], reverse=True)
