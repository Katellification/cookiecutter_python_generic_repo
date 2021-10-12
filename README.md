# cookiecutter_python_generic_repo

This is a [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/index.html) template to create a new Python repository.

## Features
- Testing with [pytest](https://docs.pytest.org/en/latest/)
- Formatting with [black](https://github.com/psf/black)
- Import sorting with [isort](https://github.com/timothycrosley/isort)
- Static typing with [mypy](http://mypy-lang.org/)
- Linting with [flake8](http://flake8.pycqa.org/en/latest/)
- Git hooks that run all the above with [pre-commit](https://pre-commit.com/)

## Usage

### Repository naming convention

1. Use [snake case](https://en.wikipedia.org/wiki/Snake_case)
1. Do not use `-` 
1. Do not use non-alphanumeric symbols other than underscore `_`

### Quickstart

```sh
# Install pipx if pipenv and cookiecutter are not installed
python3 -m pip install pipx
python3 -m pipx ensurepath

# Install pipenv using pipx
pipx install pipenv

# Use cookiecutter to create project from this template
pipx run cookiecutter https://github.com/Katellification/cookiecutter_python_generic_repo.git

# Enter project directory
cd <repo_name>

# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```
