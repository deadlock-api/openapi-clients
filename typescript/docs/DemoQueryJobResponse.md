# DemoQueryJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **string** | Stable id of the job; poll &#x60;/demo/query/{job_id}&#x60; for status and the result URL. | [default to undefined]
**status** | [**JobStatus**](JobStatus.md) |  | [default to undefined]

## Example

```typescript
import { DemoQueryJobResponse } from 'deadlock_api_client';

const instance: DemoQueryJobResponse = {
    job_id,
    status,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
