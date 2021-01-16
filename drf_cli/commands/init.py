import click
import subprocess

@click.command()
def cli():
    """
    Initialize a new Django Rest Framework project
    """

    repo_url = "https://github.com/shywn-mrk/drf-cli.git"
    command = f"git clone {repo_url}"
    subprocess.run(command.split(), shell=True)
    print('Project has been initialized successfuly!')
