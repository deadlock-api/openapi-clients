# BuildTagV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **str** |  | 
**label** | **str** |  | 
**id** | **int** |  | [readonly] 
**icon** | **str** |  | [readonly] 

## Example

```python
from assets_deadlock_api_client.models.build_tag_v2 import BuildTagV2

# TODO update the JSON string below
json = "{}"
# create an instance of BuildTagV2 from a JSON string
build_tag_v2_instance = BuildTagV2.from_json(json)
# print the JSON string representation of the object
print(BuildTagV2.to_json())

# convert the object into a dict
build_tag_v2_dict = build_tag_v2_instance.to_dict()
# create an instance of BuildTagV2 from a dict
build_tag_v2_from_dict = BuildTagV2.from_dict(build_tag_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


