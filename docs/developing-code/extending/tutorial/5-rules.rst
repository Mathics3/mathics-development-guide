Function Application via Rules
------------------------------

In the last example ``English`` is the default value of the ``language``.

We don't actually need to use a separate method to handle a parameter with
a value. Instead we could rewrite the function calls that don't supply a
language parameter into one that does by filling in the default value.

This is done by setting the class variable *rules*.

Here is how this is done.

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

    rules = {
      "Hello[person_String]": "Hello[person, English]",
    }

    def apply(self, person, language, evaluation):
      "Hello[person_String, language_]"

      if language.has_form("French"):
        return String(f"Bonjour, {person.get_string_value()}!")
      else:
        return String(f"Hello, {person.get_string_value()}!")
