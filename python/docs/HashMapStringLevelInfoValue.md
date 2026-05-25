# HashMapStringLevelInfoValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bonus_currencies** | **List[str]** |  | [optional] 
**required_gold** | **int** |  | 
**use_standard_upgrade** | **bool** |  | [optional] 

## Example

```python
from deadlock_api_client.models.hash_map_string_level_info_value import HashMapStringLevelInfoValue

# TODO update the JSON string below
json = "{}"
# create an instance of HashMapStringLevelInfoValue from a JSON string
hash_map_string_level_info_value_instance = HashMapStringLevelInfoValue.from_json(json)
# print the JSON string representation of the object
print(HashMapStringLevelInfoValue.to_json())

# convert the object into a dict
hash_map_string_level_info_value_dict = hash_map_string_level_info_value_instance.to_dict()
# create an instance of HashMapStringLevelInfoValue from a dict
hash_map_string_level_info_value_from_dict = HashMapStringLevelInfoValue.from_dict(hash_map_string_level_info_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


