Decide where in the code and document to place the code in Mathics
------------------------------------------------------------------

To find where to put ``Undefined`` in Mathics, we look this up the `WMA docs <https://reference.wolfram.com/language/ref/Undefined.html>`_.

In the dropdown menu called "Related Guides" for that, we find only one entry: "Mathematical Constant".

Inside running the Django application in the documentations section (on the right or click on the "?" if this doesn't appear), type in "Mathematical Constants", and we see there.

A ``git grep 'Mathematical Constants'`` tells us that this is located in `mathics/builtins/numbers/constants.py <https://github.com/Mathics3/mathics-core/blob/master/mathics/builtin/numbers/constants.py>`_.

Next:

.. toctree::
   :maxdepth: 1

   whatis
