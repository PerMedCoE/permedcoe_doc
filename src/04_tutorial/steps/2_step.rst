Now its time to add logic to the Building Block template. To this end, you can
use your desired text editor or Python IDE.

There is only one file that requires attention (**main.py**):

.. code-block:: CONSOLE

    cd my_building_block/src/my_building_block

    # Edit: main.py

In this file, it is necessary to develop the following methods:

- ``building_block_task`` *[MANDATORY]*
- ``invoke`` *[MANDATORY]*
- ``function_name`` *[OPTIONAL]*

The next Subsections describe each method development:

.. dropdown:: "building_block_task" method development
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
    :animate: fade-in

    The ``building_block_task`` is the core method of the Building Block. It
    is used to define the Building Block functionality, and requires attention in
    two main places: its decorators and its parameters.

    The ``building_block_task`` needs to be decorated with the ``permedcoe``'s
    decorators (in the same order from top to bottom):


    ``@container``
        To define the container to be used for the building block execution.
    ``@binary``
        To define if the ``building_block_task`` represents the execution of a
        binary application (that must be available in the container).
        It includes the information related to the binary to be executed when
        the method is invoked.
        This decorator is *optional*. When this decorator is present, the
        ``building_block_task`` method must be empty (include only ``pass``).
        However, the ``building_block_task`` can contain Python code when it
        is not defined.
    ``@task``
        To define that the method ``building_block_task`` is going to be considered
        as a single task.
        It includes the information related to the parameters, such as type and
        direction (e.g. ``FILE_IN``, ``FILE_OUT``, ``FILE_INOUT``,
        ``DIRECTORY_IN``, ``DIRECTORY_OUT``, ``DIRECTORY_INOUT``).

    Lets consider the following code as example:

    .. code-block:: PYTHON

        SAMPLE_CONTAINER = "/path/to/image.sif"

        @container(engine="SINGULARITY", image=SAMPLE_CONTAINER)
        @binary(binary="/path/to/my_binary")
        @task(dataset=FILE_IN, output=FILE_OUT)
        def building_block_task(dataset_flag="-d", dataset=None,
                                output_flag="-o", output=None,
                                operation="-x"):
        # Empty function since it represents a binary execution:
        pass

    The ``building_block_task`` is a method that is equivalent to:

    .. code-block:: CONSOLE

        /path/to/my_binary -d dataset -o output -x

    Where the decorators define:

    ``@container(engine="SINGULARITY", image=SAMPLE_CONTAINER)``
        The container that will be used to execute the Building Block.

        **It must be updated with the container path for your Building Block.**
    ``@binary(binary="/path/to/my_binary")``
        The binary to be executed by the Building Block.

        **It must be updated with the binary path for your Building Block.**
    ``@task(dataset=FILE_IN, output=FILE_OUT)``
        The parameters type and direction. In this example, there are two parameters
        that are files, one used as input (``dataset``) and another produced by
        the binary execution (``output``).

        **It must be updated with the ary path for your Building Block.**

    And the function is defined:

    .. code-block:: Python

        def building_block_task(dataset_flag="-d", dataset=None,
                                output_flag="-o", output=None,
                                operation="-x"):

    Each parameter is interpreted in order, and all of them should include the
    default value to ease the invocation (e.g. ``None`` is useful for ``FILES`` and
    ``DIRECTORIES``, whilst for the rest integers or strings can be enough).

    The two required actions in the function definition are:

    - **Define a representative function name** (e.g. ``building_block_task`` in the example)
    - **Define the function parameters parameters**

    .. IMPORTANT::

        Please, check carefully the function parameters as well as the ``@task``
        parameter definition.

    .. HINT::

        It can also be a normal python function that calls decorated
        methods.

        This will enable to exploit inner parallelism when used with
        PyCOMPSs.

.. dropdown:: "invoke" method development
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
    :animate: fade-in

    The ``invoke`` method is necessary to bind the parameters defined through
    command line into the invocation of ``building_block_task`` function.

    .. CAUTION::

        The name ``invoke`` **MUST NOT** be changed.

    The ``invoke`` method receives three parameters:

    ``input``
        List of input parameters, or the element if only one input.
    ``output``
        List of output parameters, or the element if only one output.
    ``config``
        Dictionary with the yaml configuration provided.

    Consider the following ``invoke`` example:

    .. code-block:: Python

        def invoke(input, output, config):
            operation = config["operation"]
            building_block_task(dataset=input,
                                output=output,
                                operation=operation)

    This example gets the ``operation`` field from config, and then
    invokes the ``building_block_task`` method specifying the necessary parameters
    explicitly (``dataset``, ``output`` and ``operation``).

.. dropdown:: "function_name" method development
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
    :animate: fade-in

    A building block can be invoked through command line, and the method
    used in this case is ``invoke``.

    However, since the Building Block can be used in PyCOMPSs workflows,
    the methods can be invoked directly. This means that the workflow can
    directly invoke ``building_block_task`` or any other method.

    Consequently, this method is **OPTIONAL** but it is recommended in
    order to ease the Building Block call from a PyCOMPSs workflow
    application.

    .. HINT::

        It can also be a normal python function that calls decorated
        methods.

        This will enable to exploit inner parallelism when used with
        PyCOMPSs.
