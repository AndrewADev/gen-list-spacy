# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Setup

This project uses `pipenv` for dependency management with Python 3.13:

```bash
pipenv shell
pipenv install
```

For development dependencies (includes pytest):
```bash
pipenv install --dev
```

## Running the Application

The main application extracts nouns and verbs from German text files using SpaCy:

```bash
python gen_list                              # Uses default input: ./data/article.txt
python gen_list --input=/path/to/file.txt    # Custom input file
python gen_list --output-type=csv            # CSV output format
python gen_list --help                       # See all options
```

## Testing

Run tests with pytest:
```bash
pytest                    # Run all tests
pytest tests/test_extract_list.py  # Run specific test file
```

## Architecture

- **gen_list/extract_list.py**: Core functionality for text processing using SpaCy's German language model (`de_core_news_lg`)
- **gen_list/__main__.py**: Entry point that calls the main `generate_list()` function
- Uses Click for CLI argument parsing
- Filters tokens to extract only nouns and verbs based on part-of-speech tagging
- Supports both token-list and CSV output formats

The application loads a German SpaCy model and processes text files to extract vocabulary for language learning purposes.