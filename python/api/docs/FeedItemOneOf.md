# FeedItemOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**PatchCategory**](PatchCategory.md) |  | 
**content** | **str** |  | 
**guid** | [**PatchGuid**](PatchGuid.md) |  | 
**link** | **str** |  | 
**pub_date** | **datetime** |  | 
**title** | **str** |  | 
**source** | **str** |  | 

## Example

```python
from deadlock_api_client.models.feed_item_one_of import FeedItemOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of FeedItemOneOf from a JSON string
feed_item_one_of_instance = FeedItemOneOf.from_json(json)
# print the JSON string representation of the object
print(FeedItemOneOf.to_json())

# convert the object into a dict
feed_item_one_of_dict = feed_item_one_of_instance.to_dict()
# create an instance of FeedItemOneOf from a dict
feed_item_one_of_from_dict = FeedItemOneOf.from_dict(feed_item_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


