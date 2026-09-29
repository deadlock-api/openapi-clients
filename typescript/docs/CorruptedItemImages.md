# CorruptedItemImages

Shop art for corrupted items (build 6711+). The game has no per-item corrupted icon: a corrupted item is its normal image drawn inside `frame`, with the tooltip backer of its `item_slot_type`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frame** | [**ImagePair**](ImagePair.md) |  | [default to undefined]
**frame_active** | [**ImagePair**](ImagePair.md) | Frame for an active (usable) corrupted item. | [default to undefined]
**tooltip_backers** | [**CorruptedTooltipBackers**](CorruptedTooltipBackers.md) |  | [default to undefined]

## Example

```typescript
import { CorruptedItemImages } from 'deadlock_api_client';

const instance: CorruptedItemImages = {
    frame,
    frame_active,
    tooltip_backers,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
