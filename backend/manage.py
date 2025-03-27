import subprocess
import argparse
from getpass import getpass

import os
os.environ[
    "PATH_TO_BACKEND_DOTENV_FILE"
] = "E:\\PycharmProjects\\_new\\crm-fastapi\\.env.dev"



parser = argparse.ArgumentParser(
    prog='Backend CLI',
    description='Manages backend and migrations'
)
parser.add_argument(
    'command', 
    choices=[
        "makemigrations",
        "migrate",
        "dev",
        "run",
    ]
)
parser.add_argument(
    '-m', "--message",
    default=None,
    help="makemigrations: migration message"
)


def main(args):
    match args.command:
        case "makemigrations":
            command = ["alembic", "revision", "--autogenerate"]
            if args.message is not None:
                command += ["-m", args.message]
            exit( subprocess.call(command) )

        case "migrate":
            command = ["alembic", "upgrade", "head"]
            exit( subprocess.call(command) )

        case "run":
            from app.main import main
            from app.config import config
            import uvicorn

            uvicorn.run(
                main(), host=config().INNER_HOST, port=8080
            )

        case "superuser":
            name = input("Name: ")
            email = input("Email: ")
            password = getpass()
            

if __name__ == "__main__":
    cli_args = parser.parse_args()
    main(cli_args)
