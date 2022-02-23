:fa:`cogs` Base Package Components
==================================

This section provides an overview of ``permedcoe`` package components and functionalities. Further to a Python API
for Building Block development, the package provides a command line tool that eases the execution of building blocks
or applications, and creating templates for them.

Python API
----------

The ``permedcoe`` package provides a set of public decorators, parameter type
definitions and functions to be used for Building Block implementation.

- Public decorators:

    .. code-block:: python

        from permedcoe import container
        from permedcoe import constraint
        from permedcoe import binary
        from permedcoe import mpi
        from permedcoe import task

- Parameter type definitions:

    .. code-block:: python

        from permedcoe import FILE_IN
        from permedcoe import FILE_OUT
        from permedcoe import DIRECTORY_IN
        from permedcoe import DIRECTORY_OUT

- Functions:

    .. code-block:: python

        from permedcoe import set_debug
        from permedcoe import invoke
        from permedcoe import get_environment

The usage of these decorators, type definitions and functions is described in
:ref:`04_creating/01_building_block_templates/building_block_templates:Building block structure`.

Command line
------------

The ``permedcoe`` command can be used to execute individual Building Blocks or applications. 
It can also be used to create empty building block or application templates.

.. code-block:: console

  $ permedcoe -h
  usage: permedcoe [-h] [-d] [-l {debug,info,warning,error,critical}] {execute,x,template,t} ...

  positional arguments:
    {execute,x,template,t}
      execute (x)         Execute a building block.
      template (t)        Shows an example of the requested template.

  optional arguments:
    -h, --help            show this help message and exit
    -d, --debug           Enable debug mode. Overrides log_level (default: False)
    -l {debug,info,warning,error,critical}, --log_level {debug,info,warning,error,critical}
                          Set logging level. (default: error)



Execution
~~~~~~~~~

The execution of building blocks or applications with the ``permedcoe`` command
is performed by indicating ``execute`` (or ``x``) after ``permedcoe``.
Adding the ``-h`` flag after `permedcoe execute` can be used to access help:

.. code-block:: console

  $ permedcoe execute -h
  usage: permedcoe execute [-h] {building_block,bb,application,app} ...

  positional arguments:
    {building_block,bb,application,app}
      building_block (bb)
                          Execute a building block.
      application (app)   Execute an application.

  optional arguments:
    -h, --help            show this help message and exit


Building Block execution
^^^^^^^^^^^^^^^^^^^^^^^^

To execute an available building block, follow ``permedcoe execute`` by ``building_block`` (or
``bb``).

.. WARNING::

    The building block to be executed must be installed, and its name
    (as imported in Python) has to be provided.

.. code-block:: console

    $ permedcoe execute building_block -h
    usage: permedcoe execute building_block [-h] [-i INPUT [INPUT ...]] [-o OUTPUT [OUTPUT ...]]
                                        [-c CONFIG] [-d] [-l {debug,info,warning,error,critical}]
                                        [--tmpdir TMPDIR] [--processes PROCESSES] [--gpus GPUS]
                                        [--memory MEMORY] [--mount_points MOUNT_POINTS]
                                        name

    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT [INPUT ...], --input INPUT [INPUT ...]
                            Input file/s or directory path/s (default: None)
      -o OUTPUT [OUTPUT ...], --output OUTPUT [OUTPUT ...]
                            Output file/s or directory path/s (default: None)
      -c CONFIG, --config CONFIG
                            Configuration file path (default: None)
      -d, --debug           Enable Building Block debug mode. Overrides log_level (default: False)
      -l {debug,info,warning,error,critical}, --log_level {debug,info,warning,error,critical}
                            Set logging level (default: None)
      --tmpdir TMPDIR       Temp directory to be mounted in the container (default: None)
      --processes PROCESSES
                            Number of processes for MPI executions (default: None)
      --gpus GPUS           Requirements for GPU jobs (default: None)
      --memory MEMORY       Memory requirement (default: None)
      --mount_points MOUNT_POINTS
                            Comma separated alias:folder to be mounted in the container (default: None)



Application execution
^^^^^^^^^^^^^^^^^^^^^

Alternatively, ``permedcoe execute`` can be followed by ``application`` (or
``app``) to execute an application.

.. WARNING::

    The workflow manager selected must be available in the system.

.. code-block:: console

    permedcoe execute application -h None)
    usage: permedcoe execute application [-h] [-w {none,pycompss,nextflow,snakemake}]
                                        [-f FLAGS [FLAGS ...]]
                                        name [parameters [parameters ...]]

    positional arguments:
      name                  Application to execute
      parameters            Application parameters (default: None)

    optional arguments:
      -h, --help            show this help message and exit
      -w {none,pycompss,nextflow,snakemake}, --workflow_manager {none,pycompss,nextflow,snakemake}
                            Workflow manager to use (default: none)
      -f FLAGS [FLAGS ...], --flags FLAGS [FLAGS ...]
                            Workflow manager flags (default: None)



Template creation
~~~~~~~~~~~~~~~~~

The ``permedcoe`` command can also be used to create an empty building block
or application template:

.. code-block:: console

  $ permedcoe template -h
  usage: permedcoe template [-h] [-t {all,pycompss,nextflow,snakemake}]
                            {bb,building_block,app,application} name

  positional arguments:
    {bb,building_block,app,application}
                          Creates a Building Block or Application template.
    name                  Building Block or Application name.

  optional arguments:
    -h, --help            show this help message and exit
    -t {all,pycompss,nextflow,snakemake}, --type {all,pycompss,nextflow,snakemake}
                          Application type. (default: all)

.. HINT::

     Once the artifact is created, it describes the minimal expected implementation
     actions to be done in order to complete a Building Block or an application.
