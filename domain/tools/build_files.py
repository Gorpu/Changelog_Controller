import os
import shutil
from domain.tools.cmd_shell import CMDShell as cmd
from domain.tools.git_commands import GitCommands as git


class BuildFiles():
    CHANGELOG_DIR = "changelog controller"
    CHANGELOG_NAME = "Changelog.md"
    def __init__(self):
        pass

    @staticmethod
    def create_gitignore():
        GITIGNORE_PATH = ".gitignore"

        CONTENT_FILE = """# changelog-controller ignore
changelog-controller.exe"""

        # cria README.md se não existir
        if not os.path.exists(GITIGNORE_PATH):
            with open(GITIGNORE_PATH, "w", encoding="utf-8") as f:
                f.write("")

        # lê o conteúdo atual
        with open(GITIGNORE_PATH, "r", encoding="utf-8") as f:
            conteudo = f.read()

        # só adiciona se ainda não existir
        if CONTENT_FILE not in conteudo:
            with open(GITIGNORE_PATH, "a", encoding="utf-8") as f:
                f.write("\n" + CONTENT_FILE + "\n")
    
    @staticmethod
    def readme_create():
        README_PATH = "README.md"
        HISTORY_PATH = "changelog controller"

        BLOCO_CHANGELOG = f"""<!--CHANGELOG CONTROLLER-->
## Changelog Controller
"- [Ver Histórico](changelog%20controller)"
"""

        # cria a pasta do histórico
        os.makedirs(HISTORY_PATH, exist_ok=True)

        # cria README se não existir
        if not os.path.exists(README_PATH):
            with open(README_PATH, "w", encoding="utf-8") as f:
                f.write("# Projeto\n\n")

        # lê conteúdo atualizado
        with open(README_PATH, "r", encoding="utf-8") as f:
            conteudo = f.read()

        alterado = False

        # adiciona bloco do changelog se não existir
        if "<!--CHANGELOG CONTROLLER-->" not in conteudo:
            conteudo += "\n" + BLOCO_CHANGELOG + "\n"
            alterado = True

        if alterado:
            with open(README_PATH, "w", encoding="utf-8") as f:
                f.write(conteudo)
                cmd.execute(f'git add "{README_PATH}"')

    @classmethod
    def changelog_create(
        cls,
        user: str,
        message: str,
        branch: str,
        date: str,
        feature_type: str
    ):
        try:
            if os.path.exists(cls.CHANGELOG_DIR):
                shutil.rmtree(cls.CHANGELOG_DIR)
            os.makedirs(cls.CHANGELOG_DIR, exist_ok=True)

            files = git.get_staged_files()
            files_formatted = "\n".join(f"- {f}" for f in files) or "- Nenhum arquivo"

            content = f"""\
---

## 🔄 Changelog

👤 **User:** {user}  
🌿 **Branch:** {branch}  
📅 **Date:** {date}  
🏷️ **Type:** {feature_type}

---

### 📝 Details
- {message}

---

### 📂 Files
{files_formatted}

---
"""
            changelog_path = os.path.join(cls.CHANGELOG_DIR, cls.CHANGELOG_NAME)
            with open(changelog_path, "a", encoding="utf-8") as file:
                file.write(content)
            
            return changelog_path
        except:
            return None