:fa:`magic` Usage
=================

This section shows how to develop Building Blocks using the **permedcoe** package,
and how to use them into an application.

More specifically, a Building Block is considered a unit of work, like a black box that
performs a particular computation. Consequently, it has inputs and outputs, and they
can be instantiated into applications and piped accordingly to their need.

This structure enables developers to build applications quickly and easily by choosing
the required Building Blocks and connecting them.

The **permedcoe** package enables to use them in a variety of workflow managers,
such as PyCOMPSs, Nextflow or Snakemake. It also supports the meta-workflow orchestrator Croupier,
which supports end-users to consume applications whose tasks are executed across multiple
HPC infrastructures

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   01_building_block/building_block
   02_application/application
   03_croupier/croupier
