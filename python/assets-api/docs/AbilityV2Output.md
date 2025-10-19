# AbilityV2Output


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
**properties** | [**Dict[str, ItemPropertyV2Output]**](ItemPropertyV2Output.md) |  | [optional] 
**weapon_info** | [**RawItemWeaponInfoV2Output**](RawItemWeaponInfoV2Output.md) |  | [optional] 
**type** | **str** |  | [optional] [default to 'ability']
**behaviours** | **List[str]** |  | [optional] 
**description** | [**AbilityDescriptionV2**](AbilityDescriptionV2.md) |  | 
**tooltip_details** | [**AbilityTooltipDetailsV2Output**](AbilityTooltipDetailsV2Output.md) |  | [optional] 
**upgrades** | [**List[RawAbilityUpgradeV2Output]**](RawAbilityUpgradeV2Output.md) |  | [optional] 
**ability_type** | [**AbilityTypeV2**](AbilityTypeV2.md) |  | [optional] 
**boss_damage_scale** | **float** |  | [optional] 
**dependant_abilities** | **List[str]** |  | [optional] 
**videos** | [**AbilityVideosV2**](AbilityVideosV2.md) |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.ability_v2_output import AbilityV2Output

# TODO update the JSON string below
json = "{}"
# create an instance of AbilityV2Output from a JSON string
ability_v2_output_instance = AbilityV2Output.from_json(json)
# print the JSON string representation of the object
print(AbilityV2Output.to_json())

# convert the object into a dict
ability_v2_output_dict = ability_v2_output_instance.to_dict()
# create an instance of AbilityV2Output from a dict
ability_v2_output_from_dict = AbilityV2Output.from_dict(ability_v2_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


