.. pymathics-hello documentation master file, created by
   sphinx-quickstart on Sun Nov 29 14:06:02 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Extending Mathics Tutorial
==========================
In this guide we will show how to Extend Mathics with Python code.


.. toctree::
   :maxdepth: 2

   tutorial/hello0
   tutorial/hello1
   tutorial/hello2
   tutorial/hello3
   tutorial/hello4
   tutorial/hello5

Special attributes
------------------

One can specify general attributes of a builtin in it's ``attributes``
class field. For example, let's say you expect ``Hello[{"Peter",
"Roger"}]`` to evaluate to the same as ``{Hello["Peter"],
Hello["Roger"]}``. We can to that by overwriting ``Hello``'s
``attributes`` class-field.

.. code-block:: python

  from mathics.builtin.base import Builtin, String

  class Hello(Builtin):
    """
    <dl>
      <dt>Hello[$person$]
      <dd>An example function in a Python-importable Mathics module.
    </dl>
    >> Hello["World"]
     = Hello, World!
    """

    attributes = ('Listable',)

    def apply(self, person, evaluation):
      "Hello[person_]"

      return String(f"Hello, {person.get_string_value()}!")

.. TODO: Document what which attribute does. Place a table in here

Emitting warnings
-----------------

Sometimes things go wrong. When things go wrong, we should report an error to
our users. But how can one emit a warning from inside an evaluator?

Warnings in Mathics can be specified via the ``messages`` class field. The
``messages`` class field is a dictionary whose keys are the names of possible
warning messages and whose values are template warning messages. For example,
we may want to display a warning when our users pass something other than a
string to ``Hello``:

.. code-block:: python

  from mathics.builtin.base import Builtin, String

  class Hello(Builtin):
    """
    <dl>
      <dt>Hello[$person$]
      <dd>An example function in a Python-importable Mathics module.
    </dl>
    >> Hello["World"]
     = Hello, World!
    """

    messages = {
      'nstr': '`1` is not a string',
    }

    def apply(self, person, evaluation):
      "Hello[person_]"

      if not person.has_form('String'):
        return evaluation.message('Hello', 'nstr', person)

      return String(f"Hello, {person.get_string_value()}!")

In this case, calling ``Hello[45]`` will emit the warning ``nstr: 45
is not a string``.

.. TODO: Document Operator and SympyFunction
.. TODO: Document interupts
