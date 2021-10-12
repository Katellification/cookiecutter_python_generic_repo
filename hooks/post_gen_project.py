import subprocess, time, sys

python_version = str(sys.version_info.major) + "." + str(sys.version_info.minor)

with open("Pipfile") as f:
    pipfile = f.read()
    pipfile = pipfile.replace(r"{python_version}", python_version)

with open("Pipfile", "w") as f:
    f.write(pipfile)

username = "{{ cookiecutter.github_username }}"
github_url = "https://github.com/"  # May need to be modified if using github enterprise with your own domain
org_name = "{{ cookiecutter.org_name }}"
repo_name = "{{ cookiecutter.repo_slug }}"

org_repo_to_be_created = "{{ cookiecutter.create_upstream_fork_repo_on_github }}"
remove_test_files = "{{ cookiecutter.exclude_test_files }}"

team_id = "{{ cookiecutter.github_team_id }}"
valid_team_id = team_id.isnumeric() and int(team_id) > 0
if valid_team_id:
    team_id = int(team_id)

if org_repo_to_be_created == "yes":
    # create git repo locally
    subprocess.run("git init", shell=True)
    subprocess.run("git add --all", shell=True)
    subprocess.run('git commit -m "initial commit"', shell=True)

    cmd_create_repo = (
        'curl -i -H "Content-Type: application/json" -u "%s" %sapi/v3/orgs/%s/repos -d "{\\"name\\":\\"%s\\"}"'
        % (username, github_url, org_name, repo_name)
    )

    if valid_team_id:
        cmd_create_repo = cmd_create_repo.replace(
            "}", ', \\"team_id\\":%s}' % (team_id)
        )

    # create org repo
    subprocess.run(cmd_create_repo, shell=True)

    if valid_team_id:
        # add repo to team with admin permissions -- issues getting this to work properly
        subprocess.run(
            'curl -i -X PUT -H "Content-Type: application/json" -u "%s" %sapi/v3/teams/%s/repos/%s/%s -d "{\\"permission\\":\\"admin\\"}"'
            % (username, github_url, team_id, org_name, repo_name),
            shell=True,
        )
        time.sleep(2)

    subprocess.run(
        "git remote add upstream %s%s/%s.git" % (github_url, org_name, repo_name),
        shell=True,
    )
    pushed = subprocess.run("git push -u upstream master", shell=True)

    # create fork (origin)
    if pushed == 0:
        subprocess.run(
            'curl -i -H "Content-Type: application/json" -u "%s" %sapi/v3/repos/%s/%s/forks -d ""'
            % (username, github_url, org_name, repo_name),
            shell=True,
        )
        subprocess.run(
            "git remote add origin %s%s/%s.git" % (github_url, username, repo_name),
            shell=True,
        )
        subprocess.run("git push -u origin master", shell=True)
        subprocess.run("git remote set-url --push upstream no_push", shell=True)

if remove_test_files == "yes":
    # remove test folder
    subprocess.run("rm -r test", shell=True)

    # remove pytest_cache folder
    subprocess.run("rm -r .pytest_cache", shell=True)

    # remove .coveragerc file
    subprocess.run("rm .coveragerc", shell=True)
