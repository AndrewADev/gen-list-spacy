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

Navigate to the project directory and then run these commands:

```shell
pipenv shell
pipenv install
```

Now you should be able to run the script from within a `pipenv shell`. Note that you will need to restart the `pipenv shell` if you restart your machine, but will only need to run `install` if the packages have been updated.

# Running 

1. Perform setup as above
2. Activate the environment you'll be using, if not already (e.g. `pipenv shell`)
3. Create a local folder called `data` (`mkdir data` from repo root)
4. Paste text you would like to parse for into a text file, `data/article.txt`
5. Run the script (`python gen_list > data/output.txt`). Note that you can omit the redirection of output, if you'd like to preview the results instead.

In general, the repo is currently set up to ignore files in `./data`, so that is an easy option for output files.

If you would like to use a different input path for the data file, you can do so by calling:

```shell
python gen_list --input='/path/to/your/text/file'
```

If you would like to specify an alternate output type (currently, the only additional option is CSV), you can do so by calling:
```shell
python gen_list --output-type=csv
```

Note that you can see all available options by calling:
```shell
python gen_list --help
```
