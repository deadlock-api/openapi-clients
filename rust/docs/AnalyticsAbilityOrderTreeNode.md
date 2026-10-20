# AnalyticsAbilityOrderTreeNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abilities** | **Vec<u32>** | The order prefix: one entry per ability point spent, unlocks included. Its parent node is the prefix one entry shorter. See more: <https://api.deadlock-api.com/v1/assets/heroes> | 
**avg_upgrade_time_s** | **f64** | Average game time (in seconds) at which the last upgrade in `abilities` was bought. | 
**losses** | **u64** |  | 
**matches** | **u64** |  | 
**players** | **u64** | Distinct players, counted exactly. | 
**total_assists** | **u64** |  | 
**total_deaths** | **u64** |  | 
**total_kills** | **u64** |  | 
**wins** | **u64** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


