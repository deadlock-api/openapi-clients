# AnalyticsBuffStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AvgFirstPickupTimeS** | Pointer to **NullableFloat64** | Average game time (seconds) of a player&#39;s first pickup of this buff type, over player-matches with timings, &#x60;null&#x60; without any. | [optional] 
**AvgPickupTimeS** | Pointer to **NullableFloat64** | Average game time (seconds) of the &#x60;timed_pickups&#x60;, &#x60;null&#x60; without any. | [optional] 
**BuffType** | **string** | Buff type, e.g. &#x60;hp_permanent_pickup_lv2&#x60;. Display names, units and colors: &lt;https://api.deadlock-api.com/v1/assets/misc-entities&gt; (&#x60;buff_type_name&#x60;). | 
**IsPermanent** | **bool** | Whether the buff is permanent. Temporary power-ups never carry pickup timings. | 
**Matches** | **int64** | Player-matches matching the filters (the same for every buff type). Average pickups per match: &#x60;pickups / matches&#x60;. | 
**MatchesWithPickup** | **int64** | Player-matches with at least one pickup of this buff type. | 
**Pickups** | **int64** | Total pickups of this buff type. | 
**TimedMatches** | **int64** | Player-matches matching the filters that record pickup timings (the same for every buff type): matches since build 6712 (2026-09-29) with at least one timed permanent pickup. Average stat gained per match: &#x60;total_stat_value / timed_matches&#x60;. | 
**TimedPickups** | **int64** | Pickups of this buff type with a recorded game time and stat value (build 6712+). | 
**TotalStatValue** | **float64** | Sum of the stat values granted by the &#x60;timed_pickups&#x60;, in the buff type&#39;s unit (&#x60;buff_type_value_unit&#x60; in the assets). | 

## Methods

### NewAnalyticsBuffStats

`func NewAnalyticsBuffStats(buffType string, isPermanent bool, matches int64, matchesWithPickup int64, pickups int64, timedMatches int64, timedPickups int64, totalStatValue float64, ) *AnalyticsBuffStats`

NewAnalyticsBuffStats instantiates a new AnalyticsBuffStats object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAnalyticsBuffStatsWithDefaults

`func NewAnalyticsBuffStatsWithDefaults() *AnalyticsBuffStats`

NewAnalyticsBuffStatsWithDefaults instantiates a new AnalyticsBuffStats object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAvgFirstPickupTimeS

`func (o *AnalyticsBuffStats) GetAvgFirstPickupTimeS() float64`

GetAvgFirstPickupTimeS returns the AvgFirstPickupTimeS field if non-nil, zero value otherwise.

### GetAvgFirstPickupTimeSOk

`func (o *AnalyticsBuffStats) GetAvgFirstPickupTimeSOk() (*float64, bool)`

GetAvgFirstPickupTimeSOk returns a tuple with the AvgFirstPickupTimeS field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgFirstPickupTimeS

`func (o *AnalyticsBuffStats) SetAvgFirstPickupTimeS(v float64)`

SetAvgFirstPickupTimeS sets AvgFirstPickupTimeS field to given value.

### HasAvgFirstPickupTimeS

`func (o *AnalyticsBuffStats) HasAvgFirstPickupTimeS() bool`

HasAvgFirstPickupTimeS returns a boolean if a field has been set.

### SetAvgFirstPickupTimeSNil

`func (o *AnalyticsBuffStats) SetAvgFirstPickupTimeSNil(b bool)`

 SetAvgFirstPickupTimeSNil sets the value for AvgFirstPickupTimeS to be an explicit nil

### UnsetAvgFirstPickupTimeS
`func (o *AnalyticsBuffStats) UnsetAvgFirstPickupTimeS()`

UnsetAvgFirstPickupTimeS ensures that no value is present for AvgFirstPickupTimeS, not even an explicit nil
### GetAvgPickupTimeS

`func (o *AnalyticsBuffStats) GetAvgPickupTimeS() float64`

GetAvgPickupTimeS returns the AvgPickupTimeS field if non-nil, zero value otherwise.

### GetAvgPickupTimeSOk

`func (o *AnalyticsBuffStats) GetAvgPickupTimeSOk() (*float64, bool)`

GetAvgPickupTimeSOk returns a tuple with the AvgPickupTimeS field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgPickupTimeS

`func (o *AnalyticsBuffStats) SetAvgPickupTimeS(v float64)`

SetAvgPickupTimeS sets AvgPickupTimeS field to given value.

### HasAvgPickupTimeS

`func (o *AnalyticsBuffStats) HasAvgPickupTimeS() bool`

HasAvgPickupTimeS returns a boolean if a field has been set.

### SetAvgPickupTimeSNil

`func (o *AnalyticsBuffStats) SetAvgPickupTimeSNil(b bool)`

 SetAvgPickupTimeSNil sets the value for AvgPickupTimeS to be an explicit nil

### UnsetAvgPickupTimeS
`func (o *AnalyticsBuffStats) UnsetAvgPickupTimeS()`

UnsetAvgPickupTimeS ensures that no value is present for AvgPickupTimeS, not even an explicit nil
### GetBuffType

`func (o *AnalyticsBuffStats) GetBuffType() string`

GetBuffType returns the BuffType field if non-nil, zero value otherwise.

### GetBuffTypeOk

`func (o *AnalyticsBuffStats) GetBuffTypeOk() (*string, bool)`

GetBuffTypeOk returns a tuple with the BuffType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuffType

`func (o *AnalyticsBuffStats) SetBuffType(v string)`

SetBuffType sets BuffType field to given value.


### GetIsPermanent

`func (o *AnalyticsBuffStats) GetIsPermanent() bool`

GetIsPermanent returns the IsPermanent field if non-nil, zero value otherwise.

### GetIsPermanentOk

`func (o *AnalyticsBuffStats) GetIsPermanentOk() (*bool, bool)`

GetIsPermanentOk returns a tuple with the IsPermanent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsPermanent

`func (o *AnalyticsBuffStats) SetIsPermanent(v bool)`

SetIsPermanent sets IsPermanent field to given value.


### GetMatches

`func (o *AnalyticsBuffStats) GetMatches() int64`

GetMatches returns the Matches field if non-nil, zero value otherwise.

### GetMatchesOk

`func (o *AnalyticsBuffStats) GetMatchesOk() (*int64, bool)`

GetMatchesOk returns a tuple with the Matches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatches

`func (o *AnalyticsBuffStats) SetMatches(v int64)`

SetMatches sets Matches field to given value.


### GetMatchesWithPickup

`func (o *AnalyticsBuffStats) GetMatchesWithPickup() int64`

GetMatchesWithPickup returns the MatchesWithPickup field if non-nil, zero value otherwise.

### GetMatchesWithPickupOk

`func (o *AnalyticsBuffStats) GetMatchesWithPickupOk() (*int64, bool)`

GetMatchesWithPickupOk returns a tuple with the MatchesWithPickup field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchesWithPickup

`func (o *AnalyticsBuffStats) SetMatchesWithPickup(v int64)`

SetMatchesWithPickup sets MatchesWithPickup field to given value.


### GetPickups

`func (o *AnalyticsBuffStats) GetPickups() int64`

GetPickups returns the Pickups field if non-nil, zero value otherwise.

### GetPickupsOk

`func (o *AnalyticsBuffStats) GetPickupsOk() (*int64, bool)`

GetPickupsOk returns a tuple with the Pickups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPickups

`func (o *AnalyticsBuffStats) SetPickups(v int64)`

SetPickups sets Pickups field to given value.


### GetTimedMatches

`func (o *AnalyticsBuffStats) GetTimedMatches() int64`

GetTimedMatches returns the TimedMatches field if non-nil, zero value otherwise.

### GetTimedMatchesOk

`func (o *AnalyticsBuffStats) GetTimedMatchesOk() (*int64, bool)`

GetTimedMatchesOk returns a tuple with the TimedMatches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimedMatches

`func (o *AnalyticsBuffStats) SetTimedMatches(v int64)`

SetTimedMatches sets TimedMatches field to given value.


### GetTimedPickups

`func (o *AnalyticsBuffStats) GetTimedPickups() int64`

GetTimedPickups returns the TimedPickups field if non-nil, zero value otherwise.

### GetTimedPickupsOk

`func (o *AnalyticsBuffStats) GetTimedPickupsOk() (*int64, bool)`

GetTimedPickupsOk returns a tuple with the TimedPickups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimedPickups

`func (o *AnalyticsBuffStats) SetTimedPickups(v int64)`

SetTimedPickups sets TimedPickups field to given value.


### GetTotalStatValue

`func (o *AnalyticsBuffStats) GetTotalStatValue() float64`

GetTotalStatValue returns the TotalStatValue field if non-nil, zero value otherwise.

### GetTotalStatValueOk

`func (o *AnalyticsBuffStats) GetTotalStatValueOk() (*float64, bool)`

GetTotalStatValueOk returns a tuple with the TotalStatValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalStatValue

`func (o *AnalyticsBuffStats) SetTotalStatValue(v float64)`

SetTotalStatValue sets TotalStatValue field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


