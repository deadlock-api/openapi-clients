# DeadlockApiClient.Model.MapEntity
An interactable map entity (crate, bounce pad, shop, ...). Deserialized from `map/entities.json`, which has no minimap position; that is filled in after.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Position** | **List&lt;double&gt;** | World position &#x60;[x, y, z]&#x60;, same space as the zip-line splines. Brush triggers (ropes, pads, veils, ...) are placed at their entity origin. | 
**Kind** | **string** | Variant within the category, e.g. &#x60;wooden_crate&#x60; or &#x60;secret&#x60; (shops). | [optional] 
**LeftRelative** | **double** | Position on the minimap, as fractions of its width/height. | [optional] 
**Target** | **List&lt;double&gt;** | World position &#x60;[x, y, z]&#x60; the entity sends you to: the teleporter exit or the bounce pad landing spot. | [optional] 
**Team** | **int** | Owning team (0 or 1); absent for neutral entities. | [optional] 
**TopRelative** | **double** |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

