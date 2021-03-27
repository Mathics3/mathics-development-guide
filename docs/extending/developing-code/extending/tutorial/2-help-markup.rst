Adding Help Text
----------------

Now let us add some help to the *Hello* function so that World will
know about it. This is done in the docstring
for the *Hello* class and the markup is largely XML/HTML.


.. code-block:: python

  from mathics.builtin.base import Builtin, String

  class Hello2(Builtin):
    """
    <dl>
      <dt>Hello[$person$]
      <dd>Print a "Hello" message customized for $person$.

    This is an example of how Python Builtin-Symbol documentation works.
    </dl>
    """

    def apply(person: String, evaluation) -> String:
      "Hello[person_String]"
          return String(f"Hello, {person.get_string_value()})!"

The XML tagging that gets created from the above renders in the Django
interface like this:

.. image:: Hello2.png
  :width: 400
  :alt: Rendering XML help markup in Django

In the Django interace on the right-hand side, I hit the "?" button and started typing "H E L L" and that was enough for the Django to find it. Django will pick up this change without having to restart it!

This is how the text appears geting help via ``?`` in ``mathicsscript``:

.. image:: Hello2-mathicsscript.png
  :width: 400
  :alt: Rendering XML help markup in Django

See :ref:`For Help Text <doc_help_markup>` for more a list of help-related markup.
