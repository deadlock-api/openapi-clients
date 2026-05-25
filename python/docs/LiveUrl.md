# LiveUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**broadcast_url** | **str** |  | 
**lobby_id** | **int** |  | [optional] 
**match_id** | **int** |  | 
**started_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 

## Example

```python
from deadlock_api_client.models.live_url import LiveUrl

# TODO update the JSON string below
json = "{}"
# create an instance of LiveUrl from a JSON string
live_url_instance = LiveUrl.from_json(json)
# print the JSON string representation of the object
print(LiveUrl.to_json())

# convert the object into a dict
live_url_dict = live_url_instance.to_dict()
# create an instance of LiveUrl from a dict
live_url_from_dict = LiveUrl.from_dict(live_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


