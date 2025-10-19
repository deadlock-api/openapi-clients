# UpgradeV2Input


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
**properties** | [**Dict[str, UpgradePropertyV2Input]**](UpgradePropertyV2Input.md) |  | [optional] 
**weapon_info** | [**RawItemWeaponInfoV2Input**](RawItemWeaponInfoV2Input.md) |  | [optional] 
**type** | **str** |  | [optional] [default to 'upgrade']
**shop_image** | **str** |  | [optional] 
**shop_image_webp** | **str** |  | [optional] 
**shop_image_small** | **str** |  | [optional] 
**shop_image_small_webp** | **str** |  | [optional] 
**item_slot_type** | [**ItemSlotTypeV2**](ItemSlotTypeV2.md) |  | 
**item_tier** | [**ItemTierV2**](ItemTierV2.md) |  | 
**disabled** | **bool** |  | [optional] 
**description** | [**UpgradeDescriptionV2**](UpgradeDescriptionV2.md) |  | [optional] 
**activation** | [**RawAbilityActivationV2**](RawAbilityActivationV2.md) |  | 
**imbue** | [**RawAbilityImbueV2**](RawAbilityImbueV2.md) |  | [optional] 
**component_items** | **List[str]** |  | [optional] 
**tooltip_sections** | [**List[UpgradeTooltipSectionV2Input]**](UpgradeTooltipSectionV2Input.md) |  | [optional] 

## Example

```python
from assets-deadlock-api-client.models.upgrade_v2_input import UpgradeV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeV2Input from a JSON string
upgrade_v2_input_instance = UpgradeV2Input.from_json(json)
# print the JSON string representation of the object
print(UpgradeV2Input.to_json())

# convert the object into a dict
upgrade_v2_input_dict = upgrade_v2_input_instance.to_dict()
# create an instance of UpgradeV2Input from a dict
upgrade_v2_input_from_dict = UpgradeV2Input.from_dict(upgrade_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


