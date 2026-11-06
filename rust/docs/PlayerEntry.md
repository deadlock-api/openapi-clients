# PlayerEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **u32** |  | 
**badge** | Option<**u32**> | `rank` and `peak_rank` sorts only: the rank badge the progress in `value` falls in, `0` when the player has no ranked match in range. Omitted for every other sort. See more: <https://api.deadlock-api.com/v1/assets/ranks> | [optional]
**badge_progress** | Option<**u32**> | `rank` and `peak_rank` sorts only: progress points into `badge`, out of `badge_progress_max`. In Eternus, whose subranks are percentile cuts rather than point spans, the points past the start of Eternus. `null` when the player has no ranked match in range. | [optional]
**badge_progress_max** | Option<**u32**> | `rank` and `peak_rank` sorts only: the points the subrank of `badge` spans in that match's season (`sub_rank_xp` in <https://api.deadlock-api.com/v1/assets/ranked-seasons>). `null` in Eternus and when the player has no ranked match in range. | [optional]
**matches** | **u64** |  | 
**rank** | **u64** |  | 
**value** | **f64** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


