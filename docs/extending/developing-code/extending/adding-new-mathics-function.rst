Case Example: Adding Mathics Function: KroneckerProduct
========================================================

.. _adding_KroneckerProduct:

A large part of Mathics is simply a list of built-in functions that perform some computation. When possible, w rely on SymPy, SciPy, and mpmath functions.

In :ref:`Tutorial: Adding a new Mathics Function Text <adding_KroneckerProduct>`,
Here outline the steps taken to add ``KroneckerProduct``.

The following is an outline of the overall process which we go into more depth
in subsequent section



* Find a Builtin that hasn't been implemented.
* Decide where in the code/doc to put it.
* See if it is a SymPy function. And the rest will assume yes. But if not try to SciPy and mpmath.
* Copy one of the newer existing Sympy functions and adapt. Newer existing Sympy functions have Wiki, SyPy, and WMA links. Probably in the WMA link, all you will have to do is change the copied WMA name into the new name.
* Use WMA link to adapt the docstring. It might be consulted to get the summary text too.
* Go into mathics and see that you can get "info" or "?" on the changed doc.
* Adapt the pattern match rule and parameters. This is probably the hardest part. Cases in mathics can help here. If you have put the code with related functions, often that class will be similar to some other class and that can make adapting the pattern match and body of the code easier. Also, similar classes do not follow the most recent conventions, consider updating nearby related builtins so that do follow new conventions.
* Adapt the eval method parameters and body.
* Make sure the function attributes are correct.
* Adapt some doctests and test. Examples from WMA and SymPy are a good source, but try to make the examples meaningful.
* Run the tests using python mathics/docpipeline -s <builtin name>
* Go over error conditions and error messages
* Write unit tests for all of these edge cases and uninteresting cases to try. test using python -m pytest -s test/builtin/.../test-.py`
* Run all tests.
* Create PR.

.. toctree::
   :maxdepth: 2

   KroneckerProduct/selecting-builtin
   KroneckerProduct/find-where-to-put-builtin
   KroneckerProduct/match-with-library
   KroneckerProduct/basic-skeleton
