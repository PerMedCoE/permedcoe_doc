Tutorial
========

This section provides a step-by-step by tutorial on how to deploy existing Building
Blocks and Workflows using the **permedcoe** package.

Requirements
------------

It is **required** to install the ``permedcoe`` package.
To this end, you can use **pip**:

.. code-block:: console

    python3 -m pip install permedcoe

.. TIP::

    Alternatively, it is possible to be
    `installed from source <../01_installation/installation.html#installation-from-source-code>`_

And it is also **required** to install singularity and apptainer (automatic container download).

Please, check the `Singularity installation documentation <https://sylabs.io/guides/3.0/user-guide/quick_start.html#quick-installation-steps>`__
and the `Apptainer installation documentation <https://apptainer.org/docs/admin/main/installation.html>`__.


Deployment
----------

.. dropdown:: Deploy an existing Building Block
    :animate: fade-in

    .. include:: /03_existing/03_tutorial/steps/1_building_block.rst


.. dropdown:: Deploy an existing Workflow
    :animate: fade-in

    .. include:: /03_existing/03_tutorial/steps/2_workflow.rst
