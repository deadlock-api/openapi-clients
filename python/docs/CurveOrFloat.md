# CurveOrFloat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **float** |  | [optional] 
**per_minute_after_start** | **float** |  | [optional] 

## Example

```python
from deadlock_api_client.models.curve_or_float import CurveOrFloat

# TODO update the JSON string below
json = "{}"
# create an instance of CurveOrFloat from a JSON string
curve_or_float_instance = CurveOrFloat.from_json(json)
# print the JSON string representation of the object
print(CurveOrFloat.to_json())

# convert the object into a dict
curve_or_float_dict = curve_or_float_instance.to_dict()
# create an instance of CurveOrFloat from a dict
curve_or_float_from_dict = CurveOrFloat.from_dict(curve_or_float_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


