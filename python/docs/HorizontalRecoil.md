# HorizontalRecoil


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**burst_exponent** | **float** |  | [optional] 
**range** | [**RecoilRange**](RecoilRange.md) |  | [optional] 

## Example

```python
from deadlock_api_client.models.horizontal_recoil import HorizontalRecoil

# TODO update the JSON string below
json = "{}"
# create an instance of HorizontalRecoil from a JSON string
horizontal_recoil_instance = HorizontalRecoil.from_json(json)
# print the JSON string representation of the object
print(HorizontalRecoil.to_json())

# convert the object into a dict
horizontal_recoil_dict = horizontal_recoil_instance.to_dict()
# create an instance of HorizontalRecoil from a dict
horizontal_recoil_from_dict = HorizontalRecoil.from_dict(horizontal_recoil_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


