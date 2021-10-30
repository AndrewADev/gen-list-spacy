import spacy

nlp = spacy.load("de_core_news_lg")
with open('./data/article.txt', 'r', encoding='utf-8') as file:
    doc = nlp(file.read())
    for token in doc:
        if (token.pos_ == "NOUN" or token.pos_ == "VERB"):
            # TODO: Add option for verbose/debug
            # print(token.text, token.pos_)
            print(token.text, end=', ')