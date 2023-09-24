CI/CD Pipeline
==============

Introduction: used tools
------------------------
*see "Installing the app and necessary tools" for more information*

* GitHub (online)
* Docker (software)
* docker-hub (online)
* CircleCI (online)
* Microsoft host: Azure (online)

Principle
---------
Provided everything has been properly set up.

1/ The app is uploaded/updated to the corresponding GitHub repository.

2/ CircleCI automatically detects whenever a change occurrs in the repository. Upon any changes, the pipeline is launched through a specific file ("config.yml") that provides the necessary steps to follow. |br|
The steps are divided in 2 main parts: |br|
- BUILD: the Docker image is pre-processed following specific steps/constraints such as the type of image and version of Python, running tests, etc. |br|
- DEPLOYMENT: the image is built, configured by using encrypted variables ("environment variables" or "secret variables") stored online on CircleCI, hence not publicly accessible. Once successful, the image is then uploaded ("pushed") to the corresponding docker-hub.

3/ Whenever an image is uploaded to docker-hub, it will "inform" Azure thanks to a "webhook URL" that acts as a bridge between the 2 entities. By doing so, Azure then downloads the image and automatically deploys it.

**The total process from a commit to online deployment (with actual visible changes online after refreshing the website) takes about 2 minutes**



.. |br| raw:: html
    
        <br>