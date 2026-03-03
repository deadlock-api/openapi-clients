# DraftBuckets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Bucket** | Pointer to [**NullableDraftBucket**](DraftBucket.md) |  | [optional] 
**Name** | Pointer to **NullableString** |  | [optional] 

## Methods

### NewDraftBuckets

`func NewDraftBuckets() *DraftBuckets`

NewDraftBuckets instantiates a new DraftBuckets object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDraftBucketsWithDefaults

`func NewDraftBucketsWithDefaults() *DraftBuckets`

NewDraftBucketsWithDefaults instantiates a new DraftBuckets object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBucket

`func (o *DraftBuckets) GetBucket() DraftBucket`

GetBucket returns the Bucket field if non-nil, zero value otherwise.

### GetBucketOk

`func (o *DraftBuckets) GetBucketOk() (*DraftBucket, bool)`

GetBucketOk returns a tuple with the Bucket field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBucket

`func (o *DraftBuckets) SetBucket(v DraftBucket)`

SetBucket sets Bucket field to given value.

### HasBucket

`func (o *DraftBuckets) HasBucket() bool`

HasBucket returns a boolean if a field has been set.

### SetBucketNil

`func (o *DraftBuckets) SetBucketNil(b bool)`

 SetBucketNil sets the value for Bucket to be an explicit nil

### UnsetBucket
`func (o *DraftBuckets) UnsetBucket()`

UnsetBucket ensures that no value is present for Bucket, not even an explicit nil
### GetName

`func (o *DraftBuckets) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *DraftBuckets) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *DraftBuckets) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *DraftBuckets) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *DraftBuckets) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *DraftBuckets) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


