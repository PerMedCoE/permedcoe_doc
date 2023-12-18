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

Multi-scale models are parametrized by many constants, many of them unknown, and which will impact their behaviour.
An important part of the development of such models is to set these constants' values in order to successfully
reproduce the observed biological behaviour. To perform this task, many conditions needs to be simulated to test for
possible parameter values, a very heavy computational task.

This workflow perform such a task known as a parameter sensitivity analysis, which helps characterize which parameters
are important for the observed behaviour, and to which values this parameter should be set.

The workflow uses the following building blocks, described in order of execution:

1. PhysiBoSS invasion
    - Simulate the tumor invasion model (Ruscone et al., Bioinformatics, 2023) and generate outputs.
2. Invasion analysis
    - Analyse the simulation outputs and generates plots with the quantification of single and collective migration, according to the parameter values.

For details on individual workflow steps, see the user documentation for each building block.
`GitHub repository <https://github.com/PerMedCoE/cancer-invasion-workflow>`__


Cancer diagnosis
----------------

This use case describes a computational workflow for building a mechanistic model that captures molecular differences between two cancer subtypes, with a focus on Chronic Lymphocytic Leukaemia (CLL). The study uses RNA-Seq data and a specific clinical variable, drawing on the ICGC consortium's data, making it potentially applicable to various cancer types. The analysis aims to understand cellular signalling differences between IGHV groups by employing tools to assess transcription factor activity and provide a signalling network, offering a mechanistic explanation for observed molecular changes. The creation of patient-specific Boolean models allows for studying individual patient trajectories, emphasizing the importance of personalized medicine and tailoring approaches to account for genomic heterogeneity in cancer. Overall, this use case showcases the application of mathematical modelling tools in personalized medicine to understand and adapt approaches based on individual patient characteristics.


1. cll_prepare_data: 
   - This involves an in-house script for the primary analysis of the input RNA-Seq data, focusing on tasks such as differential expression analysis and batch effect correction.
2. cll_tf_activities: 
   - This block entails the inference of transcription factor (TF) activities using DecoupleR and the quantification of molecular pathways through PROGENY.
3. cll_network_inference: 
   - This step involves network inference with CARNIVAL, leveraging Omnipath, as well as DecoupleR and PROGENY results as constraints within the linear programming problem.
4. cll_personalise_boolean_models: 
   - This block is responsible for building patient-specific boolean models by employing the PROFILE tool and input RNA-Seq data.
5. cll_run_boolean_model: 
   - It involves evaluating a single patient or group-specific model using MaBoSS.
6. cll_combine_results: 
   - This block combines patient or group-specific results from MaBoSS, assessing whether the obtained profiles are appropriately clustered and can serve as predictors of disease subtype.



For details on individual workflow steps, see the user documentation for each building block.
`GitHub repository <https://github.com/PerMedCoE/cancer-diagnosis-workflow>`__
