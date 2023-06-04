import spacy
import click

file_path = './data/article.txt'

nlp = spacy.load("de_core_news_lg")

@click.command()
@click.option('--input', default=file_path, help='Path to (plaintext) file to read from')
@click.option('--output-type', type=click.Choice(['token-list', 'csv']), help='Type of output to be generated', default='token-list')
def generate_list(input, output_type):
    with open(input, 'r', encoding='utf-8') as file:
        tokens = tokenize_file(file)
        if output_type == 'token-list':
            output_list(tokens)
        elif output_type == 'csv':
            output_csv(tokens)


def output_list(tokens):
    for token in tokens:
        # TODO: Add option for verbose/debug
        # print(token.text, token.pos_)
        print(token.text, end=', ')

def output_csv(tokens):
    print('Token', end='\r\n')
    for token in tokens:
        print(token.text, end='\r\n')


def tokenize_file(file):
    doc = nlp(file.read())
    tokens = [ token for token in doc if token.pos_ == "NOUN" or token.pos_ == "VERB" ]
    return tokens
