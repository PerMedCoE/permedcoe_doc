Available Building Blocks
=========================

This section provides general descriptions of existing PerMedCoE Building Blocks, as
well as links to building block GitHub repositories. For detailed documentation, see
the individual building block folders in the `PerMedCoE Building Blocks
repository <https://github.com/PerMedCoE/BuildingBlocks>`_. The repository also
contains `Singularity (Apptainer) definition
files <https://github.com/PerMedCoE/BuildingBlocks/tree/main/Resources/images>`_.

.. ATTENTION::

    They are currently **private** but will be available soon!


High-throughput mutant analysis
-------------------------------

Taking a Boolean model as the input, this building block uses MaBoSS to perform a single simulation per
node for all the model nodes to determine the most relevant candidate genes to be mutated
to inhibit or promote a given model output or phenotype. It produces a candidate gene list
formatted as a text file (single gene per row).

`GitHub repository <https://github.com/PerMedCoE/BuildingBlocks/tree/main/MaBoSS>`__ (currently **private** but will be available soon!)

Analysis of all simulations
---------------------------

Employs a meta-analysis to determine the predictive capacity of multiscale models with
regard to COVID-19 severity subtypes (moderate, severe or control) corresponding to
individual patients.

`GitHub repository <https://github.com/PerMedCoE/BuildingBlocks/tree/main/meta_analysis>`__ (currently **private** but will be available soon!)

Personalise patient
-------------------

Taking output data produced by the `High-throughput mutant analysis` and `Single cell processing`
building blocks (i.e. candidate genes and normalised gene expression matrices) as the input,
customises the Boolean model according to the normalised expression values obtained for genes included
in the model to have patient-specific Boolean models. In addition, for each patient, the effect of knocking out each of the candidate
genes is evaluated.

`GitHub repository <https://github.com/PerMedCoE/BuildingBlocks/tree/main/personalize_patient>`__ (currently **private** but will be available soon!)

PhysiBoSS
---------

Uses PhysiBoSS to perform multiscale simulations of the wild type and mutant
models for each patient, computing a predefined number of replicates to control for the stochastic
nature of the simulations.

`GitHub repository <https://github.com/PerMedCoE/BuildingBlocks/tree/main/PhysiBoSS>`__ (currently **private** but will be available soon!)

Single-cell processing
----------------------

Taking single-cell RNA sequencing data as the input, this building block constructs normalised expression
matrices for the different cell types detected in each dataset.

`GitHub repository <https://github.com/PerMedCoE/BuildingBlocks/tree/main/single_cell_processing>`__ (currently **private** but will be available soon!)

Build model from species
------------------------

(Description TBA)

`GitHub repository <https://github.com/PerMedCoE/BuildingBlocks/tree/main/build_model_from_species>`__ (currently **private** but will be available soon!)

Print drug results
------------------

(Description TBA)

`GitHub repository <https://github.com/PerMedCoE/BuildingBlocks/tree/main/print_drug_results>`__ (currently **private** but will be available soon!)
