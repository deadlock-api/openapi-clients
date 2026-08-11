# DeadlockApiClient.Model.LaneMatchupStat
One requested stat, read at `sample_time_s` and averaged over the matchups that reached it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Diff** | **double** | Mean of the duo&#39;s combined value minus the enemy duo&#39;s. Negative means behind. | 
**DiffStd** | **double** | Population standard deviation of &#x60;diff&#x60; across the counted matchups. | 
**Value** | **double** | Mean of the duo&#39;s combined value, summed over its two players. | 
**ValueStd** | **double** | Population standard deviation of &#x60;value&#x60; across the counted matchups. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

