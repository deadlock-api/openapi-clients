# MapEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **string** | Variant within the category, e.g. &#x60;wooden_crate&#x60; or &#x60;secret&#x60; (shops). | [optional]
**left_relative** | **float** | Position on the minimap, as fractions of its width/height. | [optional]
**position** | **float[]** | World position &#x60;[x, y, z]&#x60;, same space as the zip-line splines. Brush triggers (ropes, pads, veils, ...) are placed at their entity origin. |
**target** | **float[]** | World position &#x60;[x, y, z]&#x60; the entity sends you to: the teleporter exit or the bounce pad landing spot. | [optional]
**team** | **int** | Owning team (0 or 1); absent for neutral entities. | [optional]
**top_relative** | **float** |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
