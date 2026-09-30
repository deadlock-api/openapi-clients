# PlayerEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **u32** |  | 
**badge** | Option<**u32**> | `rank` and `peak_rank` sorts only: the rank badge the progress in `value` falls in, `0` when the player has no ranked match in range. Omitted for every other sort. See more: <https://api.deadlock-api.com/v1/assets/ranks> | [optional]
**badge_progress** | Option<**u32**> | `rank` and `peak_rank` sorts only: progress points into `badge`. A subrank spans 1000 points, the sixth of a tier 2000. `null` in Eternus, whose subranks are percentile cuts rather than point spans, and when the player has no ranked match in range. | [optional]
**matches** | **u64** |  | 
**rank** | **u64** |  | 
**value** | **f64** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


