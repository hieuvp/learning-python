# Development Setup

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Standard](#standard)
  - [pyenv](#pyenv)
  - [requirements.txt](#requirementstxt)
  - [virtualenv](#virtualenv)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Standard

### pyenv

> Python Version Management.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=pyenv.console) -->
<!-- The below code snippet is automatically added from pyenv.console -->

```console
+ pyenv versions
* system (set by /Users/hieu.van/.pyenv/version)
+ python --version
Python 2.7.16
```

<!-- AUTO-GENERATED-CONTENT:END -->

### requirements.txt

> Python Dependency Management.

- The `requirements.txt` file is used for specifying
  what python dependencies are required to run the project.
- Typically `requirements.txt` file is located in the root directory.

```shell script
pip freeze > requirements.txt
```

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=requirements.txt) -->
<!-- The below code snippet is automatically added from requirements.txt -->

```txt
pylint==2.5.3
```

<!-- The below code snippet is automatically added from pyenv.console -->
<!-- AUTO-GENERATED-CONTENT:END -->

### virtualenv

> virtualenv is a tool to create isolated Python environments.
> Since Python 3.3, a subset of it has been integrated into the standard library under the venv module.
> The venv module does not offer all features of this library,
> to name just a few more prominent:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=virtualenv.console) -->
<!-- The below code snippet is automatically added from virtualenv.console -->

```console
+ type python
python is /usr/bin/python
+ type pip
./virtualenv.sh: line 10: type: pip: not found
+ true

+ virtualenv venv
created virtual environment CPython3.8.3.final.0-64 in 389ms
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

+ pip install --quiet --upgrade pip
+ pip list
Package    Version
---------- -------
pip        20.2
setuptools 47.3.1
wheel      0.34.2
+ pip freeze

+ pip install --quiet --requirement requirements.txt
+ pip list
Package           Version
----------------- -------
astroid           2.4.2
isort             4.3.21
lazy-object-proxy 1.4.3
mccabe            0.6.1
pip               20.2
pylint            2.5.3
setuptools        47.3.1
six               1.15.0
toml              0.10.1
wheel             0.34.2
wrapt             1.12.1
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

## References

- [Installing Packages Using `pip` and Virtual Environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments)
