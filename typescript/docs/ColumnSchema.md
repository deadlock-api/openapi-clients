# ColumnSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **string** | Arrow data type, rendered as its canonical textual form (e.g. &#x60;Int32&#x60;, &#x60;Utf8&#x60;). | [default to undefined]
**name** | **string** |  | [default to undefined]
**nullable** | **boolean** |  | [default to undefined]

## Example

```typescript
import { ColumnSchema } from 'deadlock_api_client';

const instance: ColumnSchema = {
    data_type,
    name,
    nullable,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
