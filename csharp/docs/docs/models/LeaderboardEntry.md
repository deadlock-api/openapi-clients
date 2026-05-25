# DeadlockApiClient.Model.LeaderboardEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountName** | **string** | The account name of the player. | [optional] 
**BadgeLevel** | **int** | The badge level of the player (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**PossibleAccountIds** | **List&lt;int&gt;** | The possible account IDs of the player. **CAVEAT: This is not always correct, as Steam account names are not unique.** | [optional] 
**Rank** | **int** | The rank of the player (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**RankedRank** | **int** | The ranked rank of the player. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**RankedSubrank** | **int** | The ranked subrank of the player. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional] 
**TopHeroIds** | **List&lt;int&gt;** | The top hero IDs of the player. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

