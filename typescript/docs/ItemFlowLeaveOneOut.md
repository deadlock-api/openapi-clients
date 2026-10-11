# ItemFlowLeaveOneOut

The locked build path without one of its locked items: how the population changes when that item\'s constraint is dropped and every other one kept.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **number** | Its locked stage column. | [default to undefined]
**item_id** | **number** | The locked item left out. See more: &lt;https://api.deadlock-api.com/v1/assets/items&gt; | [default to undefined]
**matches** | **number** |  | [default to undefined]
**wins** | **number** |  | [default to undefined]

## Example

```typescript
import { ItemFlowLeaveOneOut } from 'deadlock_api_client';

const instance: ItemFlowLeaveOneOut = {
    column,
    item_id,
    matches,
    wins,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
