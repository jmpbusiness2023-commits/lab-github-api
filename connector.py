import requests

def get_github_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    return response.json()

def get_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    return response.json()

def get_github_languages(username):
    repos = get_github_repos(username)
    languages = {}
    for repo in repos:
        lang_url = repo['languages_url']
        lang_response = requests.get(lang_url)
        lang_data = lang_response.json()
        for lang, bytes in lang_data.items():
            languages[lang] = languages.get(lang, 0) + bytes
    return languages