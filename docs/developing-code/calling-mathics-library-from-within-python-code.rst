.. pymathics-hello documentation master file, created by
   sphinx-quickstart on Sun Nov 29 14:06:02 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Calling Mathics library from within Python code
===============================================

Mathics is also a Python library implementing a parser and a interpreter
for WL.

Using MathicsSession
--------------------

If you have a number of mathics commands in string from that you would
like evaluated, a simple way to do this is to set up a Mathics session
and call the sessions *evaluate()* function:

.. code:: py

    from mathics.session import MathicsSession
    session = MathicsSession(add_builtin=True, catch_interrupt)


    expression = "Integrate[Sin[x]/x,x]"
    result = session.evaluate(expression)
    session.evaluation.format_output(result)


As a subprocess
---------------

Another way to run mathics and get output is to invoke the
``mathics`` command-line script. Although this may be more suitable
for POSIX shell appliations, here is how to do this in Python:

.. code:: py

    import subprocess

    expression = "Integrate[Sin[x]/x,x]"
    cmd = ["mathics", "--no-completion", "-q", "--colors", "NOCOLOR"]
    result = subprocess.run(cmd.append(f"\"{expression}\"" )], stdout=subprocess.PIPE).stdout
    result = result.split("\n")[-1]
    result = result[result.find("=")+1:]

This code runs the Mathics interpreter as a subprocess, sending a the
expression as an input parameter, and extracts from the output the
result.

.. TODO: Show Expression tree evaluation
