import subprocess


class CMDShell():
    def __init__(self):
        pass

    @staticmethod
    def execute(command:str) -> tuple[str, str, int]:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )   
        return result.stdout, result.stderr, result.returncode
    