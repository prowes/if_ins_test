﻿## Info
This repo is a test automation testing assignment. The following test scenarios at the https://www.saucedemo.com/ website are being verified:
- Test locked user logging into
- Test the products sorting
- Test all the E2E shopping flow by ordering several items

## Stack
- Python
- pyTest
- Playwright

## Launching
There can be 3 ways of running it locally.

### In your virtual environment
To launch all the suite locally, you can launch the create_venv_launch.bat file. It will create a virtual environment, install all the libraries and launch the tests.

### Locally
Prerequisites: installed Python, pip. Libraries can be installed with, for example, "pip3 install -r requirements.txt" command and then you can run, for example, "pytest --screenshot=on --headed". 
More information about the arguments can be found here: https://playwright.dev/python/docs/test-runners

### Docker
The repo contains Dockerfile which can be used to build it as an image. Or you can pull it from the Dockerhub (https://hub.docker.com/repository/docker/prowes/if_ta/general):
"docker pull prowes/if_ta"
And then launch the tests with "docker run prowes/if_ta"
