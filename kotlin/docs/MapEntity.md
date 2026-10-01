
# MapEntity

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **position** | **kotlin.collections.List&lt;kotlin.Double&gt;** | World position &#x60;[x, y, z]&#x60;, same space as the zip-line splines. Brush triggers (ropes, pads, veils, ...) are placed at their entity origin. |  |
| **kind** | **kotlin.String** | Variant within the category, e.g. &#x60;wooden_crate&#x60; or &#x60;secret&#x60; (shops). |  [optional] |
| **leftRelative** | **kotlin.Double** | Position on the minimap, as fractions of its width/height. |  [optional] |
| **target** | **kotlin.collections.List&lt;kotlin.Double&gt;** | World position &#x60;[x, y, z]&#x60; the entity sends you to: the teleporter exit or the bounce pad landing spot. |  [optional] |
| **team** | **kotlin.Int** | Owning team (0 or 1); absent for neutral entities. |  [optional] |
| **topRelative** | **kotlin.Double** |  |  [optional] |



