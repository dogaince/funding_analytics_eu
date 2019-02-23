import re

from gensim.models.phrases import Phrases, Phraser


def remove_markup(text):
    tags = [
        '<b>', '<p>', '&nbsp;', '<li>', '<ol>', '<ul>', '<br>',
        '</b>', '</p>', '</li>', '</ol>', '</ul>', '</br>',
        '\n', '\t', '\r'
    ]
    for tag in tags:
        text = text.replace(tag, ' ')
    return text

def normalise_digits(text):
    text = re.sub("\d+", "XXX", text)
    return text

def lemmatize(docs, nlp):
    
    tokenized_docs = []
    for doc in docs:
        doc = nlp(doc)
        tokenized_doc = []
        for t in doc:
            if len(t) < 3:
                continue
            if t.is_stop:
                continue
            if t.like_num:
                continue
            if t.is_digit:
                continue
            if t.is_punct:
                continue
            if t.like_url:
                continue
            pos = t.pos_.upper()
            token = t.lemma_
            tokenized_doc.append(f'{token}{pos}')
        tokenized_docs.append(tokenized_doc)
    return tokenized_docs

def bigram(docs, delimiter=b'x', phraser=None):
    if phraser is not None:
        abstracts_bigrammed = phraser[docs]
        return abstracts_bigrammed
    else:
        bigrams = Phrases(docs, delimiter=delimiter)
        bigrammer = Phraser(bigrams)
        abstracts_bigrammed = bigrammer[docs]
        return abstracts_bigrammed, bigrammer

def stringify_docs(docs):
    for doc in docs:
        yield ' '.join(doc)
