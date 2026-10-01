# MapData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | Option<[**models::MapEntities**](MapEntities.md)> | Interactable map entities; only for builds whose assets were built with the map entity extraction. | [optional]
**images** | [**models::MapImages**](MapImages.md) |  | 
**neutral_camps** | Option<[**Vec<models::NeutralCamp>**](NeutralCamp.md)> | Neutral camps (build 6711+). | [optional]
**objective_positions** | [**std::collections::HashMap<String, models::ObjectivePosition>**](ObjectivePosition.md) |  | 
**radius** | **u32** |  | 
**zipline_paths** | [**Vec<models::ZiplanePath>**](ZiplanePath.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


