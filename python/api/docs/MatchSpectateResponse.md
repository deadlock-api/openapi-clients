# MatchSpectateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**broadcast_url** | **str** |  | 
**lobby_id** | **int** |  | [optional] 

## Example

```python
from deadlock-api-client.models.match_spectate_response import MatchSpectateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MatchSpectateResponse from a JSON string
match_spectate_response_instance = MatchSpectateResponse.from_json(json)
# print the JSON string representation of the object
print(MatchSpectateResponse.to_json())

# convert the object into a dict
match_spectate_response_dict = match_spectate_response_instance.to_dict()
# create an instance of MatchSpectateResponse from a dict
match_spectate_response_from_dict = MatchSpectateResponse.from_dict(match_spectate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


