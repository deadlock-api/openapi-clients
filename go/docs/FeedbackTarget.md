# FeedbackTarget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ElementText** | Pointer to **NullableString** |  | [optional] 
**Selector** | Pointer to **NullableString** |  | [optional] 
**Source** | Pointer to [**NullableSourceLocation**](SourceLocation.md) |  | [optional] 

## Methods

### NewFeedbackTarget

`func NewFeedbackTarget() *FeedbackTarget`

NewFeedbackTarget instantiates a new FeedbackTarget object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFeedbackTargetWithDefaults

`func NewFeedbackTargetWithDefaults() *FeedbackTarget`

NewFeedbackTargetWithDefaults instantiates a new FeedbackTarget object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetElementText

`func (o *FeedbackTarget) GetElementText() string`

GetElementText returns the ElementText field if non-nil, zero value otherwise.

### GetElementTextOk

`func (o *FeedbackTarget) GetElementTextOk() (*string, bool)`

GetElementTextOk returns a tuple with the ElementText field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetElementText

`func (o *FeedbackTarget) SetElementText(v string)`

SetElementText sets ElementText field to given value.

### HasElementText

`func (o *FeedbackTarget) HasElementText() bool`

HasElementText returns a boolean if a field has been set.

### SetElementTextNil

`func (o *FeedbackTarget) SetElementTextNil(b bool)`

 SetElementTextNil sets the value for ElementText to be an explicit nil

### UnsetElementText
`func (o *FeedbackTarget) UnsetElementText()`

UnsetElementText ensures that no value is present for ElementText, not even an explicit nil
### GetSelector

`func (o *FeedbackTarget) GetSelector() string`

GetSelector returns the Selector field if non-nil, zero value otherwise.

### GetSelectorOk

`func (o *FeedbackTarget) GetSelectorOk() (*string, bool)`

GetSelectorOk returns a tuple with the Selector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSelector

`func (o *FeedbackTarget) SetSelector(v string)`

SetSelector sets Selector field to given value.

### HasSelector

`func (o *FeedbackTarget) HasSelector() bool`

HasSelector returns a boolean if a field has been set.

### SetSelectorNil

`func (o *FeedbackTarget) SetSelectorNil(b bool)`

 SetSelectorNil sets the value for Selector to be an explicit nil

### UnsetSelector
`func (o *FeedbackTarget) UnsetSelector()`

UnsetSelector ensures that no value is present for Selector, not even an explicit nil
### GetSource

`func (o *FeedbackTarget) GetSource() SourceLocation`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *FeedbackTarget) GetSourceOk() (*SourceLocation, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *FeedbackTarget) SetSource(v SourceLocation)`

SetSource sets Source field to given value.

### HasSource

`func (o *FeedbackTarget) HasSource() bool`

HasSource returns a boolean if a field has been set.

### SetSourceNil

`func (o *FeedbackTarget) SetSourceNil(b bool)`

 SetSourceNil sets the value for Source to be an explicit nil

### UnsetSource
`func (o *FeedbackTarget) UnsetSource()`

UnsetSource ensures that no value is present for Source, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


