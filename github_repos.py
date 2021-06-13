import requests
import argparse

def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    r = requests.get(url)
    return r.json()


def has_stars(repo):
    return [p for p in repo if p['stargazers_count'] > 0]


def get_star_url(p):
    return (p['stargazers_count'], p['html_url'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('username', help='Enter username')
    args = parser.parse_args()
    
    repos = get_repos(args.username)
    repos_has_stars = has_stars(repos)
    stars_urls = [get_star_url(p) for p in repos_has_stars]
    stars_urls.sort(reverse=True)
    fmt = '{} - {}'
    for i in stars_urls:
        print(fmt.format(*i))


if __name__ == '__main__':
    main()
