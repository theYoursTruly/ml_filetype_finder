import json
from subprocess import run, PIPE
from json import loads

since = 1
repo_ids = []

auth_data = 'theYoursTruly:<my_token>'
api_url = 'https://api.github.com/repositories?since='

with open('repositories', 'w', encoding="utf-8") as repos_file:
    while since < 1000000:
        print('Processing batch ' + str(since))
        data = run('curl -u ' + auth_data + ' ' + api_url + str(since), stdout=PIPE, shell=True).stdout
        json_data = loads(data)

        for repo in json_data:
            if repo['id'] is None:
                since = 1000000
                break
            if repo['id'] not in repo_ids:
                repo_ids.append(repo['id'])
                if repo['owner'] is not None:
                    out_format = '{{"id": "{0}", "name": "{1}", "owner": "{2}", "url": "{3}"}},\n'
                    repos_file.write(out_format.format(repo['id'], repo['name'], repo['owner']['login'], repo['html_url']))
        since = repo_ids[-1]
