The Building Block is ready to be used from multiple workflow managers,
and we already have a template for each workflow manager:

.. dropdown:: PyCOMPSs
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
    :animate: fade-in

    Now its time to add logic to the application template.
    To this end, you can use your desired text editor or Python IDE.

    There is only one file that requires attention (**app.py**):

    .. code-block:: console

        $ cd my_application/PyCOMPSs/

        # Edit: app.py

    In this file, it is necessary to develop the following:

    Imports *[MANDATORY]*
        It is necessary to import the building block (in the template
        ``my_building_block``) methods:

        .. code-block:: python

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

            .. code-block:: python

                def main():
                    # Sample application:
                    print("Sample python application using my_building_block BB")
                    # Get parameters
                    input_file = str(sys.argv[1])
                    output_file = str(sys.argv[2])
                    conf = {}  # conf is empty since it is not used by my_building_block
                    # Building Block invocation
                    building_block_task(input_file=input_file,
                                        output_file=output_file)

            *NOTE:* That the parameters match the ``building_block_task`` function definition.



.. dropdown:: Snakemake
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
    :animate: fade-in

    Now its time to add logic to the SnakeMake application template.
    To this end, you can use your desired text editor or Python IDE.

    There is only one file that requires attention (**Snakefile**):

    .. code-block:: console

        $ cd my_application/SnakeMake/

        # Edit: Snakefile

    In this file, it is necessary to declare the building blocks as rules and implement their dependencies.
    The next code snippet shows an example using `my_bulding_block`:

    .. code-block:: console

        rule BUILDINGBLOCK:
        input:
            dataset="/path/to/dataset",
            config="/path/to/conf.yaml"
        output:
            result="/path/to/result"
        shell:
            "permedcoe execute building_block my_building_block --model {input.dataset} --result {output.result} --config {input.config}"


.. dropdown:: NextFlow
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
    :animate: fade-in

    Now its time to add logic to the NextFlow application template.
    To this end, you can use your desired text editor or Python IDE.

    There is only one file that requires attention (**NextFlow**):

    .. code-block:: console

        $ cd my_application/NextFlow/

        # Edit: NextFlow.nf

    In this file, it is necessary to declare the building blocks as rules and implement their dependencies.
    The next code snippet shows an example using `my_bulding_block`:

    .. code-block:: console

        params.input="/path/to/dataset"
        params.config="/path/to/conf.yaml"

        input_ch = Channel.fromPath(params.input)
        conf_ch = Channel.fromPath(params.config)

        process BUILDINGBLOCK {
            input:
            file dataset from input_ch
            file conf from conf_ch

            output:
            file "output" into res_ch

            """
            permedcoe execute building_block my_building_block --model $dataset --result output --config $conf
            """
        }
