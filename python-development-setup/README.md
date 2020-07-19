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
- [`requirements.txt`](#requirementstxt)
- [`venv`](#venv)
- [`virtualenvwrapper`](#virtualenvwrapper)
- [PyPI](#pypi)
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

> Simple Python version management.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=pyenv.console) -->
<!-- The below code snippet is automatically added from pyenv.console -->

```console
+ pyenv versions
* system (set by /Users/hieu.van/.pyenv/version)
+ python --version
Python 2.7.16
```

<!-- AUTO-GENERATED-CONTENT:END -->

## `requirements.txt`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=requirements.txt) -->
<!-- The below code snippet is automatically added from requirements.txt -->

```txt
pylint==2.5.3
```

<!-- The below code snippet is automatically added from pyenv.console -->
<!-- AUTO-GENERATED-CONTENT:END -->

- For Application
- Dependency Management

## `venv`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=virtualenv.console) -->
<!-- The below code snippet is automatically added from virtualenv.console -->

```console
+ type python
python is /usr/bin/python
+ type pip
./virtualenv.sh: line 7: type: pip: not found
+ true
+ rm -rf venv
+ virtualenv venv
created virtual environment CPython3.8.3.final.0-64 in 426ms
  creator CPython3Posix(dest=/Users/hieu.van/Desktop/Workspace/Experiment/learning-python/python-development-setup/venv, clear=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/hieu.van/Library/Application Support/virtualenv)
    added seed packages: pip==20.1.1, setuptools==47.3.1, wheel==0.34.2
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
+ set +x
+ source venv/bin/activate
+ type python
python is /Users/hieu.van/Desktop/Workspace/Experiment/learning-python/python-development-setup/venv/bin/python
+ type pip
pip is /Users/hieu.van/Desktop/Workspace/Experiment/learning-python/python-development-setup/venv/bin/pip
+ pip list
Package    Version
---------- -------
pip        20.1.1
setuptools 47.3.1
wheel      0.34.2
+ pip install --requirement requirements.txt
Collecting pylint==2.5.3
  Using cached pylint-2.5.3-py3-none-any.whl (324 kB)
Collecting isort<5,>=4.2.5
  Using cached isort-4.3.21-py2.py3-none-any.whl (42 kB)
Collecting mccabe<0.7,>=0.6
  Using cached mccabe-0.6.1-py2.py3-none-any.whl (8.6 kB)
Collecting toml>=0.7.1
  Using cached toml-0.10.1-py2.py3-none-any.whl (19 kB)
Collecting astroid<=2.5,>=2.4.0
  Using cached astroid-2.4.2-py3-none-any.whl (213 kB)
Processing /Users/hieu.van/Library/Caches/pip/wheels/d7/f7/3b/6853df4a25a106662f20e70ad6bd448c8ae07d12ce80fb9063/lazy_object_proxy-1.4.3-cp38-cp38-macosx_10_15_x86_64.whl
Collecting six~=1.12
  Using cached six-1.15.0-py2.py3-none-any.whl (10 kB)
Processing /Users/hieu.van/Library/Caches/pip/wheels/5f/fd/9e/b6cf5890494cb8ef0b5eaff72e5d55a70fb56316007d6dfe73/wrapt-1.12.1-cp38-cp38-macosx_10_15_x86_64.whl
Installing collected packages: isort, mccabe, toml, lazy-object-proxy, six, wrapt, astroid, pylint
Successfully installed astroid-2.4.2 isort-4.3.21 lazy-object-proxy-1.4.3 mccabe-0.6.1 pylint-2.5.3 six-1.15.0 toml-0.10.1 wrapt-1.12.1
+ pip list
Package           Version
----------------- -------
astroid           2.4.2
isort             4.3.21
lazy-object-proxy 1.4.3
mccabe            0.6.1
pip               20.1.1
pylint            2.5.3
setuptools        47.3.1
six               1.15.0
toml              0.10.1
wheel             0.34.2
wrapt             1.12.1
+ rm -rf venv
```

<!-- The below code snippet is automatically added from pyenv.console -->
<!-- AUTO-GENERATED-CONTENT:END -->

- virtualenv vs. venv

## `virtualenvwrapper`

## PyPI

how to pronounce PyPI (beginner) anthony explains #020
<https://www.youtube.com/watch?v=I5OUzCAYst8>
<http://www.howtopronounce.cc/pypi>

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
