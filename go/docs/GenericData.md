# GenericData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AimSpringStrength** | **[]float64** |  | 
**ArmorGroups** | [**[]ItemGroup**](ItemGroup.md) |  | 
**DamageFlash** | [**DamageFlash**](DamageFlash.md) |  | 
**EnemyObjectivesAndZiplineColor** | Pointer to [**NullableColor**](Color.md) |  | [optional] 
**EnemyObjectivesColor** | Pointer to [**NullableColor**](Color.md) |  | [optional] 
**EnemyZiplineColor** | Pointer to [**NullableColor**](Color.md) |  | [optional] 
**GlitchSettings** | [**GlitchSettings**](GlitchSettings.md) |  | 
**HeroKillGoldShareFrac** | **[]float64** |  | 
**ItemPricePerTier** | **[]int64** |  | 
**LaneInfo** | [**[]LaneInfo**](LaneInfo.md) |  | 
**MiniMapOffsets** | [**[]MiniMapOffsets**](MiniMapOffsets.md) |  | 
**MinimapTeamCombineColor** | Pointer to [**NullableColor**](Color.md) |  | [optional] 
**MinimapTeamRebelsColor** | Pointer to [**NullableColor**](Color.md) |  | [optional] 
**NewPlayerMetrics** | [**[]NewPlayerMetrics**](NewPlayerMetrics.md) |  | 
**ObjectiveParams** | [**ObjectiveParams**](ObjectiveParams.md) |  | 
**RejuvParams** | [**RejuvParams**](RejuvParams.md) |  | 
**SpiritGroups** | [**[]ItemGroup**](ItemGroup.md) |  | 
**StreetBrawl** | Pointer to [**NullableStreetBrawl**](StreetBrawl.md) |  | [optional] 
**TargetingSpringStrength** | **[]float64** |  | 
**TrooperKillGoldShareFrac** | **[]float64** |  | 
**WeaponGroups** | [**[]ItemGroup**](ItemGroup.md) |  | 

## Methods

### NewGenericData

`func NewGenericData(aimSpringStrength []float64, armorGroups []ItemGroup, damageFlash DamageFlash, glitchSettings GlitchSettings, heroKillGoldShareFrac []float64, itemPricePerTier []int64, laneInfo []LaneInfo, miniMapOffsets []MiniMapOffsets, newPlayerMetrics []NewPlayerMetrics, objectiveParams ObjectiveParams, rejuvParams RejuvParams, spiritGroups []ItemGroup, targetingSpringStrength []float64, trooperKillGoldShareFrac []float64, weaponGroups []ItemGroup, ) *GenericData`

NewGenericData instantiates a new GenericData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGenericDataWithDefaults

`func NewGenericDataWithDefaults() *GenericData`

NewGenericDataWithDefaults instantiates a new GenericData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAimSpringStrength

`func (o *GenericData) GetAimSpringStrength() []float64`

GetAimSpringStrength returns the AimSpringStrength field if non-nil, zero value otherwise.

### GetAimSpringStrengthOk

`func (o *GenericData) GetAimSpringStrengthOk() (*[]float64, bool)`

GetAimSpringStrengthOk returns a tuple with the AimSpringStrength field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAimSpringStrength

`func (o *GenericData) SetAimSpringStrength(v []float64)`

SetAimSpringStrength sets AimSpringStrength field to given value.


### GetArmorGroups

`func (o *GenericData) GetArmorGroups() []ItemGroup`

GetArmorGroups returns the ArmorGroups field if non-nil, zero value otherwise.

### GetArmorGroupsOk

`func (o *GenericData) GetArmorGroupsOk() (*[]ItemGroup, bool)`

GetArmorGroupsOk returns a tuple with the ArmorGroups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArmorGroups

`func (o *GenericData) SetArmorGroups(v []ItemGroup)`

SetArmorGroups sets ArmorGroups field to given value.


### GetDamageFlash

`func (o *GenericData) GetDamageFlash() DamageFlash`

GetDamageFlash returns the DamageFlash field if non-nil, zero value otherwise.

### GetDamageFlashOk

`func (o *GenericData) GetDamageFlashOk() (*DamageFlash, bool)`

GetDamageFlashOk returns a tuple with the DamageFlash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamageFlash

`func (o *GenericData) SetDamageFlash(v DamageFlash)`

SetDamageFlash sets DamageFlash field to given value.


### GetEnemyObjectivesAndZiplineColor

`func (o *GenericData) GetEnemyObjectivesAndZiplineColor() Color`

GetEnemyObjectivesAndZiplineColor returns the EnemyObjectivesAndZiplineColor field if non-nil, zero value otherwise.

### GetEnemyObjectivesAndZiplineColorOk

`func (o *GenericData) GetEnemyObjectivesAndZiplineColorOk() (*Color, bool)`

GetEnemyObjectivesAndZiplineColorOk returns a tuple with the EnemyObjectivesAndZiplineColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyObjectivesAndZiplineColor

`func (o *GenericData) SetEnemyObjectivesAndZiplineColor(v Color)`

SetEnemyObjectivesAndZiplineColor sets EnemyObjectivesAndZiplineColor field to given value.

### HasEnemyObjectivesAndZiplineColor

`func (o *GenericData) HasEnemyObjectivesAndZiplineColor() bool`

HasEnemyObjectivesAndZiplineColor returns a boolean if a field has been set.

### SetEnemyObjectivesAndZiplineColorNil

`func (o *GenericData) SetEnemyObjectivesAndZiplineColorNil(b bool)`

 SetEnemyObjectivesAndZiplineColorNil sets the value for EnemyObjectivesAndZiplineColor to be an explicit nil

### UnsetEnemyObjectivesAndZiplineColor
`func (o *GenericData) UnsetEnemyObjectivesAndZiplineColor()`

UnsetEnemyObjectivesAndZiplineColor ensures that no value is present for EnemyObjectivesAndZiplineColor, not even an explicit nil
### GetEnemyObjectivesColor

`func (o *GenericData) GetEnemyObjectivesColor() Color`

GetEnemyObjectivesColor returns the EnemyObjectivesColor field if non-nil, zero value otherwise.

### GetEnemyObjectivesColorOk

`func (o *GenericData) GetEnemyObjectivesColorOk() (*Color, bool)`

GetEnemyObjectivesColorOk returns a tuple with the EnemyObjectivesColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyObjectivesColor

`func (o *GenericData) SetEnemyObjectivesColor(v Color)`

SetEnemyObjectivesColor sets EnemyObjectivesColor field to given value.

### HasEnemyObjectivesColor

`func (o *GenericData) HasEnemyObjectivesColor() bool`

HasEnemyObjectivesColor returns a boolean if a field has been set.

### SetEnemyObjectivesColorNil

`func (o *GenericData) SetEnemyObjectivesColorNil(b bool)`

 SetEnemyObjectivesColorNil sets the value for EnemyObjectivesColor to be an explicit nil

### UnsetEnemyObjectivesColor
`func (o *GenericData) UnsetEnemyObjectivesColor()`

UnsetEnemyObjectivesColor ensures that no value is present for EnemyObjectivesColor, not even an explicit nil
### GetEnemyZiplineColor

`func (o *GenericData) GetEnemyZiplineColor() Color`

GetEnemyZiplineColor returns the EnemyZiplineColor field if non-nil, zero value otherwise.

### GetEnemyZiplineColorOk

`func (o *GenericData) GetEnemyZiplineColorOk() (*Color, bool)`

GetEnemyZiplineColorOk returns a tuple with the EnemyZiplineColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyZiplineColor

`func (o *GenericData) SetEnemyZiplineColor(v Color)`

SetEnemyZiplineColor sets EnemyZiplineColor field to given value.

### HasEnemyZiplineColor

`func (o *GenericData) HasEnemyZiplineColor() bool`

HasEnemyZiplineColor returns a boolean if a field has been set.

### SetEnemyZiplineColorNil

`func (o *GenericData) SetEnemyZiplineColorNil(b bool)`

 SetEnemyZiplineColorNil sets the value for EnemyZiplineColor to be an explicit nil

### UnsetEnemyZiplineColor
`func (o *GenericData) UnsetEnemyZiplineColor()`

UnsetEnemyZiplineColor ensures that no value is present for EnemyZiplineColor, not even an explicit nil
### GetGlitchSettings

`func (o *GenericData) GetGlitchSettings() GlitchSettings`

GetGlitchSettings returns the GlitchSettings field if non-nil, zero value otherwise.

### GetGlitchSettingsOk

`func (o *GenericData) GetGlitchSettingsOk() (*GlitchSettings, bool)`

GetGlitchSettingsOk returns a tuple with the GlitchSettings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGlitchSettings

`func (o *GenericData) SetGlitchSettings(v GlitchSettings)`

SetGlitchSettings sets GlitchSettings field to given value.


### GetHeroKillGoldShareFrac

`func (o *GenericData) GetHeroKillGoldShareFrac() []float64`

GetHeroKillGoldShareFrac returns the HeroKillGoldShareFrac field if non-nil, zero value otherwise.

### GetHeroKillGoldShareFracOk

`func (o *GenericData) GetHeroKillGoldShareFracOk() (*[]float64, bool)`

GetHeroKillGoldShareFracOk returns a tuple with the HeroKillGoldShareFrac field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroKillGoldShareFrac

`func (o *GenericData) SetHeroKillGoldShareFrac(v []float64)`

SetHeroKillGoldShareFrac sets HeroKillGoldShareFrac field to given value.


### GetItemPricePerTier

`func (o *GenericData) GetItemPricePerTier() []int64`

GetItemPricePerTier returns the ItemPricePerTier field if non-nil, zero value otherwise.

### GetItemPricePerTierOk

`func (o *GenericData) GetItemPricePerTierOk() (*[]int64, bool)`

GetItemPricePerTierOk returns a tuple with the ItemPricePerTier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemPricePerTier

`func (o *GenericData) SetItemPricePerTier(v []int64)`

SetItemPricePerTier sets ItemPricePerTier field to given value.


### GetLaneInfo

`func (o *GenericData) GetLaneInfo() []LaneInfo`

GetLaneInfo returns the LaneInfo field if non-nil, zero value otherwise.

### GetLaneInfoOk

`func (o *GenericData) GetLaneInfoOk() (*[]LaneInfo, bool)`

GetLaneInfoOk returns a tuple with the LaneInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLaneInfo

`func (o *GenericData) SetLaneInfo(v []LaneInfo)`

SetLaneInfo sets LaneInfo field to given value.


### GetMiniMapOffsets

`func (o *GenericData) GetMiniMapOffsets() []MiniMapOffsets`

GetMiniMapOffsets returns the MiniMapOffsets field if non-nil, zero value otherwise.

### GetMiniMapOffsetsOk

`func (o *GenericData) GetMiniMapOffsetsOk() (*[]MiniMapOffsets, bool)`

GetMiniMapOffsetsOk returns a tuple with the MiniMapOffsets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMiniMapOffsets

`func (o *GenericData) SetMiniMapOffsets(v []MiniMapOffsets)`

SetMiniMapOffsets sets MiniMapOffsets field to given value.


### GetMinimapTeamCombineColor

`func (o *GenericData) GetMinimapTeamCombineColor() Color`

GetMinimapTeamCombineColor returns the MinimapTeamCombineColor field if non-nil, zero value otherwise.

### GetMinimapTeamCombineColorOk

`func (o *GenericData) GetMinimapTeamCombineColorOk() (*Color, bool)`

GetMinimapTeamCombineColorOk returns a tuple with the MinimapTeamCombineColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMinimapTeamCombineColor

`func (o *GenericData) SetMinimapTeamCombineColor(v Color)`

SetMinimapTeamCombineColor sets MinimapTeamCombineColor field to given value.

### HasMinimapTeamCombineColor

`func (o *GenericData) HasMinimapTeamCombineColor() bool`

HasMinimapTeamCombineColor returns a boolean if a field has been set.

### SetMinimapTeamCombineColorNil

`func (o *GenericData) SetMinimapTeamCombineColorNil(b bool)`

 SetMinimapTeamCombineColorNil sets the value for MinimapTeamCombineColor to be an explicit nil

### UnsetMinimapTeamCombineColor
`func (o *GenericData) UnsetMinimapTeamCombineColor()`

UnsetMinimapTeamCombineColor ensures that no value is present for MinimapTeamCombineColor, not even an explicit nil
### GetMinimapTeamRebelsColor

`func (o *GenericData) GetMinimapTeamRebelsColor() Color`

GetMinimapTeamRebelsColor returns the MinimapTeamRebelsColor field if non-nil, zero value otherwise.

### GetMinimapTeamRebelsColorOk

`func (o *GenericData) GetMinimapTeamRebelsColorOk() (*Color, bool)`

GetMinimapTeamRebelsColorOk returns a tuple with the MinimapTeamRebelsColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMinimapTeamRebelsColor

`func (o *GenericData) SetMinimapTeamRebelsColor(v Color)`

SetMinimapTeamRebelsColor sets MinimapTeamRebelsColor field to given value.

### HasMinimapTeamRebelsColor

`func (o *GenericData) HasMinimapTeamRebelsColor() bool`

HasMinimapTeamRebelsColor returns a boolean if a field has been set.

### SetMinimapTeamRebelsColorNil

`func (o *GenericData) SetMinimapTeamRebelsColorNil(b bool)`

 SetMinimapTeamRebelsColorNil sets the value for MinimapTeamRebelsColor to be an explicit nil

### UnsetMinimapTeamRebelsColor
`func (o *GenericData) UnsetMinimapTeamRebelsColor()`

UnsetMinimapTeamRebelsColor ensures that no value is present for MinimapTeamRebelsColor, not even an explicit nil
### GetNewPlayerMetrics

`func (o *GenericData) GetNewPlayerMetrics() []NewPlayerMetrics`

GetNewPlayerMetrics returns the NewPlayerMetrics field if non-nil, zero value otherwise.

### GetNewPlayerMetricsOk

`func (o *GenericData) GetNewPlayerMetricsOk() (*[]NewPlayerMetrics, bool)`

GetNewPlayerMetricsOk returns a tuple with the NewPlayerMetrics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNewPlayerMetrics

`func (o *GenericData) SetNewPlayerMetrics(v []NewPlayerMetrics)`

SetNewPlayerMetrics sets NewPlayerMetrics field to given value.


### GetObjectiveParams

`func (o *GenericData) GetObjectiveParams() ObjectiveParams`

GetObjectiveParams returns the ObjectiveParams field if non-nil, zero value otherwise.

### GetObjectiveParamsOk

`func (o *GenericData) GetObjectiveParamsOk() (*ObjectiveParams, bool)`

GetObjectiveParamsOk returns a tuple with the ObjectiveParams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectiveParams

`func (o *GenericData) SetObjectiveParams(v ObjectiveParams)`

SetObjectiveParams sets ObjectiveParams field to given value.


### GetRejuvParams

`func (o *GenericData) GetRejuvParams() RejuvParams`

GetRejuvParams returns the RejuvParams field if non-nil, zero value otherwise.

### GetRejuvParamsOk

`func (o *GenericData) GetRejuvParamsOk() (*RejuvParams, bool)`

GetRejuvParamsOk returns a tuple with the RejuvParams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRejuvParams

`func (o *GenericData) SetRejuvParams(v RejuvParams)`

SetRejuvParams sets RejuvParams field to given value.


### GetSpiritGroups

`func (o *GenericData) GetSpiritGroups() []ItemGroup`

GetSpiritGroups returns the SpiritGroups field if non-nil, zero value otherwise.

### GetSpiritGroupsOk

`func (o *GenericData) GetSpiritGroupsOk() (*[]ItemGroup, bool)`

GetSpiritGroupsOk returns a tuple with the SpiritGroups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpiritGroups

`func (o *GenericData) SetSpiritGroups(v []ItemGroup)`

SetSpiritGroups sets SpiritGroups field to given value.


### GetStreetBrawl

`func (o *GenericData) GetStreetBrawl() StreetBrawl`

GetStreetBrawl returns the StreetBrawl field if non-nil, zero value otherwise.

### GetStreetBrawlOk

`func (o *GenericData) GetStreetBrawlOk() (*StreetBrawl, bool)`

GetStreetBrawlOk returns a tuple with the StreetBrawl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStreetBrawl

`func (o *GenericData) SetStreetBrawl(v StreetBrawl)`

SetStreetBrawl sets StreetBrawl field to given value.

### HasStreetBrawl

`func (o *GenericData) HasStreetBrawl() bool`

HasStreetBrawl returns a boolean if a field has been set.

### SetStreetBrawlNil

`func (o *GenericData) SetStreetBrawlNil(b bool)`

 SetStreetBrawlNil sets the value for StreetBrawl to be an explicit nil

### UnsetStreetBrawl
`func (o *GenericData) UnsetStreetBrawl()`

UnsetStreetBrawl ensures that no value is present for StreetBrawl, not even an explicit nil
### GetTargetingSpringStrength

`func (o *GenericData) GetTargetingSpringStrength() []float64`

GetTargetingSpringStrength returns the TargetingSpringStrength field if non-nil, zero value otherwise.

### GetTargetingSpringStrengthOk

`func (o *GenericData) GetTargetingSpringStrengthOk() (*[]float64, bool)`

GetTargetingSpringStrengthOk returns a tuple with the TargetingSpringStrength field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetingSpringStrength

`func (o *GenericData) SetTargetingSpringStrength(v []float64)`

SetTargetingSpringStrength sets TargetingSpringStrength field to given value.


### GetTrooperKillGoldShareFrac

`func (o *GenericData) GetTrooperKillGoldShareFrac() []float64`

GetTrooperKillGoldShareFrac returns the TrooperKillGoldShareFrac field if non-nil, zero value otherwise.

### GetTrooperKillGoldShareFracOk

`func (o *GenericData) GetTrooperKillGoldShareFracOk() (*[]float64, bool)`

GetTrooperKillGoldShareFracOk returns a tuple with the TrooperKillGoldShareFrac field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrooperKillGoldShareFrac

`func (o *GenericData) SetTrooperKillGoldShareFrac(v []float64)`

SetTrooperKillGoldShareFrac sets TrooperKillGoldShareFrac field to given value.


### GetWeaponGroups

`func (o *GenericData) GetWeaponGroups() []ItemGroup`

GetWeaponGroups returns the WeaponGroups field if non-nil, zero value otherwise.

### GetWeaponGroupsOk

`func (o *GenericData) GetWeaponGroupsOk() (*[]ItemGroup, bool)`

GetWeaponGroupsOk returns a tuple with the WeaponGroups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponGroups

`func (o *GenericData) SetWeaponGroups(v []ItemGroup)`

SetWeaponGroups sets WeaponGroups field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


