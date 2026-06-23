# TableSchemaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**Array&lt;ColumnSchema&gt;**](ColumnSchema.md) |  | [default to undefined]
**kind** | **string** | &#x60;entity&#x60; for tables discovered from the demo\&#39;s send-tables, &#x60;event&#x60; for the event tables common to every demo. | [default to undefined]
**name** | **string** |  | [default to undefined]

## Example

```typescript
import { TableSchemaResponse } from 'deadlock_api_client';

const instance: TableSchemaResponse = {
    columns,
    kind,
    name,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
