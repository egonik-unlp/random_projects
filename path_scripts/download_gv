#!/usr/bin/env python3


from dotenv import load_dotenv
import os
from github import Github
from git import Repo

load_dotenv()
ACCESS_TOKEN = os.getenv("TOKEN")

g = Github(ACCESS_TOKEN)
goodvibes_repos = g.get_organization("goodvibes-org").get_repos()

for repo in goodvibes_repos:
    try:
        repo_local = Repo.clone_from(url = repo.ssh_url, to_path = repo.full_name)
        print(f'Repo {repo.full_name} clonada con éxito')
    except Exception as e:
        print(e)
        
