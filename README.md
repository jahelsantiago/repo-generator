# REPO GENERATOR

This projects aims to automate the process of creating a repository for a candidate to participate in a test.

The logic is simple:
1. Configure your credentials in the `settings.toml` file.
2. Give the candidate's github username as an argument. `python -m repo_generator.cli <candidate_github_username>`
3. The program will download the repository provided as a url in the settings.
4. It will restart the git history deleting all the commits and creating a new one.
5. It will create a new repository in your github account with the name of the candidate and the name of the repository provided in the settings.
6. It will add the candidate and the reviewers as a collaborators to the repository.

# Requirements

- Install python and PIP
- Intall poetry `pip install poetry`
- Install the dependencies `poetry install`


## Run instructions

Run this command to sent an invitation to the candidate to participate in the test:

```bash
python -m repo_generator.cli <candidate_github_username>
```


## Configurations

The file `settings.toml` contains the configuration for the program.

```toml
[github]
username = "your_github_username"
access_token = "your_github_access_token"

[challenge]
name = "Aider-macheight" #Name of the challenge
repository_url = "https://github.com/jahelsantiago/aider.git" #Link to the original repo for the challenge
reviewers = [] #The ones that will review the submissions, provide their github usernames
```