# My-Pytest

Basic setup to show how to load modules in tests so we can run `pytest` from either the top level or for a specific test such as when using `test.vim` for an individual test file.

## Installation

You'll probably want to use [virtualenv](https://virtualenv.pypa.io/en/stable/) for package management.

If you haven't already, you can run these commands from the console in any directory:

```
brew install python  # if you want Python 2
brew install python3 # if you want Python 3
pip install virtualenv # this uses Python 2 but it should not matter for either version as you'll see later
```

Then in the project's directory, run:

```
virtualenv -p python3 env # if you want Python 2 for this project
virtualenv -p python3 env # if you want Python 3 for this project
source env/bin/activate # activate virtualenv so you're now working in a clean environment without other Python packages
pip install -r requirements.txt # install Python packages for this project, so make sure this requirements.txt file exsts
```

Every time you want to work on this project you'll need to run `source env/bin/activate`.

To run tests, you can either run all of them:

```
pytest ./test
```

Or you can run an individual test file:

```
pytest ./test/test_core.py
```
