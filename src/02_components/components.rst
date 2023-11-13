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
        from permedcoe import julia

- Parameter type definitions:

    .. code-block:: python

        from permedcoe import FILE_IN
        from permedcoe import FILE_OUT
        from permedcoe import FILE_INOUT
        from permedcoe import DIRECTORY_IN
        from permedcoe import DIRECTORY_OUT
        from permedcoe import DIRECTORY_INOUT
        from permedcoe import Type
        from permedcoe import StdIOStream
        from permedcoe import STDIN
        from permedcoe import STDOUT
        from permedcoe import STDERR

- Functions:

    .. code-block:: python

        from permedcoe import set_debug
        from permedcoe import get_environment

- Globals:

    .. code-block:: python

        from permedcoe import TMPDIR

The usage of these decorators, type definitions and functions is described in
:ref:`04_creating/01_building_block_templates/building_block_templates:Building block structure`.

Command line
------------

The ``permedcoe`` command can be used to execute individual Building Blocks or applications.
It can also be used to create empty building block or application templates.

.. code-block:: console

  $ permedcoe -h
  usage: permedcoe [-h] [-d] [-l {debug,info,warning,error,critical}] {execute,x,template,t,deploy,d} ...

  positional arguments:
    {execute,x,template,t,deploy,d}
      execute (x)         Execute a building block.
      template (t)        Shows an example of the requested template.
      deploy (d)          Download and deploy the requested workflow or building block.

  options:
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
    usage: permedcoe execute building_block [-h] name ...

    positional arguments:
      name        Building Block to execute
      parameters  Building Block parameters

    options:
      -h, --help  show this help message and exit


.. TIP::

    Specifying the name of the building block provides the parameters details.
    This example shows the parameters of the PhysiBoSS Building Block:

    .. code-block:: console

        $ permedcoe execute building_block PhysiBoSS_BB -h
        usage: permedcoe [-h] --sample SAMPLE --repetition REPETITION --prefix PREFIX --bnd_file BND_FILE
                         --cfg_file CFG_FILE --parallel PARALLEL --max_time MAX_TIME --out_file OUT_FILE
                         --err_file ERR_FILE --results_dir RESULTS_DIR [-c CONFIG] [-d]
                         [-l {debug,info,warning,error,critical}] [--tmpdir TMPDIR] [--processes PROCESSES]
                         [--gpus GPUS] [--memory MEMORY] [--mount_points MOUNT_POINTS]

        This building block is used to perform a multiscale simulation of a population of cells using
        PhysiBoSS. The tool uses the different Boolean models personalised by the Personalise patient building
        block and with the mutants selected by the High-throughput mutant analysis building block. More
        information on this tool can be found in [Ponce-de-Leon et al.
        (2022)](https://www.biorxiv.org/content/10.1101/2022.01.06.468363v1) and the [PhysiBoSS GitHub
        repository](https://github.com/PhysiBoSS/PhysiBoSS).

        options:
          -h, --help            show this help message and exit
          --sample SAMPLE       (INPUT - str) Patient's identifier
          --repetition REPETITION
                                (INPUT - int) Number of repetition to be performed
          --prefix PREFIX       (INPUT - str) Name of the model
          --bnd_file BND_FILE   (INPUT - str (file)) Name of the model's BND file
          --cfg_file CFG_FILE   (INPUT - str (file)) Name of the model's CFG file
          --parallel PARALLEL   (INPUT - int) Internal parallelism
          --max_time MAX_TIME   (INPUT - int) PhysiBoSS simulation maximum time
          --out_file OUT_FILE   (OUTPUT - str) Main output of the PhysiBoSS run
          --err_file ERR_FILE   (OUTPUT - str) Error output of the PhysiBoSS run
          --results_dir RESULTS_DIR
                                (OUTPUT - str) Results directory
          -c CONFIG, --config CONFIG
                                (CONFIG) Configuration file path
          -d, --debug           Enable Building Block debug mode. Overrides log_level
          -l {debug,info,warning,error,critical}, --log_level {debug,info,warning,error,critical}
                                Set logging level
          --tmpdir TMPDIR       Temp directory to be mounted in the container
          --processes PROCESSES
                                Number of processes for MPI executions
          --gpus GPUS           Requirements for GPU jobs
          --memory MEMORY       Memory requirement
          --mount_points MOUNT_POINTS
                                Comma separated alias:folder to be mounted in the container


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
