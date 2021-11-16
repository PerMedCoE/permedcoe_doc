The template application (``my_application``) is ready to be used with
multiple workflow managers:


.. dropdown:: PyCOMPSs
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
    :animate: fade-in

    .. CAUTION::

        It is necessary to have installed the PyCOMPSs in order to test
        the application.

        Please, check the `PyCOMPSs installation manual <https://pycompss.readthedocs.io/en/stable/Sections/00_Quickstart.html#install-compss>`_

    There is a ready to use script (``launch.sh``) in order to execute the
    application:

    .. code-block:: CONSOLE

        ./launch.sh

    .. CAUTION::

        If your application requires parameters, the ``launch.sh`` script needs
        to be tuned accordingly.

    .. TIP::

        If any error occurs, it is necessary to debug the execution. To this
        end it is helpful to check the `Troubleshooting for Python section <https://pycompss.readthedocs.io/en/stable/Sections/04_Troubleshooting/01_Debugging_examples/02_Python.html>`_
        from the PyCOMPSs documentation.

    .. TIP::

        It is possible to run the application without PyCOMPSs installed
        using the ``launch_without_pycompss.sh`` script. However, the execution
        of the application will be performed entirely sequentially.


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
