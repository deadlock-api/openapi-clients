# CrosshairCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Crosshair share code that can be imported in the game&#39;s crosshair settings. | 

## Example

```python
from deadlock_api_client.models.crosshair_code import CrosshairCode

# TODO update the JSON string below
json = "{}"
# create an instance of CrosshairCode from a JSON string
crosshair_code_instance = CrosshairCode.from_json(json)
# print the JSON string representation of the object
print(CrosshairCode.to_json())

# convert the object into a dict
crosshair_code_dict = crosshair_code_instance.to_dict()
# create an instance of CrosshairCode from a dict
crosshair_code_from_dict = CrosshairCode.from_dict(crosshair_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


