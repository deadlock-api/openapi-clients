# MapImages

CDN URLs for the minimap image layers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background** | **string** | Background layer drawn under &#x60;mid&#x60;. Only for builds before 6711; the game no longer ships it, so it is omitted from build 6711 on. | [optional] [default to undefined]
**frame** | **string** |  | [default to undefined]
**mid** | **string** | Midtown base layer. | [default to undefined]
**mid_tunnels** | **string** | Mid tunnels overlay, drawn above &#x60;mid&#x60; (build 6711+). | [optional] [default to undefined]
**minimap** | **string** | Full minimap. From build 6711 on the game ships no composed minimap, so this is the same image as &#x60;mid&#x60;: the midtown street layer as a black mask on transparency, meant to be drawn over a base colour rather than shown on its own. | [default to undefined]
**plain** | **string** | Minimap without overlays. From build 6711 on this is the same street mask as &#x60;mid&#x60; (see &#x60;minimap&#x60;). | [default to undefined]
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
