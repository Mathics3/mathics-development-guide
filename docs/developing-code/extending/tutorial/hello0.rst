Hello World - Version 0, Predefined
-----------------------------------

.. code-block:: python

  from mathics.builtin.base import Predefined

  class Hello(Predefined):
    name = "Hello"
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
most primitive class that is used for adding Mathics Symbols.

In that class you define a method *evaluate(self, evaluation)* which
is what will get called when the Symbol is evaluated. The
``evaluation`` parameter contains the evaluation environment that can
be used to get definitions of variables and other things that may be
neede to peform the function.

However here all we do is return a Mathics string, so we don't need to
use what is in evalutation.

The last thing to note is that we needed to define the class variable
``name`` so that this name gets added to the list of "builtin" definitions.
