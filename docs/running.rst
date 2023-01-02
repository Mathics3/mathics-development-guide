.. index:: running
.. _running:

Running Mathics3
================

Here we describe the ways Mathics3 can be run.


Running natively
~~~~~~~~~~~~~~~~

Command-line interface
^^^^^^^^^^^^^^^^^^^^^^

If you have installed the Mathics3 core only you can start the
rudimentary command-line shell with:

.. code:: bash

    $ mathics

If you are running code from the source tree, i.e. "develop" mode, the
the above is the same thing as running:

.. code:: bash

    $ python mathics/main.py

To get a list of options run:

::

    $ mathics --help

However note that the above CLI is pretty minimal and will stay
that way.

Full Command-line Shell
^^^^^^^^^^^^^^^^^^^^^^^

The more complete command-line shell is
`mathicsscript <https://github.com/Mathics3/mathicsscript>`_.

After installing, run:

.. code:: bash

    $ mathicsscript

To get a list of options run:

::

    $ mathicsscript --help


Currently, ``mathicsscript`` requires networkx to support matplotlib
graphics for the add-on package `pymathics-natlang <https://github.com/Mathics3/pymathics_natlang>`_.

This may be unbundled in the future In the future.

Django-based-line interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Chances are you that instead of running a command-line interface you
will want to run the fancier Django-based web server. This does support
graphics output currently (although in the future we plan to improve
that).

To start the server after Mathics3 has been installed, run:

.. code:: bash

    $ mathicsserver

The first time this command is run it will create the database file for
saving your sessions. Issue

::

    $ mathicsserver --help

to see a list of options.

You can set the used port by using the option ``-p``, as in:

::

    $ mathicsserver -p 8010

The default port for Mathics3 is 8000. Make sure you have the necessary
privileges to start an application that listens to this port. Otherwise,
you will have to run Mathics3 as super-user.

By default, the Web server is only reachable from your local machine. To
be able to access it from another computer, use the option ``-e``.

However, the server is only intended for local use, as it is a security
risk to run it openly on a public Web server!

If you are running from the source tree and instead want run the
webserver in a mode where if you make changes to the code, the webserver
will get restarted, we have a GNU Makefile target for doing that.

Here, run:

.. code:: bash

    $ make runserver

This is the same thing as running
``python mathics/manage.py runserver``.

Passing options such as setting the port to listen on is a little
different here because the option has to be a ``manage.py`` option and
that works different.py. And to complicate things further you are
running GNU Make and then have to pass tell that to pass over the
``manage.py`` option. So use pass ``o=8001`` to make in order to pass
option ``8001`` to ``manage.py``. In other words, to set the port here
to 8001:

.. code:: bash

    $ make runserver o=8001 # note, no dash

Running via docker
~~~~~~~~~~~~~~~~~~

Another way to run ``mathics`` is via `docker
<https://www.docker.com>`__ using the `Mathics3 docker image
<https://hub.docker.com/repository/docker/mathicsorg/mathics>`_ on
dockerhub.

If you do a PyPI install of the package `Mathics3 omnibus <https://pypi.org/project/Mathics-omnibus/>`_,
you will get simpler access to the docker images and a simpler way to run the various parts.

To run the command-line interface using docker image without using the Mathics3 omnibus helper script:

::

    $ docker run --rm -it --name mathics-cli -v /tmp:/usr/src/app/data mathicsorg/mathics --mode cli

However if Mathics3 omibus is installed:

::

   $ dmathicsscript

does the same thing.

If you want to add options add them at then end preceded with ``--``:
for example:

::

    $ docker run --rm -it --name mathics-cli -v /tmp:/usr/src/app/data mathicsorg/mathics --mode cli -- --help

In the above you are running ``mathicsscript`` (the enhanced CLI), not
``mathics``.

To run the Django 3.1-web interface using docker image without using the Mathics3 omnibus helper script, run :

::

    $ docker run --rm -it --name mathics-web -p 8000:8000 -v /tmp:/usr/src/app/data mathicsorg/mathics --mode ui

However the Mathics-omnibus-installed script for this simplifies this as well. So with that installed:

::

    $ dmathicsserver

does the same thing.

Consult the `docker-run
command <https://docs.docker.com/engine/reference/run/>`__ for
information about changing external port number and other for other
``docker run`` options.

Also see the previous section on security limitations.

Running Mathics3 on your server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we describes how to setup Mathics3 on a local network. There are
additional (security) considerations for running Mathics3 on a publicly
facing webserver.

Best practices for a local network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Install PyPy

   ::

       sudo apt-get install pypy

-  Install Setuptools

   ::

       curl -O http://peak.telecommunity.com/dist/ez_setup.py
       pypy ez_setup.py

-  Download and Install Mathics

   ::

       curl -L  -O https://github.com/mathics/Mathics/releases/download/v0.8/mathics-0.8.tar.gz`
       tar xzf mathics-0.8.tar.gz
       cd mathics-0.8/
       sudo pypy setup.py install

You can now run the web server with ``mathicsserver -e`` but you
probably want to make some changes first. - disable the files module by
setting ``ENABLE_FILES_MODULE = False`` in ``mathics/settings.py``
(otherwise remote users will be able to read and write local files). -
set an execution timeout in ``mathics/setttings.py``, e.g.
``TIMEOUT = 10`` for a 10s limit. - Various other changes in the
``settings.py`` file like email addresses.

You probably also want to run the server as a restricted user within a
jail shell

Running Mathics3 on a public webserver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Warning:** You should be very careful running Mathics3 publicly, there
are some potentially large security implications to be aware of!

The setup is similar but you can use ngnix to cache the static content.
Mathics3 runs as a wsgi app so you can use uwsgi. The `Django
docs <https://uwsgi-docs.readthedocs.org/en/latest/tutorials/Django_and_nginx.html>`__
are a good reference.

.. toctree::
   :maxdepth: 2


.. |Packaging status| image:: https://repology.org/badge/vertical-allrepos/mathics.svg
   :target: https://repology.org/project/mathics/versions
