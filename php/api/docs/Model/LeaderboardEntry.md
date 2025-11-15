# # LeaderboardEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **string** | The account name of the player. | [optional]
**badge_level** | **int** | The badge level of the player (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]
**possible_account_ids** | **int[]** | The possible account IDs of the player. **CAVEAT: This is not always correct, as Steam account names are not unique.** | [optional]
**rank** | **int** | The rank of the player (tier &#x3D; first digits, subtier &#x3D; last digit). See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]
**ranked_rank** | **int** | The ranked rank of the player. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]
**ranked_subrank** | **int** | The ranked subrank of the player. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | [optional]
**top_hero_ids** | **int[]** | The top hero IDs of the player. See more: &lt;https://assets.deadlock-api.com/v2/heroes&gt; | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
