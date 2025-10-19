# BuildTagV2Output


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **str** |  | 
**label** | **str** |  | 
**id** | **int** |  | [readonly] 
**icon** | **str** |  | [readonly] 

## Example

```python
from assets-deadlock-api-client.models.build_tag_v2_output import BuildTagV2Output

# TODO update the JSON string below
json = "{}"
# create an instance of BuildTagV2Output from a JSON string
build_tag_v2_output_instance = BuildTagV2Output.from_json(json)
# print the JSON string representation of the object
print(BuildTagV2Output.to_json())

# convert the object into a dict
build_tag_v2_output_dict = build_tag_v2_output_instance.to_dict()
# create an instance of BuildTagV2Output from a dict
build_tag_v2_output_from_dict = BuildTagV2Output.from_dict(build_tag_v2_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


