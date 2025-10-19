# UpgradeV2Output


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
**properties** | [**Dict[str, UpgradePropertyV2Output]**](UpgradePropertyV2Output.md) |  | [optional] 
**weapon_info** | [**RawItemWeaponInfoV2Output**](RawItemWeaponInfoV2Output.md) |  | [optional] 
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
**tooltip_sections** | [**List[UpgradeTooltipSectionV2Output]**](UpgradeTooltipSectionV2Output.md) |  | [optional] 
**is_active_item** | **bool** |  | [readonly] 
**shopable** | **bool** |  | [readonly] 
**cost** | **int** |  | [readonly] 

## Example

```python
from assets-deadlock-api-client.models.upgrade_v2_output import UpgradeV2Output

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeV2Output from a JSON string
upgrade_v2_output_instance = UpgradeV2Output.from_json(json)
# print the JSON string representation of the object
print(UpgradeV2Output.to_json())

# convert the object into a dict
upgrade_v2_output_dict = upgrade_v2_output_instance.to_dict()
# create an instance of UpgradeV2Output from a dict
upgrade_v2_output_from_dict = UpgradeV2Output.from_dict(upgrade_v2_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


