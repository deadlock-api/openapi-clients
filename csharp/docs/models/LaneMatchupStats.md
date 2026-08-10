# DeadlockApiClient.Model.LaneMatchupStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AssignedLane** | **int** | The lane the matchup was played in. See the &#x60;lane_info&#x60; array of &lt;https://api.deadlock-api.com/v1/assets/generic-data&gt;. | 
**EnemyHeroIds** | **List&lt;int&gt;** | The ascending hero id pair they laned against. | 
**HeroIds** | **List&lt;int&gt;** | The ascending hero id pair that shared the lane. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**MatchesPlayed** | **long** | The total number of lane matchups between &#x60;hero_ids&#x60; and &#x60;enemy_hero_ids&#x60; in this lane. | 
**NetWorthDiff9min** | **double** | Mean souls the duo is ahead by 9 minutes in, against that duo. Negative means behind. &#x60;0&#x60; when no counted matchup had net-worth samples for all four players. | 
**NetWorthMatches** | **long** | How many of &#x60;matches_played&#x60; carried net-worth samples for all four players. | 
**Wins** | **long** | The number of matches &#x60;hero_ids&#x60; won against &#x60;enemy_hero_ids&#x60; in this lane. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

