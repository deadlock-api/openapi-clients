# DeadlockApiClient.Model.MMRHistory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **int** |  | 
**Division** | **int** | Extracted from the rank the division (rank // 10) | 
**DivisionTier** | **int** | Extracted from the rank the division tier (rank % 10) | 
**MatchId** | **long** |  | 
**PlayerScore** | **double** | Contiguous index of the rank (1-66), derived from &#x60;rank&#x60; | 
**Rank** | **int** | The Player Rank (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | 
**StartTime** | **int** | Start time of the match | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

