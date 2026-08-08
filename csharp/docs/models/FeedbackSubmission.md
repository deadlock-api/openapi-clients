# DeadlockApiClient.Model.FeedbackSubmission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Comment** | **string** |  | 
**Kind** | **FeedbackKind** |  | 
**PageUrl** | **string** |  | 
**BuildId** | **string** |  | [optional] 
**ElementText** | **string** |  | [optional] 
**Nickname** | **string** |  | [optional] 
**Selector** | **string** |  | [optional] 
**Source** | [**SourceLocation**](SourceLocation.md) | Superseded by &#x60;targets&#x60;; still accepted so pages cached from an older build keep submitting successfully. | [optional] 
**Targets** | [**List&lt;FeedbackTarget&gt;**](FeedbackTarget.md) | The annotated elements. Left empty for general feedback. | [optional] 
**Viewport** | [**Viewport**](Viewport.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

