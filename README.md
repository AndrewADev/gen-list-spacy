# Summary

Extracts nouns & verbs from a text file via SpaCy and then prints them to stdout.

# Running

1. Activate the virtual env (per your OS & shell/terminal emulator)
2. `pip install -r requirements.txt`
3. Create a local folder called `data` (`mkdir data` from repo root)
4. Paste text into a text file, `data/article.txt`
5. Run the script (`python ./extract-list.py > data/output.txt`). Note that you can omit the redirection of output, if you'd like to preview the results instead.

In general, the repo is currently set up to ignore files in `./data`, so that is an easy option for output files.
