# DemoQueryStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **string** | Failure reason, once &#x60;failed&#x60;. | [optional] [default to undefined]
**estimated_wait_seconds** | **number** | Rough seconds until the result is ready, while &#x60;queued&#x60; or &#x60;running&#x60;. | [optional] [default to undefined]
**format** | [**OutputFormat**](OutputFormat.md) |  | [default to undefined]
**job_id** | **string** |  | [default to undefined]
**match_id** | **number** |  | [default to undefined]
**result_url** | **string** | Public URL of the result artifact, once &#x60;done&#x60;. NDJSON results are zstd-compressed (&#x60;.ndjson.zst&#x60;); Parquet results are served as-is. | [optional] [default to undefined]
**status** | [**JobStatus**](JobStatus.md) |  | [default to undefined]

## Example

```typescript
import { DemoQueryStatusResponse } from 'deadlock_api_client';

const instance: DemoQueryStatusResponse = {
    error,
    estimated_wait_seconds,
    format,
    job_id,
    match_id,
    result_url,
    status,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
