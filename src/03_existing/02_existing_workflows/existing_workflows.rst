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


COVID-19 Multiscale Modelling of the Virus and Patients’ Tissue
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

`GitHub repository <https://github.com/PerMedCoE/covid-19-workflow>`__


Drug Synergies Screening
------------------------

This pipeline simulates a drug screening on personalised cell line models. It automatically builds Boolean models of interest, then uses cell lines data (expression, mutations, copy number variations) to personalise them as MaBoSS models. Finally, this pipeline simulates multiple drug intervention on these MaBoSS models, and lists drug synergies of interest.

The workflow uses the following building blocks, described in order of execution:

1. Build model from species
2. Personalise patient
3. MaBoSS
4. Print drug results

For details on individual workflow steps, see the user documentation for each building block.
`GitHub repository <https://github.com/PerMedCoE/drug-synergies-workflow>`__


Single drug prediction
----------------------

Complementarily, the workflow supports single drug response predictions to provide a baseline prediction in cases where drug response information for a given drug and cell line is not available. As an input, the workflow needs basal gene expression data for a cell, the drug targets (they need to be known for untested drugs) and optionally CARNIVAL features (sub-network activity predicted with CARNIVAL building block) and predicts log(IC50) values. This workflow uses a custom matrix factorization approach built with Google JAX and trained with gradient descent. The workflow can be used both for training a model, and for predicting new drug responses.

The workflow uses the following building blocks in order of execution (for training a model):

1. Carnival_gex_preprocess
    - Preprocessed the basal gene expression data from GDSC. The input is a matrix of Gene x Sample expression data.
2. Progeny
    - Using the preprocessed data, it estimates pathway activities for each column in the data (for each sample). It returns a matrix of Pathways x Samples with activity values for 11 pathways.
3. Omnipath
    - It downloads latest Prior Knowledge Network of signalling. This building block can be ommited if there exists already a csv file with the network.
4. TF Enrichment
    - For each sample, transcription factor activities are estimated using Dorothea.
5. CarnivalPy
    - Using the TF activities estimated before, it runs Carnival to obtain a sub-network consistent with the TF activities (for each sample).
6. Carnival_feature_merger
    - Preselect a set of genes by the user (if specified) and merge the features with the basal gene expression data.
7. ML Jax Drug Prediction
    - Trains a model using the combined features to predict IC50 values from GDSC.

For details on individual workflow steps, please check the scripts that use each individual building block in the workflow `GitHub repository <https://github.com/PerMedCoE/single_drug_prediction>`__.


Cancer invasion
---------------

TBD

For details on individual workflow steps, see the user documentation for each building block.
`GitHub repository <https://github.com/PerMedCoE/cancer-invasion-workflow>`__