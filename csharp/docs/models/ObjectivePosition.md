# DeadlockApiClient.Model.ObjectivePosition
The top-left corner of an objective marker on the minimap, as fractions of its width/height (like a CSS `margin-left`/`margin-top`). The marker is a `Core` (30% x 8%) for the cores and an `Icon` (10% x 10%) otherwise, so its centre is this position plus half that size. Unlike `neutral_camps`, whose `left_relative`/`top_relative` are the point itself. Before build 6711 these are the HUD's schematic layout; from 6711 on they are real map positions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LeftRelative** | **double** |  | 
**TopRelative** | **double** |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

