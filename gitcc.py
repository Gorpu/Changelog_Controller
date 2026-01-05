import sys
from domain.tools.prompt import Prompt

def main(args: list[str]):
    listen_agrs = Prompt()
    params = listen_agrs.parse_args(args=args)


    listen_agrs.run_commit(
        title_commit=params.get("title", ""),
        message=params.get("content", ""),
        feature_type=params.get("type", "feat")
    )
    
main(sys.argv[1:])

