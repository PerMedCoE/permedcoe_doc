The first step to create a building block is to generate a template to start
with. The template can be created with the following ``permedcoe`` command:

.. code-block:: console

    $ permedcoe template building_block my_building_block
    Creating Building Block template
    ------------------------------------------
    To be completed:

    - definitions.py:(11):	TODO: Define your container.
    - main.py:(35):	TODO: (optional) Pure python code calling to PyCOMPSs tasks (that can be defined in this file or in another).
    - main.py:(39):	TODO: Define the binary to be used (can be within my_building_block_ASSETS_PATH (e.g. my_binary.sh)).
    - main.py:(40):	TODO: Define the inputs and output parameters.
    - main.py:(41):	TODO: Define a representative task name.
    - main.py:(42):	TODO: Define the binary parameters.
    - main.py:(43):	TODO: Define the binary parameters.
    - main.py:(44):	TODO: Define the binary parameters.
    - main.py:(45):	TODO: Add tmpdir=TMPDIR if the tmpdir will be used by the asset script.
    - main.py:(71):	TODO: Define the arguments required by the Building Block in definition.json file.
    - main.py:(73):	TODO: Declare how to run the binary specification (convert config into building_block_task call).
    - __main__.py:(13):	TODO: Add require_tmpdir=True if the asset requires to write within the tmpdir.
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
