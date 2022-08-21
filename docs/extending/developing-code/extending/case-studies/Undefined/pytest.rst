Pytest testing of ``Undefined``
================================

On github, after adding the code to ``mathics-core`` described here, we then started making use of
``Undefined`` in those existing Built-in functions that should have been using them.

In particular, we added a rules:

.. code-block:: mathematica

   Abs[Undefined] = Undefined
   Cos[Undefined] = Undefined

along with many other rules of this kind.

Here is a small unit test for ensuring these rules took effect:

.. code-block:: python


    """
    Unit tests for mathics.builtins.numbers.constants
    """
    from test.helper import check_evaluation

    def test_Undefined():
        for fn in [
            "Abs",
            "Cos",
    ]:
       check_evaluation(f"{fn}[Undefined]", "Undefined")

Since the builtin function lives inside Python file
``mathics/builtins/numbers/constants.py`` the test should be put in
``test/builtins/numbers/constants.py``.

The function ``check_evaluation()`` from module ``test.helper`` can
take quite a number of optional parameters.  But in this simple example,
we just need two. The first parameter is input that is given which is
analogous to what appears after ``>>`` and the second parameter which
gives the expected output which is analogous to what appears after ``=`` in the docstring.

Please note that docstring tests are for *interesting* user-oriented
example. Please don't use them for unit tests.

The full test example for the ``Undefined`` built-in symbol can be found in the code `here
<https://github.com/Mathics3/mathics-core/blob/master/test/builtin/numbers/test_constants.py>`_.
