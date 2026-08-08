# FeedbackSubmission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_id** | **string** |  | [optional]
**comment** | **string** |  |
**element_text** | **string** |  | [optional]
**kind** | [**\OpenAPI\Client\Model\FeedbackKind**](FeedbackKind.md) |  |
**nickname** | **string** |  | [optional]
**page_url** | **string** |  |
**selector** | **string** |  | [optional]
**source** | [**\OpenAPI\Client\Model\SourceLocation**](SourceLocation.md) | Superseded by &#x60;targets&#x60;; still accepted so pages cached from an older build keep submitting successfully. | [optional]
**targets** | [**\OpenAPI\Client\Model\FeedbackTarget[]**](FeedbackTarget.md) | The annotated elements. Left empty for general feedback. | [optional]
**viewport** | [**\OpenAPI\Client\Model\Viewport**](Viewport.md) |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
