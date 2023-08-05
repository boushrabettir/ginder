from github import Github
from github import Auth
from typing import List
from itertools import islice


def fetch_user_languages(auth_token: str) -> List[str]:
    """Fetches users top languages"""

    auth = Auth.Token(auth_token)
    gh = Github(auth=auth)

    unique_languages = {}

    user = gh.get_user()

    # https://www.geeksforgeeks.org/python-itertools-islice/#

    for repository in islice(user.get_repos(), 3):
        if repository.owner.login == user.login:
            all_languages = repository.get_languages()
            all_languages = sorted(
                all_languages.keys(), key=lambda x: x[1], reverse=True
            )

            for lang in all_languages:
                if lang not in unique_languages:
                    unique_languages[lang] = 1
                else:
                    unique_languages[lang] += 1

    # Sort list again in descending order
    unique_languages_list = sorted(
        unique_languages.keys(), key=lambda x: x[1], reverse=True
    )

    return ["python", "rust", "css"]
