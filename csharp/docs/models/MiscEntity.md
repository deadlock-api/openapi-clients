# DeadlockApiClient.Model.MiscEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClassName** | **string** |  | 
**Id** | **int** |  | 
**BreakOnDodgeTouch** | **bool** |  | [optional] 
**CollisionRadius** | **double** |  | [optional] 
**Color** | [**Color**](Color.md) |  | [optional] 
**DamagedByAbilities** | **bool** |  | [optional] 
**DamagedByBullets** | **bool** |  | [optional] 
**DamagedByMelee** | **bool** |  | [optional] 
**ExpirationDuration** | [**CurveOrFloat**](CurveOrFloat.md) |  | [optional] 
**GoldAmount** | **double** |  | [optional] 
**GoldPerMinuteAmount** | **double** |  | [optional] 
**Health** | **long** |  | [optional] 
**InitialSpawnDelayInSeconds** | **long** |  | [optional] 
**InitialSpawnDelaySeconds** | **long** | Duplicate of &#x60;initial_spawn_delay_in_seconds&#x60; for shape parity. | [optional] 
**InitialSpawnTime** | **double** |  | [optional] 
**IsMantleable** | **bool** |  | [optional] 
**Lifetime** | **double** |  | [optional] 
**LootListDeckSize** | **long** |  | [optional] 
**MVecPickupsLv2** | [**List&lt;Pickup&gt;**](Pickup.md) |  | [optional] 
**MVecPickupsLv3** | [**List&lt;Pickup&gt;**](Pickup.md) |  | [optional] 
**MatchTimeMinsForLevel2Pickups** | **long** |  | [optional] 
**MatchTimeMinsForLevel3Pickups** | **long** |  | [optional] 
**Modifier** | [**SubclassModifierDefinition**](SubclassModifierDefinition.md) |  | [optional] 
**OrbSpawnDelayMax** | **double** |  | [optional] 
**OrbSpawnDelayMin** | **double** |  | [optional] 
**PickupRadius** | [**CurveOrFloat**](CurveOrFloat.md) |  | [optional] 
**PrimaryDropChance** | **double** |  | [optional] 
**PrimaryPickups** | [**List&lt;Pickup&gt;**](Pickup.md) |  | [optional] 
**RenderAfterDeath** | **bool** |  | [optional] 
**RespawnTime** | **double** |  | [optional] 
**RollType** | **string** | Known values for &#x60;m_eRollType&#x60;. Unknown values pass through unchanged so a newly-introduced roll type doesn&#39;t 500. Known values: &#x60;ECitadelRandomRoll_BreakablePowerupPickup&#x60;, &#x60;ECitadelRandomRoll_BreakableGoldPickup&#x60;. | [optional] 
**ShowOnMinimap** | **bool** |  | [optional] 
**SolidAfterDeath** | **bool** |  | [optional] 
**SpawnInterval** | **double** |  | [optional] 
**SpawnIntervalInSeconds** | **long** |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

