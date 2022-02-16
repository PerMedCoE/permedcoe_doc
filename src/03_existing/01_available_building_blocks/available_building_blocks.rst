Available Building Blocks
=========================

This section provides general descriptions of existing PerMedCoE Building Blocks, as
well as links to building block GitHub repositories. For detailed documentation, see 
the individual building block folders in the `PerMedCoE Building Blocks 
repository <https://github.com/PerMedCoE/BuildingBlocks>`_. The repository also
contains `Singularity (Apptainer) definition 
files <https://github.com/PerMedCoE/BuildingBlocks/tree/main/Resources/images>`_.

High-throughput mutant analysis
-------------------------------

Taking a Boolean model as the input, uses MaBoSS to perform a single simulation per
mutant for all model nodes to determine the most relevant candidate genes to be mutated
to inhibit or promote a given model output (or phenotype). Outputs a candidate gene list
formatted as a text file (single gene per row).

`GitHub repository <https://github.com/PerMedCoE/BuildingBlocks/tree/main/MaBoSS>`_

Analysis of all simulations
---------------------------

Employs a meta-analysis to determine the predictive capacity of multiscale models with 
regard to COVID-19 severity subtypes (moderate, severe or control) corresponding to 
individual patients.

`GitHub repository <https://github.com/PerMedCoE/BuildingBlocks/tree/main/meta_analysis>`_

Personalise patient
-------------------

Taking output data produced by the `High-throughput mutant analysis` and `Single cell processing`
building blocks (i.e. candidate genes and normalised gene expression matrices) as the input,
customises the Boolean model according to normalised expression values obtained for genes included
in the model. In addition, for each patient, the effect of knocking out each of the candidate
genes is evaluated.

`GitHub repository <https://github.com/PerMedCoE/BuildingBlocks/tree/main/personalize_patient>`_

PhysiBoss
---------

Uses PhysiBoSS to perform multiscale simulations corresponding to unmutated (wild type) and mutant
models for each patient, computing a predefined number of replicates to control for the stochastic
nature of the simulations.

`GitHub repository <https://github.com/PerMedCoE/BuildingBlocks/tree/main/PhysiBoSS>`_

Single-cell processing
----------------------

Taking patient-specific single-cell RNA sequencing data as the input, constructs normalised expression
matrices for the different cell types detected in each subject.

`GitHub repository <https://github.com/PerMedCoE/BuildingBlocks/tree/main/single_cell_processing>`_

Build model from species
------------------------

(Description TBA)

`GitHub repository <https://github.com/PerMedCoE/BuildingBlocks/tree/main/build_model_from_species>`_

Print drug results
------------------

(Description TBA)

`GitHub repository <https://github.com/PerMedCoE/BuildingBlocks/tree/main/print_drug_results>`_
