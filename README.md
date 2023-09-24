# ABOUT

**OpenClassrooms - Développeur d'application Python - Project #13: Deploy a Django app using a modular architecture**

_Tested with Windows 10 and Python 3.10.2_

Orange County Lettings is a start-up in the real estate rental industry. The start-up, in the midst of an expansion phase in the United States, hired developers to improve their website (the actual Django app in that project).
Among the improvements to work on:
- the structure that must be changed from monolithic into modular
- optimization of the code
- set up of a CI/CD pipeline (Continuous Integration / Continuous Delivery)
- errors report via Sentry
- creation of the documentation

_Please note that to test the app locally, you DO NOT need Docker. If you wish to test the app through a Docker container, refer to the documentation._

# Hao2do (Windows)

The following steps are only to setup your machine and start the program.


## Retrieving a copy of the "depository"

- `git clone https://github.com/munchou/OpenClassrooms-Project-13.git`

or download the ZIP file and extract it in a chosen folder.


## Creating and activating the virtual environment
(Python must have been installed)
- `cd OpenClassrooms-Project-13` (or any folder where the project is located)
- `python -m venv _env_` where _env_ is the name of the folder where the environment will be created.
- Activation : `_env/Scripts/activate`
    

## Installing the needed modules

- `pip install -r requirements.txt`


## Starting the program
You must first start the server by typing
`python manage.py runserver`

You can then access the app (website) through your browser by connecting to either http://127.0.0.1:8000/ or http://localhost:8000/

To stop the server, press CTRL+C in the terminal.


## Documentation
The [DOCUMENTATION](https://openclassrooms-project-13.readthedocs.io/en/latest/) was created using Sphinx and is hosted on [Read the Docs](https://readthedocs.org/).


## Admin
`http://localhost:8000/admin` or `http://127.0.0.1:8000/admin`

user: admin, password: Abc1234!
