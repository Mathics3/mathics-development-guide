Function Application via Rules
------------------------------

In the last example of the last section we might observe that the
one-parameter form of ``Hello`` is really the same thing as a the
two-parameter version where the the ``language`` value is filled in.

Making use of that observation, we don't actually need to use a
separate method to handle a parameter with essentially a defalt
value. Instead we could rewrite the function calls that don't supply a
language parameter into one that does by filling in the default value.

This is done by setting the class variable *rules*.

Here is how this is done.

.. code-block:: python

  from mathics.builtin.base import Builtin, String
  from mathics.core.evaluation import Evaluation

  class Hello(Builtin):
      rules = {
          "Hello[person_String]": 'Hello[person, "English"]',
      }

      def apply(self, person: String, language: String, evaluation: Evaluation) -> String:
          """Hello[person_String, language_]"""
           greeting = "Bonjour" if language.value == "French" else "Hello"
          return String(f"{greeting}, {person.value}!")

This code does the same thing as in the last section.
See the session there for an example of how this works.
