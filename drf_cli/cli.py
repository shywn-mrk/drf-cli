import click
import subprocess

@click.group()
def cli():
    pass

@cli.command(help="Initialize a new Django Rest Framework project")
def init():
        repo_url = "https://github.com/shywn-mrk/drf-cli.git"
        command = f"git clone {repo_url}"
        subprocess.run(command.split(), shell=True)
        print('Project has been initialized successfuly!')
