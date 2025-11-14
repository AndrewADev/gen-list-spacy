# Summary

Extracts nouns & verbs from a text file via SpaCy (e.g. mining it for vocabulary) and then prints them to stdout.

# Initial setup

For all methods, you must first check out or download the code.

## Via `uv`

### Install `uv` (if not installed)

For the script to run, you will need to setup an environment with the dependencies. The current recommended method is using `uv`, which provides fast, reliable package installation and management:

1. Install `uv` following the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/)
2. Make sure you have Python 3.13 installed on your system

### Install the packages

Navigate to the project directory and then run:

```shell
uv sync --all-extras
```

This will create a virtual environment and install all dependencies.

### Install the SpaCy language model

After installing dependencies, download the German SpaCy language model:

```shell
uv pip install pip  # Required for spacy download command
uv run python -m spacy download de_core_news_lg
```

**Note:** If you encounter 403 errors downloading the model from GitHub, you can try downloading it manually from [SpaCy models releases](https://github.com/explosion/spacy-models/releases) and install with `uv pip install <path-to-whl>`.

# Running

1. Perform setup as above
2. Create a local folder called `data` (`mkdir data` from repo root)
3. Paste text you would like to parse for into a text file, `data/article.txt`
4. Run the script (`uv run gen_list > data/output.txt`). Note that you can omit the redirection of output, if you'd like to preview the results instead.

In general, the repo is currently set up to ignore files in `./data`, so that is an easy option for output files.

If you would like to use a different input path for the data file, you can do so by calling:

```shell
uv run gen_list --input='/path/to/your/text/file'
```

If you would like to specify an alternate output type (currently, the only additional option is CSV), you can do so by calling:
```shell
uv run gen_list --output-type=csv
```

Note that you can see all available options by calling:
```shell
uv run gen_list --help
```
