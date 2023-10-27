import click
from repo_generator.creator import create_challenge

@click.command()
@click.argument("username")
def cli(username):
    print("Creating challenge for user: {}".format(username))
    try:
        create_challenge(username)
    except Exception as e:
        print(e)
        print("Something went wrong, please try again")

if __name__ == "__main__":
    cli()