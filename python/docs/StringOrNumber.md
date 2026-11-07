# StringOrNumber

A value the game files hold either as a string (`\"14.5\"`, `\"-1m\"`) or as a number.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from deadlock_api_client.models.string_or_number import StringOrNumber

# TODO update the JSON string below
json = "{}"
# create an instance of StringOrNumber from a JSON string
string_or_number_instance = StringOrNumber.from_json(json)
# print the JSON string representation of the object
print(StringOrNumber.to_json())

# convert the object into a dict
string_or_number_dict = string_or_number_instance.to_dict()
# create an instance of StringOrNumber from a dict
string_or_number_from_dict = StringOrNumber.from_dict(string_or_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


