# MapDistrict

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Building** | Pointer to **NullableString** | Localization token, e.g. &#x60;map_district_building_docks&#x60;. Absent for districts without buildings. | [optional] 
**BuildingName** | Pointer to **NullableString** | Localized building name, e.g. &#x60;Docks&#x60;. | [optional] 
**District** | **string** | Localization token, e.g. &#x60;map_district_theater&#x60;. | 
**DistrictName** | **string** | Localized district name, e.g. &#x60;Theater&#x60;. | 

## Methods

### NewMapDistrict

`func NewMapDistrict(district string, districtName string, ) *MapDistrict`

NewMapDistrict instantiates a new MapDistrict object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMapDistrictWithDefaults

`func NewMapDistrictWithDefaults() *MapDistrict`

NewMapDistrictWithDefaults instantiates a new MapDistrict object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBuilding

`func (o *MapDistrict) GetBuilding() string`

GetBuilding returns the Building field if non-nil, zero value otherwise.

### GetBuildingOk

`func (o *MapDistrict) GetBuildingOk() (*string, bool)`

GetBuildingOk returns a tuple with the Building field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuilding

`func (o *MapDistrict) SetBuilding(v string)`

SetBuilding sets Building field to given value.

### HasBuilding

`func (o *MapDistrict) HasBuilding() bool`

HasBuilding returns a boolean if a field has been set.

### SetBuildingNil

`func (o *MapDistrict) SetBuildingNil(b bool)`

 SetBuildingNil sets the value for Building to be an explicit nil

### UnsetBuilding
`func (o *MapDistrict) UnsetBuilding()`

UnsetBuilding ensures that no value is present for Building, not even an explicit nil
### GetBuildingName

`func (o *MapDistrict) GetBuildingName() string`

GetBuildingName returns the BuildingName field if non-nil, zero value otherwise.

### GetBuildingNameOk

`func (o *MapDistrict) GetBuildingNameOk() (*string, bool)`

GetBuildingNameOk returns a tuple with the BuildingName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuildingName

`func (o *MapDistrict) SetBuildingName(v string)`

SetBuildingName sets BuildingName field to given value.

### HasBuildingName

`func (o *MapDistrict) HasBuildingName() bool`

HasBuildingName returns a boolean if a field has been set.

### SetBuildingNameNil

`func (o *MapDistrict) SetBuildingNameNil(b bool)`

 SetBuildingNameNil sets the value for BuildingName to be an explicit nil

### UnsetBuildingName
`func (o *MapDistrict) UnsetBuildingName()`

UnsetBuildingName ensures that no value is present for BuildingName, not even an explicit nil
### GetDistrict

`func (o *MapDistrict) GetDistrict() string`

GetDistrict returns the District field if non-nil, zero value otherwise.

### GetDistrictOk

`func (o *MapDistrict) GetDistrictOk() (*string, bool)`

GetDistrictOk returns a tuple with the District field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDistrict

`func (o *MapDistrict) SetDistrict(v string)`

SetDistrict sets District field to given value.


### GetDistrictName

`func (o *MapDistrict) GetDistrictName() string`

GetDistrictName returns the DistrictName field if non-nil, zero value otherwise.

### GetDistrictNameOk

`func (o *MapDistrict) GetDistrictNameOk() (*string, bool)`

GetDistrictNameOk returns a tuple with the DistrictName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDistrictName

`func (o *MapDistrict) SetDistrictName(v string)`

SetDistrictName sets DistrictName field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


