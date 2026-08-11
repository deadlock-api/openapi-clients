# LaneMatchupStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_lane** | **int** | The lane the matchup was played in, or &#x60;0&#x60; when &#x60;assigned_lane&#x60; was grouped away. See the &#x60;lane_info&#x60; array of &lt;https://api.deadlock-api.com/v1/assets/generic-data&gt;. |
**enemy_hero_ids** | **int[]** | The ascending hero id pair they laned against, or empty when grouped away. |
**hero_ids** | **int[]** | The ascending hero id pair that shared the lane, or empty when grouped away. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; |
**matches_played** | **int** | The total number of lane matchups between &#x60;hero_ids&#x60; and &#x60;enemy_hero_ids&#x60; in this lane. |
**net_worth_diff** | **float** | Mean souls the duo is ahead by at &#x60;sample_time_s&#x60;, against that duo. Negative means behind. &#x60;0&#x60; when no counted matchup lasted that long. |
**sample_matches** | **int** | How many of &#x60;matches_played&#x60; lasted to &#x60;sample_time_s&#x60; with all four players still in. Every reading on this row rests on those matchups only. |
**sample_time_s** | **int** | Seconds into the match the stat readings were taken at. Echoes the &#x60;sample_time_s&#x60; parameter. |
**stats** | [**array<string,\OpenAPI\Client\Model\LaneMatchupStat>**](LaneMatchupStat.md) | A reading per stat named in &#x60;stats&#x60;. Empty unless the parameter was set. |
**wins** | **int** | The number of matches &#x60;hero_ids&#x60; won against &#x60;enemy_hero_ids&#x60; in this lane. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
