import sys
import os
import shutil

BANNER = """ Available subcommands:

startproject -> create project
"""


def move_file(directory: str):
    if os.path.isdir(directory):
        files = os.listdir(directory)
        for file in files:
            move_file(os.path.join(directory, file))

    if not directory.endswith('-tpl'):
        return

    path = directory.split(os.sep)
    template_index = path.index("project_tempalte")
    path = path[template_index + 1:]

    new_path = os.getcwd()
    for directory_name in path[:-1]:
        new_path = os.path.join(new_path, directory_name)
        if not os.path.exists(new_path):
            print(f"creating {new_path}")
            os.mkdir(new_path)

    new_path = os.path.join(new_path, path[-1][:-4])
    shutil.copy(directory, new_path)
    print(f"creating {new_path}")


def execute_from_command_line():
    # First version of command execution
    available_commands = ["startproject"]
    args = sys.argv[1:]
    if len(args) == 0 or args[0] not in available_commands:
        return print(BANNER)

    if args[0] == "startproject":
        template_dir = os.path.join(
            os.path.dirname(__file__),
            "..",
            "conf",
            "project_tempalte"
        )
        move_file(template_dir)
