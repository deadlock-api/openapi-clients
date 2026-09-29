# NeutralCamp

A neutral camp (\"Haunt\") marker (build 6711+).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon** | **str** | Minimap icon URL. | 
**kind** | [**NeutralCampKind**](NeutralCampKind.md) |  | 
**left_relative** | **float** | Position on the minimap, as fractions of its width/height. | 
**name** | **str** | Camp entity name from the map (e.g. &#x60;theater_lobby_camp&#x60;). | 
**position** | **List[float]** | World position &#x60;[x, y, z]&#x60;, same space as the zip-line splines. | 
**top_relative** | **float** |  | 

## Example

```python
from deadlock_api_client.models.neutral_camp import NeutralCamp

# TODO update the JSON string below
json = "{}"
# create an instance of NeutralCamp from a JSON string
neutral_camp_instance = NeutralCamp.from_json(json)
# print the JSON string representation of the object
print(NeutralCamp.to_json())

# convert the object into a dict
neutral_camp_dict = neutral_camp_instance.to_dict()
# create an instance of NeutralCamp from a dict
neutral_camp_from_dict = NeutralCamp.from_dict(neutral_camp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


