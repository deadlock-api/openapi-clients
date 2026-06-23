# DemoQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | [**OutputFormat**](OutputFormat.md) | Output format of the result artifact. | [optional] [default to undefined]
**match_id** | **number** | Match whose demo to query. | [default to undefined]
**query** | **string** | SQL query to run over the demo\&#39;s entity/event tables (see &#x60;/demo/schema&#x60;). | [default to undefined]

## Example

```typescript
import { DemoQueryRequest } from 'deadlock_api_client';

const instance: DemoQueryRequest = {
    format,
    match_id,
    query,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
