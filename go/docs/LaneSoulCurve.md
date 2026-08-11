# LaneSoulCurve

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AssignedLane** | **int32** | The lane the matchup was played in, or &#x60;0&#x60; when &#x60;assigned_lane&#x60; was grouped away. See the &#x60;lane_info&#x60; array of &lt;https://api.deadlock-api.com/v1/assets/generic-data&gt;. | 
**EnemyHeroIds** | **[]int32** | The ascending hero id pair they laned against, or empty when grouped away. | 
**HeroIds** | **[]int32** | The ascending hero id pair that shared the lane, or empty when grouped away. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**MatchesPlayed** | **int64** | Lane matchups behind the row, counted at its *first* sample. This is what &#x60;min_matches&#x60; and &#x60;max_matches&#x60; filter on, so it does not move when the requested time range changes; read &#x60;sample_matches&#x60; for what any individual point rests on. | 
**NetWorthDiff** | **[]float64** | Mean souls the duo is ahead by at the matching entry of &#x60;sample_times_s&#x60;. Negative means behind. Same length as &#x60;sample_times_s&#x60;. | 
**NetWorthDiffStd** | **[]float64** | Population standard deviation of the lead across the counted matchups, at the matching entry of &#x60;sample_times_s&#x60;. Same length as &#x60;sample_times_s&#x60;.  Spread between individual games, not uncertainty about the mean: it stays wide however many matchups are counted, because lane outcomes genuinely differ that much. | 
**SampleMatches** | **[]int64** | How many lane matchups were still running at the matching entry of &#x60;sample_times_s&#x60;. Falls off towards the end of the curve as shorter matches drop out. | 
**SampleTimesS** | **[]int32** | Seconds into the match each entry of the curves was sampled at, ascending. | 
**Stats** | [**map[string]LaneStatCurve**](LaneStatCurve.md) | A curve per stat named in &#x60;stats&#x60;. Empty unless the parameter was set. | 

## Methods

### NewLaneSoulCurve

`func NewLaneSoulCurve(assignedLane int32, enemyHeroIds []int32, heroIds []int32, matchesPlayed int64, netWorthDiff []float64, netWorthDiffStd []float64, sampleMatches []int64, sampleTimesS []int32, stats map[string]LaneStatCurve, ) *LaneSoulCurve`

NewLaneSoulCurve instantiates a new LaneSoulCurve object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewLaneSoulCurveWithDefaults

`func NewLaneSoulCurveWithDefaults() *LaneSoulCurve`

NewLaneSoulCurveWithDefaults instantiates a new LaneSoulCurve object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAssignedLane

`func (o *LaneSoulCurve) GetAssignedLane() int32`

GetAssignedLane returns the AssignedLane field if non-nil, zero value otherwise.

### GetAssignedLaneOk

`func (o *LaneSoulCurve) GetAssignedLaneOk() (*int32, bool)`

GetAssignedLaneOk returns a tuple with the AssignedLane field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssignedLane

`func (o *LaneSoulCurve) SetAssignedLane(v int32)`

SetAssignedLane sets AssignedLane field to given value.


### GetEnemyHeroIds

`func (o *LaneSoulCurve) GetEnemyHeroIds() []int32`

GetEnemyHeroIds returns the EnemyHeroIds field if non-nil, zero value otherwise.

### GetEnemyHeroIdsOk

`func (o *LaneSoulCurve) GetEnemyHeroIdsOk() (*[]int32, bool)`

GetEnemyHeroIdsOk returns a tuple with the EnemyHeroIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyHeroIds

`func (o *LaneSoulCurve) SetEnemyHeroIds(v []int32)`

SetEnemyHeroIds sets EnemyHeroIds field to given value.


### GetHeroIds

`func (o *LaneSoulCurve) GetHeroIds() []int32`

GetHeroIds returns the HeroIds field if non-nil, zero value otherwise.

### GetHeroIdsOk

`func (o *LaneSoulCurve) GetHeroIdsOk() (*[]int32, bool)`

GetHeroIdsOk returns a tuple with the HeroIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroIds

`func (o *LaneSoulCurve) SetHeroIds(v []int32)`

SetHeroIds sets HeroIds field to given value.


### GetMatchesPlayed

`func (o *LaneSoulCurve) GetMatchesPlayed() int64`

GetMatchesPlayed returns the MatchesPlayed field if non-nil, zero value otherwise.

### GetMatchesPlayedOk

`func (o *LaneSoulCurve) GetMatchesPlayedOk() (*int64, bool)`

GetMatchesPlayedOk returns a tuple with the MatchesPlayed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatchesPlayed

`func (o *LaneSoulCurve) SetMatchesPlayed(v int64)`

SetMatchesPlayed sets MatchesPlayed field to given value.


### GetNetWorthDiff

`func (o *LaneSoulCurve) GetNetWorthDiff() []float64`

GetNetWorthDiff returns the NetWorthDiff field if non-nil, zero value otherwise.

### GetNetWorthDiffOk

`func (o *LaneSoulCurve) GetNetWorthDiffOk() (*[]float64, bool)`

GetNetWorthDiffOk returns a tuple with the NetWorthDiff field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetWorthDiff

`func (o *LaneSoulCurve) SetNetWorthDiff(v []float64)`

SetNetWorthDiff sets NetWorthDiff field to given value.


### GetNetWorthDiffStd

`func (o *LaneSoulCurve) GetNetWorthDiffStd() []float64`

GetNetWorthDiffStd returns the NetWorthDiffStd field if non-nil, zero value otherwise.

### GetNetWorthDiffStdOk

`func (o *LaneSoulCurve) GetNetWorthDiffStdOk() (*[]float64, bool)`

GetNetWorthDiffStdOk returns a tuple with the NetWorthDiffStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNetWorthDiffStd

`func (o *LaneSoulCurve) SetNetWorthDiffStd(v []float64)`

SetNetWorthDiffStd sets NetWorthDiffStd field to given value.


### GetSampleMatches

`func (o *LaneSoulCurve) GetSampleMatches() []int64`

GetSampleMatches returns the SampleMatches field if non-nil, zero value otherwise.

### GetSampleMatchesOk

`func (o *LaneSoulCurve) GetSampleMatchesOk() (*[]int64, bool)`

GetSampleMatchesOk returns a tuple with the SampleMatches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSampleMatches

`func (o *LaneSoulCurve) SetSampleMatches(v []int64)`

SetSampleMatches sets SampleMatches field to given value.


### GetSampleTimesS

`func (o *LaneSoulCurve) GetSampleTimesS() []int32`

GetSampleTimesS returns the SampleTimesS field if non-nil, zero value otherwise.

### GetSampleTimesSOk

`func (o *LaneSoulCurve) GetSampleTimesSOk() (*[]int32, bool)`

GetSampleTimesSOk returns a tuple with the SampleTimesS field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSampleTimesS

`func (o *LaneSoulCurve) SetSampleTimesS(v []int32)`

SetSampleTimesS sets SampleTimesS field to given value.


### GetStats

`func (o *LaneSoulCurve) GetStats() map[string]LaneStatCurve`

GetStats returns the Stats field if non-nil, zero value otherwise.

### GetStatsOk

`func (o *LaneSoulCurve) GetStatsOk() (*map[string]LaneStatCurve, bool)`

GetStatsOk returns a tuple with the Stats field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStats

`func (o *LaneSoulCurve) SetStats(v map[string]LaneStatCurve)`

SetStats sets Stats field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


