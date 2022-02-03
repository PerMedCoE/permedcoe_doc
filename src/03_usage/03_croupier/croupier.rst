Application execution with Croupier
===================================

Introduction
------------
Croupier is a meta-orchestrator that enables end-users,
either application providers and consumers to deploy and execute applications
across multiple HPC infrastructures, and move data from one infrastructure
to another. Application providers use Croupier to make their applications
available for consumers in the Croupier marketplace. Application consumers browse
available application and execute then in selected HPC infrastructures.


Disclaimer
----------
Croupier is a HPC-metaorchestration plugin installed in
the Cloudify cloud meta-orchestrator. Both application providers and consumers
will interface Croupier through its dedicated web frontend, which is not yet
integrated for PerMedCoE project. Therefore, this current version of the
documentation uses Cloudify frontend to install applications, deploy and execute
them. Once the Croupier frontend is integrated, this documentation will be
updated, replacing the Cloudify frontend.

Prerequisites
-------------
The Croupier administrator should take care of installing all required
dependencies and the Croupier plugin. Atos will provide Croupier accessible
through its frontend at http://frontend.croupier.permedcoe.eu (not yet available, stay tune!)

Cloudify installation
~~~~~~~~~~~~~~~~~~~~~
Croupier is a plugin of Cloudify cloud orchestrator (https://cloudify.co/).
To install Cloudify Community Edition, follow instructions available at: https://docs.cloudify.co/latest/trial_getting_started/set_trial_manager/download_community
The following instructions have been tested in **version 6.2.0**

Croupier installation
~~~~~~~~~~~~~~~~~~~~~
To install Croupier plugin, you need a Croupier Wagon file, compiled for CentOS.
Contact Croupier administrator (jesus.gorronogoitia@atos.net) for latest
Croupier's wheel and the ``plugin.yaml`` descriptor. Next, log into Cloudify with **admin** account.
Click on the **resources** tab in the leftmost panel. Click on the **Resources**
tab in the main page. Then, click on the **upload** button in the right of the
**Plugin list** table. Select **upload a package**

.. image:: ../../../_static/figures/cloudify_upload_plugin.png
   :width: 200
   :align: center

Then, in the wizard, browse click on the **File** button to search in your file
system for the **Croupier Wagon file**, and similarly for the **Croupier YAML file**.
Once selected, check the Plugin title is set to ``croupier``.
Click on the **Upload** button to accept.

.. image:: ../../../_static/figures/cloudify_upload_plugin_wizard.png
   :width: 600
   :align: center

Check the Croupier plugin installation in the list of plugins.

.. image:: ../../../_static/figures/cloudify_croupier_installed.png
   :width: 1000
   :align: center


Other services:
~~~~~~~~~~~~~~~
Croupier require additional services, **KeyCloak** and **Vault** to work.

- Keycloak (https://www.keycloak.org/) is an IAM service that offers a SSO across multiple application. Croupier frontend uses KeyCloak to authenticate users
- Hashicorp Vault (https://www.vaultproject.io) is a secret store. Croupier frontend uses Vault to retrieve HPC user's credentials to get access to the target HPC frontend on behalf of the user.

Contact Croupier administrator (jesus.gorronogoitia@atos.net) for
instructions to configure your KeyCloak and Vault instances to be used
by Croupier.

Application definition (Blueprint)
----------------------------------
Application providers define their applications as meta-workflows that
execute multiple tasks (in sequence or in parallel) distributed across
one or more target HPC infrastructures.
These workflows are named **blueprints** in Cloudify terminology.
They may also specify data objects, their role as tasks'
inputs and/or outputs and the transfer entities that move such data from
one source to a target.
Croupier's workflows are specified in YAML by using the **OASIS TOSCA** language (https://docs.cloudify.co/latest/developer/blueprints/).
For the following, we use the Covid19 application as an example.

The application workflow starts with a header that declares at least imports
read the Croupier workflow model. Other imports could be possible if required
by the application.

  .. code-block:: yaml

    tosca_definitions_version: cloudify_dsl_1_3
    imports:
        - http://raw.githubusercontent.com/ari-apc-lab/croupier/master/resources/types/cfy_types.yaml
        - plugin:croupier

Next, application data types can be optionally declared. In the following
example, the Covid19 application input arguments are declared

  .. code-block:: yaml

    data_types:
    permedcoe.covid19.args:
        properties:
            metadata:
                type: string
                required: true
            model_prefix:
                type: string
                required: true
            outdir:
                type: string
                required: true
            ko_file:
                type: string
                required: true
            reps:
                type: integer
                required: true
            model:
                type: string
                required: true
            data_folder:
                type: string
                required: true

Then, the application inputs should be declared.
There is a number of common inputs for a common application:

- VAULT arguments required to obtain HPC access credentials, namely ``vault_token`` and ``user``.
- HPC properties, such as the frontend ``hpc_host`` and the ``hpc_scheduler``
- PYCOMPSs arguments, such as the ``num_nodes`` and the ``exec_time``
- Application specific args. In below example, the Covid19 input arguments

The number and type of arguments are variable and they are decided by the
application provider. For instance, several Vault services can be defined,
sharing the same vault_user, but requiring different tokens. Similarly,
several HPC infrastructures can be used to distribute workflow tasks,
and requiring dedicated inputs for each infrastructure, hence. The number
and kind of PYCOMPSs arguments can be different across applications.

**Note:** This workflow COVID19 example uses PYCOMPSs as target HPC workflow
and scheduler.

  .. code-block:: yaml

    inputs:
        ########################## VAULT ######################
        vault_token:
            type: string
        vault_user:
            type: string

        ################# HPC Infrastructures #################
        hpc_host:
            type: string

        hpc_scheduler:
            type: string

        ################# Covid 19 application ################
        covid19_args:
            type: permedcoe.covid19.args

        ##################### PYCOMPSs args ###################
        num_nodes:
            type: integer
        exec_time:
            type: integer

Next, one or more Vault nodes must be declared. Vault nodes are used
as secret stores where to retrieve from the credentials required to access
the target HPC infrastructures, through ssh, to schedule workflow' tasks
(as jobs). The following block declares one Vault node of type ``croupier.nodes.Vault``.
Note that Vault properties (``token`` and ``user``) are taken from inputs
by using the ``get_input`` function:

  .. code-block:: yaml

    node_templates:
    vault:
        type: croupier.nodes.Vault
        properties:
            token: { get_input: vault_token }
            user: { get_input: vault_user }

Then, one of more HPC infrastructures (where to execute the workflow's tasks)
are declared as node instances of the type ``croupier.nodes.InfrastructureInterface``
The mandatory properties of this type must be overridden by this node definition.
Other optional properties as well. In particular:

- ``config/infrastructure_interface`` must be given with the name of the target HPC scheduler used to launch job tasks.
- ``credentials/host`` must also be given with the host name of the HPC frontend.

In this example, HPC configuration is read from declared inputs, as the
application's consumer will be prompted to provide those values. This is a common
approach when the consumer selects a target HPC infrastructure where to execute
the application. Alternatively, a fixed target HPC infrastructure can be
specified in the workflow.

- ``job_prefix`` declare a prefix for naming the submitted jobs.
- ``base_dir`` declares the path where Croupier folder for workflow execution will be created.
- ``monitoring_options/monitor_period`` declares the period of Croupier's requests to the HPC frontend to check the task job execution/queue status.
- ``workdir_prefix`` declares the name of the folder create for every task job executed. This folder will contain the deployed application, its execution logs and

Finally, the HPC infrastructure node is associated to the Vault node, by using
a relationship of type ``retrieve_credentials_from_vault`` that states that
the HPC ``credentials`` will be retrieved from that node,
declared in the ``target``

  .. code-block:: yaml

    hpc:
        type: croupier.nodes.InfrastructureInterface
        properties:
            config:
                infrastructure_interface: { get_input: hpc_scheduler }
            credentials:
                host: { get_input: hpc_host }
            job_prefix: croupier
            base_dir: $HOME
            monitoring_options:
                monitor_period: 15
            skip_cleanup: true
            workdir_prefix: "pycompss-test"
        relationships:
            - type: retrieve_credentials_from_vault
              target: vault


In a similar way, the workflow provider can define additional HPC
infrastructures in case the workflow's tasks are distributed across them.

Next, one or more tasks are defined, as node instances of type
``croupier.nodes.Job`` or its subclasses. In the following example,
a application task to be executed by **PYCOMPSs** is defined,
as an instance of type ``croupier.nodes.PyCOMPSsJob``:

  .. code-block:: yaml

    job:
        type: croupier.nodes.PyCOMPSsJob
        properties:
            job_options:
                modules:
                    - load singularity/3.5.2
                    - use /apps/modules/modulefiles/tools/COMPSs/libraries
                    - load permedcoe
                app_name: covid19
                app_source: permedcoe/PilotWorkflow/covid19_pilot_workflow/PyCOMPSs
                env:
                    - COVID19_BB_IMAGES: '${COVID19_BB_IMAGES}'
                    - COVID19_BB_ASSETS: '${COVID19_BB_ASSETS}'
                    - dataset: '${COVID19_PILOT_DATASET}'
                compss_args:
                    num_nodes: { get_input: num_nodes }
                    exec_time: { get_input: exec_time }
                    worker_working_dir: '$(pwd)'
                    log_level: off
                    graph: true
                    tracing: true
                    python_interpreter: python3
                app_file: '{COMPS_APP_PATH}/covid19_pilot.py'
                app_args: { get_input: covid19_args }
            skip_cleanup: True
        relationships:
            - type: task_managed_by_interface
              target: hpc

Every task type has its own properties, including those inherited
from the base type. For tasks of type ``croupier.nodes.PyCOMPSsJob``,
like in above example, the properties required to define a task are:

- ``modules``: list of module commands to be executed before the application is submitted by the PYCOMPSs manager.
- ``app_name``: the name of the application
- ``app_source``: path to the application source, from where it will be deployed
- ``env``: list of environment variables
- ``compss_args``: list of PYCOMPSs arguments. See `PYCOMPSs documentation <https://pycompss.readthedocs.io/en/stable/Sections/03_Execution_Environments/01_Master_worker/01_Local/01_Executing.html#runcompss-command>`_ for more details
- ``app_file``: path to the application executable file, in the deployed folder
- ``app_args``: list of application arguments. Consult the concrete application documentation

Finally, the task is declared to be run in a HPC infrastructure by setting a relationship of type
``task_managed_by_interface`` whose ``target`` points at the HPC node.

Note that in this specification of a PYCOMPSs task, some properties are
hardcoded by the application provider, while others
(e.g. ``num_nodes`` of ``compss_args``, or ``app_args``) are taken from the
declared workflow's inputs, by using the ``get_input`` function. The
application provider decides what data must be provided by the consumer as input.


Application installation
------------------------
The application provider can deploy an application into Croupier, by taking
the following procedure:

- Package the folder that contains the application workflow YAML description (and possibly other artefacts required for its deployment) into a zip file, named with with the application name.
- Log into Cloudify service, go to the **Blueprints** tab in the leftmost panel, click on the **Upload** button located on the right side, select the **Upload a blueprint package** option.

.. image:: ../../../_static/figures/cloudify_upload_blueprint.png
   :width: 200
   :align: center

- In the wizard, click on the left button with a folder icon located at the line for the **Blueprint package** field to browse your file system and locate your workflow zip file. When selected, the other wizard fields will be filled in automatically. Then, accept by clicking on **Upload** button.

.. image:: ../../../_static/figures/cloudify_upload_blueprint_wizard.png
   :width: 600
   :align: center

- Confirm your application is listed in the list of blueprints

.. image:: ../../../_static/figures/cloudify_blueprints.png
   :width: 1000
   :align: center

This procedure is followed by any application provider to deploy her applications
into the Croupier marketplace, so that they will be available to be executed by
any consumer that gets access.

Consumers can execute selected applications (from the list of blueprints)
by following a procedure that consists of two steps:

- A consumer's instance of the application (i.e. workflow) is deployed in the target infrastructure(s) with a given set of inputs
- The application's instance is executed in the target infrastructure(s)


Application instance deployment
-------------------------------
A consumer browse the list of available applications in the Cloudify list of blueprints.
To deploy a consumer's instance of the blueprint, the consumer takes the following
procedure:

- Click on the button with the rocket icon located at the leftmost side of the row of the selected application in the list of blueprints.

.. image:: ../../../_static/figures/cloudify_deploy_blueprint.png
   :width: 250
   :align: center

- In the Blueprint deployment wizard, give a ``deployment name``, and optionally, a unique, human-meaningful ``deployment-id``
- Next, provide values for the application's inputs. This can be done either by direct editing in the form, or by reading them from a ``inputs.yaml`` that is selected from the consumer's file system, by clicking on the **Load Values** button. Loaded inputs' values can be latter edited in this form, before it is submitted.
- Once the application inputs' values are provided, click on the **Deploy and Install** button. In the next wizard, click on the **Execute** button.

.. image:: ../../../_static/figures/cloudify_deploy_blueprint_wizard.png
   :width: 600
   :align: center

An example of ``inputs.yaml`` file for our Covid19 application is given below:

  .. code-block:: yaml

    # VAULT
    vault_token: 's.jaH92wPSyAPszvTro3qj4Y5C'
    vault_user: 'yosu'

    # WORKFLOW
    # HPC infrastructures
    # HPC
    hpc_host: mn1.bsc.es
    hpc_scheduler: PYCOMPSS

    # COVID19 args
    covid19_args:
      metadata: '${dataset}metadata_clean.tsv'
      model_prefix: '${dataset}epithelial_cell_2'
      outdir: '$(pwd)/results/'
      ko_file: '$(pwd)/ko_file.txt'
      reps: 2
      model: 'epithelial_cell_2'
      data_folder: '${dataset}'

    # PYCOMPSs args
    num_nodes: 2
    exec_time: 45

These consumer's specific inputs correspond to those declared in the Covid19 application's
workflow specification above. In particular, the consumer specifies the Mare Nostrum 4
as the HPC infrastructure where to deploy the application, as well as PyCOMPSs as
its scheduler. Then, the consumer's required inputs for the Covid19 application
are also given, together with few PyCOMPSs execution parameters, which must be
tuned according to the size of the Covid19 application inputs. The consumer also
provides the Vault secret token required to recover her credentials to get access to
the target HPC infrastructure. **Disclaimer**: In next Croupier release, that will
integrate its frontend, the Vault token will be injected by the frontend, after
the user logs in through the KeyCloak SSO portal.

When the application deployment starts, Cloudify shows the deployment details page.
Once the deploy is complete, you will see a workflow graph with all nodes in green
(successful deployment) or one in red (failed deployment).

.. image:: ../../../_static/figures/cloudify_deployment_success.png
   :width: 1000
   :align: center

.. image:: ../../../_static/figures/cloudify_deployment_failed.png
   :width: 1000
   :align: center

If the deployment fails, the Croupier administrator can inspect the logs, below
in the same web page, to analyse the causes.

**Note:** The workflow graph is application specific and does not reflect the
application deployment topology described above by the provider. This graph is
intended to be interpreted by the Cloudify/Croupier administrator.

Application instance execution
------------------------------
Once a consumer's instance of the application has been deployed into the target HPC
infrastructures, can be executed, by taking the following procedure:

- Click on **Execute workflow** button, and select **Croupier/run_jobs**. Then, the workflow execution will be triggered

.. image:: ../../../_static/figures/croupier_run_jobs.png
   :width: 200
   :align: center

Once the workflow has been started, the status can be monitored with the logs located in the **Deployment Events/Logs** panel at the botton of the web page.

.. image:: ../../../_static/figures/croupier_execution_logs.png
   :width: 1000
   :align: center

When the workflow completes, the status (either failed or succeeded) is reported

.. image:: ../../../_static/figures/croupier_execution_result.png
   :width: 300
   :align: center


**Disclaimer:** The procedure described above to deploy and execute an
application by the consumer will be automated by Croupier frontend in next release.