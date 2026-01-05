import subprocess
from domain.tools.cmd_shell import CMDShell


class GitCommands():
    def __init__(self):
        pass

    def get_staged_files() -> list[str]:
        stdout, _, _ = CMDShell.execute("git diff --cached --name-only")
        return [line.strip() for line in stdout.splitlines() if line.strip()]

    @staticmethod
    def commit(changelog_path:str, feature_type:str, title_commit: str,):
        message = f'{feature_type.upper()}:({title_commit.upper()}): More details in Changelog Controller'
        message = message.replace('"', "'")

        CMDShell.execute("git init")
        CMDShell.execute(f'git add "{changelog_path}"')
        CMDShell.execute('git add README.md')
        CMDShell.execute(f'git commit -m "{message}"')

    @staticmethod
    def get_user_name() -> str:
        try:
            result = subprocess.run(
                ["git", "config", "user.name"],
                capture_output=True,
                text=True
            )
            return result.stdout.strip()
        except:
            return None
    
    @staticmethod
    def get_current_branch() -> str | None:
        try:
            result = subprocess.run(
                ["git", "branch", "--show-current"],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.SubprocessError:
            return None

        