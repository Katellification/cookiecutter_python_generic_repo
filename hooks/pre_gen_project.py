import re
import sys


REPO_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

repo_slug = '{{ cookiecutter.repo_slug }}'

if not re.match(REPO_REGEX, repo_slug):
    # Modify this however suits your naming conventions
    print('ERROR: The repository name (%s) is not valid. Please do not use a - use _ instead and refer to the naming conventions.' % repo_slug)

    #Exit to cancel project
    sys.exit(1)
