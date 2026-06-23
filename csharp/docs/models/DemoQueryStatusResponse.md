# DeadlockApiClient.Model.DemoQueryStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Format** | **OutputFormat** |  | 
**JobId** | **string** |  | 
**MatchId** | **long** |  | 
**Status** | **JobStatus** |  | 
**Error** | **string** | Failure reason, once &#x60;failed&#x60;. | [optional] 
**EstimatedWaitSeconds** | **long** | Rough seconds until the result is ready, while &#x60;queued&#x60; or &#x60;running&#x60;. | [optional] 
**ResultUrl** | **string** | Public URL of the result artifact, once &#x60;done&#x60;. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

