# DraftBuckets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | [**DraftBucket**](DraftBucket.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.draft_buckets import DraftBuckets

# TODO update the JSON string below
json = "{}"
# create an instance of DraftBuckets from a JSON string
draft_buckets_instance = DraftBuckets.from_json(json)
# print the JSON string representation of the object
print(DraftBuckets.to_json())

# convert the object into a dict
draft_buckets_dict = draft_buckets_instance.to_dict()
# create an instance of DraftBuckets from a dict
draft_buckets_from_dict = DraftBuckets.from_dict(draft_buckets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


