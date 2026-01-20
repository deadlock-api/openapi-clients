# ResponseGetItemsV2ItemsGetInner


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
**properties** | [**Dict[str, UpgradePropertyV2]**](UpgradePropertyV2.md) |  | [optional] 
**weapon_info** | [**RawItemWeaponInfoV2**](RawItemWeaponInfoV2.md) |  | [optional] 
**type** | **str** |  | [optional] [default to 'ability']
**behaviours** | **List[str]** |  | [optional] 
**description** | [**UpgradeDescriptionV2**](UpgradeDescriptionV2.md) |  | 
**tooltip_details** | [**AbilityTooltipDetailsV2**](AbilityTooltipDetailsV2.md) |  | [optional] 
**upgrades** | [**List[RawAbilityUpgradeV2]**](RawAbilityUpgradeV2.md) |  | [optional] 
**ability_type** | [**AbilityTypeV2**](AbilityTypeV2.md) |  | [optional] 
**boss_damage_scale** | **float** |  | [optional] 
**dependant_abilities** | **List[str]** |  | [optional] 
**videos** | [**AbilityVideosV2**](AbilityVideosV2.md) |  | [optional] 
**shop_image** | **str** |  | [optional] 
**shop_image_webp** | **str** |  | [optional] 
**shop_image_small** | **str** |  | [optional] 
**shop_image_small_webp** | **str** |  | [optional] 
**item_slot_type** | [**ItemSlotTypeV2**](ItemSlotTypeV2.md) |  | 
**item_tier** | [**ItemTierV2**](ItemTierV2.md) |  | 
**disabled** | **bool** |  | [optional] 
**activation** | [**RawAbilityActivationV2**](RawAbilityActivationV2.md) |  | 
**imbue** | [**RawAbilityImbueV2**](RawAbilityImbueV2.md) |  | [optional] 
**component_items** | **List[str]** |  | [optional] 
**tooltip_sections** | [**List[UpgradeTooltipSectionV2]**](UpgradeTooltipSectionV2.md) |  | [optional] 
**is_active_item** | **bool** |  | [readonly] 
**shopable** | **bool** |  | [readonly] 
**cost** | **int** |  | [readonly] 

## Example

```python
from assets_deadlock_api_client.models.response_get_items_v2_items_get_inner import ResponseGetItemsV2ItemsGetInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetItemsV2ItemsGetInner from a JSON string
response_get_items_v2_items_get_inner_instance = ResponseGetItemsV2ItemsGetInner.from_json(json)
# print the JSON string representation of the object
print(ResponseGetItemsV2ItemsGetInner.to_json())

# convert the object into a dict
response_get_items_v2_items_get_inner_dict = response_get_items_v2_items_get_inner_instance.to_dict()
# create an instance of ResponseGetItemsV2ItemsGetInner from a dict
response_get_items_v2_items_get_inner_from_dict = ResponseGetItemsV2ItemsGetInner.from_dict(response_get_items_v2_items_get_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


