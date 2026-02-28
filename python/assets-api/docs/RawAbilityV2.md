# RawAbilityV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **str** |  | 
**start_trained** | **bool** |  | [optional] 
**image** | **str** |  | [optional] 
**update_time** | **int** |  | [optional] 
**properties** | [**Dict[str, RawItemPropertyV2]**](RawItemPropertyV2.md) |  | [optional] 
**weapon_info** | [**RawItemWeaponInfoV2**](RawItemWeaponInfoV2.md) |  | [optional] 
**css_class** | **str** |  | [optional] 
**type** | **str** |  | [optional] [default to 'ability']
**grant_ammo_on_cast** | **bool** |  | [optional] 
**behaviour_bits** | **str** |  | [optional] 
**upgrades** | [**List[RawAbilityUpgradeV2]**](RawAbilityUpgradeV2.md) |  | 
**ability_type** | [**AbilityTypeV2**](AbilityTypeV2.md) |  | [optional] 
**boss_damage_scale** | **float** |  | [optional] 
**dependant_abilities** | **List[str]** |  | [optional] 
**video** | **str** |  | [optional] 
**tooltip_details** | [**RawAbilityV2TooltipDetails**](RawAbilityV2TooltipDetails.md) |  | [optional] 
**dependent_abilities** | [**Dict[str, AbilityV2DependentAbilitiesValue]**](AbilityV2DependentAbilitiesValue.md) |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.raw_ability_v2 import RawAbilityV2

# TODO update the JSON string below
json = "{}"
# create an instance of RawAbilityV2 from a JSON string
raw_ability_v2_instance = RawAbilityV2.from_json(json)
# print the JSON string representation of the object
print(RawAbilityV2.to_json())

# convert the object into a dict
raw_ability_v2_dict = raw_ability_v2_instance.to_dict()
# create an instance of RawAbilityV2 from a dict
raw_ability_v2_from_dict = RawAbilityV2.from_dict(raw_ability_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


