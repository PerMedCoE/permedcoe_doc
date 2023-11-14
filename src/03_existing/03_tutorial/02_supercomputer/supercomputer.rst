Supercomputer
-------------

All PerMedCoE Building Blocks and Workflows can be deployed and executed in Supercomputers/Clusters.

Their deployment can be performed for each user in a Supercomputer following the same instructions
as with `local deployment <../01_local/local.html#Deployment>`_ (the requirements are the same, as
well as the workflow manager and Singularity).
Note that it is required that the Supercomputer's login node have access to Internet.

The main difference relies in the execution, since the Supercomputers have a job queuing system
(e.g. SLURM), and the workflows have to be submitted as jobs. To this end, the workflows have
helper scripts to automatize the job submission.

This Section will go step-by-step showing how to use the PerMedCoE artifacts in the following
Supercomputers, where the available Building Blocks and Workflows are already deployed
and ready to be used by all users with access to that Supercomputer.

SCs
~~~

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   MN4/mn4
