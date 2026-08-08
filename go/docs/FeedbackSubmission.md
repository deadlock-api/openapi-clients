# FeedbackSubmission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BuildId** | Pointer to **NullableString** |  | [optional] 
**Comment** | **string** |  | 
**ElementText** | Pointer to **NullableString** |  | [optional] 
**Kind** | [**FeedbackKind**](FeedbackKind.md) |  | 
**Nickname** | Pointer to **NullableString** |  | [optional] 
**PageUrl** | **string** |  | 
**Selector** | Pointer to **NullableString** |  | [optional] 
**Source** | Pointer to [**NullableSourceLocation**](SourceLocation.md) | Superseded by &#x60;targets&#x60;; still accepted so pages cached from an older build keep submitting successfully. | [optional] 
**Targets** | Pointer to [**[]FeedbackTarget**](FeedbackTarget.md) | The annotated elements. Left empty for general feedback. | [optional] 
**Viewport** | Pointer to [**NullableViewport**](Viewport.md) |  | [optional] 

## Methods

### NewFeedbackSubmission

`func NewFeedbackSubmission(comment string, kind FeedbackKind, pageUrl string, ) *FeedbackSubmission`

NewFeedbackSubmission instantiates a new FeedbackSubmission object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFeedbackSubmissionWithDefaults

`func NewFeedbackSubmissionWithDefaults() *FeedbackSubmission`

NewFeedbackSubmissionWithDefaults instantiates a new FeedbackSubmission object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBuildId

`func (o *FeedbackSubmission) GetBuildId() string`

GetBuildId returns the BuildId field if non-nil, zero value otherwise.

### GetBuildIdOk

`func (o *FeedbackSubmission) GetBuildIdOk() (*string, bool)`

GetBuildIdOk returns a tuple with the BuildId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuildId

`func (o *FeedbackSubmission) SetBuildId(v string)`

SetBuildId sets BuildId field to given value.

### HasBuildId

`func (o *FeedbackSubmission) HasBuildId() bool`

HasBuildId returns a boolean if a field has been set.

### SetBuildIdNil

`func (o *FeedbackSubmission) SetBuildIdNil(b bool)`

 SetBuildIdNil sets the value for BuildId to be an explicit nil

### UnsetBuildId
`func (o *FeedbackSubmission) UnsetBuildId()`

UnsetBuildId ensures that no value is present for BuildId, not even an explicit nil
### GetComment

`func (o *FeedbackSubmission) GetComment() string`

GetComment returns the Comment field if non-nil, zero value otherwise.

### GetCommentOk

`func (o *FeedbackSubmission) GetCommentOk() (*string, bool)`

GetCommentOk returns a tuple with the Comment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComment

`func (o *FeedbackSubmission) SetComment(v string)`

SetComment sets Comment field to given value.


### GetElementText

`func (o *FeedbackSubmission) GetElementText() string`

GetElementText returns the ElementText field if non-nil, zero value otherwise.

### GetElementTextOk

`func (o *FeedbackSubmission) GetElementTextOk() (*string, bool)`

GetElementTextOk returns a tuple with the ElementText field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetElementText

`func (o *FeedbackSubmission) SetElementText(v string)`

SetElementText sets ElementText field to given value.

### HasElementText

`func (o *FeedbackSubmission) HasElementText() bool`

HasElementText returns a boolean if a field has been set.

### SetElementTextNil

`func (o *FeedbackSubmission) SetElementTextNil(b bool)`

 SetElementTextNil sets the value for ElementText to be an explicit nil

### UnsetElementText
`func (o *FeedbackSubmission) UnsetElementText()`

UnsetElementText ensures that no value is present for ElementText, not even an explicit nil
### GetKind

`func (o *FeedbackSubmission) GetKind() FeedbackKind`

GetKind returns the Kind field if non-nil, zero value otherwise.

### GetKindOk

`func (o *FeedbackSubmission) GetKindOk() (*FeedbackKind, bool)`

GetKindOk returns a tuple with the Kind field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKind

`func (o *FeedbackSubmission) SetKind(v FeedbackKind)`

SetKind sets Kind field to given value.


### GetNickname

`func (o *FeedbackSubmission) GetNickname() string`

GetNickname returns the Nickname field if non-nil, zero value otherwise.

### GetNicknameOk

`func (o *FeedbackSubmission) GetNicknameOk() (*string, bool)`

GetNicknameOk returns a tuple with the Nickname field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNickname

`func (o *FeedbackSubmission) SetNickname(v string)`

SetNickname sets Nickname field to given value.

### HasNickname

`func (o *FeedbackSubmission) HasNickname() bool`

HasNickname returns a boolean if a field has been set.

### SetNicknameNil

`func (o *FeedbackSubmission) SetNicknameNil(b bool)`

 SetNicknameNil sets the value for Nickname to be an explicit nil

### UnsetNickname
`func (o *FeedbackSubmission) UnsetNickname()`

UnsetNickname ensures that no value is present for Nickname, not even an explicit nil
### GetPageUrl

`func (o *FeedbackSubmission) GetPageUrl() string`

GetPageUrl returns the PageUrl field if non-nil, zero value otherwise.

### GetPageUrlOk

`func (o *FeedbackSubmission) GetPageUrlOk() (*string, bool)`

GetPageUrlOk returns a tuple with the PageUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPageUrl

`func (o *FeedbackSubmission) SetPageUrl(v string)`

SetPageUrl sets PageUrl field to given value.


### GetSelector

`func (o *FeedbackSubmission) GetSelector() string`

GetSelector returns the Selector field if non-nil, zero value otherwise.

### GetSelectorOk

`func (o *FeedbackSubmission) GetSelectorOk() (*string, bool)`

GetSelectorOk returns a tuple with the Selector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSelector

`func (o *FeedbackSubmission) SetSelector(v string)`

SetSelector sets Selector field to given value.

### HasSelector

`func (o *FeedbackSubmission) HasSelector() bool`

HasSelector returns a boolean if a field has been set.

### SetSelectorNil

`func (o *FeedbackSubmission) SetSelectorNil(b bool)`

 SetSelectorNil sets the value for Selector to be an explicit nil

### UnsetSelector
`func (o *FeedbackSubmission) UnsetSelector()`

UnsetSelector ensures that no value is present for Selector, not even an explicit nil
### GetSource

`func (o *FeedbackSubmission) GetSource() SourceLocation`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *FeedbackSubmission) GetSourceOk() (*SourceLocation, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *FeedbackSubmission) SetSource(v SourceLocation)`

SetSource sets Source field to given value.

### HasSource

`func (o *FeedbackSubmission) HasSource() bool`

HasSource returns a boolean if a field has been set.

### SetSourceNil

`func (o *FeedbackSubmission) SetSourceNil(b bool)`

 SetSourceNil sets the value for Source to be an explicit nil

### UnsetSource
`func (o *FeedbackSubmission) UnsetSource()`

UnsetSource ensures that no value is present for Source, not even an explicit nil
### GetTargets

`func (o *FeedbackSubmission) GetTargets() []FeedbackTarget`

GetTargets returns the Targets field if non-nil, zero value otherwise.

### GetTargetsOk

`func (o *FeedbackSubmission) GetTargetsOk() (*[]FeedbackTarget, bool)`

GetTargetsOk returns a tuple with the Targets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargets

`func (o *FeedbackSubmission) SetTargets(v []FeedbackTarget)`

SetTargets sets Targets field to given value.

### HasTargets

`func (o *FeedbackSubmission) HasTargets() bool`

HasTargets returns a boolean if a field has been set.

### GetViewport

`func (o *FeedbackSubmission) GetViewport() Viewport`

GetViewport returns the Viewport field if non-nil, zero value otherwise.

### GetViewportOk

`func (o *FeedbackSubmission) GetViewportOk() (*Viewport, bool)`

GetViewportOk returns a tuple with the Viewport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetViewport

`func (o *FeedbackSubmission) SetViewport(v Viewport)`

SetViewport sets Viewport field to given value.

### HasViewport

`func (o *FeedbackSubmission) HasViewport() bool`

HasViewport returns a boolean if a field has been set.

### SetViewportNil

`func (o *FeedbackSubmission) SetViewportNil(b bool)`

 SetViewportNil sets the value for Viewport to be an explicit nil

### UnsetViewport
`func (o *FeedbackSubmission) UnsetViewport()`

UnsetViewport ensures that no value is present for Viewport, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


