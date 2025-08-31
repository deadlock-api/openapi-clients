# PartyStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matches** | **List[int]** |  | 
**matches_played** | **int** |  | 
**party_size** | **int** |  | 
**wins** | **int** |  | 

## Example

```python
from openapi_client.models.party_stats import PartyStats

# TODO update the JSON string below
json = "{}"
# create an instance of PartyStats from a JSON string
party_stats_instance = PartyStats.from_json(json)
# print the JSON string representation of the object
print(PartyStats.to_json())

# convert the object into a dict
party_stats_dict = party_stats_instance.to_dict()
# create an instance of PartyStats from a dict
party_stats_from_dict = PartyStats.from_dict(party_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


