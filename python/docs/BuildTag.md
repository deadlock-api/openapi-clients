# BuildTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **str** |  | 
**icon** | **str** |  | 
**id** | **int** |  | 
**label** | **str** |  | 

## Example

```python
from deadlock_api_client.models.build_tag import BuildTag

# TODO update the JSON string below
json = "{}"
# create an instance of BuildTag from a JSON string
build_tag_instance = BuildTag.from_json(json)
# print the JSON string representation of the object
print(BuildTag.to_json())

# convert the object into a dict
build_tag_dict = build_tag_instance.to_dict()
# create an instance of BuildTag from a dict
build_tag_from_dict = BuildTag.from_dict(build_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


