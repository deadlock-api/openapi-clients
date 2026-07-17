# DemoQueryStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | Option<**String**> | Failure reason, once `failed`. | [optional]
**estimated_wait_seconds** | Option<**u64**> | Rough seconds until the result is ready, while `queued` or `running`. | [optional]
**format** | [**models::OutputFormat**](OutputFormat.md) |  | 
**job_id** | **String** |  | 
**match_id** | **u64** |  | 
**result_url** | Option<**String**> | Public URL of the result artifact, once `done`. NDJSON results are zstd-compressed (`.ndjson.zst`); Parquet results are served as-is. | [optional]
**status** | [**models::JobStatus**](JobStatus.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


