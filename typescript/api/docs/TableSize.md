# TableSize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_compressed_bytes** | **number** | Compressed size of the table in bytes. | [optional] [default to undefined]
**data_uncompressed_bytes** | **number** | Uncompressed size of the table in bytes. | [optional] [default to undefined]
**is_view** | **boolean** | Whether the table is a view. | [default to undefined]
**rows** | **number** | Number of rows in the table. | [optional] [default to undefined]

## Example

```typescript
import { TableSize } from 'deadlock-api-client';

const instance: TableSize = {
    data_compressed_bytes,
    data_uncompressed_bytes,
    is_view,
    rows,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
