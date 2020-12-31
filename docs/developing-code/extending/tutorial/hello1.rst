Hello, World -- Version 1 with Builtin
--------------------------------------

Most of the time you'll probably need to pass information into the Function you
want to add. For this, use the ``Builtin`` class. This adds what in WL is called
a "Built-in Symbol".

The method that you should define in ``Builtin'' class will get
invoked needs to start off with the name ``apply``. As before, this
method has an ``evaluation`` parameter at the end. Other parameters
that are appropriate for the Function can be added. However those parameters
must also be listed suffixed with a `_` in the Python method's docstring in a special way.

The docstring is used by ``Builtin`` when trying to resolve what
Python method to call. The docstring looks pretty much the same as it
would look if you were defining this in Mathmatica.

For example, let's add a string parameter. In Mathics the function might look like this


.. code-block:: mathematica


  Hello[s_String] := Print["Hello, " <> s <> "!"]

In Python then the apply method looks like this:

.. code-block:: python

  def apply(s, evaluation):
    "Hello[s_String]"
        return f"Hello, {String(s)}!"

Here is the complete code:

.. code-block:: python

  from mathics.builtin.base import Builtin

  class Hello1(Builtin):
    name = "Hello1"
    def apply(s, evaluation):
      "Hello1[s_String]"
          return f"Hello, {String(s)}!"
