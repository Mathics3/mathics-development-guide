.. _decide_new_builtin_location:

Decide where in the code and document to place Builtin
======================================================

In the first step,  :ref:`Selecting Builtin to add <selecting_a_new_builtin>`, there location may already have been suggested. This is usually the case if the name is listed as a "TODO" at the bottom an existing section. Or if in an issue it is listed with other similar function names.

Using ``KroneckerProduct`` as an example, Looking that up in the `WMA docs <https://reference.wolfram.com/language/ref/KroneckerProduct.html>`_  and then looking at the Related Guides dropdown menu we se:

* Matrix Operations
* Operations on Vections

Now to a running the Django application and in the documentations section (on the right or click on the "?" if this doesn't appear), type in "Matrix", and we see there is no "Matrix Operations" section yet.

However if we type "Operations" we see "Operations on Vectors" is already there. So let's use that.

Note that Builtin Funciton Class names are in alphabetic order. (Move into later section?)


If there is no existing section in Mathics already...
-----------------------------------------------------


If there is no existing section in Mathics already, then you may decide to add a new one.

Here, you will need to add a new directory under ``mathics_core/builtins`` along with its ``_init_.py`` file to tell Python this is a module. Then you'll need to add your new module name to ``setup.py`` and ``mathics/builtin/__init__.py``.
