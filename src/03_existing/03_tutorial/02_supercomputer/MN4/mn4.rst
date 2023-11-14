MN4
---

The `MareNostrum 4 <https://www.bsc.es/marenostrum/marenostrum>`_ (MN4) supercomputer is designated as
a Special Scientific/Technical Infrastructure Facility by the Spanish Ministry of Economy,
Industry and Competitiveness and is part of the PRACE Research Infrastructure as one of the
7 Tier-0 Systems currently available for European scientists.

More details on its structure and specifications can be found in the
`MN4 documentation <https://www.bsc.es/user-support/mn4.php>`_.

Requirements
~~~~~~~~~~~~

The main requirement is to have access to the MN4 Supercomputer.

With the access granted, the first step is to connect to the MN4 Supercomputer.
Specific instructions to this end are provided in the `MN4 documentation <https://www.bsc.es/user-support/mn4.php>`_.


Deployment
~~~~~~~~~~

It is not necessary to deploy the Building Blocks, neither the Workflows, since they have
already been deployed and are available to all users by means of a module.

The users only need to load the required workflow manager (which in this example is PyCOMPSs),
singularity, and the ``permedcoe`` module, which enables to get any of the available workflows:

.. code-block:: console

    $ export COMPSS_PYTHON_VERSION=3
    $ module load COMPSs/3.2
    load java/8u131 (PATH, MANPATH, JAVA_HOME, JAVA_ROOT, JAVA_BINDIR, SDK_HOME, JDK_HOME, JRE_HOME)
    load papi/5.5.1 (PATH, LD_LIBRARY_PATH, C_INCLUDE_PATH)
    load PYTHON/3.7.4 (PATH, MANPATH, LD_LIBRARY_PATH, LIBRARY_PATH, PKG_CONFIG_PATH, C_INCLUDE_PATH, CPLUS_INCLUDE_PATH, PYTHONHOME, PYTHONPATH)
    load COMPSs/3.2 (PATH, CLASSPATH, MANPATH, GAT_LOCATION, COMPSS_HOME, JAVA_TOOL_OPTIONS, LDFLAGS, CPPFLAGS)
    $ module load singularity/3.5.2
    load SINGULARITY/3.5.2 (PATH)
    $ module use /apps/modules/modulefiles/tools/COMPSs/libraries
    $ module load permedcoe
    load permedcoe (PATH, MANPATH, IT_HOME)
    Using Python 3.7.4.

Now, the ``permedcoe`` tool is available, as well as some other commands that will ease the workflow get.
In particular, the available commands are:

get_covid19workflow
    Invoking this command will copy the Covid19 workflow in the current directory.
    Since all building blocks are available, there is no need to do anything else.

get_drug_synergies_workflow
    Invoking this command will copy the Drug Synergies workflow in the current directory.
    Since all building blocks are available, there is no need to do anything else.

get_single_drug_prediction_workflow
    Invoking this command will copy the Single Drug Prediction workflow in the current directory.
    Since all building blocks are available, there is no need to do anything else.

get_cancer_invasion_workflow
    Invoking this command will copy the Cancer Invasion workflow in the current directory.
    Since all building blocks are available, there is no need to do anything else.

For example, if the target workflow is Cancer Invasion, it is only necessary to:

.. code-block:: console

    $ get_cancer_invasion_workflow
    $ ls
    cancer-invasion-workflow
    $ cd cancer-invasion-workflow
    $cancer-invasion-workflow> ls
    BuildingBlocks  LICENSE  README.md  Resources  Tests  Workflow

The result is the same as in the local deployment.


Execution
~~~~~~~~~

Once achieved the workflow sources, the next step is to go inside the ``Workflow`` folder,
and inside the folder for the selected workflow manager (which in this case is PyCOMPSs):

.. code-block:: console

    $cancer-invasion-workflow> cd Workflow/PyCOMPSs
    $cancer-invasion-workflow/Workflow/PyCOMPSs> ls
    clean.sh  launch.sh  README.md  results  run.sh  src

Inside this folder, there is a ``launch.sh`` script that submits the execution of the
Cancer Invasion workflow to the queuing system (SLURM).

.. IMPORTANT::

    This script contains the workflow input parameters. So, if you want to run it with
    different configurations, it will be necessary to edit it and update the required
    parameters (e.g. other dataset, more replicas, or more simulation time).

.. code-block:: console

    $cancer-invasion-workflow/Workflow/PyCOMPSs> ./launch.sh
    load java/8u131 (PATH, MANPATH, JAVA_HOME, JAVA_ROOT, JAVA_BINDIR, SDK_HOME, JDK_HOME, JRE_HOME)
    load papi/5.5.1 (PATH, LD_LIBRARY_PATH, C_INCLUDE_PATH)
    load PYTHON/3.7.4 (PATH, MANPATH, LD_LIBRARY_PATH, LIBRARY_PATH, PKG_CONFIG_PATH, C_INCLUDE_PATH, CPLUS_INCLUDE_PATH, PYTHONHOME, PYTHONPATH)
    load COMPSs/3.2 (PATH, CLASSPATH, MANPATH, GAT_LOCATION, COMPSS_HOME, JAVA_TOOL_OPTIONS, LDFLAGS, CPPFLAGS)
    load SINGULARITY/3.5.2 (PATH)
    remove permedcoe (PATH, MANPATH, IT_HOME)
    Using Python 3.7.4.
    load permedcoe (PATH, MANPATH, IT_HOME)
    Using Python 3.7.4.
    SC Configuration:          default.cfg
    JobName:                   COMPSs
    Queue:                     default
    Deployment:                Master-Worker
    Reservation:               disabled
    Num Nodes:                 3
    Num Switches:              0
    GPUs per node:             0
    Job dependency:            None
    Exec-Time:                 02:00:00
    QoS:                       debug
    Constraints:               disabled
    Storage Home:              null
    Storage Properties:
    Storage container image:   false
    Storage cpu affinity:      disabled
    Other:                     --wall_clock_limit=7140
                --sc_cfg=default.cfg
                --qos=debug
                --worker_working_dir=/gpfs/projects/bscXX/bscXXYYY/PROYECTS/PerMedCoE/cancer-invasion-workflow/Workflow/PyCOMPSs
                --log_level=off
                --graph
                --tracing
                --generate_trace=true
                --python_interpreter=python3 /gpfs/projects/bscXX/bscXXYYY/PROYECTS/PerMedCoE/cancer-invasion-workflow/Workflow/PyCOMPSs/src/cancer_invasion.py /gpfs/projects/bscXX/bscXXYYY/PROYECTS/PerMedCoE/cancer-invasion-workflow/Workflow/PyCOMPSs/../../Resources/data//parameters_small.csv /gpfs/projects/bscXX/bscXXYYY/PROYECTS/PerMedCoE/cancer-invasion-workflow/Workflow/PyCOMPSs/results/ 5 4500

    Temp submit script is: /scratch/tmp/tmp.dxXN9zJOu7
    Requesting 144 processes
    Submitted batch job 30404848

The result of submitting the job is its identifier, which in this example is ``30404848``.
The job status can be checked with ``squeue``:

.. code-block:: console

    $ squeue
    JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
    30404848      main   COMPSs bscXXYYY  R       1:37      3 s01r1b25,s24r1b[60,63]

Which in this example, shows that it has already started and the workflow is being executed.

After executing the whole workflow, three main elements will appear:

compss-30404848.err
    This file contains the standard error messages shown during the execution.
    Any issue will appear in this file.

compss-30404848.out
    This file contains the standard output messages shown during the execution.
    In particular, it displays the PyCOMPSs execution output.

results
    This folder will contain the workflow results:

    .. code-block:: console

        $ cd results
        $results> tree
        .
        ├── plots
        │   ├── migration_bias.png
        │   └── migration_bias_ratio.png
        └── simulations
            ├── parameter_0
            │   └── [intermediate results]
            ├── parameter_1
            │   └── [intermediate results]
            ├── parameter_10
            │   └── [intermediate results]
            ├── parameter_2
            │   └── [intermediate results]
            ├── parameter_3
            │   └── [intermediate results]
            ├── parameter_4
            │   └── [intermediate results]
            ├── parameter_5
            │   └── [intermediate results]
            ├── parameter_6
            │   └── [intermediate results]
            ├── parameter_7
            │   └── [intermediate results]
            ├── parameter_8
            │   └── [intermediate results]
            └── parameter_9
                └── [intermediate results]

And thats it!
