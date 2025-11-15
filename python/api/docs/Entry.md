# Entry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hero_id** | **int** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**matches** | **int** |  | 
**rank** | **int** | tier &#x3D; first digits, subtier &#x3D; last digit, see more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
**value** | **float** |  | 

## Example

```python
from deadlock-api-client.models.entry import Entry

# TODO update the JSON string below
json = "{}"
# create an instance of Entry from a JSON string
entry_instance = Entry.from_json(json)
# print the JSON string representation of the object
print(Entry.to_json())

# convert the object into a dict
entry_dict = entry_instance.to_dict()
# create an instance of Entry from a dict
entry_from_dict = Entry.from_dict(entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


