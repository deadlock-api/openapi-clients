# VerticalRecoil


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**burst_constant** | **float** |  | [optional] 
**burst_exponent** | **float** |  | [optional] 
**burst_slope** | **float** |  | [optional] 
**range** | [**RecoilRange**](RecoilRange.md) |  | [optional] 

## Example

```python
from deadlock_api_client.models.vertical_recoil import VerticalRecoil

# TODO update the JSON string below
json = "{}"
# create an instance of VerticalRecoil from a JSON string
vertical_recoil_instance = VerticalRecoil.from_json(json)
# print the JSON string representation of the object
print(VerticalRecoil.to_json())

# convert the object into a dict
vertical_recoil_dict = vertical_recoil_instance.to_dict()
# create an instance of VerticalRecoil from a dict
vertical_recoil_from_dict = VerticalRecoil.from_dict(vertical_recoil_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


