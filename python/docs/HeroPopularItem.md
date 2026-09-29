# HeroPopularItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_name** | **str** |  | 
**item_id** | **int** | Item id, derived from &#x60;class_name&#x60; like &#x60;/v2/items&#x60; ids. | 
**pick_pct** | **float** | Pick rate in percent (0-100). | 
**winrate_pct** | **float** | Win rate in percent (0-100). | 

## Example

```python
from deadlock_api_client.models.hero_popular_item import HeroPopularItem

# TODO update the JSON string below
json = "{}"
# create an instance of HeroPopularItem from a JSON string
hero_popular_item_instance = HeroPopularItem.from_json(json)
# print the JSON string representation of the object
print(HeroPopularItem.to_json())

# convert the object into a dict
hero_popular_item_dict = hero_popular_item_instance.to_dict()
# create an instance of HeroPopularItem from a dict
hero_popular_item_from_dict = HeroPopularItem.from_dict(hero_popular_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


