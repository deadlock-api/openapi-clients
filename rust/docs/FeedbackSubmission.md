# FeedbackSubmission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_id** | Option<**String**> |  | [optional]
**comment** | **String** |  | 
**element_text** | Option<**String**> |  | [optional]
**kind** | [**models::FeedbackKind**](FeedbackKind.md) |  | 
**nickname** | Option<**String**> |  | [optional]
**page_url** | **String** |  | 
**selector** | Option<**String**> |  | [optional]
**source** | Option<[**models::SourceLocation**](SourceLocation.md)> | Superseded by `targets`; still accepted so pages cached from an older build keep submitting successfully. | [optional]
**targets** | Option<[**Vec<models::FeedbackTarget>**](FeedbackTarget.md)> | The annotated elements. Left empty for general feedback. | [optional]
**viewport** | Option<[**models::Viewport**](Viewport.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


