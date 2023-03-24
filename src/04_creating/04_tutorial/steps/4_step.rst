In order to test the Building Block it is necessary to install it.
To this end, the Building Block already includes a ``install.sh`` script:

.. code-block:: CONSOLE

    $ my_building_block/./install.sh

Once installed the ``my_building_block`` package, it provides the
``my_building_block`` command, that can be used from the command line.
For example:

.. code-block:: CONSOLE

  $ my_building_block -h
  usage: my_building_block [-h] --model MODEL --result RESULT [-c CONFIG] [-d]
                           [-l {debug,info,warning,error,critical}] [--tmpdir TMPDIR]
                           [--processes PROCESSES] [--gpus GPUS] [--memory MEMORY]
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



And to test the Building Block, provide the necessary parameters:

.. code-block:: CONSOLE

    # Generate a testing files
    $ echo "hello world" > hi.txt
    $ my_building_block --model hi.txt --result bye.txt

The result will be the appearance of the ``bye.txt`` file, which is a copy of ``hi.txt``.
