# LaneMatchupStat

One requested stat, read at `sample_time_s` and averaged over the matchups that reached it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diff** | **float** | Mean of the duo&#39;s combined value minus the enemy duo&#39;s. Negative means behind. | 
**diff_std** | **float** | Population standard deviation of &#x60;diff&#x60; across the counted matchups. | 
**value** | **float** | Mean of the duo&#39;s combined value, summed over its two players. | 
**value_std** | **float** | Population standard deviation of &#x60;value&#x60; across the counted matchups. | 

## Example

```python
from deadlock_api_client.models.lane_matchup_stat import LaneMatchupStat

# TODO update the JSON string below
json = "{}"
# create an instance of LaneMatchupStat from a JSON string
lane_matchup_stat_instance = LaneMatchupStat.from_json(json)
# print the JSON string representation of the object
print(LaneMatchupStat.to_json())

# convert the object into a dict
lane_matchup_stat_dict = lane_matchup_stat_instance.to_dict()
# create an instance of LaneMatchupStat from a dict
lane_matchup_stat_from_dict = LaneMatchupStat.from_dict(lane_matchup_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


