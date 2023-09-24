Description of the API
======================

The API consists of 3 apps: |br|
**oc_lettings_site**, which takes care of the index (homepage), the admin section and the customized 404 page, and links the 2 other apps together. |br|

**lettings**, which manages the main page of the rentals as well as each individual page. |br|
Returns a customized "500 error" in case of bad request (see paragraph about errors below).

**profiles**, which manages the main page of the profiles as well as each individual profile page. |br|
Returns a customized "500 error" in case of bad request (see paragraph about errors below). |br|
 |br|

**In case of errors: Sentry** |br|
Sentry was implemented in order to warn the administrator in any case any errors were to happen. There is the possibility to return customized errors, which was done in case of "bad request", or error 500. This happens when the user enters an invalid URL that targets an object that does not exist in the database (wrong letting or profile id). |br|
As for error 404 (bad URL unrelated to the database), returning an error was not deemed necessary. |br|
|br|
Instead of capturing the exception (*sentry_sdk.capture_exception(err)*) that would display a generic error that does not explicitly show where the error happened, I chose to use a customized message *sentry_sdk.capture_message(f"500 error: {err} {request}")* that would return the type of error AND the request. The latter is important as it allows the administrator to see what the user entered that led to the error, and see if it is an error from the system/database or simply a misspelling/type error. |br|
Django then returns (=displays) the customized 500.html page (*return render(request, "500.html")*).



.. |br| raw:: html
    
        <br>