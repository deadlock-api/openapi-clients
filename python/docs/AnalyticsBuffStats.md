# AnalyticsBuffStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_first_pickup_time_s** | **float** | Average game time (seconds) of a player&#39;s first pickup of this buff type, over player-matches with timings, &#x60;null&#x60; without any. | [optional] 
**avg_pickup_time_s** | **float** | Average game time (seconds) of the &#x60;timed_pickups&#x60;, &#x60;null&#x60; without any. | [optional] 
**buff_type** | **str** | Buff type, e.g. &#x60;hp_permanent_pickup_lv2&#x60;. Display names, units and colors: &lt;https://api.deadlock-api.com/v1/assets/misc-entities&gt; (&#x60;buff_type_name&#x60;). | 
**is_permanent** | **bool** | Whether the buff is permanent. Temporary power-ups never carry pickup timings. | 
**matches** | **int** | Player-matches matching the filters (the same for every buff type). Average pickups per match: &#x60;pickups / matches&#x60;. | 
**matches_with_pickup** | **int** | Player-matches with at least one pickup of this buff type. | 
**pickups** | **int** | Total pickups of this buff type. | 
**timed_matches** | **int** | Player-matches matching the filters that record pickup timings (the same for every buff type): matches since build 6712 (2026-09-29) with at least one timed permanent pickup. Average stat gained per match: &#x60;total_stat_value / timed_matches&#x60;. | 
**timed_pickups** | **int** | Pickups of this buff type with a recorded game time and stat value (build 6712+). | 
**total_stat_value** | **float** | Sum of the stat values granted by the &#x60;timed_pickups&#x60;, in the buff type&#39;s unit (&#x60;buff_type_value_unit&#x60; in the assets). | 

## Example

```python
from deadlock_api_client.models.analytics_buff_stats import AnalyticsBuffStats

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsBuffStats from a JSON string
analytics_buff_stats_instance = AnalyticsBuffStats.from_json(json)
# print the JSON string representation of the object
print(AnalyticsBuffStats.to_json())

# convert the object into a dict
analytics_buff_stats_dict = analytics_buff_stats_instance.to_dict()
# create an instance of AnalyticsBuffStats from a dict
analytics_buff_stats_from_dict = AnalyticsBuffStats.from_dict(analytics_buff_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


