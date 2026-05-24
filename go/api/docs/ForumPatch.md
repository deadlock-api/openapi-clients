# ForumPatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Category** | [**PatchCategory**](PatchCategory.md) |  | 
**Content** | **string** |  | 
**Guid** | [**PatchGuid**](PatchGuid.md) |  | 
**Link** | **string** |  | 
**PubDate** | **time.Time** |  | 
**Title** | **string** |  | 

## Methods

### NewForumPatch

`func NewForumPatch(category PatchCategory, content string, guid PatchGuid, link string, pubDate time.Time, title string, ) *ForumPatch`

NewForumPatch instantiates a new ForumPatch object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewForumPatchWithDefaults

`func NewForumPatchWithDefaults() *ForumPatch`

NewForumPatchWithDefaults instantiates a new ForumPatch object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCategory

`func (o *ForumPatch) GetCategory() PatchCategory`

GetCategory returns the Category field if non-nil, zero value otherwise.

### GetCategoryOk

`func (o *ForumPatch) GetCategoryOk() (*PatchCategory, bool)`

GetCategoryOk returns a tuple with the Category field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategory

`func (o *ForumPatch) SetCategory(v PatchCategory)`

SetCategory sets Category field to given value.


### GetContent

`func (o *ForumPatch) GetContent() string`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *ForumPatch) GetContentOk() (*string, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *ForumPatch) SetContent(v string)`

SetContent sets Content field to given value.


### GetGuid

`func (o *ForumPatch) GetGuid() PatchGuid`

GetGuid returns the Guid field if non-nil, zero value otherwise.

### GetGuidOk

`func (o *ForumPatch) GetGuidOk() (*PatchGuid, bool)`

GetGuidOk returns a tuple with the Guid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGuid

`func (o *ForumPatch) SetGuid(v PatchGuid)`

SetGuid sets Guid field to given value.


### GetLink

`func (o *ForumPatch) GetLink() string`

GetLink returns the Link field if non-nil, zero value otherwise.

### GetLinkOk

`func (o *ForumPatch) GetLinkOk() (*string, bool)`

GetLinkOk returns a tuple with the Link field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLink

`func (o *ForumPatch) SetLink(v string)`

SetLink sets Link field to given value.


### GetPubDate

`func (o *ForumPatch) GetPubDate() time.Time`

GetPubDate returns the PubDate field if non-nil, zero value otherwise.

### GetPubDateOk

`func (o *ForumPatch) GetPubDateOk() (*time.Time, bool)`

GetPubDateOk returns a tuple with the PubDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPubDate

`func (o *ForumPatch) SetPubDate(v time.Time)`

SetPubDate sets PubDate field to given value.


### GetTitle

`func (o *ForumPatch) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *ForumPatch) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *ForumPatch) SetTitle(v string)`

SetTitle sets Title field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


