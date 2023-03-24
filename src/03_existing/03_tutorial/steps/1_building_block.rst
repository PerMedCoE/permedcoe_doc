Existing Building Blocks can be deployed automatically with the ``permedcoe`` command:

.. code-block:: console

    $ export PERMEDCOE_IMAGES=/path/where/to/store/the/containers/
    $ permedcoe deploy building_block meta_analysis

    [It may take a while since it downloads the required container]

    ------------------------------------------
    ------------ STDOUT ------------
    Defaulting to user installation because normal site-packages is not writeable
    Collecting git+https://github.com/PerMedCoE/BuildingBlocks.git@main#subdirectory=meta_analysis
      Cloning https://github.com/PerMedCoE/BuildingBlocks.git (to revision main) to /tmp/pip-req-build-zdw3mlse
      Resolved https://github.com/PerMedCoE/BuildingBlocks.git to commit 84071d6665edb4a8ea90249ffb5b8e2f583ff13a
      Installing build dependencies: started
      Installing build dependencies: finished with status 'done'
      Getting requirements to build wheel: started
      Getting requirements to build wheel: finished with status 'done'
      Preparing metadata (pyproject.toml): started
      Preparing metadata (pyproject.toml): finished with status 'done'
    Requirement already satisfied: permedcoe>=0.0.8 in /home/user/.local/lib/python3.10/site-packages (from meta-analysis-BB==0.0.3) (0.0.8)
    Requirement already satisfied: pyyaml in /home/user/.local/lib/python3.10/site-packages (from permedcoe>=0.0.8->meta-analysis-BB==0.0.3) (6.0)

    ------------ STDERR ------------
      Running command git clone --filter=blob:none --quiet https://github.com/PerMedCoE/BuildingBlocks.git /tmp/pip-req-build-zdw3mlse

    ------------------------------------------


The result of this command will install the ``meta_analysis`` Building Block
and downloads its required container (stored in ``${PERMEDCOE_IMAGES}`` path).

.. IMPORTANT::

    It is recommended to keep a single ``${PERMEDCOE_IMAGES}`` folder where to
    store all Building Block containers.
