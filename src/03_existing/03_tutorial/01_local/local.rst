Local
-----

All PerMedCoE Building Blocks and Workflows can be deployed and executed in local machines.
To this end, this section provides step-by-step detailed instructions on the requirements, how to
do the deployment, and how to run the workflows.

The first step is to make sure that the target machine has the required `requirements <tutorial.html#requirements>`_.

Requirements
~~~~~~~~~~~~

For local installations, the ``permedcoe`` package is **REQUIRED** to be installed.
Since it is a Python package available in the Pypi repository, it can be easily installed using **pip**:

.. code-block:: console

    $ python3 -m pip install permedcoe

    Defaulting to user installation because normal site-packages is not writeable
    Collecting permedcoe
    Downloading permedcoe-0.0.11-py3-none-any.whl (40 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 40.6/40.6 kB 2.7 MB/s eta 0:00:00
    Requirement already satisfied: pyyaml in /home/user/.local/lib/python3.10/site-packages (from permedcoe) (6.0)
    Installing collected packages: permedcoe
    Successfully installed permedcoe-0.0.11


.. TIP::

    Alternatively, it is possible to be
    `installed from source <../../01_installation/installation.html#installation-from-source-code>`_

It is also **REQUIRED** to install Apptainer (for automatic container download).

Please, check the `Apptainer installation documentation <https://apptainer.org/docs/admin/main/installation.html>`__.


Deployment
~~~~~~~~~~

The deployment can be done for specific Building Blocks, or for complete Workflows (that automatically
deploys its required Building Blocks). This section describes how to deploy a single Building Block
and a complete Workflow:

.. dropdown:: Deploy an existing Building Block
    :animate: fade-in

    .. include:: /03_existing/03_tutorial/01_local/dropdowns/1_deploy_building_block.rst


.. dropdown:: Deploy an existing Workflow
    :animate: fade-in

    .. include:: /03_existing/03_tutorial/01_local/dropdowns/2_deploy_workflow.rst

Usage
~~~~~

This section aims at showing how to use individual Building Blocks and complete Workflows.
Please, remind that Building Blocks are designed for a specific purpose, while the
workflows use various Building Blocks in order to perform a particular analysis.

.. dropdown:: Use a Building Block
    :animate: fade-in

    .. include:: /03_existing/03_tutorial/01_local/dropdowns/3_use_building_block.rst


.. dropdown:: Use a Workflow
    :animate: fade-in

    .. include:: /03_existing/03_tutorial/01_local/dropdowns/4_use_workflow.rst