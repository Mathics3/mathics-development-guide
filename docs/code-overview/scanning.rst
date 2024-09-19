Scanning
========

.. index:: tokenizer
.. index:: scanner

We have split out the scanner into a separate `github repository
<https://pypi.org/project/Mathics-Scanner/>`_ which has its own `PyPI
package <https://pypi.org/project/Mathics-Scanner/>`_.

A little bit about the scanner...  There are two passes made in the
scanner, a "pre-scan" in found in `mathics_scanner.prescanner
<https://github.com/Mathics3/mathics-scanner/blob/master/mathics_scanner/prescanner.py>`_
which converts some WL-specific character codes to character or long
names and the `mathics_scanner.tokeniser
<https://github.com/Mathics3/mathics-scanner/blob/master/mathics_scanner/tokeniser.py>`_
which runs after that. The tokenizer breaks up a string into *tokens*,
classifications of a sequence of characters, which is then as the
atoms on which the parser pattern matches on.
