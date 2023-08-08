from github import Github, Auth
from typing import List


def fetch_user_languages(auth_token: str) -> List[str]:
    """Fetches users top languages"""

    auth = Auth.Token(auth_token)
    gh = Github(auth=auth)

    unique_languages = {}

    user = gh.get_user()

    for indx, repository in enumerate(user.get_repos(type="public")):
        if indx == 10:
            break

        if repository.owner.login == user.login:
            all_languages = repository.get_languages()
            all_languages = [key for key in all_languages.keys()]

            for lang in all_languages:
                if lang not in unique_languages:
                    unique_languages[lang] = 1
                else:
                    unique_languages[lang] += 1

    # Sort list again in descending order
    unique_languages_list = sorted(
        unique_languages.keys(), key=lambda x: unique_languages[x], reverse=True
    )

    return unique_languages_list
