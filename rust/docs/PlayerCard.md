# PlayerCard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **u32** |  | 
**ranked_badge_level** | Option<**u32**> | Rank badge after the player's latest ranked match (player cards no longer carry a rank since build 6711), `null` when no recent ranked match reports one. See more: <https://api.deadlock-api.com/v1/assets/ranks> | [optional]
**ranked_rank** | Option<**u32**> | See more: <https://api.deadlock-api.com/v1/assets/ranks> | [optional]
**ranked_subrank** | Option<**u32**> | See more: <https://api.deadlock-api.com/v1/assets/ranks> | [optional]
**slots** | [**Vec<models::PlayerCardSlot>**](PlayerCardSlot.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


