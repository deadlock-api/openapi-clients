# SteamNews

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Content** | **string** |  | 
**Guid** | [**PatchGuid**](PatchGuid.md) |  | 
**Link** | **string** |  | 
**PubDate** | **time.Time** |  | 
**Title** | **string** |  | 

## Methods

### NewSteamNews

`func NewSteamNews(content string, guid PatchGuid, link string, pubDate time.Time, title string, ) *SteamNews`

NewSteamNews instantiates a new SteamNews object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSteamNewsWithDefaults

`func NewSteamNewsWithDefaults() *SteamNews`

NewSteamNewsWithDefaults instantiates a new SteamNews object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContent

`func (o *SteamNews) GetContent() string`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *SteamNews) GetContentOk() (*string, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *SteamNews) SetContent(v string)`

SetContent sets Content field to given value.


### GetGuid

`func (o *SteamNews) GetGuid() PatchGuid`

GetGuid returns the Guid field if non-nil, zero value otherwise.

### GetGuidOk

`func (o *SteamNews) GetGuidOk() (*PatchGuid, bool)`

GetGuidOk returns a tuple with the Guid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGuid

`func (o *SteamNews) SetGuid(v PatchGuid)`

SetGuid sets Guid field to given value.


### GetLink

`func (o *SteamNews) GetLink() string`

GetLink returns the Link field if non-nil, zero value otherwise.

### GetLinkOk

`func (o *SteamNews) GetLinkOk() (*string, bool)`

GetLinkOk returns a tuple with the Link field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLink

`func (o *SteamNews) SetLink(v string)`

SetLink sets Link field to given value.


### GetPubDate

`func (o *SteamNews) GetPubDate() time.Time`

GetPubDate returns the PubDate field if non-nil, zero value otherwise.

### GetPubDateOk

`func (o *SteamNews) GetPubDateOk() (*time.Time, bool)`

GetPubDateOk returns a tuple with the PubDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPubDate

`func (o *SteamNews) SetPubDate(v time.Time)`

SetPubDate sets PubDate field to given value.


### GetTitle

`func (o *SteamNews) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *SteamNews) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *SteamNews) SetTitle(v string)`

SetTitle sets Title field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


