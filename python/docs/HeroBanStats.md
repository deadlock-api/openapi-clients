# HeroBanStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bans** | **int** | The number of matches in which this hero was banned. | 
**bucket** | **int** | The bucket value (depends on the bucket query parameter). | 
**hero_id** | **int** | The ID of the banned hero. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**matches** | **int** | The number of matches with ban data in this bucket. A hero&#39;s ban rate is &#x60;bans / matches&#x60;; a ranked match has 3 bans and an unranked match 2, so the bans of all heroes do not divide into matches by a fixed count. | 

## Example

```python
from deadlock_api_client.models.hero_ban_stats import HeroBanStats

# TODO update the JSON string below
json = "{}"
# create an instance of HeroBanStats from a JSON string
hero_ban_stats_instance = HeroBanStats.from_json(json)
# print the JSON string representation of the object
print(HeroBanStats.to_json())

# convert the object into a dict
hero_ban_stats_dict = hero_ban_stats_instance.to_dict()
# create an instance of HeroBanStats from a dict
hero_ban_stats_from_dict = HeroBanStats.from_dict(hero_ban_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


