# PlayerPerformanceCurvePoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AssistsAvg** | **float64** | Average assists at this time point | 
**AssistsStd** | **float64** | Standard deviation of assists at this time point | 
**DeathsAvg** | **float64** | Average deaths at this time point | 
**DeathsStd** | **float64** | Standard deviation of deaths at this time point | 
**GameTime** | **int32** | The time point of the data. If &#x60;resolution&#x60; (default 10) is &gt; 0, this is a percentage (0, 10, ..., 100). If &#x60;resolution&#x60; is 0, this is the match time in seconds. | 
**GoldBossAvg** | **float64** | Average souls earned from objectives at this time point | 
**GoldBossOrbAvg** | **float64** | Average souls earned from secured objective orbs at this time point | 
**GoldDeathLossAvg** | **float64** | Average souls lost on death at this time point | 
**GoldDeniedAvg** | **float64** | Average souls denied to enemies at this time point | 
**GoldLaneCreepAvg** | **float64** | Average souls earned from lane creeps at this time point | 
**GoldLaneCreepOrbsAvg** | **float64** | Average souls earned from secured lane-creep orbs at this time point | 
**GoldNeutralCreepAvg** | **float64** | Average souls earned from neutral (jungle) creeps at this time point | 
**GoldNeutralCreepOrbsAvg** | **float64** | Average souls earned from secured neutral-creep orbs at this time point | 
**GoldPlayerAvg** | **float64** | Average souls earned from hero kills at this time point | 
**GoldPlayerOrbsAvg** | **float64** | Average souls earned from secured hero-kill orbs at this time point | 
**GoldTreasureAvg** | **float64** | Average souls earned from the urn at this time point | 
**KillsAvg** | **float64** | Average kills at this time point | 
**KillsStd** | **float64** | Standard deviation of kills at this time point | 
**NetWorthAvg** | **float64** | Average net worth at this time point | 
**NetWorthStd** | **float64** | Standard deviation of net worth at this time point | 

## Methods

### NewPlayerPerformanceCurvePoint

`func NewPlayerPerformanceCurvePoint(assistsAvg float64, assistsStd float64, deathsAvg float64, deathsStd float64, gameTime int32, goldBossAvg float64, goldBossOrbAvg float64, goldDeathLossAvg float64, goldDeniedAvg float64, goldLaneCreepAvg float64, goldLaneCreepOrbsAvg float64, goldNeutralCreepAvg float64, goldNeutralCreepOrbsAvg float64, goldPlayerAvg float64, goldPlayerOrbsAvg float64, goldTreasureAvg float64, killsAvg float64, killsStd float64, netWorthAvg float64, netWorthStd float64, ) *PlayerPerformanceCurvePoint`

NewPlayerPerformanceCurvePoint instantiates a new PlayerPerformanceCurvePoint object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPlayerPerformanceCurvePointWithDefaults

`func NewPlayerPerformanceCurvePointWithDefaults() *PlayerPerformanceCurvePoint`

NewPlayerPerformanceCurvePointWithDefaults instantiates a new PlayerPerformanceCurvePoint object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAssistsAvg

`func (o *PlayerPerformanceCurvePoint) GetAssistsAvg() float64`

GetAssistsAvg returns the AssistsAvg field if non-nil, zero value otherwise.

### GetAssistsAvgOk

`func (o *PlayerPerformanceCurvePoint) GetAssistsAvgOk() (*float64, bool)`

GetAssistsAvgOk returns a tuple with the AssistsAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssistsAvg

`func (o *PlayerPerformanceCurvePoint) SetAssistsAvg(v float64)`

SetAssistsAvg sets AssistsAvg field to given value.


### GetAssistsStd

`func (o *PlayerPerformanceCurvePoint) GetAssistsStd() float64`

GetAssistsStd returns the AssistsStd field if non-nil, zero value otherwise.

### GetAssistsStdOk

`func (o *PlayerPerformanceCurvePoint) GetAssistsStdOk() (*float64, bool)`

GetAssistsStdOk returns a tuple with the AssistsStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssistsStd

`func (o *PlayerPerformanceCurvePoint) SetAssistsStd(v float64)`

SetAssistsStd sets AssistsStd field to given value.


### GetDeathsAvg

`func (o *PlayerPerformanceCurvePoint) GetDeathsAvg() float64`

GetDeathsAvg returns the DeathsAvg field if non-nil, zero value otherwise.

### GetDeathsAvgOk

`func (o *PlayerPerformanceCurvePoint) GetDeathsAvgOk() (*float64, bool)`

GetDeathsAvgOk returns a tuple with the DeathsAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeathsAvg

`func (o *PlayerPerformanceCurvePoint) SetDeathsAvg(v float64)`

SetDeathsAvg sets DeathsAvg field to given value.


### GetDeathsStd

`func (o *PlayerPerformanceCurvePoint) GetDeathsStd() float64`

GetDeathsStd returns the DeathsStd field if non-nil, zero value otherwise.

### GetDeathsStdOk

`func (o *PlayerPerformanceCurvePoint) GetDeathsStdOk() (*float64, bool)`

GetDeathsStdOk returns a tuple with the DeathsStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeathsStd

`func (o *PlayerPerformanceCurvePoint) SetDeathsStd(v float64)`

SetDeathsStd sets DeathsStd field to given value.


### GetGameTime

`func (o *PlayerPerformanceCurvePoint) GetGameTime() int32`

GetGameTime returns the GameTime field if non-nil, zero value otherwise.

### GetGameTimeOk

`func (o *PlayerPerformanceCurvePoint) GetGameTimeOk() (*int32, bool)`

GetGameTimeOk returns a tuple with the GameTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGameTime

`func (o *PlayerPerformanceCurvePoint) SetGameTime(v int32)`

SetGameTime sets GameTime field to given value.


### GetGoldBossAvg

`func (o *PlayerPerformanceCurvePoint) GetGoldBossAvg() float64`

GetGoldBossAvg returns the GoldBossAvg field if non-nil, zero value otherwise.

### GetGoldBossAvgOk

`func (o *PlayerPerformanceCurvePoint) GetGoldBossAvgOk() (*float64, bool)`

GetGoldBossAvgOk returns a tuple with the GoldBossAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldBossAvg

`func (o *PlayerPerformanceCurvePoint) SetGoldBossAvg(v float64)`

SetGoldBossAvg sets GoldBossAvg field to given value.


### GetGoldBossOrbAvg

`func (o *PlayerPerformanceCurvePoint) GetGoldBossOrbAvg() float64`

GetGoldBossOrbAvg returns the GoldBossOrbAvg field if non-nil, zero value otherwise.

### GetGoldBossOrbAvgOk

`func (o *PlayerPerformanceCurvePoint) GetGoldBossOrbAvgOk() (*float64, bool)`

GetGoldBossOrbAvgOk returns a tuple with the GoldBossOrbAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldBossOrbAvg

`func (o *PlayerPerformanceCurvePoint) SetGoldBossOrbAvg(v float64)`

SetGoldBossOrbAvg sets GoldBossOrbAvg field to given value.


### GetGoldDeathLossAvg

`func (o *PlayerPerformanceCurvePoint) GetGoldDeathLossAvg() float64`

GetGoldDeathLossAvg returns the GoldDeathLossAvg field if non-nil, zero value otherwise.

### GetGoldDeathLossAvgOk

`func (o *PlayerPerformanceCurvePoint) GetGoldDeathLossAvgOk() (*float64, bool)`

GetGoldDeathLossAvgOk returns a tuple with the GoldDeathLossAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldDeathLossAvg

`func (o *PlayerPerformanceCurvePoint) SetGoldDeathLossAvg(v float64)`

SetGoldDeathLossAvg sets GoldDeathLossAvg field to given value.


### GetGoldDeniedAvg

`func (o *PlayerPerformanceCurvePoint) GetGoldDeniedAvg() float64`

GetGoldDeniedAvg returns the GoldDeniedAvg field if non-nil, zero value otherwise.

### GetGoldDeniedAvgOk

`func (o *PlayerPerformanceCurvePoint) GetGoldDeniedAvgOk() (*float64, bool)`

GetGoldDeniedAvgOk returns a tuple with the GoldDeniedAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldDeniedAvg

`func (o *PlayerPerformanceCurvePoint) SetGoldDeniedAvg(v float64)`

SetGoldDeniedAvg sets GoldDeniedAvg field to given value.


### GetGoldLaneCreepAvg

`func (o *PlayerPerformanceCurvePoint) GetGoldLaneCreepAvg() float64`

GetGoldLaneCreepAvg returns the GoldLaneCreepAvg field if non-nil, zero value otherwise.

### GetGoldLaneCreepAvgOk

`func (o *PlayerPerformanceCurvePoint) GetGoldLaneCreepAvgOk() (*float64, bool)`

GetGoldLaneCreepAvgOk returns a tuple with the GoldLaneCreepAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldLaneCreepAvg

`func (o *PlayerPerformanceCurvePoint) SetGoldLaneCreepAvg(v float64)`

SetGoldLaneCreepAvg sets GoldLaneCreepAvg field to given value.


### GetGoldLaneCreepOrbsAvg

`func (o *PlayerPerformanceCurvePoint) GetGoldLaneCreepOrbsAvg() float64`

GetGoldLaneCreepOrbsAvg returns the GoldLaneCreepOrbsAvg field if non-nil, zero value otherwise.

### GetGoldLaneCreepOrbsAvgOk

`func (o *PlayerPerformanceCurvePoint) GetGoldLaneCreepOrbsAvgOk() (*float64, bool)`

GetGoldLaneCreepOrbsAvgOk returns a tuple with the GoldLaneCreepOrbsAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldLaneCreepOrbsAvg

`func (o *PlayerPerformanceCurvePoint) SetGoldLaneCreepOrbsAvg(v float64)`

SetGoldLaneCreepOrbsAvg sets GoldLaneCreepOrbsAvg field to given value.


### GetGoldNeutralCreepAvg

`func (o *PlayerPerformanceCurvePoint) GetGoldNeutralCreepAvg() float64`

GetGoldNeutralCreepAvg returns the GoldNeutralCreepAvg field if non-nil, zero value otherwise.

### GetGoldNeutralCreepAvgOk

`func (o *PlayerPerformanceCurvePoint) GetGoldNeutralCreepAvgOk() (*float64, bool)`

GetGoldNeutralCreepAvgOk returns a tuple with the GoldNeutralCreepAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldNeutralCreepAvg

`func (o *PlayerPerformanceCurvePoint) SetGoldNeutralCreepAvg(v float64)`

SetGoldNeutralCreepAvg sets GoldNeutralCreepAvg field to given value.


### GetGoldNeutralCreepOrbsAvg

`func (o *PlayerPerformanceCurvePoint) GetGoldNeutralCreepOrbsAvg() float64`

GetGoldNeutralCreepOrbsAvg returns the GoldNeutralCreepOrbsAvg field if non-nil, zero value otherwise.

### GetGoldNeutralCreepOrbsAvgOk

`func (o *PlayerPerformanceCurvePoint) GetGoldNeutralCreepOrbsAvgOk() (*float64, bool)`

GetGoldNeutralCreepOrbsAvgOk returns a tuple with the GoldNeutralCreepOrbsAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldNeutralCreepOrbsAvg

`func (o *PlayerPerformanceCurvePoint) SetGoldNeutralCreepOrbsAvg(v float64)`

SetGoldNeutralCreepOrbsAvg sets GoldNeutralCreepOrbsAvg field to given value.


### GetGoldPlayerAvg

`func (o *PlayerPerformanceCurvePoint) GetGoldPlayerAvg() float64`

GetGoldPlayerAvg returns the GoldPlayerAvg field if non-nil, zero value otherwise.

### GetGoldPlayerAvgOk

`func (o *PlayerPerformanceCurvePoint) GetGoldPlayerAvgOk() (*float64, bool)`

GetGoldPlayerAvgOk returns a tuple with the GoldPlayerAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldPlayerAvg

`func (o *PlayerPerformanceCurvePoint) SetGoldPlayerAvg(v float64)`

SetGoldPlayerAvg sets GoldPlayerAvg field to given value.


### GetGoldPlayerOrbsAvg

`func (o *PlayerPerformanceCurvePoint) GetGoldPlayerOrbsAvg() float64`

GetGoldPlayerOrbsAvg returns the GoldPlayerOrbsAvg field if non-nil, zero value otherwise.

### GetGoldPlayerOrbsAvgOk

`func (o *PlayerPerformanceCurvePoint) GetGoldPlayerOrbsAvgOk() (*float64, bool)`

GetGoldPlayerOrbsAvgOk returns a tuple with the GoldPlayerOrbsAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldPlayerOrbsAvg

`func (o *PlayerPerformanceCurvePoint) SetGoldPlayerOrbsAvg(v float64)`

SetGoldPlayerOrbsAvg sets GoldPlayerOrbsAvg field to given value.


### GetGoldTreasureAvg

`func (o *PlayerPerformanceCurvePoint) GetGoldTreasureAvg() float64`

GetGoldTreasureAvg returns the GoldTreasureAvg field if non-nil, zero value otherwise.

### GetGoldTreasureAvgOk

`func (o *PlayerPerformanceCurvePoint) GetGoldTreasureAvgOk() (*float64, bool)`

GetGoldTreasureAvgOk returns a tuple with the GoldTreasureAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldTreasureAvg

`func (o *PlayerPerformanceCurvePoint) SetGoldTreasureAvg(v float64)`

SetGoldTreasureAvg sets GoldTreasureAvg field to given value.


### GetKillsAvg

`func (o *PlayerPerformanceCurvePoint) GetKillsAvg() float64`

GetKillsAvg returns the KillsAvg field if non-nil, zero value otherwise.

### GetKillsAvgOk

`func (o *PlayerPerformanceCurvePoint) GetKillsAvgOk() (*float64, bool)`

GetKillsAvgOk returns a tuple with the KillsAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKillsAvg

`func (o *PlayerPerformanceCurvePoint) SetKillsAvg(v float64)`

SetKillsAvg sets KillsAvg field to given value.


### GetKillsStd

`func (o *PlayerPerformanceCurvePoint) GetKillsStd() float64`

GetKillsStd returns the KillsStd field if non-nil, zero value otherwise.

### GetKillsStdOk

`func (o *PlayerPerformanceCurvePoint) GetKillsStdOk() (*float64, bool)`

GetKillsStdOk returns a tuple with the KillsStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKillsStd

`func (o *PlayerPerformanceCurvePoint) SetKillsStd(v float64)`

SetKillsStd sets KillsStd field to given value.


### GetNetWorthAvg

`func (o *PlayerPerformanceCurvePoint) GetNetWorthAvg() float64`

GetNetWorthAvg returns the NetWorthAvg field if non-nil, zero value otherwise.

### GetNetWorthAvgOk

`func (o *PlayerPerformanceCurvePoint) GetNetWorthAvgOk() (*float64, bool)`

GetNetWorthAvgOk returns a tuple with the NetWorthAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetWorthAvg

`func (o *PlayerPerformanceCurvePoint) SetNetWorthAvg(v float64)`

SetNetWorthAvg sets NetWorthAvg field to given value.


### GetNetWorthStd

`func (o *PlayerPerformanceCurvePoint) GetNetWorthStd() float64`

GetNetWorthStd returns the NetWorthStd field if non-nil, zero value otherwise.

### GetNetWorthStdOk

`func (o *PlayerPerformanceCurvePoint) GetNetWorthStdOk() (*float64, bool)`

GetNetWorthStdOk returns a tuple with the NetWorthStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetWorthStd

`func (o *PlayerPerformanceCurvePoint) SetNetWorthStd(v float64)`

SetNetWorthStd sets NetWorthStd field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


