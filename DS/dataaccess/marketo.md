# Getting Marketo data in Python — Marketo rest API and Python API

There are two ways I have used to get Marketo data in Python. First is to use Marketo rest API directly. Second is to use the marketo Python API `marketorestpython`. I really like the `marketorestpython` library and I highly recommend everyone to use this library. But in this article, I am going to talk about both approach.

## Marketo rest API
First, we need to get `client_id`, `client_secret`, `munchkin_id`/instance URL information. Client Id and Client Secret can be set up via LaunchPoint and they can be found under Admin > LaunchPoint > View Details . And Munchkin Account ID can be found under Admin > Integration > Munchkin menu. munchkin_id is also part of the instance URL, which can be found under Admin > Integration > Web Services > REST API > Identity.

```
munchkin_id = ""
client_id = ""
client_secret= "" 
args = {'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret}
host = f'https://{munchkin_id}.mktorest.com'
```

Second, we need to get `access token` and `next page token`. Since we have all the credentials ready. We can use the Python requests library and do an HTTP GET `request` to get tokens.

```
import requests
data = requests.get(host+'/identity/oauth/token', 
                 params ={'grant_type': 'client_credentials',
                  'client_id': client_id,
                  'client_secret': client_secret},
                 headers= {'Accept-Encoding': 'gzip'}).json()
token = data['access_token']
data_nextPageToken = requests.get(host+'/rest/v1/activities/pagingtoken.json',
            params = {'access_token':token,
                      'sinceDatetime':'2019-11-01'
                     }
            ).json()
nextPageToken = data_nextPageToken['nextPageToken']
```


Next, we can use the access token to get the activities and leads data from Marketo.
```
act1 = requests.get(host+'/rest/v1/activities.json', 
             params ={'access_token': token,
                      'nextPageToken': nextPageToken,
                      'activityTypeIds':['1']
                     }).json()
leads1 = requests.get(host+'/rest/v1/leads.json', 
             params ={'access_token': token,
                      'filterType':'email',
                      'filterValues':['a@b.com','c@d.com']                
                     }).json()
```

You can see results in a pandas dataframe:
```
import pandas as pd
pd.DataFrame(act1['result'])
pd.DataFrame(leads1['result'])
```

Besides the activity and the leads data, activity type data is also worth looking at if you are wondering which activity type corresponds to which number.
```
requests.get(host+'/rest/v1/activities/types.json', 
             params ={'access_token': token                
                     }).json()['result']
```
                     
## Marketo Python API
[marketorestpython](https://github.com/jepcastelein/marketo-rest-python) library is very easy to use. To install marketorestpython, run `pip install marketorestpython`.

First we need to import the library, get `client_id`, `client_secret`, `munchkin_id` and input all the credentials in the MarketoClient function. Then we are ready to go.
```
from marketorestpython.client import MarketoClient
munchkin_id = "" 
client_id = "" 
client_secret= "" 
api_limit=None
max_retry_time=None
mc = MarketoClient(munchkin_id, client_id, client_secret, api_limit, max_retry_time)
```
To get the activity types, run:
```
mc.execute(method='get_activity_types')
```
Get activity data:
```
act = mc.execute(
    method='get_lead_activities', 
    activityTypeIds=['1'],
    sinceDatetime='2019-10-01', 
    untilDatetime='2019-10-02')
pd.DataFrame(act)
```
Get leads data:
```
lead = mc.execute(
    method='get_multiple_leads_by_filter_type', 
    filterType='email', 
    filterValues=['a@b.com','c@d.com'], 
    fields=['firstName', 'middleName', 'lastName'], 
    batchSize=None)
```
## Marketo Python API — Bulk Extract
The simple Marketo API has really low data limit, sometimes we need to export a large amount of data from Marketo. Then we need to use bulk extract.

There are several steps/methods we need to do for bulk extract: we need to create a job, enqueue a job, check job status to make sure it is completed, and then we can get the data. The only thing we need to define is the start date and the end date for the created date in the filters. If you want the whole database, you can simply make a scheduler and download data every day/month.

To bulk extract activities:
```
#create a job
new_export_job_details = mc.execute(method='create_activities_export_job', filters={'createdAt': {'endAt': '2019-10-03', 'startAt': '2019-10-01'}})
#enqueue a job
enqueued_job_details = mc.execute(method='enqueue_activities_export_job', job_id=new_export_job_details[0]['exportId'])
#check job status
export_job_status = mc.execute(method='get_activities_export_job_status', job_id=new_export_job_details[0]['exportId'])
#get data
export_file_contents = mc.execute(method='get_activities_export_job_file', job_id=new_export_job_details[0]['exportId'])
#convert data to pandas dataframe 
import pandas as pd
import io
f = io.BytesIO(export_file_contents)
df = pd.read_csv(f)
```
To bulk extract leads, in addition to the date range, you also need to define the list of fields you want to query:
```
#create a job
#list of fields: https://developers.marketo.com/rest-api/lead-database/fields/list-of-standard-fields/
new_export_job_details = mc.execute(method='create_leads_export_job', 
                                    fields=['firstName', 
                                            'lastName',
                                            'id',
                                            'email',
                                            'city',
                                            'country',
                                            'website',
                                            'company',
                                            'Department',
                                            'InferredCompany',
                                            'InferredCity',
                                            'InferredCountry',
                                            'Industry',
                                            'AnnualRevenue',
                                            'leadScore',
                                            'LeadRole',
                                            'LeadSource',
                                            'leadStatus',
                                            'Site',
                                            'State',
                                            'Title',
                                            'Unsubscribed',
                                            'UnsubscribedReason',
                                            'SFDCType',
                                            'createdAt',
                                            'updatedAt',
                                   
                                    ] 
                                    ,filters={'createdAt': {'endAt': '2019-10-01', 'startAt': '2019-10-02'}})
#enqueue a job
enqueued_job_details = mc.execute(method='enqueue_leads_export_job', job_id=new_export_job_details[0]['exportId'])
#check job status
export_job_status = mc.execute(method='get_leads_export_job_status', job_id=new_export_job_details[0]['exportId'])
# get data
export_file_contents = mc.execute(method='get_leads_export_job_file', job_id=new_export_job_details[0]['exportId'])
#convert data to pandas dataframe
import pandas as pd
import io
f = io.BytesIO(export_file_contents)
df=pd.read_csv(f)
```

Hope this article is helpful. In the next article, I am going to talk about how to set up an airflow dag to download Marketo data on a regular basis. Enjoy!

By Sophia Yang on [December 17, 2019](https://sophiamyang.medium.com/getting-marketo-data-in-python-marketo-rest-api-and-python-api-2568b777ea5b)