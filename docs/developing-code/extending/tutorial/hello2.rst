Hello World - Version 2 - Help text
-----------------------------------

Now lets add some help to the ``Hello`` function World will
know about it. This is done in the docstring
for the ``Hello`` class and the markup is largely XML/HTML.


.. code-block:: python

  from mathics.builtin.base import Builtin

  class Hello1(Builtin):
    """
    <dl>
      <dt>Hello[$person$]
      <dd>Print a "Hello" message customized for $person$.

    This is an example of how Python Builtin-Symbol documentation works.
    </dl>
    """

    name = "Hello1"
    def apply(s, evaluation):
      "Hello1[s_String]"
          return f"Hello, {String(s)}!"

The XML tagging renders in the Django interface like this:

.. image:: Hello2.png
  :width: 400
  :alt: Rendering XML help markup in Django

In the Django interace on the right-hand side, I hit the "?" button and started typing "H E L L" and that was enough for the Django to find it. Django will pick up this change without having to restart it!
