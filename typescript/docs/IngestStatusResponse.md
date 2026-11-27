# IngestStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **number** |  | [default to undefined]
**active** | **boolean** | Whether the account\&#39;s player tracker is open to everyone: it or one of its Steam friends ran an ingest client within the window, or a patron prioritizes it. | [default to undefined]
**friend_active** | **boolean** | Whether a Steam friend of the account uploaded with an ingest client within the window. | [default to undefined]
**last_upload_at** | **number** | Unix timestamp of the account\&#39;s own most recent verified upload within the window. | [optional] [default to undefined]
**prioritized** | **boolean** | Whether the account is one of a patron\&#39;s active prioritized accounts. | [default to undefined]
**window_days** | **number** | The window, in days, an upload must fall in to count. | [default to undefined]

## Example

```typescript
import { IngestStatusResponse } from 'deadlock_api_client';

const instance: IngestStatusResponse = {
    account_id,
    active,
    friend_active,
    last_upload_at,
    prioritized,
    window_days,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
