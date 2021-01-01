.. pymathics-hello documentation master file, created by
   sphinx-quickstart on Sun Nov 29 14:06:02 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Extending Mathics Tutorial
==========================

In this guide we will show how to Extend Mathics with Python code.

We'll start out with a simple "Hello, World!" function and modify that.

.. toctree::
   :maxdepth: 2

   tutorial/hello0
   tutorial/hello1
   tutorial/hello2
   tutorial/hello3

To be continued....



If a function does not return any value, the Mathics expression is
left unchanged. Note that you have to explicitly return
``Symbol["Null"]`` (which we have a defined for you in ``SymbolNull``)
if you want that to return a Null instead.

Working with multiple patterns
++++++++++++++++++++++++++++++

It's important to note that a builtin can be defined over *more than one
pattern*, such as in the following case:

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

    def apply(self, person, language, evaluation):
      "Hello[person_, language_]"

      if language.has_form("French"):
        return String(f"Bonjour, {person.get_string_value()}!")
      else:
        return String(f"Hello, {person.get_string_value()}!")

    def apply_english(self, person, evaluation):
      "Hello[person_]"
      return self.apply(person, Expression("English"), evaluation)

In this case, ``Hello["Peter", French]`` will resolve to ``"Bonjour,
Peter!"``, while ``Pymathics`Hello["Peter", English]`` and
``Pymathics`Hello["Peter"]`` will both resolve to ``"Hello, Peter!"``.

We may also want to use different definitions according to the types of the
arguments passed to a builtin. We can do so by specifying type-constraints in
the definitions's pattern, such as in the following example:

.. code-block:: python

  from mathics.builtin.base import Builtin

  class Hello(Builtin):
    """
    <dl>
      <dt>Hello[$person$]
      <dd>An example function in a Python-importable Mathics module.
    </dl>
    >> Hello["World"]
     = Hello, World!
    """

    def apply(self, person, evaluation):
      "Hello[person_String]"
      return String(f"Hello, {person.get_string_value()}!")

When evaluating a call to a builtin, Mathics will pattern-match on the inputs
and search for the most appropriate definition. If the inputs don't match any
of the patterns of the existing definitions then the entire expression is
returned unchanged. For example, if we implemented ``Hello`` as above then
``Hello[45]`` would resolve to ``Hello[45]``, because ``45`` doesn't match
``person_String`` (``45`` is not a string).

Rules
+++++

Let's recall the example given in `Working with multiple patterns`_. Notice
that ``English`` is essentially the default value of the ``language``. We
don't actually need to use multiple definitions to encode parameters with
default values. By adding an entry to the builtin's ``rules`` class-field, we
can tell Mathics that an expression should resolve the value of a different
expression, such as in the following example:

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

    rules = {
      "Hello[person_]": "Hello[person, English]",
    }

    def apply(self, person, language, evaluation):
      "Hello[person_, language_]"

      if language.has_form("French"):
        return String(f"Bonjour, {person.get_string_value()}!")
      else:
        return String(f"Hello, {person.get_string_value()}!")

In this example, the first entry in ``rules`` tells Mathics that
``Hello[person]`` is just sintactic suger for ``Hello[person, English]``.

Special attributes
++++++++++++++++++

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
+++++++++++++++++

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
