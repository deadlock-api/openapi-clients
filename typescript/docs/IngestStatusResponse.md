# IngestStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **number** |  | [default to undefined]
**active** | **boolean** | Whether the ingest tool uploaded a salt for this account within the window that was then verified. | [default to undefined]
**last_upload_at** | **number** | Unix timestamp of the most recent verified upload within the window. | [optional] [default to undefined]
**window_days** | **number** | The window, in days, an upload must fall in to count. | [default to undefined]

## Example

```typescript
import { IngestStatusResponse } from 'deadlock_api_client';

const instance: IngestStatusResponse = {
    account_id,
    active,
    last_upload_at,
    window_days,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
