# MapV1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**radius** | Option<**i32**> | The radius of the map. | [optional][default to 10752]
**images** | [**models::MapImagesV1**](MapImagesV1.md) | The images of the map. | 
**objective_positions** | [**models::ObjectivePositionsV1**](ObjectivePositionsV1.md) |  | [readonly]
**zipline_paths** | [**Vec<models::ZiplanePathV1>**](ZiplanePathV1.md) | The ziplane paths of the map. Each path is a list of P0, P1, and P2 points, describing the cubic spline. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


