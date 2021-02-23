import click
import os
import subprocess
import platform

OPERATING_SYSTEM = platform.system()

def clone_repository(name):
    """
    Clones the reposity from git and removes the .git folder
    """

    repo_url = "https://github.com/shywn-mrk/drf-starter.git"

    command = f"git clone {repo_url} {name}"
    subprocess.run(command.split(), shell=True)

    if OPERATING_SYSTEM == "Windows":
        os.system(f"rmdir /s /q \"{name}/.git\"")
    else:
        os.system(f"rm -rf {name}/.git")

# def install_requirements(name):
#     """
#     Creates a virtual environment and installs the requirements
#     """

#     parent = os.getcwd()
#     full_path = os.path.join(parent, name)
#     os.chdir(full_path)
#     os.system("python -m venv env")

#     if OPERATING_SYSTEM == "Windows":
#         !!!!!!!!this does not work!!!!!!!!
#         script_path = f"{full_path}/env/Scripts/activate"
#         exec(open(script_path).read())
#     else:
#         print("Installing requirements is not implemented for Linux or MacOS. You have to install them manually")

#     os.system("pip install -r requirements.txt")


@click.command()
@click.argument("name")
def cli(name):
    """
    Initialize a new Django Rest Framework project
    """

    try:
        clone_repository(name)

        # install_requirements(name)

        print("Project has been initialized successfuly!")
    except:
        print("Something went wrong")
