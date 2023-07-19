# TODO - Pip install below
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from github.posts import OpenSource, OpenSourceUtilizer, request_github_projects
from typing import List

# from utils import [FUNCTION NAME]
USER_LANGUAGES = []

# Grab insession right swipes
IN_SESSION_RIGHT_SWIPES: OpenSource = []

# TODO - Update commenting


# TODO - Update function
def compute_cosine_similarity() -> object:
    """"""

    description_holder = []

    for project in IN_SESSION_RIGHT_SWIPES.description:
        description_holder.append(project.description)

    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(description_holder)

    cosine_sim = cosine_similarity(matrix, matrix)

    project_to_indices = dict()

    for indx, description in enumerate(description_holder):
        project_to_indices[indx] = description

    return {"indices": project_to_indices, "cosine_similarity": cosine_sim}


def get_filtered_reccomendation() -> List[OpenSource]:
    """"""

    new_potential_project_list = request_github_projects(USER_LANGUAGES)

    # TODO - Update variable name
    x = compute_cosine_similarity()
    indices = x["indices"]
    cos_similarity = x["cosine_similarity"]

    filtered_list = []

    for description in new_potential_project_list:
        if description in indices:
            indx = indices["description"]
            similarity_score = cos_similarity[indx]

            similar_projects = []
            for i, score in enumerate(similarity_score):
                if i != indx:
                    similar_projects.append((i, score))

            similar_projects = sorted(
                similar_projects, key=lambda x: x[1], reversed=True
            )

            filtered_list.append(
                [new_potential_project_list[i] for i in range(len(similar_projects))]
            )

    return filtered_list
