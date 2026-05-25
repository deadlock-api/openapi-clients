# PatchGuid


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_perma_link** | **bool** |  | 
**text** | **str** |  | 

## Example

```python
from deadlock_api_client.models.patch_guid import PatchGuid

# TODO update the JSON string below
json = "{}"
# create an instance of PatchGuid from a JSON string
patch_guid_instance = PatchGuid.from_json(json)
# print the JSON string representation of the object
print(PatchGuid.to_json())

# convert the object into a dict
patch_guid_dict = patch_guid_instance.to_dict()
# create an instance of PatchGuid from a dict
patch_guid_from_dict = PatchGuid.from_dict(patch_guid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


