import click
import os
import subprocess

@click.command()
@click.argument('project_name')
def cli(project_name):
    """
    Initialize a new Django Rest Framework project
    """

    try:
        repo_url = "https://github.com/shywn-mrk/drf-starter.git"
        command = f"git clone {repo_url}"
        subprocess.run(command.split(), shell=True)

        os.rename('drf-starter', project_name)

        print('Project has been initialized successfuly!')
    except:
        print('Something went wrong')
