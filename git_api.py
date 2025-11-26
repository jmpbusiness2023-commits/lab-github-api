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
    print("GitHub Profile Information:")
    print(f"Name: {profile.get('name')}")
    print(f"Bio: {profile.get('bio')}")
    print(f"Public Repos: {profile.get('public_repos')}")
    print(f"Followers: {profile.get('followers')}")
    print(f"Following: {profile.get('following')}")
    print(f"Location: {profile.get('location')}")
    print(f"Blog: {profile.get('blog')}")
    print()

def display_repositories(repos):
    print("Public Repositories:")
    for repo in repos:
        print(f"- {repo['name']}: {repo['html_url']} (⭐ {repo['stargazers_count']})")
    print()

def display_languages(languages):
    print("Most Used Programming Languages:")
    sorted_languages = sorted(languages.items(), key=lambda item: item[1], reverse=True)
    for lang, bytes in sorted_languages:
        print(f"- {lang}: {bytes} bytes")
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