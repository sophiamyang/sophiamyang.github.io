# Query Intercom data in Python — Intercom rest API

First, we need to get the authentication info from Intercom by creating a “New app”. Click “New app” in the Developer Hub page.

Then you should be able to see Client ID, Client secret, and access token in your app. Great, now we can use these info to access data in Python.

```
import requests
from requests.auth import HTTPBasicAuth
token = 'xxx'
ID = 'xxx'
```

## Overview
To get a overview of the Intercom data, run:
```
data = requests.get('https://api.intercom.io/counts', auth = HTTPBasicAuth(token, ID))
data.json()
```

This will show you how many users/companies/leads/tags/segments you have in your Intercom data.

## Query users
If you want to query users with a certain criteria, you might find the [search for contacts](https://developers.intercom.com/intercom-api-reference/reference#search-for-contacts) API to be useful. Instead of using a GET request, here we need to use a POST request. For example, if you are interested in how many signups in a given timeframe, you can do the following:

```
query = {
    "query": {
        "operator": "AND",
        "value": [
          {
            "field": "signed_up_at",
            "operator": ">",
            "value": datetime.datetime(2020,7,1).timestamp()
          }, 
          {
            "field": "signed_up_at",
            "operator": "<",
            "value": datetime.datetime(2020,8,1).timestamp()
          }
        ]
}}
r = requests.post("https://api.intercom.io/contacts/search", auth = HTTPBasicAuth(token, ID), json=query)
r.json()['total_count']
```

Note that Intercom uses UNIX Timestamp. Thus, we need to make sure we convert the date into the right format. `r.json()` shows the first page of the 50 records. `r.json()[‘pages’]` shows more about the page information, like how many pages there are for this data. `r.json()[‘total_count’]` count how many users in total returned from this query.

## Other options
There is a [Python API](https://github.com/intercom/python-intercom) for Intercom. But it’s not the official API and it seems like it’s not maintained well. You are welcome to try out the Python API and let me know what you think.
 
Here is all the code mentioned above. Hope you enjoy it! See you next time!

<script src="https://gist.github.com/sophiamyang/78bc58840e1347abf351b7b963c562b9.js"></script>

By Sophia Yang on [August 19, 2020](https://sophiamyang.medium.com/query-intercom-data-in-python-intercom-rest-api-912103599a80)