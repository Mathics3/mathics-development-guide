.. index:: running
.. _running:

Running Mathics
===============

Here we describe the ways Mathics can be run.


Running natively
~~~~~~~~~~~~~~~~

Command-line interface
^^^^^^^^^^^^^^^^^^^^^^

After installing, you can run your a local Mathics command-line
interface with:

.. code:: bash

    $ mathics

If you are running code from the source tree, i.e. "develop" mode, the
the above is the same thing as running:

.. code:: bash

    $ python mathic/main.py

To get a list of options run:

::

    $ mathics --help

However note that the above CLI is pretty minimal and is likley to stay
that way.

For a more full-featured CLI see
`mathicsscript <https://github.com/Mathics3/mathicsscript>`__.

In the future, ``mathicsscript`` this may support graphics output.

Django-based-line interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Chances are you that instead of running a command-line interface you
will want to run the fancier Django-based web server. This does support
graphics output currently (although in the future we plan to improve
that).

To start the server after Mathics has been installed, run:

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

The default port for Mathics is 8000. Make sure you have the necessary
privileges to start an application that listens to this port. Otherwise,
you will have to run Mathics as super-user.

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

Another way to run ``mathics`` is via
`docker <https://www.docker.com>`__ using the \`Mathics docker image
https://hub.docker.com/repository/docker/mathicsorg/mathics on
dockerhub.

To run the command-line interface using docker image:

::

    $ docker run --rm -it --name mathics-cli -v /tmp:/usr/src/app/data mathicsorg/mathics --mode cli

If you want to add options add them at then end preceded with ``--``:
for example:

::

    $ docker run --rm -it --name mathics-cli -v /tmp:/usr/src/app/data mathicsorg/mathics --mode cli -- --help

In the above you are running ``mathicsscript`` (the enhanced CLI), not
``mathics``.

To run the Django 3.1-web interface using docker image run:

::

    $ docker run --rm -it --name mathics-web -p 8000:8000 -v /tmp:/usr/src/app/data mathicsorg/mathics --mode ui

Consult the `docker-run
command <https://docs.docker.com/engine/reference/run/>`__ for
information about changing external port number and other for other
``docker run`` options.

Also see the previous section on security limitations.

This dockerization was modified from
```sealemar/mathics-dockerized`` <https://github.com/sealemar/mathics-dockerized>`__.
See that for more details on how this works.

Running Mathics on your server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here we descrbes how to setup Mathics on a local network. There are
additional (security) considerations for running Mathics on a publically
facing webserver.

Best practises for a local network
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

Running Mathics on a public webserver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Warning:** You should be very careful running Mathics publicly, there
are some potentially large security implications to be aware of!

The setup is similar but you can use ngnix to cache the static content.
Mathics runs as a wsgi app so you can use uwsgi. The `Django
docs <https://uwsgi-docs.readthedocs.org/en/latest/tutorials/Django_and_nginx.html>`__
are a good reference.



.. |Packaging status| image:: https://repology.org/badge/vertical-allrepos/mathics.svg
   :target: https://repology.org/project/mathics/versions
