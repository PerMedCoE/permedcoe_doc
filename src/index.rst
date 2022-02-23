.. PerMedCoE Base Package documentation master file, created by
   sphinx-quickstart on Thu Mar 18 17:03:27 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PerMedCoE documentation!
===================================

.. image:: ../_static/logo_1.png
   :width: 500
   :align: center
   :target: https://permedcoe.eu

This is the HPC/Exascale Centre of Excellence for Personalised Medicine in Europe (PerMedCoE)
artifacts documentation.

The target audiences for this documentation are:

  - **Developers** (Python) aiming at contributing to the Personalized Medicine project environment with Building Blocks or Workflows.
  - **Researchers** aiming at conducting investigations using the available Building Blocks and Workflows.

This documentation is aimed at showing:

  - How to use the ``permedcoe`` package:

    - Python API
    - Command Line Interface

  - How to develop new Building Blocks
  - How to execute Building Blocks individually
  - How to develop Workflows using Building Blocks
  - How to execute Workflows using:

    - PyCOMPSs
    - Croupier

  - A step-by-step guide from creating a building block to execute a workflow.
  - A sample application

The current status of the project is **WORK IN PROGRESS**.

..
   The available resources are:

   - The ``permedcoe`` base package has been released: https://pypi.org/project/permedcoe/
   - Available workflows:

      - Covid 19

   - Available Building Blocks:

      - MaBoSS
      - Personalize Patient
      - Meta-Analysis
      - PhysiBoSS
      - Single Cell Processing


..
   **PerMedCoE** is the **HPC/Exascale Centre of Excellence for Personalised Medicine in Europe**.

   Personalised Medicine (PerMed) opens unexplored frontiers to treat diseases at the individual
   level combining clinical and omics information.
   However, the performances of the current simulation software are still insufficient to tackle
   medical problems such as tumour evolution or patient-specific treatments.
   The challenge is to develop a sustainable roadmap to scale-up the essential software for the
   cell-level simulation to the new European HPC/Exascale systems.
   Simulation of cellular mechanistic models are essential for the translation of omic data to
   medical relevant actions and these should be accessible to the end-users in the appropriate
   environment of the PerMed-specific big confidential data.
   The goal of PerMedCoE is to provide an efficient and sustainable entry point to the
   HPC/Exascale-upgraded methodology to translate omics analyses into actionable models of
   cellular functions of medical relevance.

   In this direction, the PerMedCoE project developments are based on containers enabling
   reproducible operations in heterogeneous HPC infrastructures, and their inclusion into
   efficient **building blocks (BBs)** and **workflows**.

   The ``permedcoe`` package provides a Python API necessary for the development
   of **Building Blocks (BBs)** in the **HPC/Exascale Centre of Excellence in
   Personalised Medicine** (`PerMedCoE <https://permedcoe.eu/>`_) project.

   In addition, it provides a command line tool that eases the application or
   Building Block (BB) execution, as well as being able to create empty templates for them.


.. toctree::
   :maxdepth: 4
   :caption: Contents:

   01_installation/installation
   02_components/components
   03_existing/existing
   04_creating/creating
   05_acks/acknowledgements



..
    01 is potentially a quickstart section
    06 is potentially a troubleshooting section

    Indices and tables
    ==================

    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`
