# PlayerRegionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**history** | [**List[PlayerClusterMonth]**](PlayerClusterMonth.md) | Matches per month and server cluster, newest month first. | 
**region** | **str** | The region the player played most matches in during their latest month with a known region. &#x60;null&#x60; if none of their matches has a known region. | [optional] 
**region_month** | **int** | Unix timestamp of the month &#x60;region&#x60; was taken from. | [optional] 

## Example

```python
from deadlock_api_client.models.player_region_response import PlayerRegionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerRegionResponse from a JSON string
player_region_response_instance = PlayerRegionResponse.from_json(json)
# print the JSON string representation of the object
print(PlayerRegionResponse.to_json())

# convert the object into a dict
player_region_response_dict = player_region_response_instance.to_dict()
# create an instance of PlayerRegionResponse from a dict
player_region_response_from_dict = PlayerRegionResponse.from_dict(player_region_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


