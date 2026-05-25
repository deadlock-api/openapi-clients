# FeedItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Category** | [**PatchCategory**](PatchCategory.md) |  | 
**Content** | **string** |  | 
**Guid** | [**PatchGuid**](PatchGuid.md) |  | 
**Link** | **string** |  | 
**PubDate** | **time.Time** |  | 
**Title** | **string** |  | 
**Source** | **string** |  | 

## Methods

### NewFeedItem

`func NewFeedItem(category PatchCategory, content string, guid PatchGuid, link string, pubDate time.Time, title string, source string, ) *FeedItem`

NewFeedItem instantiates a new FeedItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewFeedItemWithDefaults

`func NewFeedItemWithDefaults() *FeedItem`

NewFeedItemWithDefaults instantiates a new FeedItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCategory

`func (o *FeedItem) GetCategory() PatchCategory`

GetCategory returns the Category field if non-nil, zero value otherwise.

### GetCategoryOk

`func (o *FeedItem) GetCategoryOk() (*PatchCategory, bool)`

GetCategoryOk returns a tuple with the Category field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategory

`func (o *FeedItem) SetCategory(v PatchCategory)`

SetCategory sets Category field to given value.


### GetContent

`func (o *FeedItem) GetContent() string`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *FeedItem) GetContentOk() (*string, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *FeedItem) SetContent(v string)`

SetContent sets Content field to given value.


### GetGuid

`func (o *FeedItem) GetGuid() PatchGuid`

GetGuid returns the Guid field if non-nil, zero value otherwise.

### GetGuidOk

`func (o *FeedItem) GetGuidOk() (*PatchGuid, bool)`

GetGuidOk returns a tuple with the Guid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGuid

`func (o *FeedItem) SetGuid(v PatchGuid)`

SetGuid sets Guid field to given value.


### GetLink

`func (o *FeedItem) GetLink() string`

GetLink returns the Link field if non-nil, zero value otherwise.

### GetLinkOk

`func (o *FeedItem) GetLinkOk() (*string, bool)`

GetLinkOk returns a tuple with the Link field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLink

`func (o *FeedItem) SetLink(v string)`

SetLink sets Link field to given value.


### GetPubDate

`func (o *FeedItem) GetPubDate() time.Time`

GetPubDate returns the PubDate field if non-nil, zero value otherwise.

### GetPubDateOk

`func (o *FeedItem) GetPubDateOk() (*time.Time, bool)`

GetPubDateOk returns a tuple with the PubDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPubDate

`func (o *FeedItem) SetPubDate(v time.Time)`

SetPubDate sets PubDate field to given value.


### GetTitle

`func (o *FeedItem) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *FeedItem) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *FeedItem) SetTitle(v string)`

SetTitle sets Title field to given value.


### GetSource

`func (o *FeedItem) GetSource() string`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *FeedItem) GetSourceOk() (*string, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *FeedItem) SetSource(v string)`

SetSource sets Source field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


