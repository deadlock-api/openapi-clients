# AnalyticsHeroStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **int** |  | 
**hero_id** | **int** | See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**losses** | **int** |  | 
**matches** | **int** |  | 
**matches_per_bucket** | **int** |  | 
**permanent_buff_matches** | **int** | Matches that carry buff pickup counts. Equals &#x60;matches&#x60;, except on account-scoped queries (&#x60;account_ids&#x60; without item or ability filters): those read a per-account table that only has buff counts for matches ingested since build 6712 (late September 2026). | 
**permanent_buff_timing_matches** | **int** | Matches with pickup timings. Only matches since build 6712 (2026-09-29) record pickup times, and only players with at least one permanent pickup count here. | 
**total_assists** | **int** |  | 
**total_boss_damage** | **int** |  | 
**total_creep_damage** | **int** |  | 
**total_deaths** | **int** |  | 
**total_denies** | **int** |  | 
**total_first_permanent_buff_time_s** | **int** | Sum of the game time (seconds) of each player&#39;s first permanent buff pickup, over the &#x60;permanent_buff_timing_matches&#x60; matches. Average: &#x60;total_first_permanent_buff_time_s / permanent_buff_timing_matches&#x60;. | 
**total_kills** | **int** |  | 
**total_last_hits** | **int** |  | 
**total_max_health** | **int** |  | 
**total_net_worth** | **int** |  | 
**total_neutral_damage** | **int** |  | 
**total_permanent_buffs** | **int** | Sum of permanent buff (power-up) pickups over the &#x60;permanent_buff_matches&#x60; matches. Average per match: &#x60;total_permanent_buffs / permanent_buff_matches&#x60;. Buff types: &lt;https://api.deadlock-api.com/v1/assets/misc-entities&gt; | 
**total_player_damage** | **int** |  | 
**total_player_damage_taken** | **int** |  | 
**total_shots_hit** | **int** |  | 
**total_shots_missed** | **int** |  | 
**wins** | **int** |  | 

## Example

```python
from deadlock_api_client.models.analytics_hero_stats import AnalyticsHeroStats

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsHeroStats from a JSON string
analytics_hero_stats_instance = AnalyticsHeroStats.from_json(json)
# print the JSON string representation of the object
print(AnalyticsHeroStats.to_json())

# convert the object into a dict
analytics_hero_stats_dict = analytics_hero_stats_instance.to_dict()
# create an instance of AnalyticsHeroStats from a dict
analytics_hero_stats_from_dict = AnalyticsHeroStats.from_dict(analytics_hero_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


