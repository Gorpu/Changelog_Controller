from datetime import datetime
from domain.tools.build_files import BuildFiles 
from domain.tools.git_commands import GitCommands

class Prompt():
    def __init__(self):
        pass
 
    @classmethod
    def parse_args(cls, args: list[str]) -> dict:
        parsed = {}

        for arg in args:
            if not arg.startswith("--") or ":" not in arg:
                raise ValueError(f"Argumento inválido: {arg}")

            key, value = arg[2:].split(":", 1)
            parsed[key] = value

        return parsed

    @classmethod
    def run_commit(
        cls,
        title_commit: str,
        message: str,
        feature_type: str
    ):
        gitcc = GitCommands()
        build_file = BuildFiles()
        date = datetime.now()
        
        user = gitcc.get_user_name() or "unknown"
        branch = gitcc.get_current_branch() or "unknown"
        date = date.strftime("%Y-%m-%d %H:%M:%S")

        build_file.readme_create()
        changelog_path = build_file.changelog_create(
            user=user,
            message=message,
            branch=branch,
            date=date,
            feature_type=feature_type
        )
        gitcc.commit(
            changelog_path=changelog_path,
            feature_type=feature_type,
            title_commit=title_commit,
        )
       
        return
