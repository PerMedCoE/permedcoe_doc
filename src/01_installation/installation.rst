:fa:`save` Base Package Installation
====================================

Introduction
------------

`PerMedCoE <https://permedcoe.eu/>`_ project developments are based on containers enabling reproducible operations
in heterogeneous HPC infrastructures, and their inclusion into **building blocks (BBs)** and **workflows**.

The ``permedcoe`` package provides a command line tool that eases BB execution. It also provides a Python API necessary
for the development of BBs and enables the creation of empty BB templates.

This section shows how to install the PerMedCoE base package. A list of package dependencies is also provided.

Requirements
------------

- Python >= 3.6
- `Singularity (Apptainer) <https://singularity.lbl.gov/docs-installation>`_


Installation from Pypi
----------------------

The package is publicly available in Pypi:

.. code-block:: console

    python3 -m pip install permedcoe


Installation from source code
-----------------------------

An automatic installation script is available in the PerMedCoE base package GitHub repository:

.. code-block:: console

    git clone https://github.com/PerMedCoE/permedcoe.git
    cd permedcoe
    ./install.sh

.. ATTENTION::

    This script creates a file named ``installation_files.txt`` to keep track of the installed files.
    It is used with the ``uninstall.sh`` script to clean up the system.


Uninstall from Pypi
-------------------

The base package can be uninstalled can be done using ``pip uninstall``:

.. code-block:: console

    python3 -m pip uninstall permedcoe


Uninstall from source code
--------------------------

If installed using ``install.sh``, the base package can be uninstalled by running:

.. code-block:: console

    ./uninstall.sh

The folder can then be cleaned using the ``clean.sh`` script.

.. code-block:: console

    ./clean.sh
