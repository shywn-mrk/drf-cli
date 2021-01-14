import sys
import subprocess

def main():
    args = sys.argv[1:]

    if "init" in args:
        repo_url = "https://github.com/shywn-mrk/drf-cli.git"
        command = f"git clone {repo_url}"
        subprocess.run(command.split(), shell=True)

if __name__ == "__main__":
    main()
