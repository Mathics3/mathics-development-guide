Working with Multiple Patterns
------------------------------

Mathics allows Functions to have the same name but different function
signatures. For example maybe you can call ``Hello`` with a either
one or two parameters.

Mathics calls the a signature a "Form".

One way to implement this in Python code is to have two different
Python methods that start with the name ``apply``, one will
handle one kind of From, say of the kind we saw previously,
a person name is given. The other *apply* method will handle
another kind of Form, such as one where there is an
additional parameter, a string language value.

Here is some code for this..


.. code-block:: python

  from mathics.builtin.base import Builtin, String

  class Hello(Builtin):
    """
    <dl>
      <dt>Hello[$person$]
      <dd>Print a "Hello" message customized for $person$.

    This is an example of how Python Builtin-Symbol documentation works.
    </dl>

    Here is our test:
    >> Hello["Rocky"]
     = Hello, Rocky!
    """

    def apply(self, person, language, evaluation):
      """Hello[person_String, language_String]"""

      greeting = "Bonjuor" if language.has_form("French") else "Hello"
      return String(f"{greeting}, {person.get_string_value()}!")

    def apply_english(self, person, evaluation):
      """Hello[person_]"""

      return self.apply(person, Expression("English"), evaluation)

In this case, ``Hello["Peter", French]`` will resolve to ``"Bonjour,
Peter!"``, while ``Pymathics`Hello["Peter", English]`` and
``Pymathics`Hello["Peter"]`` will both resolve to ``"Hello, Peter!"``.

When evaluating a call to a builtin, Mathics will pattern-match on the inputs.

If the inputs don't match any of the patterns of the existing
definitions then the entire expression is returned unchanged. For
example, given the above definitions, ``Hello[45]`` would resolve to
``Hello[45]``, because 45 doesn't match the ``String`` type check part
of ``person_String``; 45 is not a string.

If a function does not return any value, the Mathics expression is
left unchanged. Note that you have to explicitly return
``Symbol["Null"]`` (which we have a defined for you in ``SymbolNull``)
if you want that to return *Null*.
