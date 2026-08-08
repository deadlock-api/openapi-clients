
# FeedbackSubmission

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **comment** | **kotlin.String** |  |  |
| **kind** | [**FeedbackKind**](FeedbackKind.md) |  |  |
| **pageUrl** | **kotlin.String** |  |  |
| **buildId** | **kotlin.String** |  |  [optional] |
| **elementText** | **kotlin.String** |  |  [optional] |
| **nickname** | **kotlin.String** |  |  [optional] |
| **selector** | **kotlin.String** |  |  [optional] |
| **source** | [**SourceLocation**](SourceLocation.md) | Superseded by &#x60;targets&#x60;; still accepted so pages cached from an older build keep submitting successfully. |  [optional] |
| **targets** | [**kotlin.collections.List&lt;FeedbackTarget&gt;**](FeedbackTarget.md) | The annotated elements. Left empty for general feedback. |  [optional] |
| **viewport** | [**Viewport**](Viewport.md) |  |  [optional] |



