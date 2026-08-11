# DeadlockApiClient.Model.LaneStatCurve
One requested stat's curve. All four arrays line up with `sample_times_s`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Diff** | **List&lt;double&gt;** | Mean of the duo&#39;s combined value minus the enemy duo&#39;s. Negative means behind. | 
**DiffStd** | **List&lt;double&gt;** | Population standard deviation of &#x60;diff&#x60; across the counted matchups. | 
**Value** | **List&lt;double&gt;** | Mean of the duo&#39;s combined value, summed over its two players. | 
**ValueStd** | **List&lt;double&gt;** | Population standard deviation of &#x60;value&#x60; across the counted matchups. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

