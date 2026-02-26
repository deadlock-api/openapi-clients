# RawUpgradeV2


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
**type** | **str** |  | [optional] [default to 'upgrade']
**shop_image** | **str** |  | [optional] 
**shop_image_small** | **str** |  | [optional] 
**item_slot_type** | [**ItemSlotTypeV2**](ItemSlotTypeV2.md) |  | 
**item_tier** | [**ItemTierV2**](ItemTierV2.md) |  | 
**disabled** | **bool** |  | [optional] 
**activation** | [**RawAbilityActivationV2**](RawAbilityActivationV2.md) |  | [optional] 
**imbue** | [**RawAbilityImbueV2**](RawAbilityImbueV2.md) |  | [optional] 
**component_items** | **List[str]** |  | [optional] 
**tooltip_sections** | [**List[RawUpgradeTooltipSectionV2]**](RawUpgradeTooltipSectionV2.md) |  | [optional] 
**upgrades** | [**List[RawAbilityUpgradeV2]**](RawAbilityUpgradeV2.md) |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.raw_upgrade_v2 import RawUpgradeV2

# TODO update the JSON string below
json = "{}"
# create an instance of RawUpgradeV2 from a JSON string
raw_upgrade_v2_instance = RawUpgradeV2.from_json(json)
# print the JSON string representation of the object
print(RawUpgradeV2.to_json())

# convert the object into a dict
raw_upgrade_v2_dict = raw_upgrade_v2_instance.to_dict()
# create an instance of RawUpgradeV2 from a dict
raw_upgrade_v2_from_dict = RawUpgradeV2.from_dict(raw_upgrade_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


