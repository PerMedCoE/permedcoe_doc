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
them. Once the Croupier frontend is integration, this documentation will be
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
Workflows are specify by using the **OASIS TOSCA** specification (https://docs.cloudify.co/latest/developer/blueprints/).


Application installation
------------------------

Application instance deployment
-------------------------------

Application instance execution
------------------------------
