# StreetBrawl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ApperRound** | **[]int64** |  | 
**BuyTime** | **[]int64** |  | 
**BuyTimeGracePeriod** | **float64** |  | 
**ComebackBonusHealth** | **int64** |  | 
**ComebackBonusHealthCritical** | **int64** |  | 
**GoldPerRound** | **[]int64** |  | 
**ItemDraftRerollsPerRound** | **[]int64** |  | 
**ItemDraftRoundsPerGameRound** | [**[]ItemDraftRoundPerGameRound**](ItemDraftRoundPerGameRound.md) |  | 
**ItemDrafts** | [**map[string]DraftBuckets**](DraftBuckets.md) |  | 
**LaneNumber** | **int64** |  | 
**ObjectiveMaxHealth** | **[]int64** |  | 
**OvertimeRespawnTimeIncrease** | **[]float64** |  | 
**OvertimeRespawnTimeIncreaseUrgent** | **[]float64** |  | 
**OvertimeTrooperDamageScale** | **[]float64** |  | 
**OvertimeTrooperHealthScale** | **[]float64** |  | 
**PreBuyTime** | **[]float64** |  | 
**RespawnTimes** | **[]int64** |  | 
**RoundLengthMinutes** | **[]int64** |  | 
**RoundLengthMinutesUrgent** | **[]float64** |  | 
**ScoreToWin** | **int64** |  | 
**ScoringTime** | **float64** |  | 
**Tier1MaxResistTime** | **float64** |  | 
**Tier2BonusHealth** | **int64** |  | 
**Tier2MaxResistTime** | **float64** |  | 
**TrooperSpawnBeforeRoundStartTimer** | **float64** |  | 
**TrooperSpawnTimer** | **[]float64** |  | 
**UltimateUnlockRound** | **int64** |  | 
**ZipBoostCooldownOnStart** | **float64** |  | 

## Methods

### NewStreetBrawl

`func NewStreetBrawl(apperRound []int64, buyTime []int64, buyTimeGracePeriod float64, comebackBonusHealth int64, comebackBonusHealthCritical int64, goldPerRound []int64, itemDraftRerollsPerRound []int64, itemDraftRoundsPerGameRound []ItemDraftRoundPerGameRound, itemDrafts map[string]DraftBuckets, laneNumber int64, objectiveMaxHealth []int64, overtimeRespawnTimeIncrease []float64, overtimeRespawnTimeIncreaseUrgent []float64, overtimeTrooperDamageScale []float64, overtimeTrooperHealthScale []float64, preBuyTime []float64, respawnTimes []int64, roundLengthMinutes []int64, roundLengthMinutesUrgent []float64, scoreToWin int64, scoringTime float64, tier1MaxResistTime float64, tier2BonusHealth int64, tier2MaxResistTime float64, trooperSpawnBeforeRoundStartTimer float64, trooperSpawnTimer []float64, ultimateUnlockRound int64, zipBoostCooldownOnStart float64, ) *StreetBrawl`

NewStreetBrawl instantiates a new StreetBrawl object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStreetBrawlWithDefaults

`func NewStreetBrawlWithDefaults() *StreetBrawl`

NewStreetBrawlWithDefaults instantiates a new StreetBrawl object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetApperRound

`func (o *StreetBrawl) GetApperRound() []int64`

GetApperRound returns the ApperRound field if non-nil, zero value otherwise.

### GetApperRoundOk

`func (o *StreetBrawl) GetApperRoundOk() (*[]int64, bool)`

GetApperRoundOk returns a tuple with the ApperRound field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApperRound

`func (o *StreetBrawl) SetApperRound(v []int64)`

SetApperRound sets ApperRound field to given value.


### GetBuyTime

`func (o *StreetBrawl) GetBuyTime() []int64`

GetBuyTime returns the BuyTime field if non-nil, zero value otherwise.

### GetBuyTimeOk

`func (o *StreetBrawl) GetBuyTimeOk() (*[]int64, bool)`

GetBuyTimeOk returns a tuple with the BuyTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuyTime

`func (o *StreetBrawl) SetBuyTime(v []int64)`

SetBuyTime sets BuyTime field to given value.


### GetBuyTimeGracePeriod

`func (o *StreetBrawl) GetBuyTimeGracePeriod() float64`

GetBuyTimeGracePeriod returns the BuyTimeGracePeriod field if non-nil, zero value otherwise.

### GetBuyTimeGracePeriodOk

`func (o *StreetBrawl) GetBuyTimeGracePeriodOk() (*float64, bool)`

GetBuyTimeGracePeriodOk returns a tuple with the BuyTimeGracePeriod field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuyTimeGracePeriod

`func (o *StreetBrawl) SetBuyTimeGracePeriod(v float64)`

SetBuyTimeGracePeriod sets BuyTimeGracePeriod field to given value.


### GetComebackBonusHealth

`func (o *StreetBrawl) GetComebackBonusHealth() int64`

GetComebackBonusHealth returns the ComebackBonusHealth field if non-nil, zero value otherwise.

### GetComebackBonusHealthOk

`func (o *StreetBrawl) GetComebackBonusHealthOk() (*int64, bool)`

GetComebackBonusHealthOk returns a tuple with the ComebackBonusHealth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComebackBonusHealth

`func (o *StreetBrawl) SetComebackBonusHealth(v int64)`

SetComebackBonusHealth sets ComebackBonusHealth field to given value.


### GetComebackBonusHealthCritical

`func (o *StreetBrawl) GetComebackBonusHealthCritical() int64`

GetComebackBonusHealthCritical returns the ComebackBonusHealthCritical field if non-nil, zero value otherwise.

### GetComebackBonusHealthCriticalOk

`func (o *StreetBrawl) GetComebackBonusHealthCriticalOk() (*int64, bool)`

GetComebackBonusHealthCriticalOk returns a tuple with the ComebackBonusHealthCritical field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComebackBonusHealthCritical

`func (o *StreetBrawl) SetComebackBonusHealthCritical(v int64)`

SetComebackBonusHealthCritical sets ComebackBonusHealthCritical field to given value.


### GetGoldPerRound

`func (o *StreetBrawl) GetGoldPerRound() []int64`

GetGoldPerRound returns the GoldPerRound field if non-nil, zero value otherwise.

### GetGoldPerRoundOk

`func (o *StreetBrawl) GetGoldPerRoundOk() (*[]int64, bool)`

GetGoldPerRoundOk returns a tuple with the GoldPerRound field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldPerRound

`func (o *StreetBrawl) SetGoldPerRound(v []int64)`

SetGoldPerRound sets GoldPerRound field to given value.


### GetItemDraftRerollsPerRound

`func (o *StreetBrawl) GetItemDraftRerollsPerRound() []int64`

GetItemDraftRerollsPerRound returns the ItemDraftRerollsPerRound field if non-nil, zero value otherwise.

### GetItemDraftRerollsPerRoundOk

`func (o *StreetBrawl) GetItemDraftRerollsPerRoundOk() (*[]int64, bool)`

GetItemDraftRerollsPerRoundOk returns a tuple with the ItemDraftRerollsPerRound field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemDraftRerollsPerRound

`func (o *StreetBrawl) SetItemDraftRerollsPerRound(v []int64)`

SetItemDraftRerollsPerRound sets ItemDraftRerollsPerRound field to given value.


### GetItemDraftRoundsPerGameRound

`func (o *StreetBrawl) GetItemDraftRoundsPerGameRound() []ItemDraftRoundPerGameRound`

GetItemDraftRoundsPerGameRound returns the ItemDraftRoundsPerGameRound field if non-nil, zero value otherwise.

### GetItemDraftRoundsPerGameRoundOk

`func (o *StreetBrawl) GetItemDraftRoundsPerGameRoundOk() (*[]ItemDraftRoundPerGameRound, bool)`

GetItemDraftRoundsPerGameRoundOk returns a tuple with the ItemDraftRoundsPerGameRound field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemDraftRoundsPerGameRound

`func (o *StreetBrawl) SetItemDraftRoundsPerGameRound(v []ItemDraftRoundPerGameRound)`

SetItemDraftRoundsPerGameRound sets ItemDraftRoundsPerGameRound field to given value.


### GetItemDrafts

`func (o *StreetBrawl) GetItemDrafts() map[string]DraftBuckets`

GetItemDrafts returns the ItemDrafts field if non-nil, zero value otherwise.

### GetItemDraftsOk

`func (o *StreetBrawl) GetItemDraftsOk() (*map[string]DraftBuckets, bool)`

GetItemDraftsOk returns a tuple with the ItemDrafts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemDrafts

`func (o *StreetBrawl) SetItemDrafts(v map[string]DraftBuckets)`

SetItemDrafts sets ItemDrafts field to given value.


### GetLaneNumber

`func (o *StreetBrawl) GetLaneNumber() int64`

GetLaneNumber returns the LaneNumber field if non-nil, zero value otherwise.

### GetLaneNumberOk

`func (o *StreetBrawl) GetLaneNumberOk() (*int64, bool)`

GetLaneNumberOk returns a tuple with the LaneNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLaneNumber

`func (o *StreetBrawl) SetLaneNumber(v int64)`

SetLaneNumber sets LaneNumber field to given value.


### GetObjectiveMaxHealth

`func (o *StreetBrawl) GetObjectiveMaxHealth() []int64`

GetObjectiveMaxHealth returns the ObjectiveMaxHealth field if non-nil, zero value otherwise.

### GetObjectiveMaxHealthOk

`func (o *StreetBrawl) GetObjectiveMaxHealthOk() (*[]int64, bool)`

GetObjectiveMaxHealthOk returns a tuple with the ObjectiveMaxHealth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectiveMaxHealth

`func (o *StreetBrawl) SetObjectiveMaxHealth(v []int64)`

SetObjectiveMaxHealth sets ObjectiveMaxHealth field to given value.


### GetOvertimeRespawnTimeIncrease

`func (o *StreetBrawl) GetOvertimeRespawnTimeIncrease() []float64`

GetOvertimeRespawnTimeIncrease returns the OvertimeRespawnTimeIncrease field if non-nil, zero value otherwise.

### GetOvertimeRespawnTimeIncreaseOk

`func (o *StreetBrawl) GetOvertimeRespawnTimeIncreaseOk() (*[]float64, bool)`

GetOvertimeRespawnTimeIncreaseOk returns a tuple with the OvertimeRespawnTimeIncrease field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOvertimeRespawnTimeIncrease

`func (o *StreetBrawl) SetOvertimeRespawnTimeIncrease(v []float64)`

SetOvertimeRespawnTimeIncrease sets OvertimeRespawnTimeIncrease field to given value.


### GetOvertimeRespawnTimeIncreaseUrgent

`func (o *StreetBrawl) GetOvertimeRespawnTimeIncreaseUrgent() []float64`

GetOvertimeRespawnTimeIncreaseUrgent returns the OvertimeRespawnTimeIncreaseUrgent field if non-nil, zero value otherwise.

### GetOvertimeRespawnTimeIncreaseUrgentOk

`func (o *StreetBrawl) GetOvertimeRespawnTimeIncreaseUrgentOk() (*[]float64, bool)`

GetOvertimeRespawnTimeIncreaseUrgentOk returns a tuple with the OvertimeRespawnTimeIncreaseUrgent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOvertimeRespawnTimeIncreaseUrgent

`func (o *StreetBrawl) SetOvertimeRespawnTimeIncreaseUrgent(v []float64)`

SetOvertimeRespawnTimeIncreaseUrgent sets OvertimeRespawnTimeIncreaseUrgent field to given value.


### GetOvertimeTrooperDamageScale

`func (o *StreetBrawl) GetOvertimeTrooperDamageScale() []float64`

GetOvertimeTrooperDamageScale returns the OvertimeTrooperDamageScale field if non-nil, zero value otherwise.

### GetOvertimeTrooperDamageScaleOk

`func (o *StreetBrawl) GetOvertimeTrooperDamageScaleOk() (*[]float64, bool)`

GetOvertimeTrooperDamageScaleOk returns a tuple with the OvertimeTrooperDamageScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOvertimeTrooperDamageScale

`func (o *StreetBrawl) SetOvertimeTrooperDamageScale(v []float64)`

SetOvertimeTrooperDamageScale sets OvertimeTrooperDamageScale field to given value.


### GetOvertimeTrooperHealthScale

`func (o *StreetBrawl) GetOvertimeTrooperHealthScale() []float64`

GetOvertimeTrooperHealthScale returns the OvertimeTrooperHealthScale field if non-nil, zero value otherwise.

### GetOvertimeTrooperHealthScaleOk

`func (o *StreetBrawl) GetOvertimeTrooperHealthScaleOk() (*[]float64, bool)`

GetOvertimeTrooperHealthScaleOk returns a tuple with the OvertimeTrooperHealthScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOvertimeTrooperHealthScale

`func (o *StreetBrawl) SetOvertimeTrooperHealthScale(v []float64)`

SetOvertimeTrooperHealthScale sets OvertimeTrooperHealthScale field to given value.


### GetPreBuyTime

`func (o *StreetBrawl) GetPreBuyTime() []float64`

GetPreBuyTime returns the PreBuyTime field if non-nil, zero value otherwise.

### GetPreBuyTimeOk

`func (o *StreetBrawl) GetPreBuyTimeOk() (*[]float64, bool)`

GetPreBuyTimeOk returns a tuple with the PreBuyTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPreBuyTime

`func (o *StreetBrawl) SetPreBuyTime(v []float64)`

SetPreBuyTime sets PreBuyTime field to given value.


### GetRespawnTimes

`func (o *StreetBrawl) GetRespawnTimes() []int64`

GetRespawnTimes returns the RespawnTimes field if non-nil, zero value otherwise.

### GetRespawnTimesOk

`func (o *StreetBrawl) GetRespawnTimesOk() (*[]int64, bool)`

GetRespawnTimesOk returns a tuple with the RespawnTimes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRespawnTimes

`func (o *StreetBrawl) SetRespawnTimes(v []int64)`

SetRespawnTimes sets RespawnTimes field to given value.


### GetRoundLengthMinutes

`func (o *StreetBrawl) GetRoundLengthMinutes() []int64`

GetRoundLengthMinutes returns the RoundLengthMinutes field if non-nil, zero value otherwise.

### GetRoundLengthMinutesOk

`func (o *StreetBrawl) GetRoundLengthMinutesOk() (*[]int64, bool)`

GetRoundLengthMinutesOk returns a tuple with the RoundLengthMinutes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRoundLengthMinutes

`func (o *StreetBrawl) SetRoundLengthMinutes(v []int64)`

SetRoundLengthMinutes sets RoundLengthMinutes field to given value.


### GetRoundLengthMinutesUrgent

`func (o *StreetBrawl) GetRoundLengthMinutesUrgent() []float64`

GetRoundLengthMinutesUrgent returns the RoundLengthMinutesUrgent field if non-nil, zero value otherwise.

### GetRoundLengthMinutesUrgentOk

`func (o *StreetBrawl) GetRoundLengthMinutesUrgentOk() (*[]float64, bool)`

GetRoundLengthMinutesUrgentOk returns a tuple with the RoundLengthMinutesUrgent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRoundLengthMinutesUrgent

`func (o *StreetBrawl) SetRoundLengthMinutesUrgent(v []float64)`

SetRoundLengthMinutesUrgent sets RoundLengthMinutesUrgent field to given value.


### GetScoreToWin

`func (o *StreetBrawl) GetScoreToWin() int64`

GetScoreToWin returns the ScoreToWin field if non-nil, zero value otherwise.

### GetScoreToWinOk

`func (o *StreetBrawl) GetScoreToWinOk() (*int64, bool)`

GetScoreToWinOk returns a tuple with the ScoreToWin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScoreToWin

`func (o *StreetBrawl) SetScoreToWin(v int64)`

SetScoreToWin sets ScoreToWin field to given value.


### GetScoringTime

`func (o *StreetBrawl) GetScoringTime() float64`

GetScoringTime returns the ScoringTime field if non-nil, zero value otherwise.

### GetScoringTimeOk

`func (o *StreetBrawl) GetScoringTimeOk() (*float64, bool)`

GetScoringTimeOk returns a tuple with the ScoringTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScoringTime

`func (o *StreetBrawl) SetScoringTime(v float64)`

SetScoringTime sets ScoringTime field to given value.


### GetTier1MaxResistTime

`func (o *StreetBrawl) GetTier1MaxResistTime() float64`

GetTier1MaxResistTime returns the Tier1MaxResistTime field if non-nil, zero value otherwise.

### GetTier1MaxResistTimeOk

`func (o *StreetBrawl) GetTier1MaxResistTimeOk() (*float64, bool)`

GetTier1MaxResistTimeOk returns a tuple with the Tier1MaxResistTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTier1MaxResistTime

`func (o *StreetBrawl) SetTier1MaxResistTime(v float64)`

SetTier1MaxResistTime sets Tier1MaxResistTime field to given value.


### GetTier2BonusHealth

`func (o *StreetBrawl) GetTier2BonusHealth() int64`

GetTier2BonusHealth returns the Tier2BonusHealth field if non-nil, zero value otherwise.

### GetTier2BonusHealthOk

`func (o *StreetBrawl) GetTier2BonusHealthOk() (*int64, bool)`

GetTier2BonusHealthOk returns a tuple with the Tier2BonusHealth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTier2BonusHealth

`func (o *StreetBrawl) SetTier2BonusHealth(v int64)`

SetTier2BonusHealth sets Tier2BonusHealth field to given value.


### GetTier2MaxResistTime

`func (o *StreetBrawl) GetTier2MaxResistTime() float64`

GetTier2MaxResistTime returns the Tier2MaxResistTime field if non-nil, zero value otherwise.

### GetTier2MaxResistTimeOk

`func (o *StreetBrawl) GetTier2MaxResistTimeOk() (*float64, bool)`

GetTier2MaxResistTimeOk returns a tuple with the Tier2MaxResistTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTier2MaxResistTime

`func (o *StreetBrawl) SetTier2MaxResistTime(v float64)`

SetTier2MaxResistTime sets Tier2MaxResistTime field to given value.


### GetTrooperSpawnBeforeRoundStartTimer

`func (o *StreetBrawl) GetTrooperSpawnBeforeRoundStartTimer() float64`

GetTrooperSpawnBeforeRoundStartTimer returns the TrooperSpawnBeforeRoundStartTimer field if non-nil, zero value otherwise.

### GetTrooperSpawnBeforeRoundStartTimerOk

`func (o *StreetBrawl) GetTrooperSpawnBeforeRoundStartTimerOk() (*float64, bool)`

GetTrooperSpawnBeforeRoundStartTimerOk returns a tuple with the TrooperSpawnBeforeRoundStartTimer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrooperSpawnBeforeRoundStartTimer

`func (o *StreetBrawl) SetTrooperSpawnBeforeRoundStartTimer(v float64)`

SetTrooperSpawnBeforeRoundStartTimer sets TrooperSpawnBeforeRoundStartTimer field to given value.


### GetTrooperSpawnTimer

`func (o *StreetBrawl) GetTrooperSpawnTimer() []float64`

GetTrooperSpawnTimer returns the TrooperSpawnTimer field if non-nil, zero value otherwise.

### GetTrooperSpawnTimerOk

`func (o *StreetBrawl) GetTrooperSpawnTimerOk() (*[]float64, bool)`

GetTrooperSpawnTimerOk returns a tuple with the TrooperSpawnTimer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrooperSpawnTimer

`func (o *StreetBrawl) SetTrooperSpawnTimer(v []float64)`

SetTrooperSpawnTimer sets TrooperSpawnTimer field to given value.


### GetUltimateUnlockRound

`func (o *StreetBrawl) GetUltimateUnlockRound() int64`

GetUltimateUnlockRound returns the UltimateUnlockRound field if non-nil, zero value otherwise.

### GetUltimateUnlockRoundOk

`func (o *StreetBrawl) GetUltimateUnlockRoundOk() (*int64, bool)`

GetUltimateUnlockRoundOk returns a tuple with the UltimateUnlockRound field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUltimateUnlockRound

`func (o *StreetBrawl) SetUltimateUnlockRound(v int64)`

SetUltimateUnlockRound sets UltimateUnlockRound field to given value.


### GetZipBoostCooldownOnStart

`func (o *StreetBrawl) GetZipBoostCooldownOnStart() float64`

GetZipBoostCooldownOnStart returns the ZipBoostCooldownOnStart field if non-nil, zero value otherwise.

### GetZipBoostCooldownOnStartOk

`func (o *StreetBrawl) GetZipBoostCooldownOnStartOk() (*float64, bool)`

GetZipBoostCooldownOnStartOk returns a tuple with the ZipBoostCooldownOnStart field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetZipBoostCooldownOnStart

`func (o *StreetBrawl) SetZipBoostCooldownOnStart(v float64)`

SetZipBoostCooldownOnStart sets ZipBoostCooldownOnStart field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


