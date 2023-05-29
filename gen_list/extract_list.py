import spacy
import click

file_path = './data/article.txt'


@click.command()
@click.option('--input', default=file_path, help='Path to (plaintext) file to read from')
def output_list(input):
    nlp = spacy.load("de_core_news_lg")
    with open(input, 'r', encoding='utf-8') as file:
        doc = nlp(file.read())
        for token in doc:
            if (token.pos_ == "NOUN" or token.pos_ == "VERB"):
                # TODO: Add option for verbose/debug
                # print(token.text, token.pos_)
                print(token.text, end=', ')

