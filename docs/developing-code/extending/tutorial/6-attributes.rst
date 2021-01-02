Class Attributes
----------------

Class attributes are used a lot in classes that create Mathics
definitions, such as in the Builtin class that we have mostly been
using.

In fact we already saw one example in the last section where the class
variable ``rules`` was used to create some Mathics *Rules* in the
definition of the *Hello* function.

Suppose you want to create a Mathics variable that starts with a
dollar sign (``$``) in accordance to the naming convention for many
system variables.

To accomplish this you assign the desired string name to class
variable ``name``, and that will override the default name.

Similarly, setting a variable's or function's attributes can be done
by setting the class variable name ``attributes``.

Suppose we want to define a variable called ``$Hello`` and don't want
lock down the attributes of this variable so that the attributes
cannot be modified.

This is done by setting the ``Locked`` attribute of in the
definition, via the ``attributes`` class variable.

Here is and example of setting some class variables to alter the
definition of a function:

.. code-block:: python

  from mathics.builtin.base import Predefined

  class Hello(Predefined):
      name = "$Hello"
      attributes = ('Locked',)

      def evaluate(self evaluation) -> String:
          return String("Hello, World!")

Here is a session that demonstrates the above code:

::

   $ mathics

   In[1]:= $Hello
   Out[1]= Hello, World!

   In[2]:= Unprotect[$Hello]
   ClearAttributes::locked: Symbol $Hello is locked.
   Out[2]= None


.. TODO: Document and link to what which attribute does. Make a table somewhere
