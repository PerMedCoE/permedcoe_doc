The Building Block template already provides a sample container located in:

.. code-block::

     $ tree my_building_block/container

     my_building_block/container/
     ├── create_container.sh
     ├── sample.def
     └── sample.sif

This folder contains:

``sample.def``
    Container definition file: Recipe to create the container.

``create_container.sh``
    Container creation script from the container definition file.
    It invokes Singularity with ``sample.def`` to generate the container
    (``sample.sif``).

``sample.sif``
    Singularity container from ``sample.def``.
