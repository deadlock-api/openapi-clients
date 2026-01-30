# GenericDataV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DamageFlash** | [**DamageFlashV2**](DamageFlashV2.md) |  | 
**GlitchSettings** | [**GlitchSettingsV2**](GlitchSettingsV2.md) |  | 
**LaneInfo** | [**[]LaneInfoV2**](LaneInfoV2.md) |  | 
**NewPlayerMetrics** | [**[]NewPlayerMetricsV2**](NewPlayerMetricsV2.md) |  | 
**MinimapTeamRebelsColor** | Pointer to [**NullableColorV1**](ColorV1.md) |  | [optional] 
**MinimapTeamCombineColor** | Pointer to [**NullableColorV1**](ColorV1.md) |  | [optional] 
**EnemyObjectivesAndZiplineColor** | Pointer to [**NullableColorV1**](ColorV1.md) |  | [optional] 
**EnemyObjectivesColor** | Pointer to [**NullableColorV1**](ColorV1.md) |  | [optional] 
**EnemyZiplineColor** | Pointer to [**NullableColorV1**](ColorV1.md) |  | [optional] 
**ItemPricePerTier** | **[]int32** |  | 
**TrooperKillGoldShareFrac** | **[]float32** |  | 
**HeroKillGoldShareFrac** | **[]float32** |  | 
**AimSpringStrength** | **[]float32** |  | 
**TargetingSpringStrength** | **[]float32** |  | 
**ObjectiveParams** | [**ObjectiveParams**](ObjectiveParams.md) |  | 
**RejuvParams** | [**RejuvParams**](RejuvParams.md) |  | 
**MiniMapOffsets** | [**[]MiniMapOffsets**](MiniMapOffsets.md) |  | 
**WeaponGroups** | [**[]ItemGroup**](ItemGroup.md) |  | 
**ArmorGroups** | [**[]ItemGroup**](ItemGroup.md) |  | 
**SpiritGroups** | [**[]ItemGroup**](ItemGroup.md) |  | 
**StreetBrawl** | Pointer to [**NullableStreetBrawl**](StreetBrawl.md) |  | [optional] 

## Methods

### NewGenericDataV2

`func NewGenericDataV2(damageFlash DamageFlashV2, glitchSettings GlitchSettingsV2, laneInfo []LaneInfoV2, newPlayerMetrics []NewPlayerMetricsV2, itemPricePerTier []int32, trooperKillGoldShareFrac []float32, heroKillGoldShareFrac []float32, aimSpringStrength []float32, targetingSpringStrength []float32, objectiveParams ObjectiveParams, rejuvParams RejuvParams, miniMapOffsets []MiniMapOffsets, weaponGroups []ItemGroup, armorGroups []ItemGroup, spiritGroups []ItemGroup, ) *GenericDataV2`

NewGenericDataV2 instantiates a new GenericDataV2 object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGenericDataV2WithDefaults

`func NewGenericDataV2WithDefaults() *GenericDataV2`

NewGenericDataV2WithDefaults instantiates a new GenericDataV2 object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDamageFlash

`func (o *GenericDataV2) GetDamageFlash() DamageFlashV2`

GetDamageFlash returns the DamageFlash field if non-nil, zero value otherwise.

### GetDamageFlashOk

`func (o *GenericDataV2) GetDamageFlashOk() (*DamageFlashV2, bool)`

GetDamageFlashOk returns a tuple with the DamageFlash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDamageFlash

`func (o *GenericDataV2) SetDamageFlash(v DamageFlashV2)`

SetDamageFlash sets DamageFlash field to given value.


### GetGlitchSettings

`func (o *GenericDataV2) GetGlitchSettings() GlitchSettingsV2`

GetGlitchSettings returns the GlitchSettings field if non-nil, zero value otherwise.

### GetGlitchSettingsOk

`func (o *GenericDataV2) GetGlitchSettingsOk() (*GlitchSettingsV2, bool)`

GetGlitchSettingsOk returns a tuple with the GlitchSettings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGlitchSettings

`func (o *GenericDataV2) SetGlitchSettings(v GlitchSettingsV2)`

SetGlitchSettings sets GlitchSettings field to given value.


### GetLaneInfo

`func (o *GenericDataV2) GetLaneInfo() []LaneInfoV2`

GetLaneInfo returns the LaneInfo field if non-nil, zero value otherwise.

### GetLaneInfoOk

`func (o *GenericDataV2) GetLaneInfoOk() (*[]LaneInfoV2, bool)`

GetLaneInfoOk returns a tuple with the LaneInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLaneInfo

`func (o *GenericDataV2) SetLaneInfo(v []LaneInfoV2)`

SetLaneInfo sets LaneInfo field to given value.


### GetNewPlayerMetrics

`func (o *GenericDataV2) GetNewPlayerMetrics() []NewPlayerMetricsV2`

GetNewPlayerMetrics returns the NewPlayerMetrics field if non-nil, zero value otherwise.

### GetNewPlayerMetricsOk

`func (o *GenericDataV2) GetNewPlayerMetricsOk() (*[]NewPlayerMetricsV2, bool)`

GetNewPlayerMetricsOk returns a tuple with the NewPlayerMetrics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNewPlayerMetrics

`func (o *GenericDataV2) SetNewPlayerMetrics(v []NewPlayerMetricsV2)`

SetNewPlayerMetrics sets NewPlayerMetrics field to given value.


### GetMinimapTeamRebelsColor

`func (o *GenericDataV2) GetMinimapTeamRebelsColor() ColorV1`

GetMinimapTeamRebelsColor returns the MinimapTeamRebelsColor field if non-nil, zero value otherwise.

### GetMinimapTeamRebelsColorOk

`func (o *GenericDataV2) GetMinimapTeamRebelsColorOk() (*ColorV1, bool)`

GetMinimapTeamRebelsColorOk returns a tuple with the MinimapTeamRebelsColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMinimapTeamRebelsColor

`func (o *GenericDataV2) SetMinimapTeamRebelsColor(v ColorV1)`

SetMinimapTeamRebelsColor sets MinimapTeamRebelsColor field to given value.

### HasMinimapTeamRebelsColor

`func (o *GenericDataV2) HasMinimapTeamRebelsColor() bool`

HasMinimapTeamRebelsColor returns a boolean if a field has been set.

### SetMinimapTeamRebelsColorNil

`func (o *GenericDataV2) SetMinimapTeamRebelsColorNil(b bool)`

 SetMinimapTeamRebelsColorNil sets the value for MinimapTeamRebelsColor to be an explicit nil

### UnsetMinimapTeamRebelsColor
`func (o *GenericDataV2) UnsetMinimapTeamRebelsColor()`

UnsetMinimapTeamRebelsColor ensures that no value is present for MinimapTeamRebelsColor, not even an explicit nil
### GetMinimapTeamCombineColor

`func (o *GenericDataV2) GetMinimapTeamCombineColor() ColorV1`

GetMinimapTeamCombineColor returns the MinimapTeamCombineColor field if non-nil, zero value otherwise.

### GetMinimapTeamCombineColorOk

`func (o *GenericDataV2) GetMinimapTeamCombineColorOk() (*ColorV1, bool)`

GetMinimapTeamCombineColorOk returns a tuple with the MinimapTeamCombineColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMinimapTeamCombineColor

`func (o *GenericDataV2) SetMinimapTeamCombineColor(v ColorV1)`

SetMinimapTeamCombineColor sets MinimapTeamCombineColor field to given value.

### HasMinimapTeamCombineColor

`func (o *GenericDataV2) HasMinimapTeamCombineColor() bool`

HasMinimapTeamCombineColor returns a boolean if a field has been set.

### SetMinimapTeamCombineColorNil

`func (o *GenericDataV2) SetMinimapTeamCombineColorNil(b bool)`

 SetMinimapTeamCombineColorNil sets the value for MinimapTeamCombineColor to be an explicit nil

### UnsetMinimapTeamCombineColor
`func (o *GenericDataV2) UnsetMinimapTeamCombineColor()`

UnsetMinimapTeamCombineColor ensures that no value is present for MinimapTeamCombineColor, not even an explicit nil
### GetEnemyObjectivesAndZiplineColor

`func (o *GenericDataV2) GetEnemyObjectivesAndZiplineColor() ColorV1`

GetEnemyObjectivesAndZiplineColor returns the EnemyObjectivesAndZiplineColor field if non-nil, zero value otherwise.

### GetEnemyObjectivesAndZiplineColorOk

`func (o *GenericDataV2) GetEnemyObjectivesAndZiplineColorOk() (*ColorV1, bool)`

GetEnemyObjectivesAndZiplineColorOk returns a tuple with the EnemyObjectivesAndZiplineColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyObjectivesAndZiplineColor

`func (o *GenericDataV2) SetEnemyObjectivesAndZiplineColor(v ColorV1)`

SetEnemyObjectivesAndZiplineColor sets EnemyObjectivesAndZiplineColor field to given value.

### HasEnemyObjectivesAndZiplineColor

`func (o *GenericDataV2) HasEnemyObjectivesAndZiplineColor() bool`

HasEnemyObjectivesAndZiplineColor returns a boolean if a field has been set.

### SetEnemyObjectivesAndZiplineColorNil

`func (o *GenericDataV2) SetEnemyObjectivesAndZiplineColorNil(b bool)`

 SetEnemyObjectivesAndZiplineColorNil sets the value for EnemyObjectivesAndZiplineColor to be an explicit nil

### UnsetEnemyObjectivesAndZiplineColor
`func (o *GenericDataV2) UnsetEnemyObjectivesAndZiplineColor()`

UnsetEnemyObjectivesAndZiplineColor ensures that no value is present for EnemyObjectivesAndZiplineColor, not even an explicit nil
### GetEnemyObjectivesColor

`func (o *GenericDataV2) GetEnemyObjectivesColor() ColorV1`

GetEnemyObjectivesColor returns the EnemyObjectivesColor field if non-nil, zero value otherwise.

### GetEnemyObjectivesColorOk

`func (o *GenericDataV2) GetEnemyObjectivesColorOk() (*ColorV1, bool)`

GetEnemyObjectivesColorOk returns a tuple with the EnemyObjectivesColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyObjectivesColor

`func (o *GenericDataV2) SetEnemyObjectivesColor(v ColorV1)`

SetEnemyObjectivesColor sets EnemyObjectivesColor field to given value.

### HasEnemyObjectivesColor

`func (o *GenericDataV2) HasEnemyObjectivesColor() bool`

HasEnemyObjectivesColor returns a boolean if a field has been set.

### SetEnemyObjectivesColorNil

`func (o *GenericDataV2) SetEnemyObjectivesColorNil(b bool)`

 SetEnemyObjectivesColorNil sets the value for EnemyObjectivesColor to be an explicit nil

### UnsetEnemyObjectivesColor
`func (o *GenericDataV2) UnsetEnemyObjectivesColor()`

UnsetEnemyObjectivesColor ensures that no value is present for EnemyObjectivesColor, not even an explicit nil
### GetEnemyZiplineColor

`func (o *GenericDataV2) GetEnemyZiplineColor() ColorV1`

GetEnemyZiplineColor returns the EnemyZiplineColor field if non-nil, zero value otherwise.

### GetEnemyZiplineColorOk

`func (o *GenericDataV2) GetEnemyZiplineColorOk() (*ColorV1, bool)`

GetEnemyZiplineColorOk returns a tuple with the EnemyZiplineColor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEnemyZiplineColor

`func (o *GenericDataV2) SetEnemyZiplineColor(v ColorV1)`

SetEnemyZiplineColor sets EnemyZiplineColor field to given value.

### HasEnemyZiplineColor

`func (o *GenericDataV2) HasEnemyZiplineColor() bool`

HasEnemyZiplineColor returns a boolean if a field has been set.

### SetEnemyZiplineColorNil

`func (o *GenericDataV2) SetEnemyZiplineColorNil(b bool)`

 SetEnemyZiplineColorNil sets the value for EnemyZiplineColor to be an explicit nil

### UnsetEnemyZiplineColor
`func (o *GenericDataV2) UnsetEnemyZiplineColor()`

UnsetEnemyZiplineColor ensures that no value is present for EnemyZiplineColor, not even an explicit nil
### GetItemPricePerTier

`func (o *GenericDataV2) GetItemPricePerTier() []int32`

GetItemPricePerTier returns the ItemPricePerTier field if non-nil, zero value otherwise.

### GetItemPricePerTierOk

`func (o *GenericDataV2) GetItemPricePerTierOk() (*[]int32, bool)`

GetItemPricePerTierOk returns a tuple with the ItemPricePerTier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetItemPricePerTier

`func (o *GenericDataV2) SetItemPricePerTier(v []int32)`

SetItemPricePerTier sets ItemPricePerTier field to given value.


### GetTrooperKillGoldShareFrac

`func (o *GenericDataV2) GetTrooperKillGoldShareFrac() []float32`

GetTrooperKillGoldShareFrac returns the TrooperKillGoldShareFrac field if non-nil, zero value otherwise.

### GetTrooperKillGoldShareFracOk

`func (o *GenericDataV2) GetTrooperKillGoldShareFracOk() (*[]float32, bool)`

GetTrooperKillGoldShareFracOk returns a tuple with the TrooperKillGoldShareFrac field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTrooperKillGoldShareFrac

`func (o *GenericDataV2) SetTrooperKillGoldShareFrac(v []float32)`

SetTrooperKillGoldShareFrac sets TrooperKillGoldShareFrac field to given value.


### GetHeroKillGoldShareFrac

`func (o *GenericDataV2) GetHeroKillGoldShareFrac() []float32`

GetHeroKillGoldShareFrac returns the HeroKillGoldShareFrac field if non-nil, zero value otherwise.

### GetHeroKillGoldShareFracOk

`func (o *GenericDataV2) GetHeroKillGoldShareFracOk() (*[]float32, bool)`

GetHeroKillGoldShareFracOk returns a tuple with the HeroKillGoldShareFrac field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeroKillGoldShareFrac

`func (o *GenericDataV2) SetHeroKillGoldShareFrac(v []float32)`

SetHeroKillGoldShareFrac sets HeroKillGoldShareFrac field to given value.


### GetAimSpringStrength

`func (o *GenericDataV2) GetAimSpringStrength() []float32`

GetAimSpringStrength returns the AimSpringStrength field if non-nil, zero value otherwise.

### GetAimSpringStrengthOk

`func (o *GenericDataV2) GetAimSpringStrengthOk() (*[]float32, bool)`

GetAimSpringStrengthOk returns a tuple with the AimSpringStrength field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAimSpringStrength

`func (o *GenericDataV2) SetAimSpringStrength(v []float32)`

SetAimSpringStrength sets AimSpringStrength field to given value.


### GetTargetingSpringStrength

`func (o *GenericDataV2) GetTargetingSpringStrength() []float32`

GetTargetingSpringStrength returns the TargetingSpringStrength field if non-nil, zero value otherwise.

### GetTargetingSpringStrengthOk

`func (o *GenericDataV2) GetTargetingSpringStrengthOk() (*[]float32, bool)`

GetTargetingSpringStrengthOk returns a tuple with the TargetingSpringStrength field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetingSpringStrength

`func (o *GenericDataV2) SetTargetingSpringStrength(v []float32)`

SetTargetingSpringStrength sets TargetingSpringStrength field to given value.


### GetObjectiveParams

`func (o *GenericDataV2) GetObjectiveParams() ObjectiveParams`

GetObjectiveParams returns the ObjectiveParams field if non-nil, zero value otherwise.

### GetObjectiveParamsOk

`func (o *GenericDataV2) GetObjectiveParamsOk() (*ObjectiveParams, bool)`

GetObjectiveParamsOk returns a tuple with the ObjectiveParams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectiveParams

`func (o *GenericDataV2) SetObjectiveParams(v ObjectiveParams)`

SetObjectiveParams sets ObjectiveParams field to given value.


### GetRejuvParams

`func (o *GenericDataV2) GetRejuvParams() RejuvParams`

GetRejuvParams returns the RejuvParams field if non-nil, zero value otherwise.

### GetRejuvParamsOk

`func (o *GenericDataV2) GetRejuvParamsOk() (*RejuvParams, bool)`

GetRejuvParamsOk returns a tuple with the RejuvParams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRejuvParams

`func (o *GenericDataV2) SetRejuvParams(v RejuvParams)`

SetRejuvParams sets RejuvParams field to given value.


### GetMiniMapOffsets

`func (o *GenericDataV2) GetMiniMapOffsets() []MiniMapOffsets`

GetMiniMapOffsets returns the MiniMapOffsets field if non-nil, zero value otherwise.

### GetMiniMapOffsetsOk

`func (o *GenericDataV2) GetMiniMapOffsetsOk() (*[]MiniMapOffsets, bool)`

GetMiniMapOffsetsOk returns a tuple with the MiniMapOffsets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMiniMapOffsets

`func (o *GenericDataV2) SetMiniMapOffsets(v []MiniMapOffsets)`

SetMiniMapOffsets sets MiniMapOffsets field to given value.


### GetWeaponGroups

`func (o *GenericDataV2) GetWeaponGroups() []ItemGroup`

GetWeaponGroups returns the WeaponGroups field if non-nil, zero value otherwise.

### GetWeaponGroupsOk

`func (o *GenericDataV2) GetWeaponGroupsOk() (*[]ItemGroup, bool)`

GetWeaponGroupsOk returns a tuple with the WeaponGroups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWeaponGroups

`func (o *GenericDataV2) SetWeaponGroups(v []ItemGroup)`

SetWeaponGroups sets WeaponGroups field to given value.


### GetArmorGroups

`func (o *GenericDataV2) GetArmorGroups() []ItemGroup`

GetArmorGroups returns the ArmorGroups field if non-nil, zero value otherwise.

### GetArmorGroupsOk

`func (o *GenericDataV2) GetArmorGroupsOk() (*[]ItemGroup, bool)`

GetArmorGroupsOk returns a tuple with the ArmorGroups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetArmorGroups

`func (o *GenericDataV2) SetArmorGroups(v []ItemGroup)`

SetArmorGroups sets ArmorGroups field to given value.


### GetSpiritGroups

`func (o *GenericDataV2) GetSpiritGroups() []ItemGroup`

GetSpiritGroups returns the SpiritGroups field if non-nil, zero value otherwise.

### GetSpiritGroupsOk

`func (o *GenericDataV2) GetSpiritGroupsOk() (*[]ItemGroup, bool)`

GetSpiritGroupsOk returns a tuple with the SpiritGroups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpiritGroups

`func (o *GenericDataV2) SetSpiritGroups(v []ItemGroup)`

SetSpiritGroups sets SpiritGroups field to given value.


### GetStreetBrawl

`func (o *GenericDataV2) GetStreetBrawl() StreetBrawl`

GetStreetBrawl returns the StreetBrawl field if non-nil, zero value otherwise.

### GetStreetBrawlOk

`func (o *GenericDataV2) GetStreetBrawlOk() (*StreetBrawl, bool)`

GetStreetBrawlOk returns a tuple with the StreetBrawl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStreetBrawl

`func (o *GenericDataV2) SetStreetBrawl(v StreetBrawl)`

SetStreetBrawl sets StreetBrawl field to given value.

### HasStreetBrawl

`func (o *GenericDataV2) HasStreetBrawl() bool`

HasStreetBrawl returns a boolean if a field has been set.

### SetStreetBrawlNil

`func (o *GenericDataV2) SetStreetBrawlNil(b bool)`

 SetStreetBrawlNil sets the value for StreetBrawl to be an explicit nil

### UnsetStreetBrawl
`func (o *GenericDataV2) UnsetStreetBrawl()`

UnsetStreetBrawl ensures that no value is present for StreetBrawl, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


