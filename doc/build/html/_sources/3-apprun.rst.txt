Quickstart : Running the application
====================================

Starting the application through Python
---------------------------------------
To start the server, in your terminal (you must be in the app root folder where "manage.py" is located): ``python manage.py runserver`` |br|
You should get a message similar to that one:

*Performing system checks...* |br|
*System check identified no issues (0 silenced).* |br|
*September 22, 2023 - 16:55:07* |br|
*Django version 3.0, using settings 'oc_lettings_site.settings'* |br|
*Starting development server at http://127.0.0.1:8000/* |br|
*Quit the server with CTRL-BREAK.* |br|

Open your browser and connect to the app through either http://127.0.0.1:8000/ or http://localhost:8000/

To stop the server, press *CTRL+C* in the terminal.


Starting the application through Docker
---------------------------------------
You can start the application by using a Docker container. To do so, start Docker (if it is not already running in the background). |br|
Download the image by opening the batch file "docker-pull-image.bat". Enter your username and your password. If you could succesfully log in, you will be asked if you wish to download the image. Type "y", press ENTER and wait for the image to have been downloaded. The program will automatically log you out once the download is complete.

You will NOT see any new file in your folder. Instead, the image is automatically downloaded in a Docker's corresponding folder and will directly appear in the Docker Desktop software. |br|

Get back to the Docker software, select the "Images" tab, and you should see the freshly downloaded image named "munchou/munchou_oc_p13" with the tag "latest". |br|
Click on the "run" button (the triangle) and in optional settings, type in "8000" in the "Ports" tab, then click "Run". |br|
A new container is created, and the image is run. You should see similar lines as above and some stuff about the /static/ folder:

*2023-09-22 21:49:05 Performing system checks...* |br|
*2023-09-22 21:49:05 * |br|
*2023-09-22 21:49:05 System check identified no issues (0 silenced).* |br|
*2023-09-22 21:49:05 September 22, 2023 - 12:49:05* |br|
*2023-09-22 21:49:05 Django version 3.0, using settings 'oc_lettings_site.settings'* |br|
*2023-09-22 21:49:05 Starting development server at http://0.0.0.0:8000/* |br|
*2023-09-22 21:49:05 Quit the server with CONTROL-C.* |br|
*...* |br|
*2023-09-22 21:49:14 [22/Sep/2023 12:49:14] "GET /static/assets/img/logo.png HTTP/1.1" 200 27037* |br|

Open your browser and connect to the app through either http://127.0.0.1:8000/ or http://localhost:8000/

Once you are done, you can either press the stop button (the square) or directly press the trash can, which will stop the run and delete the current container.


.. |br| raw:: html
    
        <br>