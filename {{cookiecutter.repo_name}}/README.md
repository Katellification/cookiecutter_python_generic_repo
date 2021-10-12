# {{cookiecutter.repo_name}}

High level project description.

## How to submit changes to this repository

To work on this repo, please create a fork and then clone your fork locally. All changes should relate to planned work. If no task exists for your change, please create one.

All work is done off of the 'master' branch.

On your local repo, add your fork as the origin remote and add a remote called 'upstream' with the checkout url of [git@github.com:{{cookiecutter.org_name}}/{{cookiecutter.repo_slug}}.git](git@github.com:{{cookiecutter.org_name}}/{{cookiecutter.repo_slug}}.git)

For each task, create a local feature branch prefixed as follows:

* `add/` for new features
* `remove/` for deletions
* `update/` for iterations on an existing feature or file changes

When work is completed and tested, submit a pull request from your feature branch on your fork to master. If the change is significant, multiple branches and pull requests are encouraged.

Your pull request will be merged to master when it is considered "Ready for production"

### Required tooling

* Text Editor / IDE with PowerShell and editorconfig support
* Python 3.6.8+
* *add any other tooling requirements here*

### Coding practices

Refer to [CONTRIBUTING.md](CONTRIBUTING.md) for coding best practices.

Ensure that you setup the following locally.

```sh
# Install pipx if pipenv is not installed
python3 -m pip install pipx
python3 -m pipx ensurepath

# Install pipenv using pipx
pipx install pipenv

# Install dependencies for the dev virtual environment
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

Work with the virtual environment locally using

```sh
# Activate the virtual environment
pipenv shell

# Deactivate the shell
exit
```

### Testing / Deployment

It is the responsibility of the developer to ensure that their code does not introduce bugs and/or performance issues.

Make sure to add any relevant tests in the testing suite.

## Contacts

{{cookiecutter.github_username}}
