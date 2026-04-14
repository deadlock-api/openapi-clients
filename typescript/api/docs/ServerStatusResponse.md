# ServerStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **string** | The server ID that reported status | [default to undefined]
**ttl_secs** | **number** | TTL in seconds before this registration expires | [default to undefined]

## Example

```typescript
import { ServerStatusResponse } from 'deadlock_api_client';

const instance: ServerStatusResponse = {
    server_id,
    ttl_secs,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
