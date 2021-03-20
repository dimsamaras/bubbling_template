# Bubbling microservice Django template
This repository is a boilerplate Django project for quickly getting started.

## env recommendations
- Python v3.9.2, install it on your local machine
```bash
$ cd <project-repo-folder>
$ python -m venv /path/to/new/virtual/environment
```
## project requirements
- for project dependencies install according to the [requirements.txt](requirements.txt) file, more on the installation of the requirements [here](https://stackoverflow.com/questions/7225900/how-to-install-packages-using-pip-according-to-the-requirements-txt-file-from-a)
```bash
$ pip install -r requirements.txt --no-index --find-links file:///tmp/packages
```
- Docker & Docker-compose for local dev environment. [official guide](https://docs.docker.com/compose/install/) and this [cheatsheet](http://dockerlabs.collabnix.com/docker/cheatsheet/)
- The Bubbling Docker compose [repo](https://github.com/bubbling-eu/bubbling-docker) can be used in order to spin up the infrastructure for local dev
```bash
$ cd <docker-repo-folder>
$ docker-compose up
```

## hard dependencies:
1. Firebase app

## this django template project provides:
1. Django dotenv and split settings
2. PostgresDB setup (default db)
3. Authentication (Firebase) AND REQUIRES connection with Common(user_operator) project
4. Swagger setup
5. PEP8 git hooks for formatting
6. Basic healthchecks app for project and db
7. The 'core' app that includes the rename command `python manage.py rename <yourprojectname> <newprojectname>`
