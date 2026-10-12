# HeroSwapStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **u32** | The bucket value (depends on the bucket query parameter). | 
**hero_id** | **u32** | The ID of the hero. See more: <https://api.deadlock-api.com/v1/assets/heroes> | 
**matches** | **u64** | The number of players who played this hero, counting only players whose pre-game hero is known. | 
**pregame_picks** | **u64** | The number of players who had this hero locked before the pre-game swap window. | 
**swapped_away** | **u64** | The number of `pregame_picks` players who swapped away from this hero. | 
**swapped_in** | **u64** | The number of players who played this hero after swapping to it from another pre-game hero. | 
**swapped_in_wins** | **u64** | The number of `swapped_in` players who won the match. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


