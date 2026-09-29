
# MapImages

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **frame** | **kotlin.String** |  |  |
| **mid** | **kotlin.String** | Midtown base layer. |  |
| **minimap** | **kotlin.String** | Full minimap. From build 6711 on the game ships no composed minimap, so this is the same image as &#x60;mid&#x60;: the midtown street layer as a black mask on transparency, meant to be drawn over a base colour rather than shown on its own. |  |
| **plain** | **kotlin.String** | Minimap without overlays. From build 6711 on this is the same street mask as &#x60;mid&#x60; (see &#x60;minimap&#x60;). |  |
| **background** | **kotlin.String** | Background layer drawn under &#x60;mid&#x60;. Only for builds before 6711; the game no longer ships it, so it is omitted from build 6711 on. |  [optional] |
| **midTunnels** | **kotlin.String** | Mid tunnels overlay, drawn above &#x60;mid&#x60; (build 6711+). |  [optional] |
| **ratTunnels** | **kotlin.String** | Rat tunnels overlay, drawn above &#x60;mid_tunnels&#x60; (build 6711+). |  [optional] |



