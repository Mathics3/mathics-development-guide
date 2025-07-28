Defining Variable ``$MachineName``
==================================

To start our list of case studies, we'll start off with a very simple example: defining a read-only variable.


The Mathics3 Built-in Symbol ``$MachineName`` holds a Mathics3 string value containing the computer machine name.

Since it is a variable, not a function we use the simpler ``Predefined`` class to define this.

Here is the code for this.


.. code-block::

    import platform
    from mathics.core.builtin import Predefined
    from mathics.core.atoms import String

    class MachineName(Predefined):
        """
        <url>:WMA link:https://reference.wolfram.com/language/ref/MachineName.html</url>

        <dl>
          <dt>'\\$MachineName'
          <dd>is a string that gives the assigned name of the computer on which Mathics3 \
              is being run, if such a name is defined.
        </dl>

        S> $MachineName
         = ...
        """

        name = "$MachineName"
        summary_text = "get the name of computer that Mathics3 is running"

        def evaluate(self, evaluation: Evaluation) -> String:
            return String(platform.uname().node)

The docstring for this class lists:

* The variable name : ``$MachineName``.
* A link to the WMA reference.
* A HTML "definition list" to enclose the define how to use this and what the variable does.
* An example of how this variable might be used. The ``S>`` indicates
  that this example can't be run in a "sandboxed" environment.

The Python code makes heavy use of the ``Predefined`` class properties
to do most of the work that to set up this variable.

The class variable ``name`` is what defines the name seen inside Mathics3. Note that ``$MachineName`` is not a valid Python class name, even though it is a valid Symbol name in Mathics3. So we specify the Mathics3 name using the class variable ``name`` of the ``Predefined`` class.

If we wanted to define a variable that matches the class name, e.g. ``MachineName``, we would not need to set this class variable. The class would use the class name as its corresponding Mathics3 Symbol name.

The ``evaluate()`` method is used to produce the read-only value of this variable. When the value is a simple literal value the class variable ``value`` can be used instead of defining function ``evaluate``.



For more detail on defining a Builtin Variable, see :ref:`Adding Builtin ``Undefined```.

Next:

:ref:`Selecting a Builtin to add`
