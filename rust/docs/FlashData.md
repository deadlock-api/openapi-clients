# FlashData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brightness** | Option<**f64**> |  | [optional]
**brightness_in_light_sensitivity_mode** | Option<**f64**> |  | [optional]
**color** | [**models::Color**](Color.md) | Flat flash color. From build 6711 on it is derived from the first `color_gradient` stop. | 
**color_gradient** | Option<[**Vec<models::ColorGradientStop>**](ColorGradientStop.md)> | Color gradient over the flash's lifetime (build 6711+). | [optional]
**coverage** | Option<**f64**> | Only present up to build 6701. | [optional]
**duration** | **f64** |  | 
**hardness** | Option<**f64**> | Only present up to build 6701. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


