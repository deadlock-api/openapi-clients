# DemoQueryStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **string** | Failure reason, once &#x60;failed&#x60;. | [optional]
**estimated_wait_seconds** | **int** | Rough seconds until the result is ready, while &#x60;queued&#x60; or &#x60;running&#x60;. | [optional]
**format** | [**\OpenAPI\Client\Model\OutputFormat**](OutputFormat.md) |  |
**job_id** | **string** |  |
**match_id** | **int** |  |
**result_url** | **string** | Public URL of the result artifact, once &#x60;done&#x60;. | [optional]
**status** | [**\OpenAPI\Client\Model\JobStatus**](JobStatus.md) |  |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
