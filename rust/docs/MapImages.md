# MapImages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background** | Option<**String**> | Background layer drawn under `mid`. Only for builds before 6711; the game no longer ships it, so it is omitted from build 6711 on. | [optional]
**frame** | **String** |  | 
**mid** | **String** | Midtown base layer. | 
**mid_tunnels** | Option<**String**> | Mid tunnels overlay, drawn above `mid` (build 6711+). | [optional]
**minimap** | **String** | Full minimap. From build 6711 on the game ships no composed minimap, so this is the same image as `mid`: the midtown street layer as a black mask on transparency, meant to be drawn over a base colour rather than shown on its own. | 
**plain** | **String** | Minimap without overlays. From build 6711 on this is the same street mask as `mid` (see `minimap`). | 
**rat_tunnels** | Option<**String**> | Rat tunnels overlay, drawn above `mid_tunnels` (build 6711+). | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


