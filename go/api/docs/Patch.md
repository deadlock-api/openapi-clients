# Patch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Author** | **string** |  | 
**Category** | [**PatchCategory**](PatchCategory.md) |  | 
**ContentEncoded** | **string** |  | 
**DcCreator** | **string** |  | 
**Guid** | [**PatchGuid**](PatchGuid.md) |  | 
**Link** | **string** |  | 
**PubDate** | **time.Time** |  | 
**SlashComments** | **string** |  | 
**Title** | **string** |  | 

## Methods

### NewPatch

`func NewPatch(author string, category PatchCategory, contentEncoded string, dcCreator string, guid PatchGuid, link string, pubDate time.Time, slashComments string, title string, ) *Patch`

NewPatch instantiates a new Patch object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPatchWithDefaults

`func NewPatchWithDefaults() *Patch`

NewPatchWithDefaults instantiates a new Patch object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuthor

`func (o *Patch) GetAuthor() string`

GetAuthor returns the Author field if non-nil, zero value otherwise.

### GetAuthorOk

`func (o *Patch) GetAuthorOk() (*string, bool)`

GetAuthorOk returns a tuple with the Author field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthor

`func (o *Patch) SetAuthor(v string)`

SetAuthor sets Author field to given value.


### GetCategory

`func (o *Patch) GetCategory() PatchCategory`

GetCategory returns the Category field if non-nil, zero value otherwise.

### GetCategoryOk

`func (o *Patch) GetCategoryOk() (*PatchCategory, bool)`

GetCategoryOk returns a tuple with the Category field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCategory

`func (o *Patch) SetCategory(v PatchCategory)`

SetCategory sets Category field to given value.


### GetContentEncoded

`func (o *Patch) GetContentEncoded() string`

GetContentEncoded returns the ContentEncoded field if non-nil, zero value otherwise.

### GetContentEncodedOk

`func (o *Patch) GetContentEncodedOk() (*string, bool)`

GetContentEncodedOk returns a tuple with the ContentEncoded field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentEncoded

`func (o *Patch) SetContentEncoded(v string)`

SetContentEncoded sets ContentEncoded field to given value.


### GetDcCreator

`func (o *Patch) GetDcCreator() string`

GetDcCreator returns the DcCreator field if non-nil, zero value otherwise.

### GetDcCreatorOk

`func (o *Patch) GetDcCreatorOk() (*string, bool)`

GetDcCreatorOk returns a tuple with the DcCreator field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDcCreator

`func (o *Patch) SetDcCreator(v string)`

SetDcCreator sets DcCreator field to given value.


### GetGuid

`func (o *Patch) GetGuid() PatchGuid`

GetGuid returns the Guid field if non-nil, zero value otherwise.

### GetGuidOk

`func (o *Patch) GetGuidOk() (*PatchGuid, bool)`

GetGuidOk returns a tuple with the Guid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGuid

`func (o *Patch) SetGuid(v PatchGuid)`

SetGuid sets Guid field to given value.


### GetLink

`func (o *Patch) GetLink() string`

GetLink returns the Link field if non-nil, zero value otherwise.

### GetLinkOk

`func (o *Patch) GetLinkOk() (*string, bool)`

GetLinkOk returns a tuple with the Link field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLink

`func (o *Patch) SetLink(v string)`

SetLink sets Link field to given value.


### GetPubDate

`func (o *Patch) GetPubDate() time.Time`

GetPubDate returns the PubDate field if non-nil, zero value otherwise.

### GetPubDateOk

`func (o *Patch) GetPubDateOk() (*time.Time, bool)`

GetPubDateOk returns a tuple with the PubDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPubDate

`func (o *Patch) SetPubDate(v time.Time)`

SetPubDate sets PubDate field to given value.


### GetSlashComments

`func (o *Patch) GetSlashComments() string`

GetSlashComments returns the SlashComments field if non-nil, zero value otherwise.

### GetSlashCommentsOk

`func (o *Patch) GetSlashCommentsOk() (*string, bool)`

GetSlashCommentsOk returns a tuple with the SlashComments field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlashComments

`func (o *Patch) SetSlashComments(v string)`

SetSlashComments sets SlashComments field to given value.


### GetTitle

`func (o *Patch) GetTitle() string`

GetTitle returns the Title field if non-nil, zero value otherwise.

### GetTitleOk

`func (o *Patch) GetTitleOk() (*string, bool)`

GetTitleOk returns a tuple with the Title field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTitle

`func (o *Patch) SetTitle(v string)`

SetTitle sets Title field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


