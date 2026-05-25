# ForumPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**PatchCategory**](PatchCategory.md) |  | 
**content** | **str** |  | 
**guid** | [**PatchGuid**](PatchGuid.md) |  | 
**link** | **str** |  | 
**pub_date** | **datetime** |  | 
**title** | **str** |  | 

## Example

```python
from deadlock_api_client.models.forum_patch import ForumPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ForumPatch from a JSON string
forum_patch_instance = ForumPatch.from_json(json)
# print the JSON string representation of the object
print(ForumPatch.to_json())

# convert the object into a dict
forum_patch_dict = forum_patch_instance.to_dict()
# create an instance of ForumPatch from a dict
forum_patch_from_dict = ForumPatch.from_dict(forum_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


