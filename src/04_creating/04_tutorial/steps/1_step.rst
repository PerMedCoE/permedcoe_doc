The first step to create a building block is to generate a template to start
with. The template can be created with the following ``permedcoe`` command:

.. code-block:: console

    $ permedcoe template building_block my_building_block

    Creating Building Block template
    ------------------------------------------
    To be completed:

    - main.py:(20):	TODO: Define your container
    - main.py:(34):	TODO: (optional) Pure python code calling to PyCOMPSs tasks (that can be defined in this file or in another).
    - main.py:(38):	TODO: Define the binary to be used.
    - main.py:(39):	TODO: Define the inputs and output parameters.
    - main.py:(40):	TODO: Define a representative task name
    - main.py:(42):	TODO: Define the binary parameters
    - main.py:(59):	TODO: Declare how to run the binary specification (convert config into building_block_task call)
    ------------------------------------------

The result of this command is a folder named ``my_building_block`` containing
a python package with all scripts and base code to start developing your
Building Block.

.. IMPORTANT::

    The Building Block name in this example is ``my_building_block``, but
    should be defined for your Building Block with a specific name (e.g.
    tool used inside the Building Block or functionality).

    This tutorial will continue using ``my_building_block``, so take it into
    account if you define a different name and swap ``my_building_block`` with
    yours.
