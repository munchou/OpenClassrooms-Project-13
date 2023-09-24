Database and models' structure
==============================

SQLite3 Database
----------------
*SQLite is a C library that provides a lightweight disk-based database that doesn't require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. It is a self-contained, file-based SQL database.* |br|
As such, we do not need to install any modules or additional software as it comes bundled with Python, and Django natively uses it upon the creation of a new project.

Database content
----------------
There are 3 main objects in the database:

**Profile (profiles_profile)** |br|
Users' / Customers' profiles. |br|
Currently 4 profiles + the admin (not publicly listed). |br|
Each profile has an id (not displayed), a favorite_city and a user_id (not displayed). |br|
A profile displays some of the the user's information stored in the "auth_user" table: first name, last name, email, and favorite city. |br|

**Lettings (lettings_letting)** |br|
Listed properties where their corresponding title is displayed. |br|
Each letting has an id (not displayed), a title, and is linked to an address_id (not displayed, see below). |br|

**Address (lettings_address)** |br|
Addresses of each property. |br|
An address has an id (not displayed), a number, a street, a city, a state, a zip code and a country ISO code. |br|

Models
------
There are 3 models shared between "lettings" and "profiles" apps: Letting, Address and Profile. The following information is from the app's docstrings.

**lettings: Letting** |br|

.. autoclass:: lettings.models.Letting
   :members:

**lettings: Address** |br|

.. autoclass:: lettings.models.Address
   :members:

**profiles: Profile** |br|

.. autoclass:: profiles.models.Profile
   :members:


.. |br| raw:: html
    
        <br>