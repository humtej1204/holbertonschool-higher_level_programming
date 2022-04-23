#!/usr/bin/python3
"""
GitHub credentials (username and password) and uses the GitHub API
to display your id
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get('https://api.github.com/user',
                     auth=(argv[1], argv[2]))
    if r.status_code == 200:
        j = r.json()
        print(j.get('id'))
    else:
        print('None')
