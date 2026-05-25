# AbilityVideos


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mp4** | **str** |  | [optional] 
**webm** | **str** |  | [optional] 

## Example

```python
from deadlock_api_client.models.ability_videos import AbilityVideos

# TODO update the JSON string below
json = "{}"
# create an instance of AbilityVideos from a JSON string
ability_videos_instance = AbilityVideos.from_json(json)
# print the JSON string representation of the object
print(AbilityVideos.to_json())

# convert the object into a dict
ability_videos_dict = ability_videos_instance.to_dict()
# create an instance of AbilityVideos from a dict
ability_videos_from_dict = AbilityVideos.from_dict(ability_videos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


