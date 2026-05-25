# StatusServices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clickhouse** | **bool** | Whether Clickhouse is reachable. | 
**postgres** | **bool** | Whether Postgres is reachable. | 
**redis** | **bool** | Whether Redis is reachable. | 

## Example

```python
from deadlock_api_client.models.status_services import StatusServices

# TODO update the JSON string below
json = "{}"
# create an instance of StatusServices from a JSON string
status_services_instance = StatusServices.from_json(json)
# print the JSON string representation of the object
print(StatusServices.to_json())

# convert the object into a dict
status_services_dict = status_services_instance.to_dict()
# create an instance of StatusServices from a dict
status_services_from_dict = StatusServices.from_dict(status_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


