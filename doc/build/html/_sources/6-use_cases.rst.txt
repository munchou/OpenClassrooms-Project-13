User guide with use cases
=========================

When things DO NOT work
-----------------------
As seen in the previous section (API), the app will either return a 404 or 500 error web page (template) in case things go sour. Please refer to the paragraph *In case of errors: Sentry* for more details. |br|

When things work
----------------
The user's requests are (supposed to be) positively handled, returning a *status code 200* and displaying the corresponding page/information (template).

Main page: displays the title and the buttons "Profile" and "Lettings".

Lettings page: displays the list of available lettings and the buttons "Home" and "Profiles". Each letting is clickable and leads to its corresponding description page. |br|
A letting page displays the letting's information as well as the buttons "Back", "Home" and "Profiles".

Profiles page: displays the list of existing profiles and the buttons "Home" and "Lettings". Each profile is clickable and leads to its corresponding description page. |br|
A profile page displays the profile's information as well as the buttons "Back", "Home" and "Lettings".


.. |br| raw:: html
    
        <br>