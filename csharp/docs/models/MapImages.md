# DeadlockApiClient.Model.MapImages
CDN URLs for the minimap image layers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Background** | **string** | Background layer. No longer shipped by the game from build 6711 on; the last extracted image is kept in the bucket. | 
**Frame** | **string** |  | 
**Mid** | **string** | Midtown base layer. | 
**Minimap** | **string** | Full minimap. From build 6711 on this is the midtown base layer. | 
**Plain** | **string** | Minimap without overlays. From build 6711 on this is the midtown base layer. | 
**MidTunnels** | **string** | Mid tunnels overlay, drawn above &#x60;mid&#x60; (build 6711+). | [optional] 
**RatTunnels** | **string** | Rat tunnels overlay, drawn above &#x60;mid_tunnels&#x60; (build 6711+). | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

