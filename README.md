## Table of Contents
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code Style](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/pycompile)

<!-- TOC -->
  * [Table of Contents](#table-of-contents)
  * [About the project](#about-the-project)
  * [Installation](#installation)
    * [Install the project 🛠️](#install-the-project-)
  * [Usage](#usage)
  * [Running test cases](#running-test-cases)
<!-- TOC -->


## About the project
The project is structured with two different modules, the `server` and the `client.`
The server is built with `FastAPI` and exposes one single endpoint `greet/` that accepts a `POST` 
request with a JSON payload.
The logic of this service is under `src/services/srv_b` to be able to abstract the logic
of the service  from the server itself.

Same for the client, the logic of the this service is under `src/services/srv_a` alongside with
an `HTTPClient` to abstract the logic of the client from the main file.

The entrypoint for the client service is at 
* `src/client.py` 
* and the entrypoint for the server service is at `src/server.py`


## Installation

### Install the project 🛠️
To automate the whole process of installing the project and its dependencies, the project list
the python dependencies in the `pyproject.toml` file and a `MakeFile` to automate the process.
The requirements are `poetry`, `make` and `pyenv` to manage the python version.
Otherwise, you can install the dependencies manually with min requirement 
`python = ">=3.11,<3.13"`


```bash
python -m venv .env 
source .env/bin/activate
pip install -r requirements.txt
```

or 
```bash
make setup-local-dev
```

## Usage
Start the server by running the following command in the terminal
```bash
uvicorn src.main:app --reload
```
In a separate terminal, run the following command to test the server,
by default the client will send 10 requests to the server,
you can change the number of requests by changing the argument.
```bash
python -m src.client 3
```


## Running test cases
To run the test cases, run the following command in the terminal
```bash
make test-local
```


