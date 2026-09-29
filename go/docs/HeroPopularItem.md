# HeroPopularItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClassName** | **string** |  | 
**ItemId** | **int32** | Item id, derived from &#x60;class_name&#x60; like &#x60;/v2/items&#x60; ids. | 
**PickPct** | **float64** | Pick rate in percent (0-100). | 
**WinratePct** | **float64** | Win rate in percent (0-100). | 

## Methods

### NewHeroPopularItem

`func NewHeroPopularItem(className string, itemId int32, pickPct float64, winratePct float64, ) *HeroPopularItem`

NewHeroPopularItem instantiates a new HeroPopularItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewHeroPopularItemWithDefaults

`func NewHeroPopularItemWithDefaults() *HeroPopularItem`

NewHeroPopularItemWithDefaults instantiates a new HeroPopularItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClassName

`func (o *HeroPopularItem) GetClassName() string`

GetClassName returns the ClassName field if non-nil, zero value otherwise.

### GetClassNameOk

`func (o *HeroPopularItem) GetClassNameOk() (*string, bool)`

GetClassNameOk returns a tuple with the ClassName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassName

`func (o *HeroPopularItem) SetClassName(v string)`

SetClassName sets ClassName field to given value.


### GetItemId

`func (o *HeroPopularItem) GetItemId() int32`

GetItemId returns the ItemId field if non-nil, zero value otherwise.

### GetItemIdOk

`func (o *HeroPopularItem) GetItemIdOk() (*int32, bool)`

GetItemIdOk returns a tuple with the ItemId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemId

`func (o *HeroPopularItem) SetItemId(v int32)`

SetItemId sets ItemId field to given value.


### GetPickPct

`func (o *HeroPopularItem) GetPickPct() float64`

GetPickPct returns the PickPct field if non-nil, zero value otherwise.

### GetPickPctOk

`func (o *HeroPopularItem) GetPickPctOk() (*float64, bool)`

GetPickPctOk returns a tuple with the PickPct field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPickPct

`func (o *HeroPopularItem) SetPickPct(v float64)`

SetPickPct sets PickPct field to given value.


### GetWinratePct

`func (o *HeroPopularItem) GetWinratePct() float64`

GetWinratePct returns the WinratePct field if non-nil, zero value otherwise.

### GetWinratePctOk

`func (o *HeroPopularItem) GetWinratePctOk() (*float64, bool)`

GetWinratePctOk returns a tuple with the WinratePct field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWinratePct

`func (o *HeroPopularItem) SetWinratePct(v float64)`

SetWinratePct sets WinratePct field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


