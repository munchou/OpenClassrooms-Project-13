Installing the app and necessary tools
======================================

What you will need:
-------------------
* git : install the latest stable version of git from https://git-scm.com/downloads
* (optional) A GitHub account: https://github.com/
* Python: install the latest stable version of Python from https://www.python.org/



[Optional] If you plan a production use, you will need:
-------------------------------------------------------
* Docker: https://www.docker.com/
* A docker-hub account: https://hub.docker.com/


Installing the application
--------------------------
* **Clone the repository OR download it**
**CLONING:** |br|
To clone the repository, first create a folder where you want it to be installed. |br|
Open your favorite terminal (Command Prompt...), go to that folder (``cd C:\yourpath\yourfolder\``) and initialize git by typing ``git init``. |br|
You can now get the app by cloning the repository: ``git clone https://github.com/munchou/OpenClassrooms-Project-13.git`` |br|

**DOWNLOADING:** |br|
Go to https://github.com/munchou/OpenClassrooms-Project-13, click the green button "<> Code" and chose "Download ZIP". |br|
Extract the ZIP file wherever you want the app to be. |br|

* **Create a virtual environment and install the necessary dependencies**
Once the repository in on your PC, though your terminal, go to that directory and create a virtual environment: |br|
``cd OpenClassrooms-Project-13`` (or any folder where the project is located) |br|
``python -m venv _env`` where _env is the name of the folder where the environment will be created. |br|
Activation: ``_env/Scripts/activate`` |br|
Install the needed modules: ``pip install -r requirements.txt``

.. |br| raw:: html
    
        <br>