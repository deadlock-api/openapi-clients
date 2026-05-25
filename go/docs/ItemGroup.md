# ItemGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ShopGroup** | **string** |  | 
**Upgrades** | **[]string** |  | 

## Methods

### NewItemGroup

`func NewItemGroup(shopGroup string, upgrades []string, ) *ItemGroup`

NewItemGroup instantiates a new ItemGroup object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewItemGroupWithDefaults

`func NewItemGroupWithDefaults() *ItemGroup`

NewItemGroupWithDefaults instantiates a new ItemGroup object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetShopGroup

`func (o *ItemGroup) GetShopGroup() string`

GetShopGroup returns the ShopGroup field if non-nil, zero value otherwise.

### GetShopGroupOk

`func (o *ItemGroup) GetShopGroupOk() (*string, bool)`

GetShopGroupOk returns a tuple with the ShopGroup field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShopGroup

`func (o *ItemGroup) SetShopGroup(v string)`

SetShopGroup sets ShopGroup field to given value.


### GetUpgrades

`func (o *ItemGroup) GetUpgrades() []string`

GetUpgrades returns the Upgrades field if non-nil, zero value otherwise.

### GetUpgradesOk

`func (o *ItemGroup) GetUpgradesOk() (*[]string, bool)`

GetUpgradesOk returns a tuple with the Upgrades field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpgrades

`func (o *ItemGroup) SetUpgrades(v []string)`

SetUpgrades sets Upgrades field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


