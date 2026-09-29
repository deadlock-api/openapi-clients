# HeroPopularItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**early_game** | [**List[HeroPopularItem]**](HeroPopularItem.md) |  | 
**late_game** | [**List[HeroPopularItem]**](HeroPopularItem.md) |  | 
**mid_game** | [**List[HeroPopularItem]**](HeroPopularItem.md) |  | 
**timestamp** | **int** | Unix timestamp (seconds) at which Valve generated the data. | [optional] 

## Example

```python
from deadlock_api_client.models.hero_popular_items import HeroPopularItems

# TODO update the JSON string below
json = "{}"
# create an instance of HeroPopularItems from a JSON string
hero_popular_items_instance = HeroPopularItems.from_json(json)
# print the JSON string representation of the object
print(HeroPopularItems.to_json())

# convert the object into a dict
hero_popular_items_dict = hero_popular_items_instance.to_dict()
# create an instance of HeroPopularItems from a dict
hero_popular_items_from_dict = HeroPopularItems.from_dict(hero_popular_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


