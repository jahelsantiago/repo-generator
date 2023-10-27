## Run instructions

Run this command to sent an invitation to the candidate to participate in the test:

```bash
python -m repo_generator.cli <candidate_github_username>
```


## Configurations

Please visit the [Github Oauth Access token](https://docs.github.com/en/enterprise-server@3.6/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) for more information about how to create a personal OAuth access token.

Once you have created the token, please add it to the `access_token` parameter in the `settings.toml` file.