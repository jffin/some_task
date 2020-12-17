from text_api.extensions import celery

from text_api.commons.sentences_finder import SentenceEmbedding


@celery.task()
def find_sentences_task(sentence, text_slug):
    return SentenceEmbedding.run(sentence, text_slug)
