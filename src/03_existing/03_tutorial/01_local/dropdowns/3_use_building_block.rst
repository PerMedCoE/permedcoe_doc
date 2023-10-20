Building Blocks can be used in two ways: from the command line or through their Python interface.

Command line
    Each Buildind Block provides a command (with the same name as the building block followed by ``_BB``)
    that can be launched from the command line. For example, the PhysiBoSS Building block
    (previously deployed) provides the ``PhysiBoSS_BB`` command.
    Its usage details can be checked using the ``--help`` or ``-h`` flag:

    .. code-block:: console

        $ PhysiBoSS_BB --help

        usage: PhysiBoSS_BB [-h] --sample SAMPLE --repetition REPETITION --prefix PREFIX --bnd_file BND_FILE --cfg_file CFG_FILE --parallel PARALLEL --max_time MAX_TIME --out_file OUT_FILE --err_file ERR_FILE
                            --results_dir RESULTS_DIR [-c CONFIG] [-d] [-l {debug,info,warning,error,critical}] [--tmpdir TMPDIR] [--processes PROCESSES] [--gpus GPUS] [--memory MEMORY] [--mount_points MOUNT_POINTS]

        This building block is used to perform a multiscale simulation of a population of cells using PhysiBoSS. The tool uses the different Boolean models personalised by the Personalise patient building block and
        with the mutants selected by the High-throughput mutant analysis building block. More information on this tool can be found in [Ponce-de-Leon et al.
        (2022)](https://www.biorxiv.org/content/10.1101/2022.01.06.468363v1) and the [PhysiBoSS GitHub repository](https://github.com/PhysiBoSS/PhysiBoSS).

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


    Thanks to the ``-h`` or ``--help``flag, the PhysiBoSS Building Block inputs and outputs are
    shown and described. All ``INPUT`` and ``OUTPUT`` flags are required in order to execute the
    Building Block. The rest of the parameters are optional and can be used to define particular
    options (e.g. ``-l`` or ``--log_level`` can be used to define the level of information to
    be printed, or the ``--tmpdir`` can be used to define a specific folder that will be mounted
    in the associated container -- this can be useful if the input parameters are in a non
    default mounted folder).


    .. CAUTION::

        All Building Blocks require the ``PERMEDCOE_IMAGES`` environment variable.
        Otherwise, it will raise the following exception:

        .. code-block:: console

            Traceback (most recent call last):
            File "/home/user/.local/bin/meta_analysis_BB", line 5, in <module>
                from meta_analysis_BB.__main__ import main
            File "/home/user/.local/lib/python3.10/site-packages/meta_analysis_BB/__init__.py", line 6, in <module>
                from meta_analysis_BB.main import *
            File "/home/user/.local/lib/python3.10/site-packages/meta_analysis_BB/main.py", line 13, in <module>
                from meta_analysis_BB.definitions import CONTAINER
            File "/home/user/.local/lib/python3.10/site-packages/meta_analysis_BB/definitions.py", line 2, in <module>
                from permedcoe.bb import CONTAINER_PATH
            File "/home/user/.local/lib/python3.10/site-packages/permedcoe/bb.py", line 24, in <module>
                CONTAINER_PATH = get_container_path()
            File "/home/user/.local/lib/python3.10/site-packages/permedcoe/bb.py", line 21, in get_container_path
                raise Exception("Please define %s environment variable with the path." % CONTAINER_PATH_VN)
            Exception: Please define PERMEDCOE_IMAGES environment variable with the path.


    The result of executing the Building Block will be a one or more output files that can
    potentially be used by other Building Block.

Python interface
    Since the Building Blocks are developed in Python, they offer a Python interface
    that can be used from Python applications.

    For example, the PhysiBoSS Building Block can be used as follows:

    .. code-block:: python

        from PhysiBoSS_BB import physiboss

        physiboss(
            sample="C141",
            repetition=1,
            prefix="epithelial_cell_2_personalized",
            bnd_file="/path/to/input_file.bnd",
            cfg_file="/path/to/input_file.cfg",
            out_file="/path/to/output_file.txt",
            err_file="/path/to/output_file.txt",
            results_dir="/path/to/results",
            parallel=1,
            max_time=8640,
            tmpdir="/path/to/tmpdir"
        )

    Note that this interface requires the same parameters as the command line interface.

    .. TIP::

        Some Building Blocks may provide more functions since they serve for multiple
        purposes (e.g. MaBoSS for default behaviour or for sensitivity analysis).

    Specific details about the python interface of each Building Block can be
    consulted in the ``main.py`` file of each Building Block repository.

    .. IMPORTANT::

        The functions provided by the Building Blocks have a set of decorators on top
        of them that are responsible of hiding the management complexities, but also
        to enable the automatic parallelization using **PyCOMPSs**. Consequently,
        any application making use of Building Blocks gets automatically parallelized
        if run using `PyCOMPSs <https://pycompss.readthedocs.io/en/stable/>`_.
        If the application is run using Python directly, it will be executed sequentially.

