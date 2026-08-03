# DeadlockApiClient.Model.RankResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Badge** | **int** | Rank badge, &#x60;tier * 10 + subrank&#x60;, including the progress the last ranked match awarded. &#x60;0&#x60; when no recent ranked match reports a rank. See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | 
**Rank** | **int** | Rank tier, &#x60;0&#x60; when unknown. | 
**Subrank** | **int** | Sub-rank within the tier, &#x60;0&#x60; when unknown. | 
**LastMatch** | [**LastRankedMatch**](LastRankedMatch.md) | Rank metadata of the ranked match the badge was read from. &#x60;null&#x60; when none of the player&#39;s recent ranked matches reports a rank. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

