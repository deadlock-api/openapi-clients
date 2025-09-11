# BadgeDistribution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**BadgeLevel** | **int32** | The badge level. See more: &lt;https://assets.deadlock-api.com/v2/ranks&gt; | 
**TotalMatches** | **int64** | The total number of matches. | 

## Methods

### NewBadgeDistribution

`func NewBadgeDistribution(badgeLevel int32, totalMatches int64, ) *BadgeDistribution`

NewBadgeDistribution instantiates a new BadgeDistribution object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBadgeDistributionWithDefaults

`func NewBadgeDistributionWithDefaults() *BadgeDistribution`

NewBadgeDistributionWithDefaults instantiates a new BadgeDistribution object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetBadgeLevel

`func (o *BadgeDistribution) GetBadgeLevel() int32`

GetBadgeLevel returns the BadgeLevel field if non-nil, zero value otherwise.

### GetBadgeLevelOk

`func (o *BadgeDistribution) GetBadgeLevelOk() (*int32, bool)`

GetBadgeLevelOk returns a tuple with the BadgeLevel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBadgeLevel

`func (o *BadgeDistribution) SetBadgeLevel(v int32)`

SetBadgeLevel sets BadgeLevel field to given value.


### GetTotalMatches

`func (o *BadgeDistribution) GetTotalMatches() int64`

GetTotalMatches returns the TotalMatches field if non-nil, zero value otherwise.

### GetTotalMatchesOk

`func (o *BadgeDistribution) GetTotalMatchesOk() (*int64, bool)`

GetTotalMatchesOk returns a tuple with the TotalMatches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalMatches

`func (o *BadgeDistribution) SetTotalMatches(v int64)`

SetTotalMatches sets TotalMatches field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


