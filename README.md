Bus system
==========

Jose gabriel guzman

![image](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter%0A%20%20:target:%20https://github.com/pydanny/cookiecutter-django/%0A%20%20:alt:%20Built%20with%20Cookiecutter%20Django)

License
:   MIT

Settings
--------

### Deployment with Docker

Prerequisites
-------------

* Docker 17.05+.
* Docker Compose 1.17+

Understanding the Docker Compose Setup
--------------------------------------

Before you begin, check out the ***local.yml*** file in the root of this project. Keep note of how it provides
configuration for the following services:

- **django:** your application running behind Gunicorn; 
- **postgres:** PostgreSQL database with the application’s relational data;
- **redis:** Redis instance for caching;
- **traefik:** Traefik reverse proxy with HTTPS on by default. Provided you have opted for

Celery (via setting use_celery to y) there are three more services:

- **celeryworker** running a Celery worker process; 
- **celerybeat** running a Celery beat process;
- **flower** running Flower. 
  
The **flower**    service is served by Traefik over HTTPS, through the port 5555. For more information about Flower and its login
credentials, check out Celery Flower instructions for local environment.

Configuring the Stack
--------------------

###  Build the Stack
This can take a while, especially the first time you run this particular command on your development system:


`$ docker-compose -f local.yml build`

Generally, if you want to emulate production environment use production.yml instead. And this is true for any other actions you might need to perform: whenever a switch is required, just do it!

### Run the Stack
This brings up both Django and PostgreSQL. The first time it is run it might take a while to get started, but subsequent runs will occur quickly.

Open a terminal at the project root and run the following for local development:

`$ docker-compose -f local.yml up`

You can also set the environment variable **COMPOSE_FILE** pointing to **local.yml** like this:

` $ export COMPOSE_FILE=local.yml `

And then run:

` $ docker-compose up `

To run in a detached (background) mode, just:

` $ docker-compose up -d`


Execute Management Commands
--------------------
As with any shell command that we wish to run in our container, this is done using the **docker-compose -f local.yml run --rm** command:




`$ docker-compose -f local.yml run --rm django python manage.py migrate`
`$ docker-compose -f local.yml run --rm django python manage.py createsuperuser`


extended documentation

https://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html#prerequisites

Access the API
--------------------
First of all remember to download and import the postman environment to access the api documentation.

https://documenter.getpostman.com/view/15549966/TzedfPM7
