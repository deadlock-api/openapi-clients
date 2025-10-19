# AbilityV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**class_name** | **str** |  | 
**name** | **str** |  | 
**start_trained** | **bool** |  | [optional] 
**image** | **str** |  | [optional] 
**image_webp** | **str** |  | [optional] 
**hero** | **int** |  | [optional] 
**heroes** | **List[int]** |  | [optional] 
**update_time** | **int** |  | [optional] 
**properties** | [**Dict[str, ItemPropertyV2Input]**](ItemPropertyV2Input.md) |  | [optional] 
**weapon_info** | [**RawItemWeaponInfoV2Input**](RawItemWeaponInfoV2Input.md) |  | [optional] 
**type** | **str** |  | [optional] [default to 'ability']
**behaviours** | **List[str]** |  | [optional] 
**description** | [**AbilityDescriptionV2**](AbilityDescriptionV2.md) |  | 
**tooltip_details** | [**AbilityTooltipDetailsV2Input**](AbilityTooltipDetailsV2Input.md) |  | [optional] 
**upgrades** | [**List[RawAbilityUpgradeV2Input]**](RawAbilityUpgradeV2Input.md) |  | [optional] 
**ability_type** | [**AbilityTypeV2**](AbilityTypeV2.md) |  | [optional] 
**boss_damage_scale** | **float** |  | [optional] 
**dependant_abilities** | **List[str]** |  | [optional] 
**videos** | [**AbilityVideosV2**](AbilityVideosV2.md) |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.ability_v2_input import AbilityV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of AbilityV2Input from a JSON string
ability_v2_input_instance = AbilityV2Input.from_json(json)
# print the JSON string representation of the object
print(AbilityV2Input.to_json())

# convert the object into a dict
ability_v2_input_dict = ability_v2_input_instance.to_dict()
# create an instance of AbilityV2Input from a dict
ability_v2_input_from_dict = AbilityV2Input.from_dict(ability_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


