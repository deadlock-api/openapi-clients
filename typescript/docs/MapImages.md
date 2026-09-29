# MapImages

CDN URLs for the minimap image layers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background** | **string** | Background layer. No longer shipped by the game from build 6711 on; the last extracted image is kept in the bucket. | [default to undefined]
**frame** | **string** |  | [default to undefined]
**mid** | **string** | Midtown base layer. | [default to undefined]
**mid_tunnels** | **string** | Mid tunnels overlay, drawn above &#x60;mid&#x60; (build 6711+). | [optional] [default to undefined]
**minimap** | **string** | Full minimap. From build 6711 on this is the midtown base layer. | [default to undefined]
**plain** | **string** | Minimap without overlays. From build 6711 on this is the midtown base layer. | [default to undefined]
**rat_tunnels** | **string** | Rat tunnels overlay, drawn above &#x60;mid_tunnels&#x60; (build 6711+). | [optional] [default to undefined]

## Example

```typescript
import { MapImages } from 'deadlock_api_client';

const instance: MapImages = {
    background,
    frame,
    mid,
    mid_tunnels,
    minimap,
    plain,
    rat_tunnels,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
