# Python Development Setup

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

### requirements.txt

If you have browsed any python projects on Github or elsewhere,
you have probably noticed a file called `requirements.txt`.
This `requirements.txt` file is used for specifying
what python packages are required to run the project you are looking at.
Typically the `requirements.txt` file is located
in the root directory of your project.

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

- For Application
- Dependency Management

### virtualenv

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
created virtual environment CPython3.8.3.final.0-64 in 368ms
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
+ pip install --quiet --requirement requirements.txt
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

- [My Simple Python Development Setup](https://medium.com/better-programming/my-simple-python-development-setup-687c31898d5b)
- [python-virtual-env](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env)
- [venv](https://docs.python.org/3/tutorial/venv.html)
- [Installing packages using pip and virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments)
