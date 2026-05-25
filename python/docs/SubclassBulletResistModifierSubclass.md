# SubclassBulletResistModifierSubclass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bullet_resist** | **int** |  | [optional] 
**bullet_resist_reduction_per_hero** | **int** |  | [optional] 

## Example

```python
from deadlock_api_client.models.subclass_bullet_resist_modifier_subclass import SubclassBulletResistModifierSubclass

# TODO update the JSON string below
json = "{}"
# create an instance of SubclassBulletResistModifierSubclass from a JSON string
subclass_bullet_resist_modifier_subclass_instance = SubclassBulletResistModifierSubclass.from_json(json)
# print the JSON string representation of the object
print(SubclassBulletResistModifierSubclass.to_json())

# convert the object into a dict
subclass_bullet_resist_modifier_subclass_dict = subclass_bullet_resist_modifier_subclass_instance.to_dict()
# create an instance of SubclassBulletResistModifierSubclass from a dict
subclass_bullet_resist_modifier_subclass_from_dict = SubclassBulletResistModifierSubclass.from_dict(subclass_bullet_resist_modifier_subclass_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


