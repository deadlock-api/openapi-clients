# BuildHero


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_account_id** | **int** |  | 
**description** | **str** |  | [optional] 
**details** | [**BuildHeroDetails**](BuildHeroDetails.md) |  | 
**development_build** | **bool** |  | [optional] 
**hero_build_id** | **int** |  | 
**hero_id** | **int** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**language** | **int** |  | 
**last_updated_timestamp** | **int** |  | [optional] 
**name** | **str** |  | 
**origin_build_id** | **int** |  | 
**publish_timestamp** | **int** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**version** | **int** |  | 

## Example

```python
from deadlock-api-client.models.build_hero import BuildHero

# TODO update the JSON string below
json = "{}"
# create an instance of BuildHero from a JSON string
build_hero_instance = BuildHero.from_json(json)
# print the JSON string representation of the object
print(BuildHero.to_json())

# convert the object into a dict
build_hero_dict = build_hero_instance.to_dict()
# create an instance of BuildHero from a dict
build_hero_from_dict = BuildHero.from_dict(build_hero_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


