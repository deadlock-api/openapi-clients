# PlayerCardSlot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Hero** | Pointer to [**NullablePlayerCardSlotHero**](PlayerCardSlotHero.md) |  | [optional] 
**SlotId** | Pointer to **NullableInt32** |  | [optional] 
**Stat** | Pointer to [**NullablePlayerCardSlotStat**](PlayerCardSlotStat.md) |  | [optional] 

## Methods

### NewPlayerCardSlot

`func NewPlayerCardSlot() *PlayerCardSlot`

NewPlayerCardSlot instantiates a new PlayerCardSlot object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPlayerCardSlotWithDefaults

`func NewPlayerCardSlotWithDefaults() *PlayerCardSlot`

NewPlayerCardSlotWithDefaults instantiates a new PlayerCardSlot object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetHero

`func (o *PlayerCardSlot) GetHero() PlayerCardSlotHero`

GetHero returns the Hero field if non-nil, zero value otherwise.

### GetHeroOk

`func (o *PlayerCardSlot) GetHeroOk() (*PlayerCardSlotHero, bool)`

GetHeroOk returns a tuple with the Hero field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHero

`func (o *PlayerCardSlot) SetHero(v PlayerCardSlotHero)`

SetHero sets Hero field to given value.

### HasHero

`func (o *PlayerCardSlot) HasHero() bool`

HasHero returns a boolean if a field has been set.

### SetHeroNil

`func (o *PlayerCardSlot) SetHeroNil(b bool)`

 SetHeroNil sets the value for Hero to be an explicit nil

### UnsetHero
`func (o *PlayerCardSlot) UnsetHero()`

UnsetHero ensures that no value is present for Hero, not even an explicit nil
### GetSlotId

`func (o *PlayerCardSlot) GetSlotId() int32`

GetSlotId returns the SlotId field if non-nil, zero value otherwise.

### GetSlotIdOk

`func (o *PlayerCardSlot) GetSlotIdOk() (*int32, bool)`

GetSlotIdOk returns a tuple with the SlotId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSlotId

`func (o *PlayerCardSlot) SetSlotId(v int32)`

SetSlotId sets SlotId field to given value.

### HasSlotId

`func (o *PlayerCardSlot) HasSlotId() bool`

HasSlotId returns a boolean if a field has been set.

### SetSlotIdNil

`func (o *PlayerCardSlot) SetSlotIdNil(b bool)`

 SetSlotIdNil sets the value for SlotId to be an explicit nil

### UnsetSlotId
`func (o *PlayerCardSlot) UnsetSlotId()`

UnsetSlotId ensures that no value is present for SlotId, not even an explicit nil
### GetStat

`func (o *PlayerCardSlot) GetStat() PlayerCardSlotStat`

GetStat returns the Stat field if non-nil, zero value otherwise.

### GetStatOk

`func (o *PlayerCardSlot) GetStatOk() (*PlayerCardSlotStat, bool)`

GetStatOk returns a tuple with the Stat field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStat

`func (o *PlayerCardSlot) SetStat(v PlayerCardSlotStat)`

SetStat sets Stat field to given value.

### HasStat

`func (o *PlayerCardSlot) HasStat() bool`

HasStat returns a boolean if a field has been set.

### SetStatNil

`func (o *PlayerCardSlot) SetStatNil(b bool)`

 SetStatNil sets the value for Stat to be an explicit nil

### UnsetStat
`func (o *PlayerCardSlot) UnsetStat()`

UnsetStat ensures that no value is present for Stat, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


