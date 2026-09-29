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
**corrupted_info** | [**CorruptedItemInfo**](CorruptedItemInfo.md) | Present on upgrades the Broker can corrupt (build 6711+). | [optional] 
**cost** | **int** |  | [optional] 
**disable_item_target** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**disabled_shop_filters** | **List[str]** | Shop filters (&#x60;snake_case&#x60; &#x60;EShopFilter*&#x60; names) this item is hidden from even though its stats would match them. | [optional] 
**imbue** | [**AbilityImbue**](AbilityImbue.md) |  | [optional] 
**is_active_item** | **bool** |  | 
**item_slot_type** | [**ItemSlotType**](ItemSlotType.md) |  | 
**item_tier** | **int** |  | 
**shop_filters** | **List[str]** | Extra shop filters (&#x60;snake_case&#x60; &#x60;EShopFilter*&#x60; names, e.g. &#x60;status_grounded&#x60;) this item shows up under, beyond those derived from its stats. | [optional] 
**shop_image** | **str** |  | [optional] 
**shop_image_small** | **str** |  | [optional] 
**shop_image_small_webp** | **str** |  | [optional] 
**shop_image_webp** | **str** |  | [optional] 
**shop_version** | **int** |  | [optional] 
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


