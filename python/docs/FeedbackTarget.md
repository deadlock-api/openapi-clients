# FeedbackTarget

One annotated element. A submission carries several when the visitor picked more than one.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**element_text** | **str** |  | [optional] 
**selector** | **str** |  | [optional] 
**source** | [**SourceLocation**](SourceLocation.md) |  | [optional] 

## Example

```python
from deadlock_api_client.models.feedback_target import FeedbackTarget

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackTarget from a JSON string
feedback_target_instance = FeedbackTarget.from_json(json)
# print the JSON string representation of the object
print(FeedbackTarget.to_json())

# convert the object into a dict
feedback_target_dict = feedback_target_instance.to_dict()
# create an instance of FeedbackTarget from a dict
feedback_target_from_dict = FeedbackTarget.from_dict(feedback_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


