# RankedSeason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_win_loss_point_grant** | **number** | Base rank points granted per win / taken per loss (build 6701+). | [optional] [default to undefined]
**calibration_matches** | **number** |  | [default to undefined]
**calibration_max_rank** | **number** | Highest rank badge (tier * 10 + subrank) placements put a player at (build 6857+). Valve\&#39;s notes for Beta Season 2 (101, Ascendant I) allow up to Ascendant III for strong previous-season performance. | [optional] [default to undefined]
**class_name** | **string** |  | [default to undefined]
**intervals** | [**Array&lt;SeasonInterval&gt;**](SeasonInterval.md) |  | [default to undefined]
**min_hero_unlock_points** | **number** | Points a hero needs to count towards &#x60;min_hero_unlocks&#x60;: 2 per win, 1 per loss (build 6857+). | [optional] [default to undefined]
**min_hero_unlocks** | **number** |  | [default to undefined]
**min_hero_wins** | **number** | Wins a hero needs to count towards &#x60;min_hero_unlocks&#x60;. Absent where the season counts hero points instead, see &#x60;min_hero_unlock_points&#x60;. | [optional] [default to undefined]
**min_wins** | **number** |  | [default to undefined]
**name** | **string** |  | [default to undefined]
**rank_info** | [**Array&lt;RankInfo&gt;**](RankInfo.md) | Rank progression settings (build 6857+). | [optional] [default to undefined]
**ranked_type** | **string** |  | [default to undefined]
**valid_party_sizes** | **Array&lt;number&gt;** |  | [default to undefined]

## Example

```typescript
import { RankedSeason } from 'deadlock_api_client';

const instance: RankedSeason = {
    base_win_loss_point_grant,
    calibration_matches,
    calibration_max_rank,
    class_name,
    intervals,
    min_hero_unlock_points,
    min_hero_unlocks,
    min_hero_wins,
    min_wins,
    name,
    rank_info,
    ranked_type,
    valid_party_sizes,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
