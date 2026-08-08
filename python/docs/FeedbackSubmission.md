# FeedbackSubmission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_id** | **str** |  | [optional] 
**comment** | **str** |  | 
**element_text** | **str** |  | [optional] 
**kind** | [**FeedbackKind**](FeedbackKind.md) |  | 
**nickname** | **str** |  | [optional] 
**page_url** | **str** |  | 
**selector** | **str** |  | [optional] 
**source** | [**SourceLocation**](SourceLocation.md) | Superseded by &#x60;targets&#x60;; still accepted so pages cached from an older build keep submitting successfully. | [optional] 
**targets** | [**List[FeedbackTarget]**](FeedbackTarget.md) | The annotated elements. Left empty for general feedback. | [optional] 
**viewport** | [**Viewport**](Viewport.md) |  | [optional] 

## Example

```python
from deadlock_api_client.models.feedback_submission import FeedbackSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackSubmission from a JSON string
feedback_submission_instance = FeedbackSubmission.from_json(json)
# print the JSON string representation of the object
print(FeedbackSubmission.to_json())

# convert the object into a dict
feedback_submission_dict = feedback_submission_instance.to_dict()
# create an instance of FeedbackSubmission from a dict
feedback_submission_from_dict = FeedbackSubmission.from_dict(feedback_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


