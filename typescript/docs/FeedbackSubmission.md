# FeedbackSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_id** | **string** |  | [optional] [default to undefined]
**comment** | **string** |  | [default to undefined]
**element_text** | **string** |  | [optional] [default to undefined]
**kind** | [**FeedbackKind**](FeedbackKind.md) |  | [default to undefined]
**nickname** | **string** |  | [optional] [default to undefined]
**page_url** | **string** |  | [default to undefined]
**selector** | **string** |  | [optional] [default to undefined]
**source** | [**SourceLocation**](SourceLocation.md) | Superseded by &#x60;targets&#x60;; still accepted so pages cached from an older build keep submitting successfully. | [optional] [default to undefined]
**targets** | [**Array&lt;FeedbackTarget&gt;**](FeedbackTarget.md) | The annotated elements. Left empty for general feedback. | [optional] [default to undefined]
**viewport** | [**Viewport**](Viewport.md) |  | [optional] [default to undefined]

## Example

```typescript
import { FeedbackSubmission } from 'deadlock_api_client';

const instance: FeedbackSubmission = {
    build_id,
    comment,
    element_text,
    kind,
    nickname,
    page_url,
    selector,
    source,
    targets,
    viewport,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
