# ItemOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ability_type** | [**AbilityType**](AbilityType.md) |  | [optional] 
**behaviours** | **List[str]** |  | [optional] 
**boss_damage_scale** | **float** |  | [optional] 
**class_name** | **str** |  | 
**dependant_abilities** | **List[str]** |  | [optional] 
**dependent_abilities** | [**Dict[str, DependantAbilities]**](DependantAbilities.md) | Abilities this one depends on. Entries whose ability has no data are left out. | [optional] 
**description** | [**AbilityDescription**](AbilityDescription.md) |  | 
**grant_ammo_on_cast** | **bool** |  | [optional] 
**hero** | **int** |  | [optional] 
**heroes** | **List[int]** |  | [optional] 
**id** | **int** |  | 
**image** | **str** |  | [optional] 
**image_webp** | **str** |  | [optional] 
**name** | **str** |  | 
**properties** | [**Dict[str, ItemProperty]**](ItemProperty.md) |  | [optional] 
**start_trained** | **bool** |  | [optional] 
**tooltip_details** | [**AbilityTooltipDetails**](AbilityTooltipDetails.md) |  | [optional] 
**update_time** | **int** |  | [optional] 
**upgrades** | [**List[RawAbilityUpgrade]**](RawAbilityUpgrade.md) |  | [optional] 
**videos** | [**AbilityVideos**](AbilityVideos.md) |  | [optional] 
**weapon_info** | [**RawItemWeaponInfoInner**](RawItemWeaponInfoInner.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from deadlock_api_client.models.item_one_of import ItemOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ItemOneOf from a JSON string
item_one_of_instance = ItemOneOf.from_json(json)
# print the JSON string representation of the object
print(ItemOneOf.to_json())

# convert the object into a dict
item_one_of_dict = item_one_of_instance.to_dict()
# create an instance of ItemOneOf from a dict
item_one_of_from_dict = ItemOneOf.from_dict(item_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


