.. _builtin_case_studies:

Case Studies for Adding Builtins
================================

A large part of Mathics is simply a list of built-in functions that perform some computation. When possible, rely on SymPy, SciPy, and mpmath functions.

Selecting a Builtin to add
--------------------------

.. _selecting_a_builtin_to_add:


Finding a Builtin that hasn't been implemented. This is pretty easy. Generally you start out having a desire for a specific
function. However if not, there are github feature requests with the label `"New Builtin Function or Variable"
<https://github.com/Mathics3/mathics-core/labels/New%20Builtin%20Function%20or%20Variable>`_.

There are also TODO's at the bottom of the newer sections/modules for missing builtin functions for that particular class or function.

Below are a few examples of actual Mathics Builtins that we have added.

As we added these Builtins, we recorded the steps that were taken. We ordered the list below to go from the simpile to more advanced.



.. toctree::
   :maxdepth: 1

   Undefined
   KroneckerProduct
   Curl


See also :ref:`Tutorial: Adding a new Mathics Function`.
