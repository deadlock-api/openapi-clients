# RankedSeason

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_win_loss_point_grant** | **int** | Base rank points granted per win / taken per loss (build 6701+). | [optional]
**calibration_matches** | **int** |  |
**calibration_max_rank** | **int** | Highest rank badge (tier * 10 + subrank) placements put a player at (build 6857+). Valve&#39;s notes for Beta Season 2 (101, Ascendant I) allow up to Ascendant III for strong previous-season performance. | [optional]
**class_name** | **string** |  |
**intervals** | [**\OpenAPI\Client\Model\SeasonInterval[]**](SeasonInterval.md) |  |
**min_hero_unlock_points** | **int** | Points a hero needs to count towards &#x60;min_hero_unlocks&#x60;: 2 per win, 1 per loss (build 6857+). | [optional]
**min_hero_unlocks** | **int** |  |
**min_hero_wins** | **int** | Wins a hero needs to count towards &#x60;min_hero_unlocks&#x60;. Absent where the season counts hero points instead, see &#x60;min_hero_unlock_points&#x60;. | [optional]
**min_wins** | **int** |  |
**name** | **string** |  |
**rank_info** | [**\OpenAPI\Client\Model\RankInfo[]**](RankInfo.md) | Rank progression settings (build 6857+). | [optional]
**ranked_type** | **string** |  |
**valid_party_sizes** | **int[]** |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
