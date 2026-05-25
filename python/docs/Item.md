# Item


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ability_type** | [**AbilityType**](AbilityType.md) |  | [optional] 
**behaviours** | **List[str]** |  | [optional] 
**boss_damage_scale** | **float** |  | [optional] 
**class_name** | **str** |  | 
**dependant_abilities** | **List[str]** |  | [optional] 
**dependent_abilities** | [**Dict[str, DependantAbilities]**](DependantAbilities.md) |  | [optional] 
**description** | [**UpgradeDescription**](UpgradeDescription.md) |  | 
**grant_ammo_on_cast** | **bool** |  | [optional] 
**hero** | **int** |  | [optional] 
**heroes** | **List[int]** |  | [optional] 
**id** | **int** |  | 
**image** | **str** |  | [optional] 
**image_webp** | **str** |  | [optional] 
**name** | **str** |  | 
**properties** | [**Dict[str, UpgradeProperty]**](UpgradeProperty.md) |  | [optional] 
**start_trained** | **bool** |  | [optional] 
**tooltip_details** | [**AbilityTooltipDetails**](AbilityTooltipDetails.md) |  | [optional] 
**type** | [**ItemType**](ItemType.md) |  | 
**update_time** | **int** |  | [optional] 
**upgrades** | [**List[RawAbilityUpgrade]**](RawAbilityUpgrade.md) |  | [optional] 
**videos** | [**AbilityVideos**](AbilityVideos.md) |  | [optional] 
**weapon_info** | [**RawItemWeaponInfoInner**](RawItemWeaponInfoInner.md) |  | [optional] 
**crosshair_css_class** | **str** |  | [optional] 
**custom_crosshair_settings** | [**RawCustomCrosshairSettings**](RawCustomCrosshairSettings.md) |  | [optional] 
**use_custom_crosshair_settings** | **bool** |  | [optional] 
**activation** | [**AbilityActivation**](AbilityActivation.md) |  | 
**component_items** | **List[str]** |  | [optional] 
**cost** | **int** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**imbue** | [**AbilityImbue**](AbilityImbue.md) |  | [optional] 
**is_active_item** | **bool** |  | 
**item_slot_type** | [**ItemSlotType**](ItemSlotType.md) |  | 
**item_tier** | **int** |  | 
**shop_image** | **str** |  | [optional] 
**shop_image_small** | **str** |  | [optional] 
**shop_image_small_webp** | **str** |  | [optional] 
**shop_image_webp** | **str** |  | [optional] 
**shopable** | **bool** |  | 
**tooltip_sections** | [**List[UpgradeTooltipSection]**](UpgradeTooltipSection.md) |  | [optional] 

## Example

```python
from deadlock_api_client.models.item import Item

# TODO update the JSON string below
json = "{}"
# create an instance of Item from a JSON string
item_instance = Item.from_json(json)
# print the JSON string representation of the object
print(Item.to_json())

# convert the object into a dict
item_dict = item_instance.to_dict()
# create an instance of Item from a dict
item_from_dict = Item.from_dict(item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


