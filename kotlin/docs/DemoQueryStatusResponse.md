
# DemoQueryStatusResponse

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **format** | [**OutputFormat**](OutputFormat.md) |  |  |
| **jobId** | **kotlin.String** |  |  |
| **matchId** | **kotlin.Long** |  |  |
| **status** | [**JobStatus**](JobStatus.md) |  |  |
| **error** | **kotlin.String** | Failure reason, once &#x60;failed&#x60;. |  [optional] |
| **estimatedWaitSeconds** | **kotlin.Long** | Rough seconds until the result is ready, while &#x60;queued&#x60; or &#x60;running&#x60;. |  [optional] |
| **resultUrl** | **kotlin.String** | Public URL of the result artifact, once &#x60;done&#x60;. NDJSON results are zstd-compressed (&#x60;.ndjson.zst&#x60;); Parquet results are served as-is. |  [optional] |



