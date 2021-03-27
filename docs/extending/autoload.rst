.. autoload:

Mathics Setup Code Read on Loading
==================================

Although a lot of the Mathics core is written in Python for efficiency, it is sometimes easier and nicer just to have little bits for core code written in Mathics.

When Mathics starts up, it reads files written in the Mathics dialect of Wolfram Language that are found in  `mathics/autoload <https://github.com/mathics/Mathics/tree/master/mathics/autoload>`_ .


For example in a file called ``settings.m`` which have some Mathics-oriented variables that are set to default values.

One way to implement more primitives that are missing in Mathics but are in the Wolfram Language might be to implement the primitive using existing Mathics constructs. And then this function definition can be added to a file inside a directory of Mathics files that gets read on startup.
