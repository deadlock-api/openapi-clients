# DeadlockApiClient.Model.MMRHistory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **int** |  | 
**Division** | **int** | Extracted from the rank the division (rank // 10) | 
**DivisionTier** | **int** | Extracted from the rank the division tier (rank % 10) | 
**MatchId** | **long** |  | 
**PlayerScore** | **double** | Player Score is the index for the rank array (internally used for the rank regression) | 
**Rank** | **int** | The Player Rank (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
**StartTime** | **int** | Start time of the match | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

