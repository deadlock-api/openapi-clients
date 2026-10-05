# PlayerPerformanceCurvePoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AssistsAvg** | **float64** | Average assists at this time point | 
**AssistsStd** | **float64** | Standard deviation of assists at this time point | 
**BossDamageAvg** | **float64** | Average damage dealt to objectives at this time point | 
**BossDamageStd** | **float64** | Standard deviation of &#x60;boss_damage_avg&#x60; at this time point | 
**BossKillsAvg** | **float64** | Average objectives killed (last hits) at this time point | 
**BossKillsStd** | **float64** | Standard deviation of &#x60;boss_kills_avg&#x60; at this time point | 
**CreepDamageAvg** | **float64** | Average damage dealt to lane creeps at this time point | 
**CreepDamageStd** | **float64** | Standard deviation of &#x60;creep_damage_avg&#x60; at this time point | 
**CreepKillsAvg** | **float64** | Average lane creeps killed (last hits) at this time point | 
**CreepKillsStd** | **float64** | Standard deviation of &#x60;creep_kills_avg&#x60; at this time point | 
**DeathsAvg** | **float64** | Average deaths at this time point | 
**DeathsStd** | **float64** | Standard deviation of deaths at this time point | 
**DeniesAvg** | **float64** | Average lane creeps denied at this time point | 
**DeniesStd** | **float64** | Standard deviation of &#x60;denies_avg&#x60; at this time point | 
**GameTime** | **int32** | The time point of the data. If &#x60;resolution&#x60; (default 10) is &gt; 0, this is a percentage (0, 10, ..., 100). If &#x60;resolution&#x60; is 0, this is the match time in seconds. | 
**GoldAbilityAssassinateAvg** | **float64** | Average souls earned from the Assassinate ability at this time point | 
**GoldAbilityAssassinateStd** | **float64** | Standard deviation of &#x60;gold_ability_assassinate_avg&#x60; at this time point | 
**GoldAssistsAvg** | **float64** | Average souls earned from assists at this time point (part of &#x60;gold_player_avg&#x60;) | 
**GoldAssistsStd** | **float64** | Standard deviation of &#x60;gold_assists_avg&#x60; at this time point | 
**GoldBossAvg** | **float64** | Average souls earned from objectives at this time point | 
**GoldBossOrbAvg** | **float64** | Average souls earned from secured objective orbs at this time point | 
**GoldBossOrbStd** | **float64** | Standard deviation of &#x60;gold_boss_orb_avg&#x60; at this time point | 
**GoldBossStd** | **float64** | Standard deviation of &#x60;gold_boss_avg&#x60; at this time point | 
**GoldBreakableAvg** | **float64** | Average souls earned from breakables (crates, statues) at this time point | 
**GoldBreakableStd** | **float64** | Standard deviation of &#x60;gold_breakable_avg&#x60; at this time point | 
**GoldDeathLossAvg** | **float64** | Average souls lost on death at this time point | 
**GoldDeathLossStd** | **float64** | Standard deviation of &#x60;gold_death_loss_avg&#x60; at this time point | 
**GoldDeniedAvg** | **float64** | Average souls denied to enemies at this time point | 
**GoldDeniedStd** | **float64** | Standard deviation of &#x60;gold_denied_avg&#x60; at this time point | 
**GoldItemCultistSacrificeAvg** | **float64** | Average souls earned from the Cultist Sacrifice item at this time point | 
**GoldItemCultistSacrificeStd** | **float64** | Standard deviation of &#x60;gold_item_cultist_sacrifice_avg&#x60; at this time point | 
**GoldItemGooseEggAvg** | **float64** | Average souls earned from the Golden Goose Egg item at this time point | 
**GoldItemGooseEggStd** | **float64** | Standard deviation of &#x60;gold_item_goose_egg_avg&#x60; at this time point | 
**GoldItemTrophyCollectorAvg** | **float64** | Average souls earned from the Trophy Collector item at this time point | 
**GoldItemTrophyCollectorStd** | **float64** | Standard deviation of &#x60;gold_item_trophy_collector_avg&#x60; at this time point | 
**GoldLaneCreepAvg** | **float64** | Average souls earned from lane creeps at this time point | 
**GoldLaneCreepOrbsAvg** | **float64** | Average souls earned from secured lane-creep orbs at this time point | 
**GoldLaneCreepOrbsStd** | **float64** | Standard deviation of &#x60;gold_lane_creep_orbs_avg&#x60; at this time point | 
**GoldLaneCreepStd** | **float64** | Standard deviation of &#x60;gold_lane_creep_avg&#x60; at this time point | 
**GoldNeutralCreepAvg** | **float64** | Average souls earned from neutral (jungle) creeps at this time point | 
**GoldNeutralCreepOrbsAvg** | **float64** | Average souls earned from secured neutral-creep orbs at this time point | 
**GoldNeutralCreepOrbsStd** | **float64** | Standard deviation of &#x60;gold_neutral_creep_orbs_avg&#x60; at this time point | 
**GoldNeutralCreepStd** | **float64** | Standard deviation of &#x60;gold_neutral_creep_avg&#x60; at this time point | 
**GoldPlayerAvg** | **float64** | Average souls earned from hero kills at this time point, including assist souls (see &#x60;gold_assists_avg&#x60;) | 
**GoldPlayerOrbsAvg** | **float64** | Average souls earned from secured hero-kill orbs at this time point | 
**GoldPlayerOrbsStd** | **float64** | Standard deviation of &#x60;gold_player_orbs_avg&#x60; at this time point | 
**GoldPlayerStd** | **float64** | Standard deviation of &#x60;gold_player_avg&#x60; at this time point | 
**GoldTeamBonusAvg** | **float64** | Average souls earned from the team bonus at this time point | 
**GoldTeamBonusStd** | **float64** | Standard deviation of &#x60;gold_team_bonus_avg&#x60; at this time point | 
**GoldTreasureAvg** | **float64** | Average souls earned from the urn at this time point | 
**GoldTreasureStd** | **float64** | Standard deviation of &#x60;gold_treasure_avg&#x60; at this time point | 
**KillsAvg** | **float64** | Average kills at this time point | 
**KillsStd** | **float64** | Standard deviation of kills at this time point | 
**NetWorthAvg** | **float64** | Average net worth at this time point | 
**NetWorthStd** | **float64** | Standard deviation of net worth at this time point | 
**NeutralDamageAvg** | **float64** | Average damage dealt to neutral (jungle) creeps at this time point | 
**NeutralDamageStd** | **float64** | Standard deviation of &#x60;neutral_damage_avg&#x60; at this time point | 
**NeutralKillsAvg** | **float64** | Average neutral (jungle) creeps killed at this time point | 
**NeutralKillsStd** | **float64** | Standard deviation of &#x60;neutral_kills_avg&#x60; at this time point | 
**PermanentBuffsAvg** | Pointer to **NullableFloat64** | Average permanent buff (power-up) pickups collected up to this time point. Only matches since build 6712 (2026-09-29) record pickup times, so only players with at least one timed permanent pickup count; &#x60;null&#x60; when there are none. | [optional] 
**PermanentBuffsStd** | Pointer to **NullableFloat64** | Standard deviation of &#x60;permanent_buffs_avg&#x60; at this time point; &#x60;null&#x60; when there are no players with timed permanent pickups. | [optional] 
**PlayerBarrieringAvg** | **float64** | Average barrier (shield) provided at this time point | 
**PlayerBarrieringStd** | **float64** | Standard deviation of &#x60;player_barriering_avg&#x60; at this time point | 
**PlayerDamageAvg** | **float64** | Average damage dealt to enemy heroes at this time point | 
**PlayerDamageStd** | **float64** | Standard deviation of &#x60;player_damage_avg&#x60; at this time point | 
**PlayerHealingAvg** | **float64** | Average healing done at this time point | 
**PlayerHealingStd** | **float64** | Standard deviation of &#x60;player_healing_avg&#x60; at this time point | 
**SelfDamageAvg** | **float64** | Average self-inflicted damage at this time point | 
**SelfDamageStd** | **float64** | Standard deviation of &#x60;self_damage_avg&#x60; at this time point | 

## Methods

### NewPlayerPerformanceCurvePoint

`func NewPlayerPerformanceCurvePoint(assistsAvg float64, assistsStd float64, bossDamageAvg float64, bossDamageStd float64, bossKillsAvg float64, bossKillsStd float64, creepDamageAvg float64, creepDamageStd float64, creepKillsAvg float64, creepKillsStd float64, deathsAvg float64, deathsStd float64, deniesAvg float64, deniesStd float64, gameTime int32, goldAbilityAssassinateAvg float64, goldAbilityAssassinateStd float64, goldAssistsAvg float64, goldAssistsStd float64, goldBossAvg float64, goldBossOrbAvg float64, goldBossOrbStd float64, goldBossStd float64, goldBreakableAvg float64, goldBreakableStd float64, goldDeathLossAvg float64, goldDeathLossStd float64, goldDeniedAvg float64, goldDeniedStd float64, goldItemCultistSacrificeAvg float64, goldItemCultistSacrificeStd float64, goldItemGooseEggAvg float64, goldItemGooseEggStd float64, goldItemTrophyCollectorAvg float64, goldItemTrophyCollectorStd float64, goldLaneCreepAvg float64, goldLaneCreepOrbsAvg float64, goldLaneCreepOrbsStd float64, goldLaneCreepStd float64, goldNeutralCreepAvg float64, goldNeutralCreepOrbsAvg float64, goldNeutralCreepOrbsStd float64, goldNeutralCreepStd float64, goldPlayerAvg float64, goldPlayerOrbsAvg float64, goldPlayerOrbsStd float64, goldPlayerStd float64, goldTeamBonusAvg float64, goldTeamBonusStd float64, goldTreasureAvg float64, goldTreasureStd float64, killsAvg float64, killsStd float64, netWorthAvg float64, netWorthStd float64, neutralDamageAvg float64, neutralDamageStd float64, neutralKillsAvg float64, neutralKillsStd float64, playerBarrieringAvg float64, playerBarrieringStd float64, playerDamageAvg float64, playerDamageStd float64, playerHealingAvg float64, playerHealingStd float64, selfDamageAvg float64, selfDamageStd float64, ) *PlayerPerformanceCurvePoint`

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


### GetBossDamageAvg

`func (o *PlayerPerformanceCurvePoint) GetBossDamageAvg() float64`

GetBossDamageAvg returns the BossDamageAvg field if non-nil, zero value otherwise.

### GetBossDamageAvgOk

`func (o *PlayerPerformanceCurvePoint) GetBossDamageAvgOk() (*float64, bool)`

GetBossDamageAvgOk returns a tuple with the BossDamageAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBossDamageAvg

`func (o *PlayerPerformanceCurvePoint) SetBossDamageAvg(v float64)`

SetBossDamageAvg sets BossDamageAvg field to given value.


### GetBossDamageStd

`func (o *PlayerPerformanceCurvePoint) GetBossDamageStd() float64`

GetBossDamageStd returns the BossDamageStd field if non-nil, zero value otherwise.

### GetBossDamageStdOk

`func (o *PlayerPerformanceCurvePoint) GetBossDamageStdOk() (*float64, bool)`

GetBossDamageStdOk returns a tuple with the BossDamageStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBossDamageStd

`func (o *PlayerPerformanceCurvePoint) SetBossDamageStd(v float64)`

SetBossDamageStd sets BossDamageStd field to given value.


### GetBossKillsAvg

`func (o *PlayerPerformanceCurvePoint) GetBossKillsAvg() float64`

GetBossKillsAvg returns the BossKillsAvg field if non-nil, zero value otherwise.

### GetBossKillsAvgOk

`func (o *PlayerPerformanceCurvePoint) GetBossKillsAvgOk() (*float64, bool)`

GetBossKillsAvgOk returns a tuple with the BossKillsAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBossKillsAvg

`func (o *PlayerPerformanceCurvePoint) SetBossKillsAvg(v float64)`

SetBossKillsAvg sets BossKillsAvg field to given value.


### GetBossKillsStd

`func (o *PlayerPerformanceCurvePoint) GetBossKillsStd() float64`

GetBossKillsStd returns the BossKillsStd field if non-nil, zero value otherwise.

### GetBossKillsStdOk

`func (o *PlayerPerformanceCurvePoint) GetBossKillsStdOk() (*float64, bool)`

GetBossKillsStdOk returns a tuple with the BossKillsStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBossKillsStd

`func (o *PlayerPerformanceCurvePoint) SetBossKillsStd(v float64)`

SetBossKillsStd sets BossKillsStd field to given value.


### GetCreepDamageAvg

`func (o *PlayerPerformanceCurvePoint) GetCreepDamageAvg() float64`

GetCreepDamageAvg returns the CreepDamageAvg field if non-nil, zero value otherwise.

### GetCreepDamageAvgOk

`func (o *PlayerPerformanceCurvePoint) GetCreepDamageAvgOk() (*float64, bool)`

GetCreepDamageAvgOk returns a tuple with the CreepDamageAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreepDamageAvg

`func (o *PlayerPerformanceCurvePoint) SetCreepDamageAvg(v float64)`

SetCreepDamageAvg sets CreepDamageAvg field to given value.


### GetCreepDamageStd

`func (o *PlayerPerformanceCurvePoint) GetCreepDamageStd() float64`

GetCreepDamageStd returns the CreepDamageStd field if non-nil, zero value otherwise.

### GetCreepDamageStdOk

`func (o *PlayerPerformanceCurvePoint) GetCreepDamageStdOk() (*float64, bool)`

GetCreepDamageStdOk returns a tuple with the CreepDamageStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreepDamageStd

`func (o *PlayerPerformanceCurvePoint) SetCreepDamageStd(v float64)`

SetCreepDamageStd sets CreepDamageStd field to given value.


### GetCreepKillsAvg

`func (o *PlayerPerformanceCurvePoint) GetCreepKillsAvg() float64`

GetCreepKillsAvg returns the CreepKillsAvg field if non-nil, zero value otherwise.

### GetCreepKillsAvgOk

`func (o *PlayerPerformanceCurvePoint) GetCreepKillsAvgOk() (*float64, bool)`

GetCreepKillsAvgOk returns a tuple with the CreepKillsAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreepKillsAvg

`func (o *PlayerPerformanceCurvePoint) SetCreepKillsAvg(v float64)`

SetCreepKillsAvg sets CreepKillsAvg field to given value.


### GetCreepKillsStd

`func (o *PlayerPerformanceCurvePoint) GetCreepKillsStd() float64`

GetCreepKillsStd returns the CreepKillsStd field if non-nil, zero value otherwise.

### GetCreepKillsStdOk

`func (o *PlayerPerformanceCurvePoint) GetCreepKillsStdOk() (*float64, bool)`

GetCreepKillsStdOk returns a tuple with the CreepKillsStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreepKillsStd

`func (o *PlayerPerformanceCurvePoint) SetCreepKillsStd(v float64)`

SetCreepKillsStd sets CreepKillsStd field to given value.


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


### GetDeniesAvg

`func (o *PlayerPerformanceCurvePoint) GetDeniesAvg() float64`

GetDeniesAvg returns the DeniesAvg field if non-nil, zero value otherwise.

### GetDeniesAvgOk

`func (o *PlayerPerformanceCurvePoint) GetDeniesAvgOk() (*float64, bool)`

GetDeniesAvgOk returns a tuple with the DeniesAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeniesAvg

`func (o *PlayerPerformanceCurvePoint) SetDeniesAvg(v float64)`

SetDeniesAvg sets DeniesAvg field to given value.


### GetDeniesStd

`func (o *PlayerPerformanceCurvePoint) GetDeniesStd() float64`

GetDeniesStd returns the DeniesStd field if non-nil, zero value otherwise.

### GetDeniesStdOk

`func (o *PlayerPerformanceCurvePoint) GetDeniesStdOk() (*float64, bool)`

GetDeniesStdOk returns a tuple with the DeniesStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeniesStd

`func (o *PlayerPerformanceCurvePoint) SetDeniesStd(v float64)`

SetDeniesStd sets DeniesStd field to given value.


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


### GetGoldAbilityAssassinateAvg

`func (o *PlayerPerformanceCurvePoint) GetGoldAbilityAssassinateAvg() float64`

GetGoldAbilityAssassinateAvg returns the GoldAbilityAssassinateAvg field if non-nil, zero value otherwise.

### GetGoldAbilityAssassinateAvgOk

`func (o *PlayerPerformanceCurvePoint) GetGoldAbilityAssassinateAvgOk() (*float64, bool)`

GetGoldAbilityAssassinateAvgOk returns a tuple with the GoldAbilityAssassinateAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldAbilityAssassinateAvg

`func (o *PlayerPerformanceCurvePoint) SetGoldAbilityAssassinateAvg(v float64)`

SetGoldAbilityAssassinateAvg sets GoldAbilityAssassinateAvg field to given value.


### GetGoldAbilityAssassinateStd

`func (o *PlayerPerformanceCurvePoint) GetGoldAbilityAssassinateStd() float64`

GetGoldAbilityAssassinateStd returns the GoldAbilityAssassinateStd field if non-nil, zero value otherwise.

### GetGoldAbilityAssassinateStdOk

`func (o *PlayerPerformanceCurvePoint) GetGoldAbilityAssassinateStdOk() (*float64, bool)`

GetGoldAbilityAssassinateStdOk returns a tuple with the GoldAbilityAssassinateStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldAbilityAssassinateStd

`func (o *PlayerPerformanceCurvePoint) SetGoldAbilityAssassinateStd(v float64)`

SetGoldAbilityAssassinateStd sets GoldAbilityAssassinateStd field to given value.


### GetGoldAssistsAvg

`func (o *PlayerPerformanceCurvePoint) GetGoldAssistsAvg() float64`

GetGoldAssistsAvg returns the GoldAssistsAvg field if non-nil, zero value otherwise.

### GetGoldAssistsAvgOk

`func (o *PlayerPerformanceCurvePoint) GetGoldAssistsAvgOk() (*float64, bool)`

GetGoldAssistsAvgOk returns a tuple with the GoldAssistsAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldAssistsAvg

`func (o *PlayerPerformanceCurvePoint) SetGoldAssistsAvg(v float64)`

SetGoldAssistsAvg sets GoldAssistsAvg field to given value.


### GetGoldAssistsStd

`func (o *PlayerPerformanceCurvePoint) GetGoldAssistsStd() float64`

GetGoldAssistsStd returns the GoldAssistsStd field if non-nil, zero value otherwise.

### GetGoldAssistsStdOk

`func (o *PlayerPerformanceCurvePoint) GetGoldAssistsStdOk() (*float64, bool)`

GetGoldAssistsStdOk returns a tuple with the GoldAssistsStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldAssistsStd

`func (o *PlayerPerformanceCurvePoint) SetGoldAssistsStd(v float64)`

SetGoldAssistsStd sets GoldAssistsStd field to given value.


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


### GetGoldBossOrbStd

`func (o *PlayerPerformanceCurvePoint) GetGoldBossOrbStd() float64`

GetGoldBossOrbStd returns the GoldBossOrbStd field if non-nil, zero value otherwise.

### GetGoldBossOrbStdOk

`func (o *PlayerPerformanceCurvePoint) GetGoldBossOrbStdOk() (*float64, bool)`

GetGoldBossOrbStdOk returns a tuple with the GoldBossOrbStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldBossOrbStd

`func (o *PlayerPerformanceCurvePoint) SetGoldBossOrbStd(v float64)`

SetGoldBossOrbStd sets GoldBossOrbStd field to given value.


### GetGoldBossStd

`func (o *PlayerPerformanceCurvePoint) GetGoldBossStd() float64`

GetGoldBossStd returns the GoldBossStd field if non-nil, zero value otherwise.

### GetGoldBossStdOk

`func (o *PlayerPerformanceCurvePoint) GetGoldBossStdOk() (*float64, bool)`

GetGoldBossStdOk returns a tuple with the GoldBossStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldBossStd

`func (o *PlayerPerformanceCurvePoint) SetGoldBossStd(v float64)`

SetGoldBossStd sets GoldBossStd field to given value.


### GetGoldBreakableAvg

`func (o *PlayerPerformanceCurvePoint) GetGoldBreakableAvg() float64`

GetGoldBreakableAvg returns the GoldBreakableAvg field if non-nil, zero value otherwise.

### GetGoldBreakableAvgOk

`func (o *PlayerPerformanceCurvePoint) GetGoldBreakableAvgOk() (*float64, bool)`

GetGoldBreakableAvgOk returns a tuple with the GoldBreakableAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldBreakableAvg

`func (o *PlayerPerformanceCurvePoint) SetGoldBreakableAvg(v float64)`

SetGoldBreakableAvg sets GoldBreakableAvg field to given value.


### GetGoldBreakableStd

`func (o *PlayerPerformanceCurvePoint) GetGoldBreakableStd() float64`

GetGoldBreakableStd returns the GoldBreakableStd field if non-nil, zero value otherwise.

### GetGoldBreakableStdOk

`func (o *PlayerPerformanceCurvePoint) GetGoldBreakableStdOk() (*float64, bool)`

GetGoldBreakableStdOk returns a tuple with the GoldBreakableStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldBreakableStd

`func (o *PlayerPerformanceCurvePoint) SetGoldBreakableStd(v float64)`

SetGoldBreakableStd sets GoldBreakableStd field to given value.


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


### GetGoldDeathLossStd

`func (o *PlayerPerformanceCurvePoint) GetGoldDeathLossStd() float64`

GetGoldDeathLossStd returns the GoldDeathLossStd field if non-nil, zero value otherwise.

### GetGoldDeathLossStdOk

`func (o *PlayerPerformanceCurvePoint) GetGoldDeathLossStdOk() (*float64, bool)`

GetGoldDeathLossStdOk returns a tuple with the GoldDeathLossStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldDeathLossStd

`func (o *PlayerPerformanceCurvePoint) SetGoldDeathLossStd(v float64)`

SetGoldDeathLossStd sets GoldDeathLossStd field to given value.


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


### GetGoldDeniedStd

`func (o *PlayerPerformanceCurvePoint) GetGoldDeniedStd() float64`

GetGoldDeniedStd returns the GoldDeniedStd field if non-nil, zero value otherwise.

### GetGoldDeniedStdOk

`func (o *PlayerPerformanceCurvePoint) GetGoldDeniedStdOk() (*float64, bool)`

GetGoldDeniedStdOk returns a tuple with the GoldDeniedStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldDeniedStd

`func (o *PlayerPerformanceCurvePoint) SetGoldDeniedStd(v float64)`

SetGoldDeniedStd sets GoldDeniedStd field to given value.


### GetGoldItemCultistSacrificeAvg

`func (o *PlayerPerformanceCurvePoint) GetGoldItemCultistSacrificeAvg() float64`

GetGoldItemCultistSacrificeAvg returns the GoldItemCultistSacrificeAvg field if non-nil, zero value otherwise.

### GetGoldItemCultistSacrificeAvgOk

`func (o *PlayerPerformanceCurvePoint) GetGoldItemCultistSacrificeAvgOk() (*float64, bool)`

GetGoldItemCultistSacrificeAvgOk returns a tuple with the GoldItemCultistSacrificeAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldItemCultistSacrificeAvg

`func (o *PlayerPerformanceCurvePoint) SetGoldItemCultistSacrificeAvg(v float64)`

SetGoldItemCultistSacrificeAvg sets GoldItemCultistSacrificeAvg field to given value.


### GetGoldItemCultistSacrificeStd

`func (o *PlayerPerformanceCurvePoint) GetGoldItemCultistSacrificeStd() float64`

GetGoldItemCultistSacrificeStd returns the GoldItemCultistSacrificeStd field if non-nil, zero value otherwise.

### GetGoldItemCultistSacrificeStdOk

`func (o *PlayerPerformanceCurvePoint) GetGoldItemCultistSacrificeStdOk() (*float64, bool)`

GetGoldItemCultistSacrificeStdOk returns a tuple with the GoldItemCultistSacrificeStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldItemCultistSacrificeStd

`func (o *PlayerPerformanceCurvePoint) SetGoldItemCultistSacrificeStd(v float64)`

SetGoldItemCultistSacrificeStd sets GoldItemCultistSacrificeStd field to given value.


### GetGoldItemGooseEggAvg

`func (o *PlayerPerformanceCurvePoint) GetGoldItemGooseEggAvg() float64`

GetGoldItemGooseEggAvg returns the GoldItemGooseEggAvg field if non-nil, zero value otherwise.

### GetGoldItemGooseEggAvgOk

`func (o *PlayerPerformanceCurvePoint) GetGoldItemGooseEggAvgOk() (*float64, bool)`

GetGoldItemGooseEggAvgOk returns a tuple with the GoldItemGooseEggAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldItemGooseEggAvg

`func (o *PlayerPerformanceCurvePoint) SetGoldItemGooseEggAvg(v float64)`

SetGoldItemGooseEggAvg sets GoldItemGooseEggAvg field to given value.


### GetGoldItemGooseEggStd

`func (o *PlayerPerformanceCurvePoint) GetGoldItemGooseEggStd() float64`

GetGoldItemGooseEggStd returns the GoldItemGooseEggStd field if non-nil, zero value otherwise.

### GetGoldItemGooseEggStdOk

`func (o *PlayerPerformanceCurvePoint) GetGoldItemGooseEggStdOk() (*float64, bool)`

GetGoldItemGooseEggStdOk returns a tuple with the GoldItemGooseEggStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldItemGooseEggStd

`func (o *PlayerPerformanceCurvePoint) SetGoldItemGooseEggStd(v float64)`

SetGoldItemGooseEggStd sets GoldItemGooseEggStd field to given value.


### GetGoldItemTrophyCollectorAvg

`func (o *PlayerPerformanceCurvePoint) GetGoldItemTrophyCollectorAvg() float64`

GetGoldItemTrophyCollectorAvg returns the GoldItemTrophyCollectorAvg field if non-nil, zero value otherwise.

### GetGoldItemTrophyCollectorAvgOk

`func (o *PlayerPerformanceCurvePoint) GetGoldItemTrophyCollectorAvgOk() (*float64, bool)`

GetGoldItemTrophyCollectorAvgOk returns a tuple with the GoldItemTrophyCollectorAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldItemTrophyCollectorAvg

`func (o *PlayerPerformanceCurvePoint) SetGoldItemTrophyCollectorAvg(v float64)`

SetGoldItemTrophyCollectorAvg sets GoldItemTrophyCollectorAvg field to given value.


### GetGoldItemTrophyCollectorStd

`func (o *PlayerPerformanceCurvePoint) GetGoldItemTrophyCollectorStd() float64`

GetGoldItemTrophyCollectorStd returns the GoldItemTrophyCollectorStd field if non-nil, zero value otherwise.

### GetGoldItemTrophyCollectorStdOk

`func (o *PlayerPerformanceCurvePoint) GetGoldItemTrophyCollectorStdOk() (*float64, bool)`

GetGoldItemTrophyCollectorStdOk returns a tuple with the GoldItemTrophyCollectorStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldItemTrophyCollectorStd

`func (o *PlayerPerformanceCurvePoint) SetGoldItemTrophyCollectorStd(v float64)`

SetGoldItemTrophyCollectorStd sets GoldItemTrophyCollectorStd field to given value.


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


### GetGoldLaneCreepOrbsStd

`func (o *PlayerPerformanceCurvePoint) GetGoldLaneCreepOrbsStd() float64`

GetGoldLaneCreepOrbsStd returns the GoldLaneCreepOrbsStd field if non-nil, zero value otherwise.

### GetGoldLaneCreepOrbsStdOk

`func (o *PlayerPerformanceCurvePoint) GetGoldLaneCreepOrbsStdOk() (*float64, bool)`

GetGoldLaneCreepOrbsStdOk returns a tuple with the GoldLaneCreepOrbsStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldLaneCreepOrbsStd

`func (o *PlayerPerformanceCurvePoint) SetGoldLaneCreepOrbsStd(v float64)`

SetGoldLaneCreepOrbsStd sets GoldLaneCreepOrbsStd field to given value.


### GetGoldLaneCreepStd

`func (o *PlayerPerformanceCurvePoint) GetGoldLaneCreepStd() float64`

GetGoldLaneCreepStd returns the GoldLaneCreepStd field if non-nil, zero value otherwise.

### GetGoldLaneCreepStdOk

`func (o *PlayerPerformanceCurvePoint) GetGoldLaneCreepStdOk() (*float64, bool)`

GetGoldLaneCreepStdOk returns a tuple with the GoldLaneCreepStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldLaneCreepStd

`func (o *PlayerPerformanceCurvePoint) SetGoldLaneCreepStd(v float64)`

SetGoldLaneCreepStd sets GoldLaneCreepStd field to given value.


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


### GetGoldNeutralCreepOrbsStd

`func (o *PlayerPerformanceCurvePoint) GetGoldNeutralCreepOrbsStd() float64`

GetGoldNeutralCreepOrbsStd returns the GoldNeutralCreepOrbsStd field if non-nil, zero value otherwise.

### GetGoldNeutralCreepOrbsStdOk

`func (o *PlayerPerformanceCurvePoint) GetGoldNeutralCreepOrbsStdOk() (*float64, bool)`

GetGoldNeutralCreepOrbsStdOk returns a tuple with the GoldNeutralCreepOrbsStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldNeutralCreepOrbsStd

`func (o *PlayerPerformanceCurvePoint) SetGoldNeutralCreepOrbsStd(v float64)`

SetGoldNeutralCreepOrbsStd sets GoldNeutralCreepOrbsStd field to given value.


### GetGoldNeutralCreepStd

`func (o *PlayerPerformanceCurvePoint) GetGoldNeutralCreepStd() float64`

GetGoldNeutralCreepStd returns the GoldNeutralCreepStd field if non-nil, zero value otherwise.

### GetGoldNeutralCreepStdOk

`func (o *PlayerPerformanceCurvePoint) GetGoldNeutralCreepStdOk() (*float64, bool)`

GetGoldNeutralCreepStdOk returns a tuple with the GoldNeutralCreepStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldNeutralCreepStd

`func (o *PlayerPerformanceCurvePoint) SetGoldNeutralCreepStd(v float64)`

SetGoldNeutralCreepStd sets GoldNeutralCreepStd field to given value.


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


### GetGoldPlayerOrbsStd

`func (o *PlayerPerformanceCurvePoint) GetGoldPlayerOrbsStd() float64`

GetGoldPlayerOrbsStd returns the GoldPlayerOrbsStd field if non-nil, zero value otherwise.

### GetGoldPlayerOrbsStdOk

`func (o *PlayerPerformanceCurvePoint) GetGoldPlayerOrbsStdOk() (*float64, bool)`

GetGoldPlayerOrbsStdOk returns a tuple with the GoldPlayerOrbsStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldPlayerOrbsStd

`func (o *PlayerPerformanceCurvePoint) SetGoldPlayerOrbsStd(v float64)`

SetGoldPlayerOrbsStd sets GoldPlayerOrbsStd field to given value.


### GetGoldPlayerStd

`func (o *PlayerPerformanceCurvePoint) GetGoldPlayerStd() float64`

GetGoldPlayerStd returns the GoldPlayerStd field if non-nil, zero value otherwise.

### GetGoldPlayerStdOk

`func (o *PlayerPerformanceCurvePoint) GetGoldPlayerStdOk() (*float64, bool)`

GetGoldPlayerStdOk returns a tuple with the GoldPlayerStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldPlayerStd

`func (o *PlayerPerformanceCurvePoint) SetGoldPlayerStd(v float64)`

SetGoldPlayerStd sets GoldPlayerStd field to given value.


### GetGoldTeamBonusAvg

`func (o *PlayerPerformanceCurvePoint) GetGoldTeamBonusAvg() float64`

GetGoldTeamBonusAvg returns the GoldTeamBonusAvg field if non-nil, zero value otherwise.

### GetGoldTeamBonusAvgOk

`func (o *PlayerPerformanceCurvePoint) GetGoldTeamBonusAvgOk() (*float64, bool)`

GetGoldTeamBonusAvgOk returns a tuple with the GoldTeamBonusAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldTeamBonusAvg

`func (o *PlayerPerformanceCurvePoint) SetGoldTeamBonusAvg(v float64)`

SetGoldTeamBonusAvg sets GoldTeamBonusAvg field to given value.


### GetGoldTeamBonusStd

`func (o *PlayerPerformanceCurvePoint) GetGoldTeamBonusStd() float64`

GetGoldTeamBonusStd returns the GoldTeamBonusStd field if non-nil, zero value otherwise.

### GetGoldTeamBonusStdOk

`func (o *PlayerPerformanceCurvePoint) GetGoldTeamBonusStdOk() (*float64, bool)`

GetGoldTeamBonusStdOk returns a tuple with the GoldTeamBonusStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldTeamBonusStd

`func (o *PlayerPerformanceCurvePoint) SetGoldTeamBonusStd(v float64)`

SetGoldTeamBonusStd sets GoldTeamBonusStd field to given value.


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


### GetGoldTreasureStd

`func (o *PlayerPerformanceCurvePoint) GetGoldTreasureStd() float64`

GetGoldTreasureStd returns the GoldTreasureStd field if non-nil, zero value otherwise.

### GetGoldTreasureStdOk

`func (o *PlayerPerformanceCurvePoint) GetGoldTreasureStdOk() (*float64, bool)`

GetGoldTreasureStdOk returns a tuple with the GoldTreasureStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGoldTreasureStd

`func (o *PlayerPerformanceCurvePoint) SetGoldTreasureStd(v float64)`

SetGoldTreasureStd sets GoldTreasureStd field to given value.


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


### GetNeutralDamageAvg

`func (o *PlayerPerformanceCurvePoint) GetNeutralDamageAvg() float64`

GetNeutralDamageAvg returns the NeutralDamageAvg field if non-nil, zero value otherwise.

### GetNeutralDamageAvgOk

`func (o *PlayerPerformanceCurvePoint) GetNeutralDamageAvgOk() (*float64, bool)`

GetNeutralDamageAvgOk returns a tuple with the NeutralDamageAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNeutralDamageAvg

`func (o *PlayerPerformanceCurvePoint) SetNeutralDamageAvg(v float64)`

SetNeutralDamageAvg sets NeutralDamageAvg field to given value.


### GetNeutralDamageStd

`func (o *PlayerPerformanceCurvePoint) GetNeutralDamageStd() float64`

GetNeutralDamageStd returns the NeutralDamageStd field if non-nil, zero value otherwise.

### GetNeutralDamageStdOk

`func (o *PlayerPerformanceCurvePoint) GetNeutralDamageStdOk() (*float64, bool)`

GetNeutralDamageStdOk returns a tuple with the NeutralDamageStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNeutralDamageStd

`func (o *PlayerPerformanceCurvePoint) SetNeutralDamageStd(v float64)`

SetNeutralDamageStd sets NeutralDamageStd field to given value.


### GetNeutralKillsAvg

`func (o *PlayerPerformanceCurvePoint) GetNeutralKillsAvg() float64`

GetNeutralKillsAvg returns the NeutralKillsAvg field if non-nil, zero value otherwise.

### GetNeutralKillsAvgOk

`func (o *PlayerPerformanceCurvePoint) GetNeutralKillsAvgOk() (*float64, bool)`

GetNeutralKillsAvgOk returns a tuple with the NeutralKillsAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNeutralKillsAvg

`func (o *PlayerPerformanceCurvePoint) SetNeutralKillsAvg(v float64)`

SetNeutralKillsAvg sets NeutralKillsAvg field to given value.


### GetNeutralKillsStd

`func (o *PlayerPerformanceCurvePoint) GetNeutralKillsStd() float64`

GetNeutralKillsStd returns the NeutralKillsStd field if non-nil, zero value otherwise.

### GetNeutralKillsStdOk

`func (o *PlayerPerformanceCurvePoint) GetNeutralKillsStdOk() (*float64, bool)`

GetNeutralKillsStdOk returns a tuple with the NeutralKillsStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNeutralKillsStd

`func (o *PlayerPerformanceCurvePoint) SetNeutralKillsStd(v float64)`

SetNeutralKillsStd sets NeutralKillsStd field to given value.


### GetPermanentBuffsAvg

`func (o *PlayerPerformanceCurvePoint) GetPermanentBuffsAvg() float64`

GetPermanentBuffsAvg returns the PermanentBuffsAvg field if non-nil, zero value otherwise.

### GetPermanentBuffsAvgOk

`func (o *PlayerPerformanceCurvePoint) GetPermanentBuffsAvgOk() (*float64, bool)`

GetPermanentBuffsAvgOk returns a tuple with the PermanentBuffsAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPermanentBuffsAvg

`func (o *PlayerPerformanceCurvePoint) SetPermanentBuffsAvg(v float64)`

SetPermanentBuffsAvg sets PermanentBuffsAvg field to given value.

### HasPermanentBuffsAvg

`func (o *PlayerPerformanceCurvePoint) HasPermanentBuffsAvg() bool`

HasPermanentBuffsAvg returns a boolean if a field has been set.

### SetPermanentBuffsAvgNil

`func (o *PlayerPerformanceCurvePoint) SetPermanentBuffsAvgNil(b bool)`

 SetPermanentBuffsAvgNil sets the value for PermanentBuffsAvg to be an explicit nil

### UnsetPermanentBuffsAvg
`func (o *PlayerPerformanceCurvePoint) UnsetPermanentBuffsAvg()`

UnsetPermanentBuffsAvg ensures that no value is present for PermanentBuffsAvg, not even an explicit nil
### GetPermanentBuffsStd

`func (o *PlayerPerformanceCurvePoint) GetPermanentBuffsStd() float64`

GetPermanentBuffsStd returns the PermanentBuffsStd field if non-nil, zero value otherwise.

### GetPermanentBuffsStdOk

`func (o *PlayerPerformanceCurvePoint) GetPermanentBuffsStdOk() (*float64, bool)`

GetPermanentBuffsStdOk returns a tuple with the PermanentBuffsStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPermanentBuffsStd

`func (o *PlayerPerformanceCurvePoint) SetPermanentBuffsStd(v float64)`

SetPermanentBuffsStd sets PermanentBuffsStd field to given value.

### HasPermanentBuffsStd

`func (o *PlayerPerformanceCurvePoint) HasPermanentBuffsStd() bool`

HasPermanentBuffsStd returns a boolean if a field has been set.

### SetPermanentBuffsStdNil

`func (o *PlayerPerformanceCurvePoint) SetPermanentBuffsStdNil(b bool)`

 SetPermanentBuffsStdNil sets the value for PermanentBuffsStd to be an explicit nil

### UnsetPermanentBuffsStd
`func (o *PlayerPerformanceCurvePoint) UnsetPermanentBuffsStd()`

UnsetPermanentBuffsStd ensures that no value is present for PermanentBuffsStd, not even an explicit nil
### GetPlayerBarrieringAvg

`func (o *PlayerPerformanceCurvePoint) GetPlayerBarrieringAvg() float64`

GetPlayerBarrieringAvg returns the PlayerBarrieringAvg field if non-nil, zero value otherwise.

### GetPlayerBarrieringAvgOk

`func (o *PlayerPerformanceCurvePoint) GetPlayerBarrieringAvgOk() (*float64, bool)`

GetPlayerBarrieringAvgOk returns a tuple with the PlayerBarrieringAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerBarrieringAvg

`func (o *PlayerPerformanceCurvePoint) SetPlayerBarrieringAvg(v float64)`

SetPlayerBarrieringAvg sets PlayerBarrieringAvg field to given value.


### GetPlayerBarrieringStd

`func (o *PlayerPerformanceCurvePoint) GetPlayerBarrieringStd() float64`

GetPlayerBarrieringStd returns the PlayerBarrieringStd field if non-nil, zero value otherwise.

### GetPlayerBarrieringStdOk

`func (o *PlayerPerformanceCurvePoint) GetPlayerBarrieringStdOk() (*float64, bool)`

GetPlayerBarrieringStdOk returns a tuple with the PlayerBarrieringStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerBarrieringStd

`func (o *PlayerPerformanceCurvePoint) SetPlayerBarrieringStd(v float64)`

SetPlayerBarrieringStd sets PlayerBarrieringStd field to given value.


### GetPlayerDamageAvg

`func (o *PlayerPerformanceCurvePoint) GetPlayerDamageAvg() float64`

GetPlayerDamageAvg returns the PlayerDamageAvg field if non-nil, zero value otherwise.

### GetPlayerDamageAvgOk

`func (o *PlayerPerformanceCurvePoint) GetPlayerDamageAvgOk() (*float64, bool)`

GetPlayerDamageAvgOk returns a tuple with the PlayerDamageAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerDamageAvg

`func (o *PlayerPerformanceCurvePoint) SetPlayerDamageAvg(v float64)`

SetPlayerDamageAvg sets PlayerDamageAvg field to given value.


### GetPlayerDamageStd

`func (o *PlayerPerformanceCurvePoint) GetPlayerDamageStd() float64`

GetPlayerDamageStd returns the PlayerDamageStd field if non-nil, zero value otherwise.

### GetPlayerDamageStdOk

`func (o *PlayerPerformanceCurvePoint) GetPlayerDamageStdOk() (*float64, bool)`

GetPlayerDamageStdOk returns a tuple with the PlayerDamageStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerDamageStd

`func (o *PlayerPerformanceCurvePoint) SetPlayerDamageStd(v float64)`

SetPlayerDamageStd sets PlayerDamageStd field to given value.


### GetPlayerHealingAvg

`func (o *PlayerPerformanceCurvePoint) GetPlayerHealingAvg() float64`

GetPlayerHealingAvg returns the PlayerHealingAvg field if non-nil, zero value otherwise.

### GetPlayerHealingAvgOk

`func (o *PlayerPerformanceCurvePoint) GetPlayerHealingAvgOk() (*float64, bool)`

GetPlayerHealingAvgOk returns a tuple with the PlayerHealingAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerHealingAvg

`func (o *PlayerPerformanceCurvePoint) SetPlayerHealingAvg(v float64)`

SetPlayerHealingAvg sets PlayerHealingAvg field to given value.


### GetPlayerHealingStd

`func (o *PlayerPerformanceCurvePoint) GetPlayerHealingStd() float64`

GetPlayerHealingStd returns the PlayerHealingStd field if non-nil, zero value otherwise.

### GetPlayerHealingStdOk

`func (o *PlayerPerformanceCurvePoint) GetPlayerHealingStdOk() (*float64, bool)`

GetPlayerHealingStdOk returns a tuple with the PlayerHealingStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayerHealingStd

`func (o *PlayerPerformanceCurvePoint) SetPlayerHealingStd(v float64)`

SetPlayerHealingStd sets PlayerHealingStd field to given value.


### GetSelfDamageAvg

`func (o *PlayerPerformanceCurvePoint) GetSelfDamageAvg() float64`

GetSelfDamageAvg returns the SelfDamageAvg field if non-nil, zero value otherwise.

### GetSelfDamageAvgOk

`func (o *PlayerPerformanceCurvePoint) GetSelfDamageAvgOk() (*float64, bool)`

GetSelfDamageAvgOk returns a tuple with the SelfDamageAvg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSelfDamageAvg

`func (o *PlayerPerformanceCurvePoint) SetSelfDamageAvg(v float64)`

SetSelfDamageAvg sets SelfDamageAvg field to given value.


### GetSelfDamageStd

`func (o *PlayerPerformanceCurvePoint) GetSelfDamageStd() float64`

GetSelfDamageStd returns the SelfDamageStd field if non-nil, zero value otherwise.

### GetSelfDamageStdOk

`func (o *PlayerPerformanceCurvePoint) GetSelfDamageStdOk() (*float64, bool)`

GetSelfDamageStdOk returns a tuple with the SelfDamageStd field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSelfDamageStd

`func (o *PlayerPerformanceCurvePoint) SetSelfDamageStd(v float64)`

SetSelfDamageStd sets SelfDamageStd field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


