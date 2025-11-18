# CreateCustomRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** | If a callback url is provided, we will send a POST request to this url when the match starts. | [optional] 
**cheats_enabled** | **bool** |  | [optional] 
**disable_auto_ready** | **bool** | If auto-ready is disabled, the bot will not automatically ready up. You need to call the &#x60;ready&#x60; endpoint to ready up. | [optional] 
**duplicate_heroes_enabled** | **bool** |  | [optional] 
**experimental_heroes_enabled** | **bool** |  | [optional] 
**is_publicly_visible** | **bool** |  | [optional] 
**min_roster_size** | **int** |  | [optional] 
**randomize_lanes** | **bool** |  | [optional] 
**region_mode** | [**RegionMode**](RegionMode.md) |  | [optional] 

## Example

```python
from deadlock_api_client.models.create_custom_request import CreateCustomRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomRequest from a JSON string
create_custom_request_instance = CreateCustomRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCustomRequest.to_json())

# convert the object into a dict
create_custom_request_dict = create_custom_request_instance.to_dict()
# create an instance of CreateCustomRequest from a dict
create_custom_request_from_dict = CreateCustomRequest.from_dict(create_custom_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


