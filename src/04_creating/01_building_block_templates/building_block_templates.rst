Building Block Templates
========================

Building Block template creation
--------------------------------

The first suggested step is to start with a template created with the
``permedcoe`` command:

.. code-block:: console

  permedcoe template building_block my_building_block

The result of this command is a folder containing a python package
with all scripts and base code to start developing your Building Block.

.. TIP::

    More than one Building Block can be included within the created package.

.. HINT::

    The Building Block template creation provides the main actions to be
    performed in order to complete your building block:

    .. code-block:: console

        Creating Building Block template
        ------------------------------------------
        To be completed:

        - definitions.py:(11):	TODO: Define your container.
        - main.py:(35):	TODO: (optional) Pure python code calling to PyCOMPSs tasks (that can be defined in this file or in another).
        - main.py:(39):	TODO: Define the binary to be used (can be within my_building_block_ASSETS_PATH (e.g. my_binary.sh)).
        - main.py:(40):	TODO: Define the inputs and output parameters.
        - main.py:(41):	TODO: Define a representative task name.
        - main.py:(42):	TODO: Define the binary parameters.
        - main.py:(43):	TODO: Define the binary parameters.
        - main.py:(44):	TODO: Define the binary parameters.
        - main.py:(45):	TODO: Add tmpdir=TMPDIR if the tmpdir will be used by the asset script.
        - main.py:(71):	TODO: Define the arguments required by the Building Block in definition.json file.
        - main.py:(73):	TODO: Declare how to run the binary specification (convert config into building_block_task call).
        - __main__.py:(13):	TODO: Add require_tmpdir=True if the asset requires to write within the tmpdir.
        ------------------------------------------



Package structure
-----------------

The package contains the following scripts:

.. code-block:: console

    .
    ├── build.sh
    ├── clean.sh
    ├── container
    │   ├── create_container.sh
    │   └── sample.def
    ├── install_sc.sh
    ├── install.sh
    ├── pyproject.toml
    ├── README.md
    ├── setup.cfg
    ├── setup.py
    ├── src
    │   └── my_building_block
    │       ├── assets
    │       │   └── my_binary.sh
    │       ├── definition.json
    │       ├── definitions.py
    │       ├── __init__.py
    │       ├── __main__.py
    │       └── main.py
    └── uninstall.sh


+-------------------------------------------+----------------------------------------------------------+
| **File name**                             | **Description**                                          |
+-------------------------------------------+----------------------------------------------------------+
| build.sh                                  | Script that builds the package                           |
+-------------------------------------------+----------------------------------------------------------+
| clean.sh                                  | Script that cleans build files                           |
+-------------------------------------------+----------------------------------------------------------+
| container/create_container.sh             | Script that builds the container defined in `sample.def` |
+-------------------------------------------+----------------------------------------------------------+
| container/sample.def                      | Container definition file                                |
+-------------------------------------------+----------------------------------------------------------+
| install_sc.sh                             | Manual installation script for supercomputer             |
+-------------------------------------------+----------------------------------------------------------+
| install.sh                                | Manual installation script                               |
+-------------------------------------------+----------------------------------------------------------+
| pyproject.toml                            | Building requirements                                    |
+-------------------------------------------+----------------------------------------------------------+
| README.md                                 | Package description                                      |
+-------------------------------------------+----------------------------------------------------------+
| setup.cfg                                 | Package configuration (Pypi metadata)                    |
+-------------------------------------------+----------------------------------------------------------+
| setup.py                                  | Package setup                                            |
+-------------------------------------------+----------------------------------------------------------+
| src/my_building_block/                    | Folder that contains the building block                  |
+-------------------------------------------+----------------------------------------------------------+
| src/my_building_block/assets/             | Folder that contains the building block assets           |
+-------------------------------------------+----------------------------------------------------------+
| src/my_building_block/assets/my_binary.sh | Asset script example                                     |
+-------------------------------------------+----------------------------------------------------------+
| src/my_building_block/definition.json     | Building Block parameters definition file                |
+-------------------------------------------+----------------------------------------------------------+
| src/my_building_block/definitions.py      | Building Block global definitions                        |
+-------------------------------------------+----------------------------------------------------------+
| src/my_building_block/__init__.py         | Package import resolver                                  |
+-------------------------------------------+----------------------------------------------------------+
| src/my_building_block/__main__.py         | Building block invocation file                           |
+-------------------------------------------+----------------------------------------------------------+
| src/my_building_block/main.py             | **Building block main file**                             |
+-------------------------------------------+----------------------------------------------------------+
| uninstall.sh                              | Uninstall script                                         |
+-------------------------------------------+----------------------------------------------------------+


Building Block structure
------------------------

There are a set of rules to implement a PerMedCoE compliant Building Block:

- Complete `definition.json` file with the Building Block required parameters.
  - Declare inputs and outputs.
- Complete `definitions.py` with the appropriate container file name.
  - Define the container/s within `definitions.py` file (`CONTAINER` variable).
- Provide a Python script `main.py` with the following structure and adapt to your needs (check all `TODO` marked lines):

  - Sample `main.py`:

    .. code-block:: python

        # Decorator imports
        from permedcoe import constraint       # To define constraints needs (e.g. number of cores)
        from permedcoe import container        # To define container related needs
        from permedcoe import binary           # To define binary to execute related needs
        from permedcoe import mpi              # To define an mpi binary to execute related needs (can not be used with @binary)
        from permedcoe import task             # To define task related needs
        # @task supported types
        from permedcoe import FILE_IN          # To define file type and direction
        from permedcoe import FILE_OUT         # To define file type and direction
        from permedcoe import FILE_INOUT       # To define file type and direction
        from permedcoe import DIRECTORY_IN     # To define directory type and direction
        from permedcoe import DIRECTORY_OUT    # To define directory type and direction
        from permedcoe import DIRECTORY_INOUT  # To define directory type and direction
        # Other permedcoe available functionalities
        from permedcoe import Arguments        # Arguments definition
        from permedcoe import get_environment  # Get variables from invocation (tmpdir, processes, gpus, memory)
        from permedcoe import TMPDIR           # Default tmpdir key

        # Import single container and assets definitions
        from NEW_NAME.definitions import NEW_NAME_ASSETS_PATH  # binary could be in this folder
        from NEW_NAME.definitions import NEW_NAME_CONTAINER
        from NEW_NAME.definitions import COMPUTING_UNITS

        def function_name(*args, **kwargs):
            """Extended python interface:
            To be used only with PyCOMPSs - Enables to define a workflow within the building block.
            Tasks are not forced to be binaries: PyCOMPSs supports tasks that are pure python code.

            # PyCOMPSs help: https://pycompss.readthedocs.io/en/latest/Sections/02_App_Development/02_Python.html

            Requirement: all tasks should be executed in a container (with the same container definition)
                         to ensure that they all have the same requirements.
            """
            print("Building Block entry point to be used with PyCOMPSs")
            # TODO: (optional) Pure python code calling to PyCOMPSs tasks (that can be defined in this file or in another).

        @container(engine="SINGULARITY", image=NEW_NAME_CONTAINER)
        @binary(binary="cp")                                        # TODO: Define the binary to be used (can be within NEW_NAME_ASSETS_PATH (e.g. my_binary.sh)).
        @task(input_file=FILE_IN, output_file=FILE_OUT)             # TODO: Define the inputs and output parameters.
        def building_block_task(                                    # TODO: Define a representative task name.
            input_file=None,                                        # TODO: Define the binary parameters.
            output_file=None,                                       # TODO: Define the binary parameters.
            verbose="-v"):                                          # TODO: Define the binary parameters.
            # TODO: Add tmpdir=TMPDIR if the tmpdir will be used by the asset script.
            """Summary.

            The Definition is equal to:
               cp <input_file> <output_file> -v
            Empty function since it represents a binary execution:

            :param input_file: Input file description, defaults to None
            :type input_file: str, optional
            :param verbose: Verbose description, defaults to "-v"
            :type verbose: str, optional
            # :param tmpdir: Temporary directory, defaults to TMPDIR
            # :type tmpdir: str, optional
            """
            pass

        def invoke(arguments, config):
            """Common interface.

            Args:
                arguments (args): Building Block parsed arguments.
                config (dict): Configuration dictionary.
            Returns:
                None
            """
            # TODO: Define the arguments required by the Building Block in definition.json file.

            # TODO: Declare how to run the binary specification (convert config into building_block_task call).
            # Sample config parameter get:
            #     operation = config["operation"]
            # Then operation can be used to tune the building_block_task parameters or even be a parameter.
            # Sample permedcoe environment get:
            #     env_vars = get_environment()
            # Retrieves the extra flags from permedcoe.
            input_file = arguments.model
            output_file = arguments.result
            # tmpdir = arguments.tmpdir
            building_block_task(input_file=input_file,
                                output_file=output_file)
                                # tmpdir=tmpdir)

  - Use the decorators provided by `permedcoe` package. They provide the capability to use the BB in various workflow managers transparently. In other words, the BB developer does not have to deal with the peculiarities of the workflow managers.

  - A BB can be a single executable, but it can be a more complex code if the `NEW_NAME_extended` function is implemented and used with PyCOMPSs.

  - It is necessary to have function (`invoke`) with a specific signature: `(arguments, config)`.

  - The `invoke` function provides the command line interface for the BB as shown in the [usage](#usage) section. In addition, it parses the Yaml config file and invokes the `NEW_NAME` function with the appropriate parameters.

  - The BB `binary` must be defined with the `@task`, `@binary` and `@container` decorators (`NEW_NAME_task`). This function needs to declare the binary flags, and it is invoked from the `NEW_NAME` function.

  - The `@task` decorator must declare the type of the file or directories for the binary invocation. In particular, using the parameter name and `FILE_IN`/`FILE_OUT`/`DIRECTORY_IN`/`DIRECTORY_OUT` to define if the parameter is a file or a directory and if the binary is consuming the file/directory or it is producing it.

  - Uncomment `tmpdir` variable if the binary uses an asset that requires to writting permissions. So the asset writes in a controlled temporary directory. Don't forget to set `require_tmpdir=True` in `__main__.py` within the `invoker` call.


Deployment
----------

Installation
~~~~~~~~~~~~

The package provides two ways to install this package (from Pypi and manually):

- From Pypi:

  After uploading the package to Pypi it can be installed as usual Python packages:

  .. code-block:: console

    pip install my_building_block

  or more specifically:

  .. code-block:: console

    python3 -m pip install my_building_block

- From source code:

  This package provides an automatic installation script, but it is necessary to install the ``permedcoe``
  package before the ``my_building_block`` package since it is required by ``my_building_block``.

  .. code-block:: console

    # Install permedcoe package
    git clone https://github.com/PerMedCoE/permedcoe.git
    cd permedcoe
    ./install.sh
    # Install my_building_block
    cd ../my_building_block
    ./install.sh


Usage
~~~~~

The ``my_building_block`` package provides a clear interface that allows it to be used with multiple workflow managers
(e.g. PyCOMPSs, NextFlow and Snakemake).

- Command line interface:

  Once installed the ``my_building_block`` package, it provides the ``my_building_block``
  command, that can be used from the command line. For example:

  .. code-block:: console

    $ my_building_block -h
    usage: my_building_block [-h] --model MODEL --result RESULT [-c CONFIG] [-d] [-l {debug,info,warning,error,critical}] [--tmpdir TMPDIR] [--processes PROCESSES] [--gpus GPUS] [--memory MEMORY]
                         [--mount_points MOUNT_POINTS]

    my_building_block Building Block short description. Give more details about the Building Block.

    options:
      -h, --help            show this help message and exit
      --model MODEL         (INPUT - str (file)) Input file (model)
      --result RESULT       (OUTPUT - str) Result file
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


  This interface can be used within any workflow manager that requires binaries (e.g. NextFlow and Snakemake).

  In addition, it can be used with PyCOMPSs by importing the decorated function or any other specific for PyCOMPSs.

  .. code-block:: python

    from my_building_block import building_block_task

    building_block_task(input=None,
                        output=None)

- Extension for PyCOMPSs:

  Moreover, a BB can also implement a Python function not limited to the input (file/s or directory/ies),
  output (file/s or directory/ies) and config (yaml file) signature.
  This enables application developers to use the BB with PyCOMPSs using Python objects instead of files among BBs.

  .. code-block:: python

    from my_building_block import function_name

    function_name(*args, **kwargs)  # specific interface

Uninstall
~~~~~~~~~

Uninstall can be done as usual ``pip`` packages:

There are two ways to uninstall this package, that depends on the way that it was installed (from Pypi or using ``install.sh``):

- From Pypi:

  .. code-block:: console

    pip uninstall my_building_block

  or more specifically:

  .. code-block:: console

    python3 -m pip uninstall my_building_block


- From manual installation (using ``install.sh``):

  .. code-block:: console

    ./uninstall.sh


  And then the folder can be cleaned as well using the ``clean.sh`` script.

  .. code-block:: console

    ./clean.sh


Best practices
--------------

There are a set of best practices suggested to BB developers:

- Use a code style:
    - `pep8 <https://www.python.org/dev/peps/pep-0008/>`_
    - `black <https://github.com/psf/black>`_

- Document your BB.
