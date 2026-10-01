# MapEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | Option<**String**> | Variant within the category, e.g. `wooden_crate` or `secret` (shops). | [optional]
**left_relative** | Option<**f64**> | Position on the minimap, as fractions of its width/height. | [optional]
**position** | **Vec<f64>** | World position `[x, y, z]`, same space as the zip-line splines. Brush triggers (ropes, pads, veils, ...) are placed at their entity origin. | 
**target** | Option<**Vec<f64>**> | World position `[x, y, z]` the entity sends you to: the teleporter exit or the bounce pad landing spot. | [optional]
**team** | Option<**u32**> | Owning team (0 or 1); absent for neutral entities. | [optional]
**top_relative** | Option<**f64**> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


