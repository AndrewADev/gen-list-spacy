# Summary

Extracts nouns & verbs from a text file via SpaCy (e.g. mining it for vocabulary) and then prints them to stdout.

# Initial setup

For all methods, you must first check out or download the code.

## Via `pipenv`

### Install `pipenv` (if not installed)

For the script to run, you will need to setup an environment with the dependencies. The current recommended method is using `pipenv`, which helps manage the details of the virtual envionment, and provides deterministic builds via a lockfile (while requiring a specific python version):

1. Make sure you have both `python` (3.10) as well as `pip` installed on your system
2. Run `pip install pipenv --user`

See the `pipenv` [docs for details](https://pipenv.pypa.io/en/latest/installation/#pipenv-installation)

### Install the packages

Navigate to the Run these steps:
```shell
pipenv shell
pipenv install
```

Now you should be able to run the script from within a `pipenv shell`. Note that you will need to restart the `pipenv shell` if you restart your machine, but will only need to run `install` if the packages have been updated.

## Via `pip` and virtual environment (legacy)

Previous recomendation (no longer supported, may be removed)

1. Activate the virtual env (per your OS & shell/terminal emulator)
2. `pip install -r requirements.txt`

# Running 

1. Perform setup as above
2. Activate the environment you'll be using, if not already (e.g. `pipenv shell`)
3. Create a local folder called `data` (`mkdir data` from repo root)
4. Paste text you would like to parse for into a text file, `data/article.txt`
5. Run the script (`python ./extract-list.py > data/output.txt`). Note that you can omit the redirection of output, if you'd like to preview the results instead.

In general, the repo is currently set up to ignore files in `./data`, so that is an easy option for output files.
