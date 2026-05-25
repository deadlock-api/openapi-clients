# StartingStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_stat_name** | **str** |  | 
**value** | **float** |  | 

## Example

```python
from deadlock_api_client.models.starting_stat import StartingStat

# TODO update the JSON string below
json = "{}"
# create an instance of StartingStat from a JSON string
starting_stat_instance = StartingStat.from_json(json)
# print the JSON string representation of the object
print(StartingStat.to_json())

# convert the object into a dict
starting_stat_dict = starting_stat_instance.to_dict()
# create an instance of StartingStat from a dict
starting_stat_from_dict = StartingStat.from_dict(starting_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


