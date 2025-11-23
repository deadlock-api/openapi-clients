# BulletResistModifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bullet_resist** | **int** |  | [optional] 
**bullet_resist_reduction_per_hero** | **int** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.bullet_resist_modifier import BulletResistModifier

# TODO update the JSON string below
json = "{}"
# create an instance of BulletResistModifier from a JSON string
bullet_resist_modifier_instance = BulletResistModifier.from_json(json)
# print the JSON string representation of the object
print(BulletResistModifier.to_json())

# convert the object into a dict
bullet_resist_modifier_dict = bullet_resist_modifier_instance.to_dict()
# create an instance of BulletResistModifier from a dict
bullet_resist_modifier_from_dict = BulletResistModifier.from_dict(bullet_resist_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


