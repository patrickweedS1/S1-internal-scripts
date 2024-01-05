import requests

baseurl = 'https://usea1-support3.sentinelone.net'
apitoken = "Token "
accountID = ''
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
nextCursor = ''

headers = {
    "Content-type": "application/json",
    "user-agent": USER_AGENT,
    "Authorization": apitoken
    }

params = {
    "nextCursor": nextCursor,
    "accountIds": accountID,
    "limit": "300"
}

r = requests.get(baseurl + '/web/api/v2.1/agents', headers=headers, params=params).json()
print(r)