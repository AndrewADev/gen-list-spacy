# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Setup

This project uses `uv` for dependency management with Python 3.13:

```bash
uv sync --all-extras # Install all dependencies including dev dependencies
```

After installing dependencies, download the German SpaCy language model:
```bash
uv pip install pip  # Required for spacy download command
uv run python -m spacy download de_core_news_lg
```

**Note:** If you encounter 403 errors downloading the model from GitHub, you can try:
1. Download manually from [SpaCy models releases](https://github.com/explosion/spacy-models/releases) and install with `uv pip install <path-to-whl>`
2. Or use `pip install https://github.com/explosion/spacy-models/releases/download/de_core_news_lg-3.8.0/de_core_news_lg-3.8.0-py3-none-any.whl` directly (may require GitHub authentication in some environments)

To run commands in the uv environment:
```bash
uv run <command>     # Run a command in the virtual environment
```

## Running the Application

The main application extracts nouns and verbs from German text files using SpaCy:

```bash
uv run gen_list                              # Uses default input: ./data/article.txt
uv run gen_list --input=/path/to/file.txt    # Custom input file
uv run gen_list --output-type=csv            # CSV output format
uv run gen_list --help                       # See all options
```

## Testing

Run tests with pytest:
```bash
uv run pytest                    # Run all tests
uv run pytest tests/test_extract_list.py  # Run specific test file
```

## Architecture

- **gen_list/extract_list.py**: Core functionality for text processing using SpaCy's German language model (`de_core_news_lg`)
- **gen_list/__main__.py**: Entry point that calls the main `generate_list()` function
- Uses Click for CLI argument parsing
- Filters tokens to extract only nouns and verbs based on part-of-speech tagging
- Supports both token-list and CSV output formats

The application loads a German SpaCy model and processes text files to extract vocabulary for language learning purposes.