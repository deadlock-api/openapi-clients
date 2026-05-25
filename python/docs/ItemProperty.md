# ItemProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_set_token_override** | **bool** |  | [optional] 
**conditional** | **str** |  | [optional] 
**css_class** | **str** |  | [optional] 
**disable_value** | **str** |  | [optional] 
**display_units** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**loc_token_override** | **str** |  | [optional] 
**negative_attribute** | **bool** |  | [optional] 
**postfix** | **str** |  | [optional] 
**postvalue_label** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**provided_property_type** | **str** |  | [optional] 
**scale_function** | [**RawItemPropertyScaleFunctionSubclass**](RawItemPropertyScaleFunctionSubclass.md) |  | [optional] 
**street_brawl_value** | **str** |  | [optional] 
**usage_flags** | [**List[StatsUsageFlag]**](StatsUsageFlag.md) |  | [optional] 
**value** | **str** | Raw JSON value preserves the source distinction between numeric and stringly-typed bonuses (&#x60;\&quot;14.5\&quot;&#x60; vs &#x60;14.5&#x60;). | [optional] 

## Example

```python
from deadlock_api_client.models.item_property import ItemProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ItemProperty from a JSON string
item_property_instance = ItemProperty.from_json(json)
# print the JSON string representation of the object
print(ItemProperty.to_json())

# convert the object into a dict
item_property_dict = item_property_instance.to_dict()
# create an instance of ItemProperty from a dict
item_property_from_dict = ItemProperty.from_dict(item_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


