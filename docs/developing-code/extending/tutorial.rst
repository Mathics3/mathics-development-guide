.. pymathics-hello documentation master file, created by
   sphinx-quickstart on Sun Nov 29 14:06:02 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Extending Mathics Tutorial
==========================

In this guide we will show how to Extend Mathics with Python code.

We'll start out with a simple "Hello, World" function and modify that.

Hello World - Version 0, Predefined
-----------------------------------

.. code-block:: python

  from mathics.builtin.base import Predefined

  class Hello(Predefined):
    def evaluate(self, evaluation):
      return String(f"Hello, World!")

Add the above at the end to a file in `mathics.builtin
<https://github.com/mathics/Mathics/tree/master/mathics/builtin.ast>`_
like ``system.py``,

Later on, we will show how to add code without modify the Mathics core, but
for now we'll start simple.

Now start mathics from the Mathics source tree:

::

   $ python mathics/main.py
   Mathics 2.0.0dev
   ...
   In[1]:= Hello  # FIXME: Not sure what's wrong here.
   In[1]:= Hello
   Out[1]= Hello, World!


Now let's go over the code. For a Symbol ``Hello`` we
define a Python ``Class`` of type ``Predefined``. ``Predifined`` is prehaps the
most primitive class that is used for adding Variables and Functions.

In that class you define a method ``evaluate(self, evaluation)`` which
is what will get called when the Symbol is evaluated. The
``evaluation`` parameter contains the evaluation environment that can
be used to get definitions of variables and other things that may be
neede to peform the function.

However here all we do is return a Mathics string, so we don't need to
use what is in evalutation.

The last thing to note is that we needed to define the class variable
``name`` so that this name gets added to the list of "builtin" definitions.


Hello1 - Builtin
----------------

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

To be continued....



The class starts with a Python docstring that specifies the
documentation and tests for the symbol.  Please refer to
:ref:`Documentation markup <doc_markup>` for more details on how to
write the documentation.

Python functions starting with "apply" are converted to built-in rules. Their
docstring is compiled to the corresponding Mathics pattern. Pattern variables
used in the pattern are passed to the Python function by their same name, plus
an additional evaluation object. This object is needed to evaluate further
expressions, print messages in the Python code, etc. Unsurprisingly, the return
value of the Python function is the expression that is replaced for the matched
pattern. If the function does not return any value, the Mathics expression is
left unchanged. Note that you have to return ``Symbol["Null"]`` explicitly if
you want that.

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
