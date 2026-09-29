# BreakablePowerupLootParams

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LootListDeckSize** | Pointer to **NullableInt64** |  | [optional] 
**PickupsByMatchTimeMins** | **map[string]map[string]float64** | Match time in minutes (string key) from which a loot table applies, mapped to &#x60;{pickup_name: relative weight}&#x60;. | 

## Methods

### NewBreakablePowerupLootParams

`func NewBreakablePowerupLootParams(pickupsByMatchTimeMins map[string]map[string]float64, ) *BreakablePowerupLootParams`

NewBreakablePowerupLootParams instantiates a new BreakablePowerupLootParams object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBreakablePowerupLootParamsWithDefaults

`func NewBreakablePowerupLootParamsWithDefaults() *BreakablePowerupLootParams`

NewBreakablePowerupLootParamsWithDefaults instantiates a new BreakablePowerupLootParams object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLootListDeckSize

`func (o *BreakablePowerupLootParams) GetLootListDeckSize() int64`

GetLootListDeckSize returns the LootListDeckSize field if non-nil, zero value otherwise.

### GetLootListDeckSizeOk

`func (o *BreakablePowerupLootParams) GetLootListDeckSizeOk() (*int64, bool)`

GetLootListDeckSizeOk returns a tuple with the LootListDeckSize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLootListDeckSize

`func (o *BreakablePowerupLootParams) SetLootListDeckSize(v int64)`

SetLootListDeckSize sets LootListDeckSize field to given value.

### HasLootListDeckSize

`func (o *BreakablePowerupLootParams) HasLootListDeckSize() bool`

HasLootListDeckSize returns a boolean if a field has been set.

### SetLootListDeckSizeNil

`func (o *BreakablePowerupLootParams) SetLootListDeckSizeNil(b bool)`

 SetLootListDeckSizeNil sets the value for LootListDeckSize to be an explicit nil

### UnsetLootListDeckSize
`func (o *BreakablePowerupLootParams) UnsetLootListDeckSize()`

UnsetLootListDeckSize ensures that no value is present for LootListDeckSize, not even an explicit nil
### GetPickupsByMatchTimeMins

`func (o *BreakablePowerupLootParams) GetPickupsByMatchTimeMins() map[string]map[string]float64`

GetPickupsByMatchTimeMins returns the PickupsByMatchTimeMins field if non-nil, zero value otherwise.

### GetPickupsByMatchTimeMinsOk

`func (o *BreakablePowerupLootParams) GetPickupsByMatchTimeMinsOk() (*map[string]map[string]float64, bool)`

GetPickupsByMatchTimeMinsOk returns a tuple with the PickupsByMatchTimeMins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPickupsByMatchTimeMins

`func (o *BreakablePowerupLootParams) SetPickupsByMatchTimeMins(v map[string]map[string]float64)`

SetPickupsByMatchTimeMins sets PickupsByMatchTimeMins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


