# ItemFlowEdge

A transition between an item in one column and an item in the next column, counted across players who purchased both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_column** | **number** | The column of the source item. | [default to undefined]
**from_item_id** | **number** |  | [default to undefined]
**losses** | **number** |  | [default to undefined]
**matches** | **number** |  | [default to undefined]
**to_item_id** | **number** |  | [default to undefined]
**wins** | **number** |  | [default to undefined]

## Example

```typescript
import { ItemFlowEdge } from 'deadlock_api_client';

const instance: ItemFlowEdge = {
    from_column,
    from_item_id,
    losses,
    matches,
    to_item_id,
    wins,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
