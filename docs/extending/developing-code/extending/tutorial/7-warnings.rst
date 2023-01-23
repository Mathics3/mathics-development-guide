Emitting warnings
-----------------

Sometimes things go wrong. When things go wrong, we should report an error to
our users. But how can one emit a warning from inside an evaluator?

Warnings in Mathics3 can be specified via the ``messages`` class field. The
``messages`` class field is a dictionary whose keys are the names of possible
warning messages and whose values are template warning messages. For example,
we may want to display a warning when our users pass something other than a
string to ``Hello``:

.. code-block:: python

  from typing import Optional
  from mathics.builtin.base import Builtin, String
  from mathics.core.evaluation import Evaluation

  class Hello(Builtin):
    """
    <dl>
      <dt>Hello[$person$]
      <dd>An example function in a Python-importable Mathics3 module.
    </dl>
    >> Hello["World"]
     = Hello, World!
    """

    messages = {
      'nstr': '`1` is not a string',
    }

    def eval(self, person: String, evaluation: Evaluation) -> Optional[String]:
      "Hello[person_]"

      if not person.has_form('String'):
        return evaluation.message('Hello', 'nstr', person)

      return String(f"Hello, {person.value}!")

In this case, calling ``Hello[45]`` will emit the warning ``nstr: 45
is not a string``.
