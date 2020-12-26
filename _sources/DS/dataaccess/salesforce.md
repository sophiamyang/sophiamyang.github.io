# Query Salesforce Data in Python
*Using simple_salesforce Python API*

Salesforce is probably the most annoying database I have worked with. [This web page](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_erd_majors.htm) illustrates the relationships among the objects (i.e., data tables) stored in Salesforce. You might think it doesn’t look that bad. Well, in reality, the relationship of your tables can be a lot messier than this illustration. Let’s work through this and see how we can query salesforce data while remaining sane.


## Objects
Where can we find what tables and variables are available in Salesforce? To get an overview of all the tables (objects) and variables (entities). We can go to Salesforce `Developer Console — File — Open — Objects` to get a list of tables in Salesforce. And if we double click on one Object, we can see all the variable names. We can also query data directly in the Developer Console. But I prefer to use Python to do all the queries.

## Naming conventions
Two things to keep in mind before we start querying:
### Custom object
We can create various custom objects in Salesforce. They all end with __c. The variables will be named like `objectname__c` in the table.
### Parent-child relationship
Many objects in Salesforce have parent-child relationships. It is a one-to-many relationship. For example, one account can have many contacts. Thus `Account` is the parent object and `Contact` is the child object. We can query the parent table in the child query and query the child table in the parent query. But the name of the table can be different depending on if the object is a child or a parent in the query.

- Child-to-parent

For example, when we query the `Contact` table directly, we use `Contact` and we can query the name variable from the parent table `Account`.
```
SELECT Account.Name, Name, Email FROM Contact
```

- Parent-to-child

However, when `Contact` is a child object, we use the plural `Contacts` :
```
SELECT Name,(SELECT Name, Email FROM Contacts) FROM Account
```

I don’t know why Salesforce is designed this way. It is very confusing. If you need to find out the relationship between two objects, this [article](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_parent_child.htm) talks about how to identify parent and child relationships. There are also many other types of relationships that we will not cover in this article. Check out this [article](https://help.salesforce.com/articleView?id=overview_of_custom_object_relationships.htm&type=5) for details.

## simple-salesforce
Now we can start using simple-salesforce to query Salesforce data in Python. First, let’s install the `simple-salesforce` package in Python:
```
pip install simple-salesforce
```
Then we can import `Salesforce` and instantiate a Salesforce object.
```
from simple_salesforce import Salesforce
sf = Salesforce (
    username = "YOUR_USER_NAME",
    password = "YOUR_PASSWORD",
    security_token = "YOUR TOKEN",
    instance_url = "YOUR INSTANCE"
)
```
## Example Queries in Python
There are two ways to query data. The first way is the normal Salesforce API with `sf.query`, this method has a limit of 2000 records. The second way is the bulk API with `sf.bulk.OBJECT.query` . Note that with the bulk API you will need to define the object name in the method. Not sure why this is designed this way. Below are two examples using the normal API and the bulk API. I almost always use the bulk API.

In these two examples, we queried the `Opportunity` table, where `Account`, `RecordType`, and `CreatedBy` are the parent of `Opportunity`, and `Histories` and `ActivityHistories` are the children of `Opportunity`.

<script src="https://gist.github.com/sophiamyang/7749094c482bf7903eb41f107fe6f317.js"></script>

Results are pandas data frames with parents and children showing up as json fields. Then we can get information from the json field, here is an example:
```
import operator as op
df_oppo['accname'] = df_oppo['Account'].map(op.itemgetter('Name'))
```
Now you know how to query Salesforce data in Python. Once you understand the parent-child relationship and figure out the available tables and variables, you can query anything from anywhere.

References:  
https://simple-salesforce.readthedocs.io/en/latest/index.html  
https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_relationships_parent_child.htm  

By Sophia Yang on [November 19, 2020](https://medium.com/swlh/query-salesforce-data-in-python-e290a00e3cba)