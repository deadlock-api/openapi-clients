# DeadlockApiClient.Model.LaneSoulCurve
**⚠️ Subject to change:** newly added, fields may change or be removed without notice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AssignedLane** | **int** | The lane the matchup was played in, or &#x60;0&#x60; when &#x60;assigned_lane&#x60; was grouped away. See the &#x60;lane_info&#x60; array of &lt;https://api.deadlock-api.com/v1/assets/generic-data&gt;. | 
**EnemyHeroIds** | **List&lt;int&gt;** | The ascending hero id pair they laned against, or empty when grouped away. | 
**HeroIds** | **List&lt;int&gt;** | The ascending hero id pair that shared the lane, or empty when grouped away. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**MatchesPlayed** | **long** | Lane matchups behind the row, counted at its *first* sample. This is what &#x60;min_matches&#x60; and &#x60;max_matches&#x60; filter on, so it does not move when the requested time range changes; read &#x60;sample_matches&#x60; for what any individual point rests on. | 
**NetWorthDiff** | **List&lt;double&gt;** | Mean souls the duo is ahead by at the matching entry of &#x60;sample_times_s&#x60;. Negative means behind. Same length as &#x60;sample_times_s&#x60;. | 
**NetWorthDiffStd** | **List&lt;double&gt;** | Population standard deviation of the lead across the counted matchups, at the matching entry of &#x60;sample_times_s&#x60;. Same length as &#x60;sample_times_s&#x60;.  Spread between individual games, not uncertainty about the mean: it stays wide however many matchups are counted, because lane outcomes genuinely differ that much. | 
**SampleMatches** | **List&lt;long&gt;** | How many lane matchups were still running at the matching entry of &#x60;sample_times_s&#x60;. Falls off towards the end of the curve as shorter matches drop out. | 
**SampleTimesS** | **List&lt;int&gt;** | Seconds into the match each entry of the curves was sampled at, ascending. | 
**Stats** | [**Dictionary&lt;string, LaneStatCurve&gt;**](LaneStatCurve.md) | A curve per stat named in &#x60;stats&#x60;. Empty unless the parameter was set. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

