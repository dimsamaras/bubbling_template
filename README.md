# Bubbling microservice Django template

## project requirements
- Python v3.9.2, install it on your local machine 
```bash
$ cd <project-repo-folder>
$ python -m venv /path/to/new/virtual/environment
```
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
## dependencies
1. Firebase app 
2. PostgresDB (default db)

## Provides
1. Authentication (Firebase) AND REQUIRES connection with Common(user_operator) project
2. Swagger setup
3. PEP8 git hooks for formatting
4. Basic healthchecks for project and db