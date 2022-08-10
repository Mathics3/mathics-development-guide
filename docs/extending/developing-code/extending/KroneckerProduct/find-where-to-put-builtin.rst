.. _decide_new_builtin_location:

Decide where in the code and document to place Builtin
======================================================

In the first step,  :ref:`Selecting Builtin to add <selecting_a_new_builtin>`, there location may already have been suggested. This is usually the case if the name is listed as a "TODO" at the bottom an existing section. Or if in an issue it is listed with other similar function names.

Using ``KroneckerProduct`` as an example, Looking that up in the `WMA docs <https://reference.wolfram.com/language/ref/KroneckerProduct.html>`_  and then looking at the Related Guides dropdown menu we see:

* Matrix Operations
* Operations on Vections

Now to a running the Django application and in the documentations section (on the right or click on the "?" if this doesn't appear), type in "Matrix", and we see there is no "Matrix Operations" section yet.

However if we type "Operations" we see "Operations on Vectors" is already there and it has a subsection called "Vector Space Operations". So let's use that.

A ``git grep 'Vector Space Operations'`` tells us that this is located in ``mathics/builtins/vectors/vector_space_operations.py``.

When there is no existing section in Mathics already...
-------------------------------------------------------

When an existing section or subsection does not exist, see if there is a nother categorization of the function for which we already do have a section or subsection.

If not you will need to add a new directory. Then you'll need to add your new module name to ``setup.py`` and ``mathics/builtin/__init__.py``.
