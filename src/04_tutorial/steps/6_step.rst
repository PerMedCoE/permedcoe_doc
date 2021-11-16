The Building Block is ready to be used from multiple workflow managers:

.. dropdown:: PyCOMPSs
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
    :animate: fade-in

    Now its time to add logic to the application template.
    To this end, you can use your desired text editor or Python IDE.

    There is only one file that requires attention (**app.py**):

    .. code-block:: CONSOLE

        cd my_application/PyCOMPSs/

        # Edit: app.py

    In this file, it is necessary to develop the following:

    Imports *[MANDATORY]*
        It is necessary to import the building block (in the template
        ``my_building_block``) methods:

        .. code-block:: PYTHON

            # Import building block entry points
            from my_building_block import invoke
            from my_building_block import my_building_block_task

        .. TIP::

            You can import any other method from the Building Block.

    ``main`` method *[MANDATORY]*
        It is required to implement the logic of the application that
        uses the building blocks methods.

        It can use directly ``invoke`` to mimic the command line interface.
        But you can use any other method from the Building Blocks and invoke
        them directly.

        .. TIP::

            The ``my_application`` already uses ``my_building_block``.


.. dropdown:: Snakemake
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
    :animate: fade-in

    To be completed...

.. dropdown:: NextFlow
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
    :animate: fade-in

    To be completed...
