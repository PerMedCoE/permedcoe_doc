:fa:`support` Existing Building Blocks and Workflows
====================================================

This section provides a list of available PerMedCoE building blocks (BB), existing
workflows and links to further user documentation.

Building blocks are executed using the **permedcoe** base package. In PerMedCoE,
a BB is considered a unit of work, like a black box that performs a particular
computation. Consequently, it has inputs and outputs, and can be instantiated
into applications and piped as required. Combinations of several building blocks
can be used to execute different workflows.

The **permedcoe** package enables BB execution using a variety of workflow managers,
such as PyCOMPSs, Snakemake or Nextflow.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   01_available_building_blocks/available_building_blocks
   02_existing_workflows/existing_workflows
   03_tutorial/tutorial
