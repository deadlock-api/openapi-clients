# StreetBrawl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RespawnTimes** | **[]int32** |  | 
**GoldPerRound** | **[]int32** |  | 
**ApperRound** | **[]int32** |  | 
**ItemDraftRerollsPerRound** | **[]int32** |  | 
**RoundLengthMinutes** | **[]int32** |  | 
**RoundLengthMinutesUrgent** | **[]float32** |  | 
**OvertimeRespawnTimeIncrease** | **[]float32** |  | 
**OvertimeRespawnTimeIncreaseUrgent** | **[]float32** |  | 
**OvertimeTrooperHealthScale** | **[]float32** |  | 
**OvertimeTrooperDamageScale** | **[]float32** |  | 
**BuyTime** | **[]int32** |  | 
**PreBuyTime** | **[]float32** |  | 
**ScoreToWin** | **int32** |  | 
**ScoringTime** | **float32** |  | 
**LaneNumber** | **int32** |  | 
**ObjectiveMaxHealth** | **[]int32** |  | 
**Tier2BonusHealth** | **int32** |  | 
**ComebackBonusHealth** | **int32** |  | 
**ComebackBonusHealthCritical** | **int32** |  | 
**TrooperSpawnTimer** | **[]float32** |  | 
**TrooperSpawnBeforeRoundStartTimer** | **float32** |  | 
**ZipBoostCooldownOnStart** | **float32** |  | 
**BuyTimeGracePeriod** | **float32** |  | 
**Tier1MaxResistTime** | **float32** |  | 
**Tier2MaxResistTime** | **float32** |  | 
**UltimateUnlockRound** | **int32** |  | 
**ItemDraftRoundsPerGameRound** | [**[]ItemDraftRoundPerGameRound**](ItemDraftRoundPerGameRound.md) |  | 
**OutlineColorFriend** | Pointer to **[]int32** |  | [optional] 
**OutlineColorEnemy** | Pointer to **[]int32** |  | [optional] 
**OutlineColorTeam1** | Pointer to **[]int32** |  | [optional] 
**OutlineColorTeam2** | Pointer to **[]int32** |  | [optional] 
**OutlineColorNeutral** | Pointer to **[]int32** |  | [optional] 

## Methods

### NewStreetBrawl

`func NewStreetBrawl(respawnTimes []int32, goldPerRound []int32, apperRound []int32, itemDraftRerollsPerRound []int32, roundLengthMinutes []int32, roundLengthMinutesUrgent []float32, overtimeRespawnTimeIncrease []float32, overtimeRespawnTimeIncreaseUrgent []float32, overtimeTrooperHealthScale []float32, overtimeTrooperDamageScale []float32, buyTime []int32, preBuyTime []float32, scoreToWin int32, scoringTime float32, laneNumber int32, objectiveMaxHealth []int32, tier2BonusHealth int32, comebackBonusHealth int32, comebackBonusHealthCritical int32, trooperSpawnTimer []float32, trooperSpawnBeforeRoundStartTimer float32, zipBoostCooldownOnStart float32, buyTimeGracePeriod float32, tier1MaxResistTime float32, tier2MaxResistTime float32, ultimateUnlockRound int32, itemDraftRoundsPerGameRound []ItemDraftRoundPerGameRound, ) *StreetBrawl`

NewStreetBrawl instantiates a new StreetBrawl object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStreetBrawlWithDefaults

`func NewStreetBrawlWithDefaults() *StreetBrawl`

NewStreetBrawlWithDefaults instantiates a new StreetBrawl object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRespawnTimes

`func (o *StreetBrawl) GetRespawnTimes() []int32`

GetRespawnTimes returns the RespawnTimes field if non-nil, zero value otherwise.

### GetRespawnTimesOk

`func (o *StreetBrawl) GetRespawnTimesOk() (*[]int32, bool)`

GetRespawnTimesOk returns a tuple with the RespawnTimes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRespawnTimes

`func (o *StreetBrawl) SetRespawnTimes(v []int32)`

SetRespawnTimes sets RespawnTimes field to given value.


### GetGoldPerRound

`func (o *StreetBrawl) GetGoldPerRound() []int32`

GetGoldPerRound returns the GoldPerRound field if non-nil, zero value otherwise.

### GetGoldPerRoundOk

`func (o *StreetBrawl) GetGoldPerRoundOk() (*[]int32, bool)`

GetGoldPerRoundOk returns a tuple with the GoldPerRound field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldPerRound

`func (o *StreetBrawl) SetGoldPerRound(v []int32)`

SetGoldPerRound sets GoldPerRound field to given value.


### GetApperRound

`func (o *StreetBrawl) GetApperRound() []int32`

GetApperRound returns the ApperRound field if non-nil, zero value otherwise.

### GetApperRoundOk

`func (o *StreetBrawl) GetApperRoundOk() (*[]int32, bool)`

GetApperRoundOk returns a tuple with the ApperRound field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApperRound

`func (o *StreetBrawl) SetApperRound(v []int32)`

SetApperRound sets ApperRound field to given value.


### GetItemDraftRerollsPerRound

`func (o *StreetBrawl) GetItemDraftRerollsPerRound() []int32`

GetItemDraftRerollsPerRound returns the ItemDraftRerollsPerRound field if non-nil, zero value otherwise.

### GetItemDraftRerollsPerRoundOk

`func (o *StreetBrawl) GetItemDraftRerollsPerRoundOk() (*[]int32, bool)`

GetItemDraftRerollsPerRoundOk returns a tuple with the ItemDraftRerollsPerRound field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemDraftRerollsPerRound

`func (o *StreetBrawl) SetItemDraftRerollsPerRound(v []int32)`

SetItemDraftRerollsPerRound sets ItemDraftRerollsPerRound field to given value.


### GetRoundLengthMinutes

`func (o *StreetBrawl) GetRoundLengthMinutes() []int32`

GetRoundLengthMinutes returns the RoundLengthMinutes field if non-nil, zero value otherwise.

### GetRoundLengthMinutesOk

`func (o *StreetBrawl) GetRoundLengthMinutesOk() (*[]int32, bool)`

GetRoundLengthMinutesOk returns a tuple with the RoundLengthMinutes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRoundLengthMinutes

`func (o *StreetBrawl) SetRoundLengthMinutes(v []int32)`

SetRoundLengthMinutes sets RoundLengthMinutes field to given value.


### GetRoundLengthMinutesUrgent

`func (o *StreetBrawl) GetRoundLengthMinutesUrgent() []float32`

GetRoundLengthMinutesUrgent returns the RoundLengthMinutesUrgent field if non-nil, zero value otherwise.

### GetRoundLengthMinutesUrgentOk

`func (o *StreetBrawl) GetRoundLengthMinutesUrgentOk() (*[]float32, bool)`

GetRoundLengthMinutesUrgentOk returns a tuple with the RoundLengthMinutesUrgent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRoundLengthMinutesUrgent

`func (o *StreetBrawl) SetRoundLengthMinutesUrgent(v []float32)`

SetRoundLengthMinutesUrgent sets RoundLengthMinutesUrgent field to given value.


### GetOvertimeRespawnTimeIncrease

`func (o *StreetBrawl) GetOvertimeRespawnTimeIncrease() []float32`

GetOvertimeRespawnTimeIncrease returns the OvertimeRespawnTimeIncrease field if non-nil, zero value otherwise.

### GetOvertimeRespawnTimeIncreaseOk

`func (o *StreetBrawl) GetOvertimeRespawnTimeIncreaseOk() (*[]float32, bool)`

GetOvertimeRespawnTimeIncreaseOk returns a tuple with the OvertimeRespawnTimeIncrease field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOvertimeRespawnTimeIncrease

`func (o *StreetBrawl) SetOvertimeRespawnTimeIncrease(v []float32)`

SetOvertimeRespawnTimeIncrease sets OvertimeRespawnTimeIncrease field to given value.


### GetOvertimeRespawnTimeIncreaseUrgent

`func (o *StreetBrawl) GetOvertimeRespawnTimeIncreaseUrgent() []float32`

GetOvertimeRespawnTimeIncreaseUrgent returns the OvertimeRespawnTimeIncreaseUrgent field if non-nil, zero value otherwise.

### GetOvertimeRespawnTimeIncreaseUrgentOk

`func (o *StreetBrawl) GetOvertimeRespawnTimeIncreaseUrgentOk() (*[]float32, bool)`

GetOvertimeRespawnTimeIncreaseUrgentOk returns a tuple with the OvertimeRespawnTimeIncreaseUrgent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOvertimeRespawnTimeIncreaseUrgent

`func (o *StreetBrawl) SetOvertimeRespawnTimeIncreaseUrgent(v []float32)`

SetOvertimeRespawnTimeIncreaseUrgent sets OvertimeRespawnTimeIncreaseUrgent field to given value.


### GetOvertimeTrooperHealthScale

`func (o *StreetBrawl) GetOvertimeTrooperHealthScale() []float32`

GetOvertimeTrooperHealthScale returns the OvertimeTrooperHealthScale field if non-nil, zero value otherwise.

### GetOvertimeTrooperHealthScaleOk

`func (o *StreetBrawl) GetOvertimeTrooperHealthScaleOk() (*[]float32, bool)`

GetOvertimeTrooperHealthScaleOk returns a tuple with the OvertimeTrooperHealthScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOvertimeTrooperHealthScale

`func (o *StreetBrawl) SetOvertimeTrooperHealthScale(v []float32)`

SetOvertimeTrooperHealthScale sets OvertimeTrooperHealthScale field to given value.


### GetOvertimeTrooperDamageScale

`func (o *StreetBrawl) GetOvertimeTrooperDamageScale() []float32`

GetOvertimeTrooperDamageScale returns the OvertimeTrooperDamageScale field if non-nil, zero value otherwise.

### GetOvertimeTrooperDamageScaleOk

`func (o *StreetBrawl) GetOvertimeTrooperDamageScaleOk() (*[]float32, bool)`

GetOvertimeTrooperDamageScaleOk returns a tuple with the OvertimeTrooperDamageScale field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOvertimeTrooperDamageScale

`func (o *StreetBrawl) SetOvertimeTrooperDamageScale(v []float32)`

SetOvertimeTrooperDamageScale sets OvertimeTrooperDamageScale field to given value.


### GetBuyTime

`func (o *StreetBrawl) GetBuyTime() []int32`

GetBuyTime returns the BuyTime field if non-nil, zero value otherwise.

### GetBuyTimeOk

`func (o *StreetBrawl) GetBuyTimeOk() (*[]int32, bool)`

GetBuyTimeOk returns a tuple with the BuyTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuyTime

`func (o *StreetBrawl) SetBuyTime(v []int32)`

SetBuyTime sets BuyTime field to given value.


### GetPreBuyTime

`func (o *StreetBrawl) GetPreBuyTime() []float32`

GetPreBuyTime returns the PreBuyTime field if non-nil, zero value otherwise.

### GetPreBuyTimeOk

`func (o *StreetBrawl) GetPreBuyTimeOk() (*[]float32, bool)`

GetPreBuyTimeOk returns a tuple with the PreBuyTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPreBuyTime

`func (o *StreetBrawl) SetPreBuyTime(v []float32)`

SetPreBuyTime sets PreBuyTime field to given value.


### GetScoreToWin

`func (o *StreetBrawl) GetScoreToWin() int32`

GetScoreToWin returns the ScoreToWin field if non-nil, zero value otherwise.

### GetScoreToWinOk

`func (o *StreetBrawl) GetScoreToWinOk() (*int32, bool)`

GetScoreToWinOk returns a tuple with the ScoreToWin field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScoreToWin

`func (o *StreetBrawl) SetScoreToWin(v int32)`

SetScoreToWin sets ScoreToWin field to given value.


### GetScoringTime

`func (o *StreetBrawl) GetScoringTime() float32`

GetScoringTime returns the ScoringTime field if non-nil, zero value otherwise.

### GetScoringTimeOk

`func (o *StreetBrawl) GetScoringTimeOk() (*float32, bool)`

GetScoringTimeOk returns a tuple with the ScoringTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScoringTime

`func (o *StreetBrawl) SetScoringTime(v float32)`

SetScoringTime sets ScoringTime field to given value.


### GetLaneNumber

`func (o *StreetBrawl) GetLaneNumber() int32`

GetLaneNumber returns the LaneNumber field if non-nil, zero value otherwise.

### GetLaneNumberOk

`func (o *StreetBrawl) GetLaneNumberOk() (*int32, bool)`

GetLaneNumberOk returns a tuple with the LaneNumber field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLaneNumber

`func (o *StreetBrawl) SetLaneNumber(v int32)`

SetLaneNumber sets LaneNumber field to given value.


### GetObjectiveMaxHealth

`func (o *StreetBrawl) GetObjectiveMaxHealth() []int32`

GetObjectiveMaxHealth returns the ObjectiveMaxHealth field if non-nil, zero value otherwise.

### GetObjectiveMaxHealthOk

`func (o *StreetBrawl) GetObjectiveMaxHealthOk() (*[]int32, bool)`

GetObjectiveMaxHealthOk returns a tuple with the ObjectiveMaxHealth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectiveMaxHealth

`func (o *StreetBrawl) SetObjectiveMaxHealth(v []int32)`

SetObjectiveMaxHealth sets ObjectiveMaxHealth field to given value.


### GetTier2BonusHealth

`func (o *StreetBrawl) GetTier2BonusHealth() int32`

GetTier2BonusHealth returns the Tier2BonusHealth field if non-nil, zero value otherwise.

### GetTier2BonusHealthOk

`func (o *StreetBrawl) GetTier2BonusHealthOk() (*int32, bool)`

GetTier2BonusHealthOk returns a tuple with the Tier2BonusHealth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTier2BonusHealth

`func (o *StreetBrawl) SetTier2BonusHealth(v int32)`

SetTier2BonusHealth sets Tier2BonusHealth field to given value.


### GetComebackBonusHealth

`func (o *StreetBrawl) GetComebackBonusHealth() int32`

GetComebackBonusHealth returns the ComebackBonusHealth field if non-nil, zero value otherwise.

### GetComebackBonusHealthOk

`func (o *StreetBrawl) GetComebackBonusHealthOk() (*int32, bool)`

GetComebackBonusHealthOk returns a tuple with the ComebackBonusHealth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComebackBonusHealth

`func (o *StreetBrawl) SetComebackBonusHealth(v int32)`

SetComebackBonusHealth sets ComebackBonusHealth field to given value.


### GetComebackBonusHealthCritical

`func (o *StreetBrawl) GetComebackBonusHealthCritical() int32`

GetComebackBonusHealthCritical returns the ComebackBonusHealthCritical field if non-nil, zero value otherwise.

### GetComebackBonusHealthCriticalOk

`func (o *StreetBrawl) GetComebackBonusHealthCriticalOk() (*int32, bool)`

GetComebackBonusHealthCriticalOk returns a tuple with the ComebackBonusHealthCritical field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetComebackBonusHealthCritical

`func (o *StreetBrawl) SetComebackBonusHealthCritical(v int32)`

SetComebackBonusHealthCritical sets ComebackBonusHealthCritical field to given value.


### GetTrooperSpawnTimer

`func (o *StreetBrawl) GetTrooperSpawnTimer() []float32`

GetTrooperSpawnTimer returns the TrooperSpawnTimer field if non-nil, zero value otherwise.

### GetTrooperSpawnTimerOk

`func (o *StreetBrawl) GetTrooperSpawnTimerOk() (*[]float32, bool)`

GetTrooperSpawnTimerOk returns a tuple with the TrooperSpawnTimer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrooperSpawnTimer

`func (o *StreetBrawl) SetTrooperSpawnTimer(v []float32)`

SetTrooperSpawnTimer sets TrooperSpawnTimer field to given value.


### GetTrooperSpawnBeforeRoundStartTimer

`func (o *StreetBrawl) GetTrooperSpawnBeforeRoundStartTimer() float32`

GetTrooperSpawnBeforeRoundStartTimer returns the TrooperSpawnBeforeRoundStartTimer field if non-nil, zero value otherwise.

### GetTrooperSpawnBeforeRoundStartTimerOk

`func (o *StreetBrawl) GetTrooperSpawnBeforeRoundStartTimerOk() (*float32, bool)`

GetTrooperSpawnBeforeRoundStartTimerOk returns a tuple with the TrooperSpawnBeforeRoundStartTimer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrooperSpawnBeforeRoundStartTimer

`func (o *StreetBrawl) SetTrooperSpawnBeforeRoundStartTimer(v float32)`

SetTrooperSpawnBeforeRoundStartTimer sets TrooperSpawnBeforeRoundStartTimer field to given value.


### GetZipBoostCooldownOnStart

`func (o *StreetBrawl) GetZipBoostCooldownOnStart() float32`

GetZipBoostCooldownOnStart returns the ZipBoostCooldownOnStart field if non-nil, zero value otherwise.

### GetZipBoostCooldownOnStartOk

`func (o *StreetBrawl) GetZipBoostCooldownOnStartOk() (*float32, bool)`

GetZipBoostCooldownOnStartOk returns a tuple with the ZipBoostCooldownOnStart field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetZipBoostCooldownOnStart

`func (o *StreetBrawl) SetZipBoostCooldownOnStart(v float32)`

SetZipBoostCooldownOnStart sets ZipBoostCooldownOnStart field to given value.


### GetBuyTimeGracePeriod

`func (o *StreetBrawl) GetBuyTimeGracePeriod() float32`

GetBuyTimeGracePeriod returns the BuyTimeGracePeriod field if non-nil, zero value otherwise.

### GetBuyTimeGracePeriodOk

`func (o *StreetBrawl) GetBuyTimeGracePeriodOk() (*float32, bool)`

GetBuyTimeGracePeriodOk returns a tuple with the BuyTimeGracePeriod field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuyTimeGracePeriod

`func (o *StreetBrawl) SetBuyTimeGracePeriod(v float32)`

SetBuyTimeGracePeriod sets BuyTimeGracePeriod field to given value.


### GetTier1MaxResistTime

`func (o *StreetBrawl) GetTier1MaxResistTime() float32`

GetTier1MaxResistTime returns the Tier1MaxResistTime field if non-nil, zero value otherwise.

### GetTier1MaxResistTimeOk

`func (o *StreetBrawl) GetTier1MaxResistTimeOk() (*float32, bool)`

GetTier1MaxResistTimeOk returns a tuple with the Tier1MaxResistTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTier1MaxResistTime

`func (o *StreetBrawl) SetTier1MaxResistTime(v float32)`

SetTier1MaxResistTime sets Tier1MaxResistTime field to given value.


### GetTier2MaxResistTime

`func (o *StreetBrawl) GetTier2MaxResistTime() float32`

GetTier2MaxResistTime returns the Tier2MaxResistTime field if non-nil, zero value otherwise.

### GetTier2MaxResistTimeOk

`func (o *StreetBrawl) GetTier2MaxResistTimeOk() (*float32, bool)`

GetTier2MaxResistTimeOk returns a tuple with the Tier2MaxResistTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTier2MaxResistTime

`func (o *StreetBrawl) SetTier2MaxResistTime(v float32)`

SetTier2MaxResistTime sets Tier2MaxResistTime field to given value.


### GetUltimateUnlockRound

`func (o *StreetBrawl) GetUltimateUnlockRound() int32`

GetUltimateUnlockRound returns the UltimateUnlockRound field if non-nil, zero value otherwise.

### GetUltimateUnlockRoundOk

`func (o *StreetBrawl) GetUltimateUnlockRoundOk() (*int32, bool)`

GetUltimateUnlockRoundOk returns a tuple with the UltimateUnlockRound field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUltimateUnlockRound

`func (o *StreetBrawl) SetUltimateUnlockRound(v int32)`

SetUltimateUnlockRound sets UltimateUnlockRound field to given value.


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


### GetOutlineColorFriend

`func (o *StreetBrawl) GetOutlineColorFriend() []int32`

GetOutlineColorFriend returns the OutlineColorFriend field if non-nil, zero value otherwise.

### GetOutlineColorFriendOk

`func (o *StreetBrawl) GetOutlineColorFriendOk() (*[]int32, bool)`

GetOutlineColorFriendOk returns a tuple with the OutlineColorFriend field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutlineColorFriend

`func (o *StreetBrawl) SetOutlineColorFriend(v []int32)`

SetOutlineColorFriend sets OutlineColorFriend field to given value.

### HasOutlineColorFriend

`func (o *StreetBrawl) HasOutlineColorFriend() bool`

HasOutlineColorFriend returns a boolean if a field has been set.

### SetOutlineColorFriendNil

`func (o *StreetBrawl) SetOutlineColorFriendNil(b bool)`

 SetOutlineColorFriendNil sets the value for OutlineColorFriend to be an explicit nil

### UnsetOutlineColorFriend
`func (o *StreetBrawl) UnsetOutlineColorFriend()`

UnsetOutlineColorFriend ensures that no value is present for OutlineColorFriend, not even an explicit nil
### GetOutlineColorEnemy

`func (o *StreetBrawl) GetOutlineColorEnemy() []int32`

GetOutlineColorEnemy returns the OutlineColorEnemy field if non-nil, zero value otherwise.

### GetOutlineColorEnemyOk

`func (o *StreetBrawl) GetOutlineColorEnemyOk() (*[]int32, bool)`

GetOutlineColorEnemyOk returns a tuple with the OutlineColorEnemy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutlineColorEnemy

`func (o *StreetBrawl) SetOutlineColorEnemy(v []int32)`

SetOutlineColorEnemy sets OutlineColorEnemy field to given value.

### HasOutlineColorEnemy

`func (o *StreetBrawl) HasOutlineColorEnemy() bool`

HasOutlineColorEnemy returns a boolean if a field has been set.

### SetOutlineColorEnemyNil

`func (o *StreetBrawl) SetOutlineColorEnemyNil(b bool)`

 SetOutlineColorEnemyNil sets the value for OutlineColorEnemy to be an explicit nil

### UnsetOutlineColorEnemy
`func (o *StreetBrawl) UnsetOutlineColorEnemy()`

UnsetOutlineColorEnemy ensures that no value is present for OutlineColorEnemy, not even an explicit nil
### GetOutlineColorTeam1

`func (o *StreetBrawl) GetOutlineColorTeam1() []int32`

GetOutlineColorTeam1 returns the OutlineColorTeam1 field if non-nil, zero value otherwise.

### GetOutlineColorTeam1Ok

`func (o *StreetBrawl) GetOutlineColorTeam1Ok() (*[]int32, bool)`

GetOutlineColorTeam1Ok returns a tuple with the OutlineColorTeam1 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutlineColorTeam1

`func (o *StreetBrawl) SetOutlineColorTeam1(v []int32)`

SetOutlineColorTeam1 sets OutlineColorTeam1 field to given value.

### HasOutlineColorTeam1

`func (o *StreetBrawl) HasOutlineColorTeam1() bool`

HasOutlineColorTeam1 returns a boolean if a field has been set.

### SetOutlineColorTeam1Nil

`func (o *StreetBrawl) SetOutlineColorTeam1Nil(b bool)`

 SetOutlineColorTeam1Nil sets the value for OutlineColorTeam1 to be an explicit nil

### UnsetOutlineColorTeam1
`func (o *StreetBrawl) UnsetOutlineColorTeam1()`

UnsetOutlineColorTeam1 ensures that no value is present for OutlineColorTeam1, not even an explicit nil
### GetOutlineColorTeam2

`func (o *StreetBrawl) GetOutlineColorTeam2() []int32`

GetOutlineColorTeam2 returns the OutlineColorTeam2 field if non-nil, zero value otherwise.

### GetOutlineColorTeam2Ok

`func (o *StreetBrawl) GetOutlineColorTeam2Ok() (*[]int32, bool)`

GetOutlineColorTeam2Ok returns a tuple with the OutlineColorTeam2 field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutlineColorTeam2

`func (o *StreetBrawl) SetOutlineColorTeam2(v []int32)`

SetOutlineColorTeam2 sets OutlineColorTeam2 field to given value.

### HasOutlineColorTeam2

`func (o *StreetBrawl) HasOutlineColorTeam2() bool`

HasOutlineColorTeam2 returns a boolean if a field has been set.

### SetOutlineColorTeam2Nil

`func (o *StreetBrawl) SetOutlineColorTeam2Nil(b bool)`

 SetOutlineColorTeam2Nil sets the value for OutlineColorTeam2 to be an explicit nil

### UnsetOutlineColorTeam2
`func (o *StreetBrawl) UnsetOutlineColorTeam2()`

UnsetOutlineColorTeam2 ensures that no value is present for OutlineColorTeam2, not even an explicit nil
### GetOutlineColorNeutral

`func (o *StreetBrawl) GetOutlineColorNeutral() []int32`

GetOutlineColorNeutral returns the OutlineColorNeutral field if non-nil, zero value otherwise.

### GetOutlineColorNeutralOk

`func (o *StreetBrawl) GetOutlineColorNeutralOk() (*[]int32, bool)`

GetOutlineColorNeutralOk returns a tuple with the OutlineColorNeutral field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutlineColorNeutral

`func (o *StreetBrawl) SetOutlineColorNeutral(v []int32)`

SetOutlineColorNeutral sets OutlineColorNeutral field to given value.

### HasOutlineColorNeutral

`func (o *StreetBrawl) HasOutlineColorNeutral() bool`

HasOutlineColorNeutral returns a boolean if a field has been set.

### SetOutlineColorNeutralNil

`func (o *StreetBrawl) SetOutlineColorNeutralNil(b bool)`

 SetOutlineColorNeutralNil sets the value for OutlineColorNeutral to be an explicit nil

### UnsetOutlineColorNeutral
`func (o *StreetBrawl) UnsetOutlineColorNeutral()`

UnsetOutlineColorNeutral ensures that no value is present for OutlineColorNeutral, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


