# CorruptedItemImages

Shop art for corrupted items (build 6711+). The game has no per-item corrupted icon: a corrupted item is its normal image drawn inside `frame`, with the tooltip backer of its `item_slot_type`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frame** | [**ImagePair**](ImagePair.md) |  | 
**frame_active** | [**ImagePair**](ImagePair.md) | Frame for an active (usable) corrupted item. | 
**tooltip_backers** | [**CorruptedTooltipBackers**](CorruptedTooltipBackers.md) |  | 

## Example

```python
from deadlock_api_client.models.corrupted_item_images import CorruptedItemImages

# TODO update the JSON string below
json = "{}"
# create an instance of CorruptedItemImages from a JSON string
corrupted_item_images_instance = CorruptedItemImages.from_json(json)
# print the JSON string representation of the object
print(CorruptedItemImages.to_json())

# convert the object into a dict
corrupted_item_images_dict = corrupted_item_images_instance.to_dict()
# create an instance of CorruptedItemImages from a dict
corrupted_item_images_from_dict = CorruptedItemImages.from_dict(corrupted_item_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


