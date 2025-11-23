# RangedArmorModifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range_min** | **float** |  | [optional] 
**range_max** | **float** |  | [optional] 
**invuln_range** | **float** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.ranged_armor_modifier import RangedArmorModifier

# TODO update the JSON string below
json = "{}"
# create an instance of RangedArmorModifier from a JSON string
ranged_armor_modifier_instance = RangedArmorModifier.from_json(json)
# print the JSON string representation of the object
print(RangedArmorModifier.to_json())

# convert the object into a dict
ranged_armor_modifier_dict = ranged_armor_modifier_instance.to_dict()
# create an instance of RangedArmorModifier from a dict
ranged_armor_modifier_from_dict = RangedArmorModifier.from_dict(ranged_armor_modifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


