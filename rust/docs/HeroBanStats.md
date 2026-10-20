# HeroBanStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bans** | **u64** | The number of matches in which this hero was banned. | 
**bucket** | **u32** | The bucket value (depends on the bucket query parameter). | 
**hero_id** | **u32** | The ID of the banned hero. See more: <https://api.deadlock-api.com/v1/assets/heroes> | 
**matches** | **u64** | The number of matches with ban data in this bucket. A hero's ban rate is `bans / matches`; a ranked match has 3 bans and an unranked match 2, so the bans of all heroes do not divide into matches by a fixed count. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


