# FlashData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brightness** | **float** |  | [optional]
**brightness_in_light_sensitivity_mode** | **float** |  | [optional]
**color** | [**\OpenAPI\Client\Model\Color**](Color.md) | Flat flash color. From build 6711 on it is derived from the first &#x60;color_gradient&#x60; stop. |
**color_gradient** | [**\OpenAPI\Client\Model\ColorGradientStop[]**](ColorGradientStop.md) | Color gradient over the flash&#39;s lifetime (build 6711+). | [optional]
**coverage** | **float** | Only present up to build 6701. | [optional]
**duration** | **float** |  |
**hardness** | **float** | Only present up to build 6701. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
