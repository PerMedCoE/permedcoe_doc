The first step to create an application is to generate a template to start
with. The template can be created with the following ``permedcoe`` command:

.. code-block:: console

    permedcoe template application my_application

The result of this command is a folder named ``my_application`` containing
a three folders: NextFlow, PyCOMPSs and Snakemake. Each subfolder contains
a template for that workflow manager with all scripts and base code to start
developing your application.

.. IMPORTANT::

    The application name in this example is ``my_application``, but
    should be defined for your application with a specific name.

    This tutorial will continue using ``my_application`, so take it into
    account if you define a different name and swap ``my_application`` with
    yours.


.. TIP::

    It is possible to create the template for a single workflow manager by
    specifying it in the template creation:

    .. code-block:: console

        permedcoe template application -t <WORKFLOW_MANAGER> my_application

    Where ``<WORKFLOW_MANAGER>`` can be: *pycompss*, *nextflow* or *snakemake*.
