# NeutralCamp

A neutral camp (\"Haunt\") marker (build 6711+).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon** | **string** | Minimap icon URL. | [default to undefined]
**kind** | [**NeutralCampKind**](NeutralCampKind.md) |  | [default to undefined]
**left_relative** | **number** | Position on the minimap, as fractions of its width/height. | [default to undefined]
**name** | **string** | Camp entity name from the map (e.g. &#x60;theater_lobby_camp&#x60;). | [default to undefined]
**position** | **Array&lt;number&gt;** | World position &#x60;[x, y, z]&#x60;, same space as the zip-line splines. | [default to undefined]
**top_relative** | **number** |  | [default to undefined]

## Example

```typescript
import { NeutralCamp } from 'deadlock_api_client';

const instance: NeutralCamp = {
    icon,
    kind,
    left_relative,
    name,
    position,
    top_relative,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
