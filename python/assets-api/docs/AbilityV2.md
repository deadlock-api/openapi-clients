# AbilityV2


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
**properties** | [**Dict[str, ItemPropertyV2]**](ItemPropertyV2.md) |  | [optional] 
**weapon_info** | [**RawItemWeaponInfoV2**](RawItemWeaponInfoV2.md) |  | [optional] 
**type** | **str** |  | [optional] [default to 'ability']
**grant_ammo_on_cast** | **bool** |  | [optional] 
**behaviours** | **List[str]** |  | [optional] 
**description** | [**AbilityDescriptionV2**](AbilityDescriptionV2.md) |  | 
**tooltip_details** | [**AbilityTooltipDetailsV2**](AbilityTooltipDetailsV2.md) |  | [optional] 
**upgrades** | [**List[RawAbilityUpgradeV2]**](RawAbilityUpgradeV2.md) |  | [optional] 
**ability_type** | [**AbilityTypeV2**](AbilityTypeV2.md) |  | [optional] 
**boss_damage_scale** | **float** |  | [optional] 
**dependant_abilities** | **List[str]** |  | [optional] 
**videos** | [**AbilityVideosV2**](AbilityVideosV2.md) |  | [optional] 
**dependent_abilities** | [**Dict[str, DependantAbilities]**](DependantAbilities.md) |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.ability_v2 import AbilityV2

# TODO update the JSON string below
json = "{}"
# create an instance of AbilityV2 from a JSON string
ability_v2_instance = AbilityV2.from_json(json)
# print the JSON string representation of the object
print(AbilityV2.to_json())

# convert the object into a dict
ability_v2_dict = ability_v2_instance.to_dict()
# create an instance of AbilityV2 from a dict
ability_v2_from_dict = AbilityV2.from_dict(ability_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


