# RollType

Known values for `m_eRollType`. Unknown values pass through as [`RollType::Other`] so a newly-introduced roll type doesn't 500.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**other** | **str** |  | 

## Example

```python
from deadlock_api_client.models.roll_type import RollType

# TODO update the JSON string below
json = "{}"
# create an instance of RollType from a JSON string
roll_type_instance = RollType.from_json(json)
# print the JSON string representation of the object
print(RollType.to_json())

# convert the object into a dict
roll_type_dict = roll_type_instance.to_dict()
# create an instance of RollType from a dict
roll_type_from_dict = RollType.from_dict(roll_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


