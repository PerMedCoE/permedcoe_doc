The Building Block template already provides a sample container definition
located in:

.. code-block:: CONSOLE

     $ tree my_building_block/container

     my_building_block/container/
     ├── create_container.sh
     └── sample.def

This folder contains:

``sample.def``
    Container definition file: Recipe to create the container.

``create_container.sh``
    Container creation script from the container definition file.
    It invokes Singularity with ``sample.def`` to generate the container
    (``sample.sif``).

In order to continue with the tutorial it is necessary to create the sample
container from  ``sample.def`` with ``create_container.sh``:

.. code-block:: CONSOLE

    $ cd my_building_block/container
    $ ./create_container.sh

.. CAUTION::

    The ``create_container.sh`` script requires root privileges and assumes
    that the ``singularity`` command is available in ``$PATH`` as root.

    If ``sudo: singularity: command not found`` error happens, the container
    can be created by defining explicitly the singularity path:

    .. code-block:: CONSOLE

        $ sudo /usr/local/bin/singularity build sample.sif sample.def
