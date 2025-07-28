Thoughts and Experience from Adding Builtins
============================================

Here are some thoughts and guidelines in writing new primitives (called "Builtins") to Mathics3. These are based what I (rocky) feel are mistakes in the project that have plagued the project.


Don't Reinvent the Wheel
------------------------

In the history of this project, when faced with adding a new Builtin Function, several times code was written from scratch rather than consider whether one of the existing Mathematics libraries can be hooked into. For example, consister Mathics3's ``Transpose`` Builtin Function to transpose a Mathics3 ``Matrix`` or an ``Array``.

In the 2-D case, the code to write this is pretty simple, you copy swap the *i* and *j* components of the array.

But when we run into the 3-dimensional situation, and one should assume in WL there will always be generalizations and complications, things are no longer as simple. Now you need introduce which axes to swap. Both WL and SymPy allow this to be specified with a ``Permute`` function. Also, there is the problem of determining compatibilty on the size axes that are going to be swapped to make sure they are compatible.

Lest you think this is an isolated case, in the history of the project the same kind of thing happens implementing calculus functions such as ``FindRoot[]``, ``FindMinimum[]`` or ``FinMaximum``.

While it might be intelletually satisfying to write fun to write such code in Python, please refrain from doing so.

The Mathics3 project has always been understaffed and undermaintained. By hooking into SymPy or some other package, the code has a better chance of being maintained as well as getting expanded and generalized, if that isn't the situation intially.

In fact such generalization and maintanence problem occured in the case of image processing routines where it was initally done using more original code. By switching to the Python Pillow library, we fixed a number of bugs in the code and problems handling some image formats, but we were also were able to support many more image formats.

So instead of writing image processing routines, effort was spent to figure out how to *interface* with the Pillow library and encapsilate a Pillow image object as a Mathics3 object.

The same thing went on with encapsulating a Mathics3 Network Graph object as a NetworkX Graph object. NetworkX is a Python package for handling Network Graphs.

Caching Expression cache vs. @lru
+++++++++++++++++++++++++++++++++

Don't Micromanage Python
-------------------------

* flattening calls,
* ordering conditions of an "if" statements
* assuming Cython, rewriting into another Programming Language (or some technology) is going to fix gross inefficiencies in design of the code.

Misuse of Rewrite Rules
------------------------


Overusing Expensive Evaluate
----------------------------
