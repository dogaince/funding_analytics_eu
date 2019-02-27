import re

from gensim.models.phrases import Phrases, Phraser


def remove_markup(text):
#     tags = [
#         '<b>', '<p>', '&nbsp;', '<li>', '<ol>', '<ul>', '<br>',
#         '</b>', '</p>', '</li>', '</ol>', '</ul>', '</br>',
#         '\n', '\t', '\r'
#     ]
    tags = ["a","abbr","acronym","address","area","b","base","bdo","big",
            "blockquote","body","br","button","caption","cite","code","col",
            "colgroup","dd","del","dfn","div","dl","DOCTYPE","dt","em","fieldset",
            "form","h1","h2","h3","h4","h5","h6","head","html","hr","i","img",
            "input","ins","kbd","label","legend","li","link","map","meta",
            "noscript","object","ol","optgroup","option","p","param","pre","q",
            "samp","script","select","small","span","strong","style","sub",
            "sup","table","tbody","td","textarea","tfoot","th","thead",
            "title","tr","tt","ul","var"]
    
    for tag in tags:
        text = text.replace('<{}>'.format(tag), ' ')
        text = text.replace('</{}>'.format(tag), ' ')
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
