# ItemDraftsValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Bucket** | Pointer to [**NullableDraftBucket**](DraftBucket.md) |  | [optional] 
**Name** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewItemDraftsValue

`func NewItemDraftsValue() *ItemDraftsValue`

NewItemDraftsValue instantiates a new ItemDraftsValue object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewItemDraftsValueWithDefaults

`func NewItemDraftsValueWithDefaults() *ItemDraftsValue`

NewItemDraftsValueWithDefaults instantiates a new ItemDraftsValue object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBucket

`func (o *ItemDraftsValue) GetBucket() DraftBucket`

GetBucket returns the Bucket field if non-nil, zero value otherwise.

### GetBucketOk

`func (o *ItemDraftsValue) GetBucketOk() (*DraftBucket, bool)`

GetBucketOk returns a tuple with the Bucket field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBucket

`func (o *ItemDraftsValue) SetBucket(v DraftBucket)`

SetBucket sets Bucket field to given value.

### HasBucket

`func (o *ItemDraftsValue) HasBucket() bool`

HasBucket returns a boolean if a field has been set.

### SetBucketNil

`func (o *ItemDraftsValue) SetBucketNil(b bool)`

 SetBucketNil sets the value for Bucket to be an explicit nil

### UnsetBucket
`func (o *ItemDraftsValue) UnsetBucket()`

UnsetBucket ensures that no value is present for Bucket, not even an explicit nil
### GetName

`func (o *ItemDraftsValue) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ItemDraftsValue) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ItemDraftsValue) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *ItemDraftsValue) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *ItemDraftsValue) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *ItemDraftsValue) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


