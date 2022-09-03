Finishing up ``Curl[]``
=======================

We have a basic version of ``Curl``. There is more that could be done though:

* Add unit tests using ``pytest``
* Extend to the other forms of Curl, possibly using SymPy

There is however one last step that we *will* do here: note that we have added this builtin function.

The place to do this is in `CHANGES.rst <https://github.com/Mathics3/mathics-core/blob/master/CHANGES.rst>`_.


Find the section lablewed `New Builtins`` at the top of the pages and add this function.
As we saw for adding classes, please add the name in alphabetic order.

.. code-block:: diff

    Here is a "diff" after we added this function:

    diff --git a/CHANGES.rst b/CHANGES.rst
    index 23a37db0..ec80c087 100644
    --- a/CHANGES.rst
    +++ b/CHANGES.rst
    @@ -11,6 +11,7 @@ New Builtins

     #. ``$BoxForms``
     #. ``ClebschGordan``
    +#. ``Curl`` (2-D and 3-D vector forms only)
     #. ``Kurtosis``
     #. ``PauliMatrix``
     #. ``SixJSymbol``
