from dataclasses import dataclass
from typing import List
from github import Github
import random


# Holds the max amount of languages
MAX_LANGUAGE_LENGTH = 3

# Holds the max amount of github projects
MAX_GH_PROJECT_LENGTH = 15


@dataclass
class OpenSource:
    """Data class holding data for an open source object"""

    # Respective id
    id: int

    # Name of repository
    name: str

    # Description
    description: str

    # link to repository
    link: str

    # Name of owner
    owner: str

    # Language(s) used
    languages: List[str]

    # Stars on project
    stars: float


@dataclass
class OpenSourceUtilizer:
    """Holds a list of Open Source objects"""

    open_source_list: List[OpenSource]


def random_lang_list(lang: List[str]) -> List[str]:
    """Returns a list of 3 random languages"""

    # Holding the languages of the list
    lang_list_query = []

    while len(lang_list_query) <= MAX_LANGUAGE_LENGTH:
        # Choose a random language from the list
        chosen_language = random.choice(lang)

        if chosen_language not in lang_list_query:
            lang_list_query.append(chosen_language.lower())

    return lang_list_query


def request_user_lang_list(user_languages: List[str]) -> List[str]:
    """Retrieves 3 most used languages by the user"""

    # Holds default languages if the length of user languages is 0
    DEFAULT_LANGUAGES = [
        "rust",
        "python",
        "java",
        "javascript",
        "php",
        "html",
        "css",
        "c++",
        "c#",
    ]

    # If there are no top languages, fetch 3 from the default list
    if len(user_languages) == 0:
        return random_lang_list(DEFAULT_LANGUAGES)

    # Fetch 3 random languages from the user language list
    if len(user_languages) > MAX_LANGUAGE_LENGTH:
        return random_lang_list(user_languages)

    # Fetch the remainder languages if the value is less than the MAX_LANGUAGE_LENGTH
    if len(user_languages) < MAX_LANGUAGE_LENGTH:
        languages_required = abs(len(user_languages) - 3)

        for _ in range(languages_required):
            chosen_language = random.choice(DEFAULT_LANGUAGES)
            user_languages.append(chosen_language)
            DEFAULT_LANGUAGES.remove(chosen_language)

        return user_languages

    # Return the user language list if the length is equal to MAX_LANGUAGE_LENGTH
    return user_languages


def retrieve_top_repo_languages(repository) -> List[str]:
    """Retrieves up to three top languages from the current repository"""

    # Holds the top three languages from the repository
    lang_dict = {
        key: value
        for indx, (key, value) in enumerate(repository.get_languages().items())
        if indx <= 3
    }

    # Convert into a list
    top_languages = list(lang_dict.keys())

    return top_languages


def request_github_projects(user_languages: List[str]) -> OpenSourceUtilizer:
    """Requests Github Repository information"""

    # Create Open Source Utilizer instance
    open_source_utilizer = OpenSourceUtilizer([])

    # Create a github instance
    gh = Github()

    # Hold the user languages in a query variable
    query = user_languages

    # Index variable to traverse through the query list
    indx = 0

    # Continue adding more projects until the list is at max length
    while len(OpenSourceUtilizer.open_source_list) <= MAX_GH_PROJECT_LENGTH:
        # Create Open Source instance
        open_source_project = OpenSource()

        # Every language must have 5 projects each within the final list
        if len(open_source_utilizer) / 5 == len(open_source_utilizer) // 5:
            indx += 1

        repositories = gh.search_repositories(f"topic:{query[indx]}")

        for repository in repositories:
            open_source_project.id = repository.id
            open_source_project.name = repository.name
            open_source_project.description = repository.description
            open_source_project.link = repository.html_url
            open_source_project.owner = repository.owner.login
            open_source_project.languages = retrieve_top_repo_languages(repository)
            open_source_project.stars = repository.stargazers_count

        # Add current object to the finalized list
        open_source_utilizer.open_source_list.append(open_source_project)

    return open_source_utilizer
