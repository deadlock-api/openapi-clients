# ResponseGetItemV2ItemsIdOrClassNameGet


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
**type** | **str** |  | [optional] [default to 'ability']
**behaviours** | **List[str]** |  | [optional] 
**description** | [**UpgradeDescriptionV2**](UpgradeDescriptionV2.md) |  | 
**tooltip_details** | [**AbilityTooltipDetailsV2Output**](AbilityTooltipDetailsV2Output.md) |  | [optional] 
**upgrades** | [**List[RawAbilityUpgradeV2Output]**](RawAbilityUpgradeV2Output.md) |  | [optional] 
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
**tooltip_sections** | [**List[UpgradeTooltipSectionV2Output]**](UpgradeTooltipSectionV2Output.md) |  | [optional] 
**is_active_item** | **bool** |  | [readonly] 
**shopable** | **bool** |  | [readonly] 
**cost** | **int** |  | [readonly] 

## Example

```python
from assets-deadlock-api-client.models.response_get_item_v2_items_id_or_class_name_get import ResponseGetItemV2ItemsIdOrClassNameGet

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetItemV2ItemsIdOrClassNameGet from a JSON string
response_get_item_v2_items_id_or_class_name_get_instance = ResponseGetItemV2ItemsIdOrClassNameGet.from_json(json)
# print the JSON string representation of the object
print(ResponseGetItemV2ItemsIdOrClassNameGet.to_json())

# convert the object into a dict
response_get_item_v2_items_id_or_class_name_get_dict = response_get_item_v2_items_id_or_class_name_get_instance.to_dict()
# create an instance of ResponseGetItemV2ItemsIdOrClassNameGet from a dict
response_get_item_v2_items_id_or_class_name_get_from_dict = ResponseGetItemV2ItemsIdOrClassNameGet.from_dict(response_get_item_v2_items_id_or_class_name_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


