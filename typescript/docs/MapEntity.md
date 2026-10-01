# MapEntity

An interactable map entity (crate, bounce pad, shop, ...). Deserialized from `map/entities.json`, which has no minimap position; that is filled in after.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **string** | Variant within the category, e.g. &#x60;wooden_crate&#x60; or &#x60;secret&#x60; (shops). | [optional] [default to undefined]
**left_relative** | **number** | Position on the minimap, as fractions of its width/height. | [optional] [default to undefined]
**position** | **Array&lt;number&gt;** | World position &#x60;[x, y, z]&#x60;, same space as the zip-line splines. Brush triggers (ropes, pads, veils, ...) are placed at their entity origin. | [default to undefined]
**target** | **Array&lt;number&gt;** | World position &#x60;[x, y, z]&#x60; the entity sends you to: the teleporter exit or the bounce pad landing spot. | [optional] [default to undefined]
**team** | **number** | Owning team (0 or 1); absent for neutral entities. | [optional] [default to undefined]
**top_relative** | **number** |  | [optional] [default to undefined]

## Example

```typescript
import { MapEntity } from 'deadlock_api_client';

const instance: MapEntity = {
    kind,
    left_relative,
    position,
    target,
    team,
    top_relative,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
