# HeroSwapStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **int** | The bucket value (depends on the bucket query parameter). | 
**hero_id** | **int** | The ID of the hero. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**matches** | **int** | The number of players who played this hero, counting only players whose pre-game hero is known. | 
**pregame_picks** | **int** | The number of players who had this hero locked before the pre-game swap window. | 
**swapped_away** | **int** | The number of &#x60;pregame_picks&#x60; players who swapped away from this hero. | 
**swapped_in** | **int** | The number of players who played this hero after swapping to it from another pre-game hero. | 
**swapped_in_wins** | **int** | The number of &#x60;swapped_in&#x60; players who won the match. | 

## Example

```python
from deadlock_api_client.models.hero_swap_stats import HeroSwapStats

# TODO update the JSON string below
json = "{}"
# create an instance of HeroSwapStats from a JSON string
hero_swap_stats_instance = HeroSwapStats.from_json(json)
# print the JSON string representation of the object
print(HeroSwapStats.to_json())

# convert the object into a dict
hero_swap_stats_dict = hero_swap_stats_instance.to_dict()
# create an instance of HeroSwapStats from a dict
hero_swap_stats_from_dict = HeroSwapStats.from_dict(hero_swap_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


