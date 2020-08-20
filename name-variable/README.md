# `__name__` Variable

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [An introduction to the `__name__` variable and its usage in Python](#an-introduction-to-the-__name__-variable-and-its-usage-in-python)
- [Why is the `__name__` variable used](#why-is-the-__name__-variable-used)
- [What values can the `__name__` variable contain](#what-values-can-the-__name__-variable-contain)
- [Scenario 1 - Run the script](#scenario-1---run-the-script)
- [Scenario 2 - Import the script in another script](#scenario-2---import-the-script-in-another-script)
- [Conclusion](#conclusion)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## An introduction to the `__name__` variable and its usage in Python

You've most likely seen the `__name__` variable
when you've gone through Python code.
Below you see an example code snippet of how it may look:

```python
if __name__ == '__main__':    main()
```

In this article,
I want to show you how you can make use of this variable to create modules in Python.

## Why is the `__name__` variable used

The `__name__` variable (two underscores before and after) is a special Python variable.
It gets its value depending on how we execute the containing script.

Sometimes you write a script with functions that might be useful in other scripts as well.
In Python, you can import that script as a module in another script.

Thanks to this special variable,
you can decide whether you want to run the script.
Or that you want to import the functions defined in the script.

## What values can the `__name__` variable contain

When you run your script,
the `__name__` variable equals `__main__`.
When you import the containing script, it will contain the name of the script.

Let us take a look at these two use cases and describe the process with two illustrations.

## Scenario 1 - Run the script

Suppose we wrote the script nameScript.py as follows:

```python
def myFunction():    print 'The value of __name__ is ' + __name__
```

```python
def main():    myFunction()
```

```python
if __name__ == '__main__':    main()
```

If you run `nameScript.py`, the process below is followed.

<div align="center">
<img src="https://cdn-media-1.freecodecamp.org/images/PljpjxnM1OMMW7IkexNxVfwrKhP0RH-isapH" width="900">
</div>

Before all other code is run,
the `__name__` variable is set to `__main__`.
After that, the main and myFunction def statements are run.
Because the condition evaluates to true, the main function is called.
This, in turn, calls myFunction. This prints out the value of `__main__`.

## Scenario 2 - Import the script in another script

If we want to re-use myFunction in another script,
for example importingScript.py, we can import nameScript.py as a module.

The code in importingScript.py could be as follows:

```python
import nameScript as ns
```

```python
ns.myFunction()
```

We then have two scopes: one of importingScript and the second scope of nameScript.
In the illustration,
you'll see how it differs from the first use case.

<div align="center">
<img src="https://cdn-media-1.freecodecamp.org/images/k9OxzvJAP-s5qeZg88jUCOCVy1syrQu4oKds" width="900">
</div>

In importingScript.py the `__name__` variable is set to `__main__`.
By importing nameScript, Python starts looking for a file by adding `.py` to the module name.
It then runs the code contained in the imported file.

But this time it is set to nameScript.
Again the def statements for main and myFunction are run.
But, now the condition evaluates to false and main is not called.

In `importingScript.py` we call myFunction which outputs nameScript.
NameScript is known to myFunction when that function was defined.

If you would print `__name__` in the importingScript,
this would output `__main__`.
The reason for this is that Python uses the value known in the scope of importingScript.

## Conclusion

In this short article,
I explained how you can use the `__name__` variable to write modules.
You can also run these modules on their own.
This can be done by making use of how the values of these variables change
depending on where they occur.

## References

- [What's in a (Python's) `__name__`?](https://www.freecodecamp.org/news/whats-in-a-python-s-name-506262fe61e8)
- [`__name__` (A Special variable) in Python](https://www.tutorialspoint.com/name-a-special-variable-in-python)
