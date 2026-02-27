# ResponseGetRawItemsRawItemsGetInner


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
**dependent_abilities** | [**Dict[str, DependantAbilities]**](DependantAbilities.md) |  | [optional] 
**shop_image** | **str** |  | [optional] 
**shop_image_small** | **str** |  | [optional] 
**item_slot_type** | [**ItemSlotTypeV2**](ItemSlotTypeV2.md) |  | 
**item_tier** | [**ItemTierV2**](ItemTierV2.md) |  | 
**disabled** | **bool** |  | [optional] 
**activation** | [**RawAbilityActivationV2**](RawAbilityActivationV2.md) |  | [optional] 
**imbue** | [**RawAbilityImbueV2**](RawAbilityImbueV2.md) |  | [optional] 
**component_items** | **List[str]** |  | [optional] 
**tooltip_sections** | [**List[RawUpgradeTooltipSectionV2]**](RawUpgradeTooltipSectionV2.md) |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.response_get_raw_items_raw_items_get_inner import ResponseGetRawItemsRawItemsGetInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetRawItemsRawItemsGetInner from a JSON string
response_get_raw_items_raw_items_get_inner_instance = ResponseGetRawItemsRawItemsGetInner.from_json(json)
# print the JSON string representation of the object
print(ResponseGetRawItemsRawItemsGetInner.to_json())

# convert the object into a dict
response_get_raw_items_raw_items_get_inner_dict = response_get_raw_items_raw_items_get_inner_instance.to_dict()
# create an instance of ResponseGetRawItemsRawItemsGetInner from a dict
response_get_raw_items_raw_items_get_inner_from_dict = ResponseGetRawItemsRawItemsGetInner.from_dict(response_get_raw_items_raw_items_get_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


