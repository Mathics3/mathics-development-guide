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

.. TODO: Describe "name"
.. TODO: Document what which attribute does. Make a table somewhere
