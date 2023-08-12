import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from posts import OpenSource, OpenSourceUtilizer, request_github_projects
from typing import List
import utils as ut
import json


def compute_cosine_similarity(right_swipes: List[object]) -> object:
    """Returns cosine similarity based on right-swipes"""

    # Holds desciption for each project
    description_holder = []

    in_session_right_swipes = eval(right_swipes)

    for project in in_session_right_swipes:
        description_holder.append(project["desc"])

    vectorizer = TfidfVectorizer()

    # Transform descriptions into numerical values
    matrix = vectorizer.fit_transform(description_holder)

    cosine_sim = cosine_similarity(matrix, matrix)

    return cosine_sim


def get_filtered_reccomendation(
    right_swipes: List[object], token: str
) -> List[OpenSource]:
    """Retrieves filtered recommendation list"""

    # Create Open Source Utilizer instance
    open_source_utilizer = OpenSourceUtilizer([])

    USER_LANGUAGES = ut.fetch_user_languages(token)

    # Retrieve new project list to be filtered out
    new_unfiltered_project_list: List[OpenSource] = request_github_projects(
        USER_LANGUAGES, token
    )

    cos_similarity = compute_cosine_similarity(right_swipes)

    for i, _ in enumerate(new_unfiltered_project_list):
        if i in cos_similarity:
            similarity_score = cos_similarity[i]
            # Holds tuples for similarity - E.g. [(0, 0.85), (1, 0.76), (2, 0.92)]
            similar_project_score = []

            for j, score in enumerate(similarity_score):
                if j != i:
                    similar_project_score.append((j, score))

            # Sort list to prioritize projects from most important to least based on score
            similar_project_score = sorted(
                similar_project_score, key=lambda x: x[1], reverse=True
            )
            open_source_utilizer.open_source_list.append(
                [new_unfiltered_project_list[idx] for idx, _ in similar_project_score]
            )

    return open_source_utilizer.open_source_list
