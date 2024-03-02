# {{ cookiecutter.project_name }}

[![falco](https://img.shields.io/badge/built%20with-falco-success)](https://github.com/Tobi-De/falco)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)

## Prerequisites

- `Python 3.11+`
- `hatch 1.9.1+`

## Development

### Create a new virtual environment

```shell
hatch shell
```

### Install pre-commit

```shell
git init && pre-commit install
```

Ensure that the Python version specified in your `.pre-commit-config.yaml` file aligns with the Python version installed on your system.

### Apply migrations

```shell
hatch run migrate
```

### Create a superuser

Follow the tip described [here](https://falco.oluwatobi.dev/guides/tips_and_extra.html#create-superuser-from-environment-variables) and execute the command below to create a superuser.

```shell
python manage.py createsuperuser --no-input
```

### Run the django development server

```shell
falco work
```
