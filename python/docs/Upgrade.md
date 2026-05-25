# Upgrade


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation** | [**AbilityActivation**](AbilityActivation.md) |  | 
**class_name** | **str** |  | 
**component_items** | **List[str]** |  | [optional] 
**cost** | **int** |  | [optional] 
**description** | [**UpgradeDescription**](UpgradeDescription.md) |  | [optional] 
**disabled** | **bool** |  | [optional] 
**hero** | **int** |  | [optional] 
**heroes** | **List[int]** |  | [optional] 
**id** | **int** |  | 
**image** | **str** |  | [optional] 
**image_webp** | **str** |  | [optional] 
**imbue** | [**AbilityImbue**](AbilityImbue.md) |  | [optional] 
**is_active_item** | **bool** |  | 
**item_slot_type** | [**ItemSlotType**](ItemSlotType.md) |  | 
**item_tier** | **int** |  | 
**name** | **str** |  | 
**properties** | [**Dict[str, UpgradeProperty]**](UpgradeProperty.md) |  | [optional] 
**shop_image** | **str** |  | [optional] 
**shop_image_small** | **str** |  | [optional] 
**shop_image_small_webp** | **str** |  | [optional] 
**shop_image_webp** | **str** |  | [optional] 
**shopable** | **bool** |  | 
**start_trained** | **bool** |  | [optional] 
**tooltip_sections** | [**List[UpgradeTooltipSection]**](UpgradeTooltipSection.md) |  | [optional] 
**type** | [**ItemType**](ItemType.md) |  | 
**update_time** | **int** |  | [optional] 
**upgrades** | [**List[RawAbilityUpgrade]**](RawAbilityUpgrade.md) |  | [optional] 
**weapon_info** | [**RawItemWeaponInfoInner**](RawItemWeaponInfoInner.md) |  | [optional] 

## Example

```python
from deadlock_api_client.models.upgrade import Upgrade

# TODO update the JSON string below
json = "{}"
# create an instance of Upgrade from a JSON string
upgrade_instance = Upgrade.from_json(json)
# print the JSON string representation of the object
print(Upgrade.to_json())

# convert the object into a dict
upgrade_dict = upgrade_instance.to_dict()
# create an instance of Upgrade from a dict
upgrade_from_dict = Upgrade.from_dict(upgrade_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


