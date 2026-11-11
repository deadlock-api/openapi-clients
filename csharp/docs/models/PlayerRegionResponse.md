# DeadlockApiClient.Model.PlayerRegionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **int** |  | 
**History** | [**List&lt;PlayerClusterMonth&gt;**](PlayerClusterMonth.md) | Matches per month and server cluster, newest month first. | 
**Region** | **string** | The region the player played most matches in during their latest month with a known region. &#x60;null&#x60; if none of their matches has a known region. | [optional] 
**RegionMonth** | **int** | Unix timestamp of the month &#x60;region&#x60; was taken from. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

