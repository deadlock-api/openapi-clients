# HashMapValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg** | **float** |  | 
**percentile1** | **float** |  | 
**percentile10** | **float** |  | 
**percentile25** | **float** |  | 
**percentile5** | **float** |  | 
**percentile50** | **float** |  | 
**percentile75** | **float** |  | 
**percentile90** | **float** |  | 
**percentile95** | **float** |  | 
**percentile99** | **float** |  | 
**std** | **float** |  | 

## Example

```python
from openapi_client.models.hash_map_value import HashMapValue

# TODO update the JSON string below
json = "{}"
# create an instance of HashMapValue from a JSON string
hash_map_value_instance = HashMapValue.from_json(json)
# print the JSON string representation of the object
print(HashMapValue.to_json())

# convert the object into a dict
hash_map_value_dict = hash_map_value_instance.to_dict()
# create an instance of HashMapValue from a dict
hash_map_value_from_dict = HashMapValue.from_dict(hash_map_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


