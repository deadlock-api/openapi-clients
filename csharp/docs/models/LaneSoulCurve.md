# DeadlockApiClient.Model.LaneSoulCurve
**⚠️ Subject to change:** newly added, fields may change or be removed without notice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AssignedLane** | **int** | The lane the matchup was played in. See the &#x60;lane_info&#x60; array of &lt;https://api.deadlock-api.com/v1/assets/generic-data&gt;. | 
**EnemyHeroIds** | **List&lt;int&gt;** | The ascending hero id pair they laned against. | 
**HeroIds** | **List&lt;int&gt;** | The ascending hero id pair that shared the lane. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**MatchesPlayed** | **long** | Lane matchups behind the curve, counted at its *least* covered sample. A match that ended before 900s still contributes to the earlier points, so the earlier points rest on at least this many matchups and never fewer. | 
**NetWorthDiff** | **List&lt;double&gt;** | Mean souls the duo is ahead by at the matching entry of &#x60;sample_times_s&#x60;. Negative means behind. Same length as &#x60;sample_times_s&#x60;. | 
**NetWorthDiffStd** | **List&lt;double&gt;** | Population standard deviation of the lead across the counted matchups, at the matching entry of &#x60;sample_times_s&#x60;. Same length as &#x60;sample_times_s&#x60;.  Spread between individual games, not uncertainty about the mean: it stays wide however many matchups are counted, because lane outcomes genuinely differ that much. | 
**SampleTimesS** | **List&lt;int&gt;** | Seconds into the match each entry of &#x60;net_worth_diff&#x60; was sampled at, ascending. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

