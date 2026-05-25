# FeedItemOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**guid** | [**PatchGuid**](PatchGuid.md) |  | 
**link** | **str** |  | 
**pub_date** | **datetime** |  | 
**title** | **str** |  | 
**source** | **str** |  | 

## Example

```python
from deadlock_api_client.models.feed_item_one_of1 import FeedItemOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of FeedItemOneOf1 from a JSON string
feed_item_one_of1_instance = FeedItemOneOf1.from_json(json)
# print the JSON string representation of the object
print(FeedItemOneOf1.to_json())

# convert the object into a dict
feed_item_one_of1_dict = feed_item_one_of1_instance.to_dict()
# create an instance of FeedItemOneOf1 from a dict
feed_item_one_of1_from_dict = FeedItemOneOf1.from_dict(feed_item_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


