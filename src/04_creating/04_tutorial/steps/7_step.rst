The template application (``my_application``) is ready to be used with
multiple workflow managers:


.. dropdown:: PyCOMPSs
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
    :animate: fade-in

    .. CAUTION::

        It is necessary to have installed PyCOMPSs in order to test the application.

        Please, check the `PyCOMPSs installation manual <https://pycompss.readthedocs.io/en/stable/Sections/00_Quickstart.html#install-compss>`_

    There is a ready to use script (``launch.sh``) in order to execute the application:

    .. code-block:: CONSOLE

        $ cd my_application/PyCOMPSs
        $ ./launch.sh hi.txt bye2.txt

        ------------------------------------------
        ------------ STDOUT ------------
        [  INFO] Inferred PYTHON language
        [  INFO] Using default location for project file: /opt/COMPSs//Runtime/configuration/xml/projects/default_project.xml
        [  INFO] Using default location for resources file: /opt/COMPSs//Runtime/configuration/xml/resources/default_resources.xml
        [  INFO] Using default execution type: compss

        ----------------- Executing app.py --------------------------

        Binding debug is activated
        [BINDING-COMMONS] - @JNI_On - Creating the JVM
        [BINDING-COMMONS]  -  @create_vm  -  reading file in JVM_OPTIONS_FILE
        [BINDING-COMMONS]  -  @create_vm  -  Launching JVM
        [BINDING-COMMONS]  -  @create_vm  -  JVM Ready
        [BINDING-COMMONS] - @JNI_On - Obtaining Runtime classes
        Loading LoggerManager
        [BINDING-COMMONS] - @JNI_On - Creating runtime object
        [(505)    API]  -  Deploying COMPSs Runtime v3.1
        [BINDING-COMMONS] - @JNI_On - Calling runtime start
        [(506)    API]  -  Starting COMPSs Runtime v3.1
        [(506)    API]  -  Initializing components
        [(880)    API]  -  Ready to process tasks
        [BINDING-COMMONS] - @Init JNI Types
        [BINDING-COMMONS] - @Init JNI Types DONE
        [BINDING-COMMONS] - @Init JNI Master
        [BINDING-COMMONS] - @Init JNI Methods
        [BINDING-COMMONS] - @Init JNI Methods DONE
        [BINDING-COMMONS] - @Init JNI OnFailure Types
        [BINDING-COMMONS] - @Init JNI Direction Types
        [BINDING-COMMONS] - @Init JNI Direction Types DONE
        [BINDING-COMMONS] - @Init JNI Stream Types
        [BINDING-COMMONS] - @Init JNI Stream Types
        [BINDING-COMMONS] - @Init JNI Parameter Prefix
        [BINDING-COMMONS] - @Init JNI Parameter Prefix DONE
        [BINDING-COMMONS] - @Init Master DONE
        [BINDING-COMMONS] - @JNI_Get_AppDir - Getting application directory.
        [BINDING-COMMONS] - @JNI_Get_AppDir - directory name: /home/user/.COMPSs/app.py_01/
        Sample python application using my_building_block BB
        [(888)    API]  -  Registering CoreElement my_building_block.main.building_block_task
        [(889)    API]  -  	 - Implementation: my_building_block.main.building_block_task
        [(889)    API]  -  	 - Constraints   :
        [(889)    API]  -  	 - Type          : CONTAINER
        [(889)    API]  -  	 - I/O            : False
        [(889)    API]  -  	 - ImplTypeArgs  :
        [(889)    API]  -  		 Arg: SINGULARITY
        [(889)    API]  -  		 Arg: /home/user/permedcoe/my_building_block/container/sample.sif
        [(889)    API]  -  		 Arg: CET_BINARY
        [(889)    API]  -  		 Arg: cp
        [(889)    API]  -  		 Arg: [unassigned]
        [(889)    API]  -  		 Arg: [unassigned]
        [(889)    API]  -  		 Arg: false
        [BINDING-COMMONS] - @JNI_RegisterCE - Task registered: my_building_block.main.building_block_task
        [BINDING-COMMONS] - @JNI_ExecuteTaskNew - Processing task execution in bindings-common.
        [BINDING-COMMONS] - @JNI_ExecuteTaskNew - Processing parameter 0
        [BINDING-COMMONS] - @process_param
        [BINDING-COMMONS] - @process_param - ENUM DATA_TYPE: 9
        [BINDING-COMMONS] - @process_param - File: hi.txt
        [BINDING-COMMONS] - @process_param - ENUM DIRECTION: 0
        [BINDING-COMMONS] - @process_param - ENUM STD IO STREAM: 3
        [BINDING-COMMONS] - @process_param - PREFIX: null
        [BINDING-COMMONS] - @process_param - NAME: #kwarg_input_file
        [BINDING-COMMONS] - @process_param - CONTENT TYPE: FILE
        [BINDING-COMMONS] - @process_param - WEIGHT : 1.0
        [BINDING-COMMONS] - @process_param - KEEP RENAME : 0
        [BINDING-COMMONS] - @JNI_ExecuteTaskNew - Processing parameter 1
        [BINDING-COMMONS] - @process_param
        [BINDING-COMMONS] - @process_param - ENUM DATA_TYPE: 9
        [BINDING-COMMONS] - @process_param - File: bye2.txt
        [BINDING-COMMONS] - @process_param - ENUM DIRECTION: 1
        [BINDING-COMMONS] - @process_param - ENUM STD IO STREAM: 3
        [BINDING-COMMONS] - @process_param - PREFIX: null
        [BINDING-COMMONS] - @process_param - NAME: #kwarg_output_file
        [BINDING-COMMONS] - @process_param - CONTENT TYPE: FILE
        [BINDING-COMMONS] - @process_param - WEIGHT : 1.0
        [BINDING-COMMONS] - @process_param - KEEP RENAME : 0
        [BINDING-COMMONS] - @JNI_ExecuteTaskNew - Processing parameter 2
        [BINDING-COMMONS] - @process_param
        [BINDING-COMMONS] - @process_param - ENUM DATA_TYPE: 8
        [BINDING-COMMONS] - @process_param - String: -v
        [BINDING-COMMONS] - @process_param - ENUM DIRECTION: 0
        [BINDING-COMMONS] - @process_param - ENUM STD IO STREAM: 3
        [BINDING-COMMONS] - @process_param - PREFIX: null
        [BINDING-COMMONS] - @process_param - NAME: #kwarg_verbose
        [BINDING-COMMONS] - @process_param - CONTENT TYPE: #UNDEFINED#:#UNDEFINED#
        [BINDING-COMMONS] - @process_param - WEIGHT : 1.0
        [BINDING-COMMONS] - @process_param - KEEP RENAME : 1
        [(902)    API]  -  Creating task from method my_building_block.main.building_block_task for application 0
        [(902)    API]  -  There are 3 parameters
        [(905)    API]  -   Parameter 0 has type FILE_T
        [(909)    API]  -   Parameter 1 has type FILE_T
        [(909)    API]  -   Parameter 2 has type STRING_T
        [BINDING-COMMONS] - @JNI_ExecuteTaskNew - Task processed.
        [BINDING-COMMONS] - @JNI_Off
        [BINDING-COMMONS] - @Off - Waiting to end tasks
        [(912)    API]  -  No more tasks for app 0
        [(4229)    API]  -  Getting Result Files for app0
        [BINDING-COMMONS] - @Off - Stopping runtime
        [(4265)    API]  -  Stopping Wall Clock limit Timer
        [(4265)    API]  -  Stop IT reached
        [(4265)    API]  -  Stopping Graph generation...
        [(4265)    API]  -  Stopping AP...
        [(4266)    API]  -  Stopping TD...
        [(4418)    API]  -  Stopping Comm...
        [(4419)    API]  -  Runtime stopped
        [(4419)    API]  -  Execution Finished
        [BINDING-COMMONS] - @Off - Revoke thread access to JVM
        [BINDING-COMMONS] - @Off - Removing JVM
        [BINDING-COMMONS] - @Off - Removing environment
        [BINDING-COMMONS] - @Off - End

        ------------------------------------------------------------

        ------------ STDERR ------------
        WARNING: COMPSs Properties file is null. Setting default values
        2021-11-16 15:43:46,197 - DEBUG - Executing container_f wrapper.
        2021-11-16 15:43:46,198 - DEBUG - Configuring @container core element.
        2021-11-16 15:43:46,198 - DEBUG - Executing binary_f wrapper.
        2021-11-16 15:43:46,198 - DEBUG - Configuring @binary core element.
        2021-11-16 15:43:46,198 - DEBUG - [@TASK] Task type of function building_block_task in module my_building_block.main: CONTAINER
        2021-11-16 15:43:46,199 - DEBUG - Configuring core element.
        2021-11-16 15:43:46,199 - DEBUG - [@TASK] Registering the function building_block_task in module my_building_block.main
        2021-11-16 15:43:46,199 - DEBUG - Registering CE with signature: my_building_block.main.building_block_task
        2021-11-16 15:43:46,199 - DEBUG - 	 - Implementation signature: my_building_block.main.building_block_task
        2021-11-16 15:43:46,199 - DEBUG - 	 - Implementation constraints:
        2021-11-16 15:43:46,199 - DEBUG - 	 - Implementation type: CONTAINER
        2021-11-16 15:43:46,199 - DEBUG - 	 - Implementation type arguments: SINGULARITY /home/user/permedcoe/my_building_block/container/sample.sif CET_BINARY cp [unassigned] [unassigned] false
        2021-11-16 15:43:46,204 - DEBUG - CE with signature my_building_block.main.building_block_task registered.
        2021-11-16 15:43:46,209 - DEBUG - Final type for parameter #kwarg_input_file: 9
        2021-11-16 15:43:46,210 - DEBUG - Final type for parameter #kwarg_output_file: 9
        2021-11-16 15:43:46,210 - DEBUG - Final type for parameter #kwarg_verbose: 8
        2021-11-16 15:43:46,210 - DEBUG - TASK: building_block_task of type 1, in module my_building_block.main, in class
        2021-11-16 15:43:46,210 - DEBUG - Processing task:
        2021-11-16 15:43:46,210 - DEBUG - 	- App id: 0
        2021-11-16 15:43:46,210 - DEBUG - 	- Signature: my_building_block.main.building_block_task
        2021-11-16 15:43:46,210 - DEBUG - 	- Has target: False
        2021-11-16 15:43:46,210 - DEBUG - 	- Names: #kwarg_input_file #kwarg_output_file #kwarg_verbose
        2021-11-16 15:43:46,210 - DEBUG - 	- Values: hi.txt bye2.txt -v
        2021-11-16 15:43:46,210 - DEBUG - 	- COMPSs types: 9 9 8
        2021-11-16 15:43:46,210 - DEBUG - 	- COMPSs directions: 0 1 0
        2021-11-16 15:43:46,210 - DEBUG - 	- COMPSs streams: 3 3 3
        2021-11-16 15:43:46,211 - DEBUG - 	- COMPSs prefixes: null null null
        2021-11-16 15:43:46,211 - DEBUG - 	- Content Types: FILE FILE #UNDEFINED#:#UNDEFINED#
        2021-11-16 15:43:46,211 - DEBUG - 	- Weights: 1.0 1.0 1.0
        2021-11-16 15:43:46,211 - DEBUG - 	- Keep_renames: False False True
        2021-11-16 15:43:46,211 - DEBUG - 	- Priority: False
        2021-11-16 15:43:46,211 - DEBUG - 	- Num nodes: 1
        2021-11-16 15:43:46,211 - DEBUG - 	- Reduce: False
        2021-11-16 15:43:46,211 - DEBUG - 	- Chunk Size: 0
        2021-11-16 15:43:46,211 - DEBUG - 	- Replicated: False
        2021-11-16 15:43:46,211 - DEBUG - 	- Distributed: False
        2021-11-16 15:43:46,211 - DEBUG - 	- On failure behavior: RETRY
        2021-11-16 15:43:46,212 - DEBUG - 	- Task time out: 0
        2021-11-16 15:43:46,223 - DEBUG - --- END ---
        2021-11-16 15:43:46,223 - INFO - Stopping runtime...
        2021-11-16 15:43:46,223 - INFO - Cleaning objects...
        2021-11-16 15:43:46,223 - INFO - Stopping COMPSs...
        2021-11-16 15:43:50,330 - INFO - Cleaning temps...
        2021-11-16 15:43:50,345 - INFO - COMPSs stopped

        ------------------------------------------


    .. CAUTION::

        If your application requires parameters, the ``launch.sh`` script needs
        to be tuned accordingly.

    .. TIP::

        The output is very verbose since PyCOMPSs has been executed in debug
        mode. It can be executed silently by removing the ``-d`` flag from
        the ``launch.sh`` script.

    .. TIP::

        If any error occurs, it is necessary to debug the execution. To this
        end it is helpful to execute in debug mode (as it is currently) and
        check the `Troubleshooting for Python section <https://pycompss.readthedocs.io/en/stable/Sections/04_Troubleshooting/01_Debugging_examples/02_Python.html>`_
        from the PyCOMPSs documentation.

    .. TIP::

        It is possible to run the application without PyCOMPSs installed
        using the ``launch_without_pycompss.sh`` script. However, the execution
        of the application will be performed entirely sequentially.


.. dropdown:: Snakemake
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
    :animate: fade-in

    .. CAUTION::

        It is necessary to have installed Snakemake in order to test the application.

    There is a ready to use script (``launch.sh``) in order to execute the application:

    .. code-block:: CONSOLE

        $ cd my_application/SnakeMake
        $ ./launch.sh

.. dropdown:: NextFlow
    :container: + shadow
    :title: bg-primary text-white font-weight-bold
    :animate: fade-in

    .. CAUTION::

        It is necessary to have installed NextFlow in order to test the application.

    There is a ready to use script (``launch.sh``) in order to execute the application:

    .. code-block:: CONSOLE

        $ cd my_application/NextFlow
        $ ./launch.sh
