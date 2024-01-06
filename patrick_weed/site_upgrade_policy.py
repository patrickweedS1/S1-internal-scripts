import requests

baseurl = 'https://usea1-css-s101.sentinelone.net'
apitoken = "Token "
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

headers = {
    "Content-type": "application/json",
    "user-agent": USER_AGENT,
    "Authorization": apitoken
    }

params = {
    "limit": "1000"
}

r = requests.get(baseurl + '/web/api/v2.1/sites', headers=headers, params=params).json()
all_sites = r['data']['sites']

site_ids = []
for each in all_sites:
    site_ids.append(each['id'])

def site_policy(site_id):
    params = {
        "limit": "10",
        "osType": "windows",
        "scopeLevel": "site",
        "skip": "0",
        "sortBy": "priority",
        "sortOrder": "desc",
        "scopeId": site_id
    }
    upgrade_policy = requests.get(baseurl + '/web/api/v2.1/upgrade-policy/policies', headers=headers, params=params).json()
    return upgrade_policy

for id in site_ids:
    policy = site_policy(id)
    print(policy)