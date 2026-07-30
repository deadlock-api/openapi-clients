# LeaderboardEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **string** | The account name of the player. | [optional]
**possible_account_ids** | **int[]** | The possible account IDs of the player. **CAVEAT: This is not always correct, as Steam account names are not unique.** | [optional]
**rank** | **int** | The rank of the player (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://api.deadlock-api.com/v1/assets/ranks&gt; | [optional]
**top_hero_ids** | **int[]** | The top hero IDs of the player. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
