# DraftBucket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**normal** | **float** |  | [optional] 
**good** | **float** |  | [optional] 

## Example

```python
from assets_deadlock_api_client.models.draft_bucket import DraftBucket

# TODO update the JSON string below
json = "{}"
# create an instance of DraftBucket from a JSON string
draft_bucket_instance = DraftBucket.from_json(json)
# print the JSON string representation of the object
print(DraftBucket.to_json())

# convert the object into a dict
draft_bucket_dict = draft_bucket_instance.to_dict()
# create an instance of DraftBucket from a dict
draft_bucket_from_dict = DraftBucket.from_dict(draft_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


