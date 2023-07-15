from dataclasses import dataclass
from typing import List
from github import Github
from time import sleep


@dataclass
class OpenSource:
    """Data class holding data for an open source object"""

    # Respective id
    id: int

    # Name of repository
    name: str

    # Name of owner
    owner: str

    # Language(s) used
    languages: List[str]

    # Description
    description: str

    # Stars on project
    stars: float


@dataclass
class OpenSourceUtilizer:
    """Holds a list of Open Source objects"""

    open_source_list: List[OpenSource]
