# A function that returns a list of top languages used by the GitHub user
from github import Github
from github import Auth
from typing import List

# This is the access token that is used to access the user's information
auth = Auth.Token('token') # this an example access token
g = Github(auth=auth)

def fetch_token() -> List[str]:
  # Store the languages in a dictionary
  unique_languages = {} 

  # Store the top languages in a list
  top_languages_list = []

  # Loop through the user's repositories
  for repo in g.get_user().get_repos():
    # Ensure that the repository is owned by the user
    if repo.owner.login == g.get_user().login:
      # Loop through the languages used in the repository
      for lang in repo.get_languages():
        # Check if the language is not in the dictionary of languages
        if lang not in unique_languages:
          # Add the language to the dictionary
          unique_languages[lang] = 1
        else:
          # Increment the language count by 1
          unique_languages[lang] += 1 
       
  # Sort the languages in descending order depending on the number of times they are used
  sorting_languages = sorted(unique_languages.items(), key = lambda x:x[1], reverse = True) 
  # Get the top 3 languages used by the user
  top_3_languages = sorting_languages[:3] 
  # Loop through the top languages to get the language name
  for key, value in top_3_languages: 
      # Add the language name to the list of top languages
      top_languages_list.append(key) 
  # Return the list of top 3 languages used by the user
  return top_languages_list 

print(fetch_token()) # this is for testing purposes to make sure the function works
