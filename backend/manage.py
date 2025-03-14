import subprocess
import argparse


parser = argparse.ArgumentParser(
    prog='Backend CLI',
    description='Manages backend and migrations'
)
parser.add_argument(
    'command', 
    choices=[
        "makemigrations",
        "migrate",
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
            subprocess.call(command)

        case "migrate":
            subprocess.call([
                "alembic", "upgrade", "head"
            ])
        
        case "run":
            from app.main import app
            from app.config import config
            import uvicorn

            uvicorn.run(
                app, host=config().INNER_HOST, port=5000
            )


if __name__ == "__main__":
    cli_args = parser.parse_args()
    main(cli_args)
