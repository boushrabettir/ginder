import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from posts import OpenSource, OpenSourceUtilizer, request_github_projects
from typing import List
import utils as ut


def compute_cosine_similarity() -> object:
    """Returns a dictionary with cosine similarity and a dictionary"""

    # Holds desciption for each project
    description_holder = []

    # Grab insession right swipes
    in_session_right_swipes: OpenSource = []

    for project in in_session_right_swipes:
        description_holder.append(project.description)

    vectorizer = TfidfVectorizer()

    # Transform descriptions into numerical values
    matrix = vectorizer.fit_transform(description_holder)

    cosine_sim = cosine_similarity(matrix, matrix)

    # Holds key/pair value where key is a number, value is the description
    project_to_indices = dict()

    for indx, description in enumerate(description_holder):
        project_to_indices[indx] = description

    return {"indices": project_to_indices, "cosine_similarity": cosine_sim}


def get_filtered_reccomendation() -> List[OpenSource]:
    """Retrieves filtered recommendation list"""

    USER_LANGUAGES = ut.fetch_top_three_languages()

    # Retrieve new project list to be filtered out
    new_unfiltered_project_list: OpenSourceUtilizer = request_github_projects(
        USER_LANGUAGES
    )

    data = compute_cosine_similarity()

    # Holds object and numpy array in seperate variables
    indices = data["indices"]
    cos_similarity = data["cosine_similarity"]

    # Holds the filtered reccomendation list
    filtered_list_reccomendation: List[OpenSource] = []

    for project in new_unfiltered_project_list.open_source_list:
        if project.description in indices:
            indx = indices["description"]
            similarity_score = cos_similarity[indx]

            # Holds tuples for similarity - E.g. [(0, 0.85), (1, 0.76), (2, 0.92)]
            similar_project_score = []

            for i, score in enumerate(similarity_score):
                if i != indx:
                    similar_project_score.append((i, score))

            # Sort list to priotize list from most important to least based on score
            similar_project_score = sorted(
                similar_project_score, key=lambda x: x[1], reversed=True
            )

            filtered_list_reccomendation.append(
                [
                    new_unfiltered_project_list[i]
                    for i in range(len(similar_project_score))
                ]
            )

    # Add filtered list in our utilizer
    OpenSourceUtilizer.open_source_list.extend(filtered_list_reccomendation)

    return OpenSourceUtilizer.open_source_list
