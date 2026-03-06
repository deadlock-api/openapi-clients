# HeroEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hero_id** | **int** | See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | 
**matches** | **int** |  | 
**rank** | **int** |  | 
**value** | **float** |  | 

## Example

```python
from deadlock_api_client.models.hero_entry import HeroEntry

# TODO update the JSON string below
json = "{}"
# create an instance of HeroEntry from a JSON string
hero_entry_instance = HeroEntry.from_json(json)
# print the JSON string representation of the object
print(HeroEntry.to_json())

# convert the object into a dict
hero_entry_dict = hero_entry_instance.to_dict()
# create an instance of HeroEntry from a dict
hero_entry_from_dict = HeroEntry.from_dict(hero_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


