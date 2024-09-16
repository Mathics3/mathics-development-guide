.. _parsing_a_string:

Python Code for Scanning and Parsing a String
---------------------------------------------

Inside Python, here is how you parse a string:

.. code-block:: python

   from mathics.core.parser import parse, SingleLineFeeder
   from mathics.core.definitions import Definitions

   definitions = Definitions(add_builtin=True)
   str_expression = "1 + 2 / 3"
   expr = parse(definitions, SingleLineFeeder(str_expression))
   print("type", type(expr))
   print("expr: ", expr)

Running the above produces:

::

   type <class 'mathics.core.expression.Expression'>
   expr:  System`Plus[1, System`Times[2, System`Power[3, -1]]]

The function ``SingleLineFeeder`` should be supplied by the front-end.
It reads input a line and a time and returns that back to the parser.
