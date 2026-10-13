# Convar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **object** | Default value, typed by &#x60;type&#x60;: a bool, number or string, &#x60;[r, g, b, a]&#x60; for &#x60;color&#x60;, and an array of floats for vectors / &#x60;qangle&#x60;. | 
**description** | **str** | Help text shown by the in-game console. | [optional] 
**flags** | **int** | Raw &#x60;FCVAR_*&#x60; flag bits. | 
**type** | [**ConvarType**](ConvarType.md) |  | 

## Example

```python
from deadlock_api_client.models.convar import Convar

# TODO update the JSON string below
json = "{}"
# create an instance of Convar from a JSON string
convar_instance = Convar.from_json(json)
# print the JSON string representation of the object
print(Convar.to_json())

# convert the object into a dict
convar_dict = convar_instance.to_dict()
# create an instance of Convar from a dict
convar_from_dict = Convar.from_dict(convar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


