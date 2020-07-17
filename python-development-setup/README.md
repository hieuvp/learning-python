# Python Development Setup

Composable set of tools, each tool solving one problem.
I highly recommend this setup for two main reasons.

It is composable. You can start from plain `requirements.txt`
and add tools as you decide to solve other problems from the table above;
It is based on pip, which is installed everywhere and is the standard for installing packages.

`pip` and `virtualenv` are standard tools.

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [`pyenv`](#pyenv)
- [`venv`](#venv)
- [`virtualenvwrapper`](#virtualenvwrapper)
- [PyPI](#pypi)
- [`requirements.txt`](#requirementstxt)
- [`pip`](#pip)
- [`setup.py`](#setuppy)
- [`tox.ini`](#toxini)
- [`pip-tools`](#pip-tools)
- [`pipenv`](#pipenv)
- [`poetry`](#poetry)
- [pypa](#pypa)
- [anaconda](#anaconda)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## `pyenv`

Although not required,
the `pyenv` wiki recommends installing some additional libraries.

```shell script
brew install sqlite3 zlib
```

## `venv`

```shell script
which python && which pip
unalias python && unalias pip
which python && which pip
virtualenv venv
source venv/bin/activate
which python && which pip
pip install --requirement requirements.txt
pip install -r requirements.txt
pip list
```

- virtualenv vs. venv

## `virtualenvwrapper`

## PyPI

how to pronounce PyPI (beginner) anthony explains #020
<https://www.youtube.com/watch?v=I5OUzCAYst8>
<http://www.howtopronounce.cc/pypi>

## `requirements.txt`

- For Application
- Dependency Management

## `pip`

```shell script
pip list
```

```shell script
pip freeze
pip freeze > requirements.txt
```

## `setup.py`

For Library (e.g. flask)

## `tox.ini`

```shell script
tox
```

## `pip-tools`

<https://github.com/jazzband/pip-tools> => install?

## `pipenv`

The future is uncertain
More popular

Pipfile
Pipfile.lock

## `poetry`

The future is uncertain
better UI, supports packaging

poetry.lock

## pypa

- <https://www.pypa.io/en/latest/>

## anaconda

- <https://www.anaconda.com/>  
  => Data Science

## References

- [My Simple Python Development Setup](https://medium.com/better-programming/my-simple-python-development-setup-687c31898d5b)
- [python-virtual-env](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env)
- [venv](https://docs.python.org/3/tutorial/venv.html)
- [installing-using-pip-and-virtual-environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments)
