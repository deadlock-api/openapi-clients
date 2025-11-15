# LeaderboardEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | Option<**String**> | The account name of the player. | [optional]
**badge_level** | Option<**u32**> | The badge level of the player (tier = first digits, subtier = last digit). See more: <https://assets.deadlock-api.com/v2/ranks> | [optional]
**possible_account_ids** | Option<**Vec<u32>**> | The possible account IDs of the player. **CAVEAT: This is not always correct, as Steam account names are not unique.** | [optional]
**rank** | Option<**u32**> | The rank of the player (tier = first digits, subtier = last digit). See more: <https://assets.deadlock-api.com/v2/ranks> | [optional]
**ranked_rank** | Option<**u32**> | The ranked rank of the player. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional]
**ranked_subrank** | Option<**u32**> | The ranked subrank of the player. See more: <https://assets.deadlock-api.com/v2/ranks> | [optional]
**top_hero_ids** | Option<**Vec<u32>**> | The top hero IDs of the player. See more: <https://assets.deadlock-api.com/v2/heroes> | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


