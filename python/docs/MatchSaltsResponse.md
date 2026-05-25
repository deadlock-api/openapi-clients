# MatchSaltsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** |  | [optional] 
**demo_url** | **str** |  | [optional] 
**match_id** | **int** |  | 
**metadata_salt** | **int** |  | [optional] 
**metadata_url** | **str** |  | [optional] 
**replay_salt** | **int** |  | [optional] 

## Example

```python
from deadlock_api_client.models.match_salts_response import MatchSaltsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MatchSaltsResponse from a JSON string
match_salts_response_instance = MatchSaltsResponse.from_json(json)
# print the JSON string representation of the object
print(MatchSaltsResponse.to_json())

# convert the object into a dict
match_salts_response_dict = match_salts_response_instance.to_dict()
# create an instance of MatchSaltsResponse from a dict
match_salts_response_from_dict = MatchSaltsResponse.from_dict(match_salts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


