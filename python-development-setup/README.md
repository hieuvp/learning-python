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

- [Standard Tools](#standard-tools)
  - [`$ pyenv`](#-pyenv)
  - [`requirements.txt`](#requirementstxt)
  - [`$ virtualenv`](#-virtualenv)
- [`virtualenvwrapper`](#virtualenvwrapper)
- [PyPI](#pypi)
- [`setup.py`](#setuppy)
- [`tox.ini`](#toxini)
- [`pip-tools`](#pip-tools)
- [`pipenv`](#pipenv)
- [`poetry`](#poetry)
- [pypa](#pypa)
- [anaconda](#anaconda)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Standard Tools

### `$ pyenv`

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

### `requirements.txt`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=requirements.txt) -->
<!-- The below code snippet is automatically added from requirements.txt -->

```txt
pylint==2.5.3
```

<!-- The below code snippet is automatically added from pyenv.console -->
<!-- AUTO-GENERATED-CONTENT:END -->

- For Application
- Dependency Management

### `$ virtualenv`

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
created virtual environment CPython3.8.3.final.0-64 in 441ms
  creator CPython3Posix(dest=/Users/hieu.van/Desktop/Workspace/Experiment/learning-python/python-development-setup/venv, clear=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/hieu.van/Library/Application Support/virtualenv)
    added seed packages: pip==20.1.1, setuptools==47.2.0, wheel==0.34.2
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
setuptools 47.2.0
wheel      0.34.2
+ pip install --requirement requirements.txt
Collecting pylint==2.5.3
  Downloading pylint-2.5.3-py3-none-any.whl (324 kB)
Collecting toml>=0.7.1
  Downloading toml-0.10.1-py2.py3-none-any.whl (19 kB)
Collecting astroid<=2.5,>=2.4.0
  Downloading astroid-2.4.2-py3-none-any.whl (213 kB)
Collecting mccabe<0.7,>=0.6
  Downloading mccabe-0.6.1-py2.py3-none-any.whl (8.6 kB)
Collecting isort<5,>=4.2.5
  Downloading isort-4.3.21-py2.py3-none-any.whl (42 kB)
Collecting six~=1.12
  Downloading six-1.15.0-py2.py3-none-any.whl (10 kB)
Collecting lazy-object-proxy==1.4.*
  Downloading lazy-object-proxy-1.4.3.tar.gz (34 kB)
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
    Preparing wheel metadata: started
    Preparing wheel metadata: finished with status 'done'
Collecting wrapt~=1.11
  Downloading wrapt-1.12.1.tar.gz (27 kB)
Building wheels for collected packages: lazy-object-proxy, wrapt
  Building wheel for lazy-object-proxy (PEP 517): started
  Building wheel for lazy-object-proxy (PEP 517): finished with status 'done'
  Created wheel for lazy-object-proxy: filename=lazy_object_proxy-1.4.3-cp38-cp38-macosx_10_15_x86_64.whl size=19532 sha256=33ffb4b07984e78167f162d944230aa211b293be85c552ae331e67db67e57148
  Stored in directory: /Users/hieu.van/Library/Caches/pip/wheels/d7/f7/3b/6853df4a25a106662f20e70ad6bd448c8ae07d12ce80fb9063
  Building wheel for wrapt (setup.py): started
  Building wheel for wrapt (setup.py): finished with status 'done'
  Created wheel for wrapt: filename=wrapt-1.12.1-cp38-cp38-macosx_10_15_x86_64.whl size=32590 sha256=64979140f6ecfb108b13681873b3964d950654ca891f947019cc246000f591ee
  Stored in directory: /Users/hieu.van/Library/Caches/pip/wheels/5f/fd/9e/b6cf5890494cb8ef0b5eaff72e5d55a70fb56316007d6dfe73
Successfully built lazy-object-proxy wrapt
Installing collected packages: toml, six, lazy-object-proxy, wrapt, astroid, mccabe, isort, pylint
Successfully installed astroid-2.4.2 isort-4.3.21 lazy-object-proxy-1.4.3 mccabe-0.6.1 pylint-2.5.3 six-1.15.0 toml-0.10.1 wrapt-1.12.1
+ pip freeze
astroid==2.4.2
isort==4.3.21
lazy-object-proxy==1.4.3
mccabe==0.6.1
pylint==2.5.3
six==1.15.0
toml==0.10.1
wrapt==1.12.1
+ rm -rf venv
```

<!-- The below code snippet is automatically added from pyenv.console -->
<!-- AUTO-GENERATED-CONTENT:END -->

## `virtualenvwrapper`

## PyPI

how to pronounce PyPI (beginner) anthony explains #020
<https://www.youtube.com/watch?v=I5OUzCAYst8>
<http://www.howtopronounce.cc/pypi>
Pie-Pea-Eye
"Py-P-I"

`/paɪ/` `/piː/` `/aɪ/`

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
