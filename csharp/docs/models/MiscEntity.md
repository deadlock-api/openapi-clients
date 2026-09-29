# DeadlockApiClient.Model.MiscEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClassName** | **string** |  | 
**Id** | **int** |  | 
**BreakOnDodgeTouch** | **bool** |  | [optional] 
**BuffTypeGraphColor** | [**Color**](Color.md) | Permanent pickups: color used for the buff in the stat graph. | [optional] 
**BuffTypeLocString** | **string** | Permanent pickups: localization token of the stat the buff raises. | [optional] 
**BuffTypeValueUnit** | **string** | Permanent pickups: unit of the buff value (e.g. &#x60;Percent&#x60;, &#x60;Meters&#x60;). | [optional] 
**CollisionRadius** | **double** |  | [optional] 
**Color** | [**Color**](Color.md) |  | [optional] 
**DamagedByAbilities** | **bool** |  | [optional] 
**DamagedByBullets** | **bool** |  | [optional] 
**DamagedByMelee** | **bool** |  | [optional] 
**DamagedBySlide** | **bool** |  | [optional] 
**ExpirationDuration** | [**CurveOrFloat**](CurveOrFloat.md) |  | [optional] 
**GoldAmount** | **double** |  | [optional] 
**GoldPerMinuteAmount** | **double** |  | [optional] 
**Health** | **long** |  | [optional] 
**HeavyMeleeHitCount** | **long** |  | [optional] 
**HeavyMeleeOnly** | **bool** |  | [optional] 
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
**PickupChances** | **Dictionary&lt;string, double&gt;** | Pickup name to relative weight (build 6711+); replaces the &#x60;primary_pickups&#x60; / &#x60;m_vecPickups_lv*&#x60; lists. | [optional] 
**PickupRadius** | [**CurveOrFloat**](CurveOrFloat.md) |  | [optional] 
**PowerupDropChance** | **double** | Drop chance (percent) for build 6711+; replaces &#x60;primary_drop_chance&#x60;. | [optional] 
**PrimaryDropChance** | **double** | Pre-6711 builds only; see &#x60;powerup_drop_chance&#x60;. | [optional] 
**PrimaryPickups** | [**List&lt;Pickup&gt;**](Pickup.md) |  | [optional] 
**RenderAfterDeath** | **bool** |  | [optional] 
**RespawnTime** | **double** |  | [optional] 
**RollType** | **string** | Known values for &#x60;m_eRollType&#x60;. Unknown values pass through unchanged so a newly-introduced roll type doesn&#39;t 500. Known values: &#x60;ECitadelRandomRoll_BreakablePowerupPickup&#x60;, &#x60;ECitadelRandomRoll_BreakableGoldPickup&#x60;. | [optional] 
**ShowOnMinimap** | **bool** |  | [optional] 
**SolidAfterDeath** | **bool** |  | [optional] 
**SpawnInterval** | **double** |  | [optional] 
**SpawnIntervalInSeconds** | **long** |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

