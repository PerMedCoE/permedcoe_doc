Existing Workflows can be deployed automatically with the ``permedcoe`` command:

.. code-block:: console

    $ export PERMEDCOE_IMAGES=/path/where/to/store/the/containers/
    $ permedcoe deploy workflow covid-19-workflow
    SUCCESS: Workflow deployed.

    [It may take a while since it deployes all building blocks required by this workflow]


The result of this command will deploy the ``covid-19-workflow`` Workflow
within the current directory. It further installs the required Building Blocks
as well as downloads their required containers (storing them in ``${PERMEDCOE_IMAGES}`` path).

.. IMPORTANT::

    It is recommended to keep a single ``${PERMEDCOE_IMAGES}`` folder where to
    store all Building Block containers.
