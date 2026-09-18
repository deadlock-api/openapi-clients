# HeroStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**accuracy** | **float** |  | 
**assists** | **int** |  | 
**assists_per_min** | **float** |  | 
**creeps_per_min** | **float** |  | 
**crit_shot_rate** | **float** |  | 
**damage_mitigated_per_min** | **float** |  | 
**damage_per_min** | **float** |  | 
**damage_per_soul** | **float** |  | 
**damage_taken_per_min** | **float** |  | 
**damage_taken_per_soul** | **float** |  | 
**deaths** | **int** |  | 
**deaths_per_min** | **float** |  | 
**denies_per_match** | **float** |  | 
**denies_per_min** | **float** |  | 
**ending_level** | **float** |  | 
**hero_id** | **int** | See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**kills** | **int** |  | 
**kills_per_min** | **float** |  | 
**last_hits_per_min** | **float** |  | 
**last_played** | **int** |  | 
**matches** | **List[int]** |  | 
**matches_played** | **int** |  | 
**mvp_rank_counts** | **List[int]** | Matches by the MVP rank Valve awarded the player: index 0 is rank 1 (MVP), index 1 is rank 2, index 2 is rank 3. Only the top three players of a match get a rank. | 
**mvp_rated_matches** | **int** | Matches played since Valve started reporting MVP ranks (2026-01-06). Divide &#x60;mvp_rank_counts&#x60; by this, not by &#x60;matches_played&#x60;, when the time range reaches further back. | 
**networth_per_min** | **float** |  | 
**obj_damage_per_min** | **float** |  | 
**obj_damage_per_soul** | **float** |  | 
**time_played** | **int** |  | 
**total_boss_damage** | **int** |  | 
**total_creep_damage** | **int** |  | 
**total_neutral_damage** | **int** |  | 
**total_player_damage** | **int** |  | 
**total_player_damage_taken** | **int** |  | 
**wins** | **int** |  | 

## Example

```python
from deadlock_api_client.models.hero_stats import HeroStats

# TODO update the JSON string below
json = "{}"
# create an instance of HeroStats from a JSON string
hero_stats_instance = HeroStats.from_json(json)
# print the JSON string representation of the object
print(HeroStats.to_json())

# convert the object into a dict
hero_stats_dict = hero_stats_instance.to_dict()
# create an instance of HeroStats from a dict
hero_stats_from_dict = HeroStats.from_dict(hero_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


