Existing Workflows
==================

This section provides general descriptions of existing PerMedCoE Workflows, as
well as links to Workflow GitHub repositories. 

Basic examples
--------------

A basic example application comprised of a single building block can be found
in `this repository <https://github.com/PerMedCoE/basic_application>`_.

A more complex application involving several building blocks that internally
call ``gromacs`` `can be found here <https://github.com/PerMedCoE/Lysozyme_in_water>`_.

.. TIP::

    Note that, for these basic examples, the workflow repository contains both the
    Building Block and the application. In other examples, Building Blocks are
    maintained in a `separate repository <https://github.com/PerMedCoE/BuildingBlocks>`_.

COVID-19 multiscale modelling of the virus and patients’ tissue
---------------------------------------------------------------

Uses multiscale simulations to predict patient-specific SARS‑CoV‑2 severity subtypes 
(moderate, severe or control), using single-cell RNA-Seq data, MaBoSS and PhysiBoSS. 
Boolean models are used to determine the behaviour of individual agents as a function
of extracellular conditions and the concentration of different  substrates, including 
the number of virions. Predictions of severity subtypes are based on a meta-analysis of 
personalised model outputs simulating cellular apoptosis regulation in epithelial cells 
infected by SARS‑CoV‑2.

The workflow uses the following building blocks, described in order of execution:

1. High-throughput mutant analysis
2. Single-cell processing
3. Personalise patient
4. PhysiBoSS
5. Analysis of all simulations

For details on individual workflow steps, see the user documentation for each building block.

`GitHub repository <https://github.com/PerMedCoE/covid-19-workflow>`_
