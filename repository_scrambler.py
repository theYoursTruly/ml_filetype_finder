from github import Github, GithubException

gh = Github()

with open('repositories', 'w') as f:
    repo_ids = []
    for i in range(1, 1000000, 1000):
        print('writing batch:', i)
        try:
            for repo in gh.get_repos(since=i):
                if repo.id not in repo_ids:
                    repo_ids.append(repo.id)
                    f.write('{{"id": "{0}", "name": "{1}", "owner": "{2}", "url": "{3}"}},\n'.format(repo.id, repo.name, repo.owner.name, repo.html_url))
        except GithubException:
            print('Exception - stop.')
            break
