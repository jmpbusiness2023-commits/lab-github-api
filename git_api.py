from flask import Flask, jsonify, request
from connector import get_github_profile, get_github_repos, get_github_languages

app = Flask(__name__)

@app.route('/api/github/profile/<username>', methods=['GET'])

def api_get_github_profile(username):
    profile = get_github_profile(username)
    return jsonify(profile)

@app.route('/api/github/repos/<username>', methods=['GET'])
def api_get_github_repos(username):
    repos = get_github_repos(username)
    return jsonify(repos)

@app.route('/api/github/languages/<username>', methods=['GET'])
def api_get_github_languages(username):
    languages = get_github_languages(username)
    return jsonify(languages)

def display_profile_info(profile):
    print(f"GitHub Profile: {profile.get('login')}")
    print(f"Name: {profile.get('name')}")
    print(f"Username: {profile.get('login')}")
    print(f"Bio: {profile.get('bio')}")
    print(f"Public Repos: {profile.get('public_repos')}")
    print(f"Followers: {profile.get('followers')}")
    print(f"Following: {profile.get('following')}")
    print(f"Location: {profile.get('location')}")
    print(f"Profile URL: {profile.get('html_url')}")
    print()

def display_repositories(repos):
    print("Repositories ---------------------")
    for repo in repos:
        print(f"- {repo['name']}")
        print(f"View Repo (URL): {repo['html_url']}")
        print(f"Stars: {repo['stargazers_count']}, Forks: {repo['forks_count']}")
        print(f"Language: {repo['language']}")
        print(f"Last Updated: {repo['updated_at']}")
        print("\n") 
    print()

def display_languages(languages):
    print("Most Used Languages")
    sorted_languages = sorted(languages.items(), key=lambda item: item[1], reverse=True)
    for lang, bytes in sorted_languages:
        print(f"- {lang}: {bytes} bytes")
    print()

def display_popular_repositories(repos, min_stars=50):
    print(f"Most Starred Repos")
    popular_repos = [repo for repo in repos if repo['stargazers_count'] >= min_stars]
    for repo in popular_repos:
        print(f"{repo['name']} - {repo['stargazers_count']} stars")
    print()
    
def main():
    username = input("Enter GitHub username: ")
    profile = get_github_profile(username)
    if 'message' in profile and profile['message'] == 'Not Found':
        print("User not found.")
        return
    repos = get_github_repos(username)
    languages = get_github_languages(username)

    display_profile_info(profile)
    display_repositories(repos)
    display_languages(languages)


if __name__ == '__main__':
    app.run(debug=True)