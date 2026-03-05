# PlayerEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**matches** | **int** |  | 
**rank** | **int** | tier &#x3D; first digits, subtier &#x3D; last digit, see more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
**value** | **float** |  | 

## Example

```python
from deadlock_api_client.models.player_entry import PlayerEntry

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerEntry from a JSON string
player_entry_instance = PlayerEntry.from_json(json)
# print the JSON string representation of the object
print(PlayerEntry.to_json())

# convert the object into a dict
player_entry_dict = player_entry_instance.to_dict()
# create an instance of PlayerEntry from a dict
player_entry_from_dict = PlayerEntry.from_dict(player_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


