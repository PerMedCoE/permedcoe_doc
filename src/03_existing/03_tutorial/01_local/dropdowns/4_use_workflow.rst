Existing workflows that have been deployed have a particular structure:

.. code-block:: console

    $ cd covid-19-workflow
    $covid-19-workflow> ls
    BuildingBlocks  LICENSE  README.md  Resources  Tests  Workflow

The contents are:

LICENSE
    The workflow license file.

README.md
    The workflow description file.
    It provides details about the workflow.

BuildingBlocks
    This folder contains a set of helper scripts to install or
    uninstall the Workflow required Building Blocks.
    They are used by the automatic deployment performed by
    the ``permedcoe`` package and command.

Resources
    This folder contains a set of minimal data in order
    to run the Workflow (i.e. testing dataset).

Tests
    This folder contains a set of testing scripts.
    These scripts are able to run each individual
    Building Block for debugging purposes.

Workflow
    This is the **MAIN FOLDER** since it contains the workflow files.
    In particular, it can contain three subfolders:

    .. code-block:: console

        $covid-19-workflow> cd Workflow
        $covid-19-workflow/Workflow> ls
        NextFlow  PyCOMPSs  SnakeMake

    Each subfolder is aimed at contain the workflow for that
    particular workflow manager. For example, the covid-19 workflow
    is available in for the three workflow managers.

    One peculiarity of the three workflow managers is that Snakemake
    and NextFlow workflows use the command line interface of the
    Building Blocks involved, while PyCOMPSs workflow uses their
    Python interface.

    In addition to the workflow file, each folder also includes
    a ``launch.sh`` script in order to ease the workflow execution.

As seen in the contents, the ``Workflow`` folder contains the main
workflow files. Consequently, it is necessary to go inside that
folder in order to execute the workflow.

.. code-block:: console

        $covid-19-workflow> cd Workflow
        $covid-19-workflow/Workflow> 

The next step is to decide which workflow manager is going to be
used:

.. code-block:: console

        $covid-19-workflow/Workflow> ls
        NextFlow  PyCOMPSs  SnakeMake

The covid-19 workflow is available for NextFlow, SnakeMake and PyCOMPSs.

.. IMPORTANT::

    The workflow manager **MUST** be installed in the machine in
    order to run the workflow.

    - `NextFlow installation <https://www.nextflow.io/docs/latest/getstarted.html#installation>`_
    - `SnakeMake installation <https://snakemake.readthedocs.io/en/stable/getting_started/installation.html>`_
    - `PyCOMPSs installation <https://pycompss.readthedocs.io/en/stable/Sections/00_Quickstart.html#install-compss>`_

Once decided the workflow manager to be used, specific details about how to run the
workflow with each of them is provided in the next drop-down sections:

.. dropdown:: NextFlow
    :animate: fade-in

    If the chosen workflow manager is NextFlow, the next step is to go inside the folder:

    .. code-block:: console

        $covid-19-workflow/Workflow> cd NextFlow
        $covid-19-workflow/Workflow/NextFlow> ls
        covid19_pilot.nf  launch.sh

    covid-19_pilot.nf
        This is the workflow script.

    launch.sh
        Script that launches the workflow with the testing dataset.

    The way to run the workflow is:

    .. code-block:: console

        $covid-19-workflow/Workflow/NextFlow> ./launch.sh

        [Wait for completion]


    And the results will be stored within the current folder within the ``results`` folder.

.. dropdown:: SnakeMake
    :animate: fade-in

    If the chosen workflow manager is SnakeMake, the next step is to go inside the folder:

    .. code-block:: console

        $covid-19-workflow/Workflow> cd SnakeMake
        $covid-19-workflow/Workflow/SnakeMake> ls
        config.yml  launch.sh  run.sh  Snakefile  split.sh

    config.yml
        Configuration file.

    launch.sh
        Script that launches the workflow with the testing dataset using SLURM.

    run.sh
        Script that launches the workflow with the testing dataset.

    Snakefile
        This is the workflow script.

    split.sh
        Helper script required by the Snakefile.

    The way to run the workflow is:

    .. code-block:: console

        $covid-19-workflow/Workflow/SnakeMake> ./run.sh

        [Wait for completion]


    And the results will be stored within the current folder within the ``results`` folder.

.. dropdown:: PyCOMPSs
    :animate: fade-in

    If the chosen workflow manager is PyCOMPSs, the next step is to go inside the folder:

    .. code-block:: console

        $covid-19-workflow/Workflow> cd PyCOMPSs
        $covid-19-workflow/Workflow/PyCOMPSs> ls
        0_prepare_dataset.sh
        a_launch.sh
        a_run.sh
        b_1_launch.sh
        b_1_run.sh
        b_2_launch_per_patient.sh
        b_2_launch.sh
        b_2_run_per_patient.sh
        b_2_run.sh
        b_3_launch.sh
        b_3_run.sh
        clean.sh
        README.md
        src
        src_split

    0_prepare_dataset.sh
        This script downloads and configures the testing dataset.
        It just requires to be executed once and without parameters (``./0_prepare_dataset.sh``)

    a_launch.sh
        Script that launches the workflow with the testing dataset within a supercomputer.

    a_run.sh
        Script that runs the workflow with the testing dataset.

    src
        Folder that contains the workflow written in Python and using PyCOMPSs.

    clean.sh
        Helper script that cleans the current folder after running the workflow. Use with caution since it removes all result files.

    src_split and ``b_\*`` scripts
        The ``src_split`` folder contains the workflow split in three parts, so that it can be executed partially or even
        in different machines. Accordingly, the ``b_\*`` scripts are aimed at launching or running each part.

    The way to run the workflow (automatically parallelized with PyCOMPSs) is:

    .. code-block:: console

        $covid-19-workflow/Workflow/PyCOMPSs> ./a_run.sh

        WARNING: PERMEDCOE_IMAGES environment variable not set. Using default: /home/user/github/projects/PerMedCoE/BuildingBlocks/Resources/images/
        [ INFO ] Inferred PYTHON language
        [ INFO ] Using default location for project file: /opt/COMPSs//Runtime/configuration/xml/projects/default_project.xml
        [ INFO ] Using default location for resources file: /opt/COMPSs//Runtime/configuration/xml/resources/default_resources.xml
        [ INFO ] Using default execution type: compss

        ----------------- Executing covid19_pilot.py --------------------------

        WARNING: COMPSs Properties file is null. Setting default values
        [(834)    API]  -  Starting COMPSs Runtime v3.2.rc2310 (build 20231017-1637.r77b4be4b8ac4f722dd3de105161229b849a545d4)
        ---------------------------
        | Covid-19 Pilot Workflow |
        ---------------------------

        >>> WELCOME TO THE PILOT WORKFLOW
        > Parameters:
            - metadata file: /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/../../Resources/data/metadata_small.tsv
            - model prefix: /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/../../Resources/data/epithelial_cell_2
            - output folder: /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/
            - ko file: /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/ko_file.txt
            - replicates: 2
            - model: epithelial_cell_2
            - data folder: /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/../../Resources/data
            - max time: 100


        KO file not detected, running MABOSS
        > SINGLE CELL PROCESSING C141
        > PERSONALIZING PATIENT C141
        >> prefix: epithelial_cell_2_personalized
        >>> Repetition: 1
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized_1.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized_1.err
        >>> Repetition: 2
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized_2.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized_2.err
        >> prefix: epithelial_cell_2_personalized__M_ko
        >>> Repetition: 1
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__M_ko_1.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__M_ko_1.err
        >>> Repetition: 2
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__M_ko_2.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__M_ko_2.err
        >> prefix: epithelial_cell_2_personalized__CASP9_cell_active_ko
        >>> Repetition: 1
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__CASP9_cell_active_ko_1.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__CASP9_cell_active_ko_1.err
        >>> Repetition: 2
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__CASP9_cell_active_ko_2.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__CASP9_cell_active_ko_2.err
        >> prefix: epithelial_cell_2_personalized__CASP8_ko
        >>> Repetition: 1
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__CASP8_ko_1.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__CASP8_ko_1.err
        >>> Repetition: 2
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__CASP8_ko_2.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__CASP8_ko_2.err
        >> prefix: epithelial_cell_2_personalized__FASLG_ko
        >>> Repetition: 1
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__FASLG_ko_1.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__FASLG_ko_1.err
        >>> Repetition: 2
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__FASLG_ko_2.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__FASLG_ko_2.err
        >> prefix: epithelial_cell_2_personalized__FADD_ko
        >>> Repetition: 1
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__FADD_ko_1.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__FADD_ko_1.err
        >>> Repetition: 2
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__FADD_ko_2.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__FADD_ko_2.err
        >> prefix: epithelial_cell_2_personalized__CASP3_ko
        >>> Repetition: 1
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__CASP3_ko_1.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__CASP3_ko_1.err
        >>> Repetition: 2
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__CASP3_ko_2.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__CASP3_ko_2.err
        >> prefix: epithelial_cell_2_personalized__FAS_FASL_complex_ko
        >>> Repetition: 1
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__FAS_FASL_complex_ko_1.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__FAS_FASL_complex_ko_1.err
        >>> Repetition: 2
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__FAS_FASL_complex_ko_2.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__FAS_FASL_complex_ko_2.err
        >> prefix: epithelial_cell_2_personalized__Apoptosome_complex_ko
        >>> Repetition: 1
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__Apoptosome_complex_ko_1.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__Apoptosome_complex_ko_1.err
        >>> Repetition: 2
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__Apoptosome_complex_ko_2.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_results/output_C141_epithelial_cell_2_personalized__Apoptosome_complex_ko_2.err
        > SINGLE CELL PROCESSING C142
        > PERSONALIZING PATIENT C142
        >> prefix: epithelial_cell_2_personalized
        >>> Repetition: 1
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized_1.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized_1.err
        >>> Repetition: 2
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized_2.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized_2.err
        >> prefix: epithelial_cell_2_personalized__M_ko
        >>> Repetition: 1
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__M_ko_1.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__M_ko_1.err
        >>> Repetition: 2
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__M_ko_2.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__M_ko_2.err
        >> prefix: epithelial_cell_2_personalized__CASP9_cell_active_ko
        >>> Repetition: 1
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__CASP9_cell_active_ko_1.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__CASP9_cell_active_ko_1.err
        >>> Repetition: 2
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__CASP9_cell_active_ko_2.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__CASP9_cell_active_ko_2.err
        >> prefix: epithelial_cell_2_personalized__CASP8_ko
        >>> Repetition: 1
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__CASP8_ko_1.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__CASP8_ko_1.err
        >>> Repetition: 2
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__CASP8_ko_2.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__CASP8_ko_2.err
        >> prefix: epithelial_cell_2_personalized__FASLG_ko
        >>> Repetition: 1
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__FASLG_ko_1.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__FASLG_ko_1.err
        >>> Repetition: 2
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__FASLG_ko_2.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__FASLG_ko_2.err
        >> prefix: epithelial_cell_2_personalized__FADD_ko
        >>> Repetition: 1
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__FADD_ko_1.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__FADD_ko_1.err
        >>> Repetition: 2
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__FADD_ko_2.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__FADD_ko_2.err
        >> prefix: epithelial_cell_2_personalized__CASP3_ko
        >>> Repetition: 1
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__CASP3_ko_1.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__CASP3_ko_1.err
        >>> Repetition: 2
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__CASP3_ko_2.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__CASP3_ko_2.err
        >> prefix: epithelial_cell_2_personalized__FAS_FASL_complex_ko
        >>> Repetition: 1
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__FAS_FASL_complex_ko_1.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__FAS_FASL_complex_ko_1.err
        >>> Repetition: 2
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__FAS_FASL_complex_ko_2.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__FAS_FASL_complex_ko_2.err
        >> prefix: epithelial_cell_2_personalized__Apoptosome_complex_ko
        >>> Repetition: 1
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__Apoptosome_complex_ko_1.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__Apoptosome_complex_ko_1.err
        >>> Repetition: 2
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__Apoptosome_complex_ko_2.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_results/output_C142_epithelial_cell_2_personalized__Apoptosome_complex_ko_2.err
        >> prefix: epithelial_cell_2_personalized
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_replicates_analysis/epithelial_cell_2_personalized.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_replicates_analysis/epithelial_cell_2_personalized.err
        >> prefix: epithelial_cell_2_personalized__M_ko
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_replicates_analysis/epithelial_cell_2_personalized__M_ko.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_replicates_analysis/epithelial_cell_2_personalized__M_ko.err
        >> prefix: epithelial_cell_2_personalized__CASP9_cell_active_ko
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_replicates_analysis/epithelial_cell_2_personalized__CASP9_cell_active_ko.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_replicates_analysis/epithelial_cell_2_personalized__CASP9_cell_active_ko.err
        >> prefix: epithelial_cell_2_personalized__CASP8_ko
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_replicates_analysis/epithelial_cell_2_personalized__CASP8_ko.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_replicates_analysis/epithelial_cell_2_personalized__CASP8_ko.err
        >> prefix: epithelial_cell_2_personalized__FASLG_ko
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_replicates_analysis/epithelial_cell_2_personalized__FASLG_ko.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_replicates_analysis/epithelial_cell_2_personalized__FASLG_ko.err
        >> prefix: epithelial_cell_2_personalized__FADD_ko
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_replicates_analysis/epithelial_cell_2_personalized__FADD_ko.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_replicates_analysis/epithelial_cell_2_personalized__FADD_ko.err
        >> prefix: epithelial_cell_2_personalized__CASP3_ko
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_replicates_analysis/epithelial_cell_2_personalized__CASP3_ko.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_replicates_analysis/epithelial_cell_2_personalized__CASP3_ko.err
        >> prefix: epithelial_cell_2_personalized__FAS_FASL_complex_ko
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_replicates_analysis/epithelial_cell_2_personalized__FAS_FASL_complex_ko.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_replicates_analysis/epithelial_cell_2_personalized__FAS_FASL_complex_ko.err
        >> prefix: epithelial_cell_2_personalized__Apoptosome_complex_ko
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_replicates_analysis/epithelial_cell_2_personalized__Apoptosome_complex_ko.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C141/physiboss_replicates_analysis/epithelial_cell_2_personalized__Apoptosome_complex_ko.err
        >> prefix: epithelial_cell_2_personalized
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_replicates_analysis/epithelial_cell_2_personalized.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_replicates_analysis/epithelial_cell_2_personalized.err
        >> prefix: epithelial_cell_2_personalized__M_ko
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_replicates_analysis/epithelial_cell_2_personalized__M_ko.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_replicates_analysis/epithelial_cell_2_personalized__M_ko.err
        >> prefix: epithelial_cell_2_personalized__CASP9_cell_active_ko
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_replicates_analysis/epithelial_cell_2_personalized__CASP9_cell_active_ko.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_replicates_analysis/epithelial_cell_2_personalized__CASP9_cell_active_ko.err
        >> prefix: epithelial_cell_2_personalized__CASP8_ko
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_replicates_analysis/epithelial_cell_2_personalized__CASP8_ko.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_replicates_analysis/epithelial_cell_2_personalized__CASP8_ko.err
        >> prefix: epithelial_cell_2_personalized__FASLG_ko
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_replicates_analysis/epithelial_cell_2_personalized__FASLG_ko.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_replicates_analysis/epithelial_cell_2_personalized__FASLG_ko.err
        >> prefix: epithelial_cell_2_personalized__FADD_ko
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_replicates_analysis/epithelial_cell_2_personalized__FADD_ko.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_replicates_analysis/epithelial_cell_2_personalized__FADD_ko.err
        >> prefix: epithelial_cell_2_personalized__CASP3_ko
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_replicates_analysis/epithelial_cell_2_personalized__CASP3_ko.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_replicates_analysis/epithelial_cell_2_personalized__CASP3_ko.err
        >> prefix: epithelial_cell_2_personalized__FAS_FASL_complex_ko
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_replicates_analysis/epithelial_cell_2_personalized__FAS_FASL_complex_ko.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_replicates_analysis/epithelial_cell_2_personalized__FAS_FASL_complex_ko.err
        >> prefix: epithelial_cell_2_personalized__Apoptosome_complex_ko
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_replicates_analysis/epithelial_cell_2_personalized__Apoptosome_complex_ko.out
            - /home/user/github/projects/PerMedCoE/covid-19-workflow/Workflow/PyCOMPSs/results/C142/physiboss_replicates_analysis/epithelial_cell_2_personalized__Apoptosome_complex_ko.err
        [(1277810)    API]  -  Execution Finished

        ------------------------------------------------------------



    And the results will be stored within the current folder within the ``results`` folder.

    .. code-block:: console

        $covid-19-workflow/Workflow/PyCOMPSs> cd results
        $covid-19-workflow/Workflow/PyCOMPSs/results> tree

        .
        ├── C141
        │   ├── personalize_patient
        │   │   └── [personalize_patient results]
        │   ├── physiboss_replicates_analysis
        │   │   └── [physiboss_replicates_analysis results]
        │   ├── physiboss_results
        │   │   └── [physiboss_results results]
        │   └── single_cell_processing
        │   │   └── [single_cell_processing results]
        ├── C142
        │   ├── personalize_patient
        │   │   └── [personalize-patient-results]
        │   ├── physiboss_replicates_analysis
        │   │   └── [physiboss_replicates_analysis results]
        │   ├── physiboss_results
        │   │   └── [physiboss_results results]
        │   └── single_cell_processing
        │       └── [single_cell_processing results]
        └── meta_analysis
            ├── cd8s_C141_Apoptosome_complex_ko_.png
            ├── cd8s_C141_CASP3_ko_.png
            ├── cd8s_C141_CASP8_ko_.png
            ├── cd8s_C141_CASP9_cell_active_ko_.png
            ├── cd8s_C141_FADD_ko_.png
            ├── cd8s_C141_FAS_FASL_complex_ko_.png
            ├── cd8s_C141_FASLG_ko_.png
            ├── cd8s_C141_M_ko_.png
            ├── cd8s_C141.png
            ├── cd8s_C142_Apoptosome_complex_ko_.png
            ├── cd8s_C142_CASP3_ko_.png
            ├── cd8s_C142_CASP8_ko_.png
            ├── cd8s_C142_CASP9_cell_active_ko_.png
            ├── cd8s_C142_FADD_ko_.png
            ├── cd8s_C142_FAS_FASL_complex_ko_.png
            ├── cd8s_C142_FASLG_ko_.png
            ├── cd8s_C142_M_ko_.png
            ├── cd8s_C142.png
            ├── cd8_traces_C141_Apoptosome_complex_ko_.png
            ├── cd8_traces_C141_CASP3_ko_.png
            ├── cd8_traces_C141_CASP8_ko_.png
            ├── cd8_traces_C141_CASP9_cell_active_ko_.png
            ├── cd8_traces_C141_FADD_ko_.png
            ├── cd8_traces_C141_FAS_FASL_complex_ko_.png
            ├── cd8_traces_C141_FASLG_ko_.png
            ├── cd8_traces_C141_M_ko_.png
            ├── cd8_traces_C141.png
            ├── cd8_traces_C142_Apoptosome_complex_ko_.png
            ├── cd8_traces_C142_CASP3_ko_.png
            ├── cd8_traces_C142_CASP8_ko_.png
            ├── cd8_traces_C142_CASP9_cell_active_ko_.png
            ├── cd8_traces_C142_FADD_ko_.png
            ├── cd8_traces_C142_FAS_FASL_complex_ko_.png
            ├── cd8_traces_C142_FASLG_ko_.png
            ├── cd8_traces_C142_M_ko_.png
            ├── cd8_traces_C142.png
            ├── clustermap_genes.png
            ├── clustermap_patients.png
            ├── clustermap.png
            ├── clustermap_traces.png
            ├── dendogram_genes.png
            ├── dendogram_patients.png
            ├── dendogram.png
            ├── dendogram_traces.png
            ├── epithelials_C141_Apoptosome_complex_ko_.png
            ├── epithelials_C141_CASP3_ko_.png
            ├── epithelials_C141_CASP8_ko_.png
            ├── epithelials_C141_CASP9_cell_active_ko_.png
            ├── epithelials_C141_FADD_ko_.png
            ├── epithelials_C141_FAS_FASL_complex_ko_.png
            ├── epithelials_C141_FASLG_ko_.png
            ├── epithelials_C141_M_ko_.png
            ├── epithelials_C141.png
            ├── epithelials_C142_Apoptosome_complex_ko_.png
            ├── epithelials_C142_CASP3_ko_.png
            ├── epithelials_C142_CASP8_ko_.png
            ├── epithelials_C142_CASP9_cell_active_ko_.png
            ├── epithelials_C142_FADD_ko_.png
            ├── epithelials_C142_FAS_FASL_complex_ko_.png
            ├── epithelials_C142_FASLG_ko_.png
            ├── epithelials_C142_M_ko_.png
            ├── epithelials_C142.png
            ├── epithelials_traces_C141_Apoptosome_complex_ko_.png
            ├── epithelials_traces_C141_CASP3_ko_.png
            ├── epithelials_traces_C141_CASP8_ko_.png
            ├── epithelials_traces_C141_CASP9_cell_active_ko_.png
            ├── epithelials_traces_C141_FADD_ko_.png
            ├── epithelials_traces_C141_FAS_FASL_complex_ko_.png
            ├── epithelials_traces_C141_FASLG_ko_.png
            ├── epithelials_traces_C141_M_ko_.png
            ├── epithelials_traces_C141.png
            ├── epithelials_traces_C142_Apoptosome_complex_ko_.png
            ├── epithelials_traces_C142_CASP3_ko_.png
            ├── epithelials_traces_C142_CASP8_ko_.png
            ├── epithelials_traces_C142_CASP9_cell_active_ko_.png
            ├── epithelials_traces_C142_FADD_ko_.png
            ├── epithelials_traces_C142_FAS_FASL_complex_ko_.png
            ├── epithelials_traces_C142_FASLG_ko_.png
            ├── epithelials_traces_C142_M_ko_.png
            ├── epithelials_traces_C142.png
            ├── macrophages_C141_Apoptosome_complex_ko_.png
            ├── macrophages_C141_CASP3_ko_.png
            ├── macrophages_C141_CASP8_ko_.png
            ├── macrophages_C141_CASP9_cell_active_ko_.png
            ├── macrophages_C141_FADD_ko_.png
            ├── macrophages_C141_FAS_FASL_complex_ko_.png
            ├── macrophages_C141_FASLG_ko_.png
            ├── macrophages_C141_M_ko_.png
            ├── macrophages_C141.png
            ├── macrophages_C142_Apoptosome_complex_ko_.png
            ├── macrophages_C142_CASP3_ko_.png
            ├── macrophages_C142_CASP8_ko_.png
            ├── macrophages_C142_CASP9_cell_active_ko_.png
            ├── macrophages_C142_FADD_ko_.png
            ├── macrophages_C142_FAS_FASL_complex_ko_.png
            ├── macrophages_C142_FASLG_ko_.png
            ├── macrophages_C142_M_ko_.png
            └── macrophages_C142.png

        11 directories, 100 files
