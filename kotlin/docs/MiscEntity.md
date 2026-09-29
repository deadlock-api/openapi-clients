
# MiscEntity

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **className** | **kotlin.String** |  |  |
| **id** | **kotlin.Int** |  |  |
| **breakOnDodgeTouch** | **kotlin.Boolean** |  |  [optional] |
| **buffTypeGraphColor** | [**Color**](Color.md) | Permanent pickups: color used for the buff in the stat graph. |  [optional] |
| **buffTypeLocString** | **kotlin.String** | Permanent pickups: localization token of the stat the buff raises. |  [optional] |
| **buffTypeValueUnit** | **kotlin.String** | Permanent pickups: unit of the buff value (e.g. &#x60;Percent&#x60;, &#x60;Meters&#x60;). |  [optional] |
| **collisionRadius** | **kotlin.Double** |  |  [optional] |
| **color** | [**Color**](Color.md) |  |  [optional] |
| **damagedByAbilities** | **kotlin.Boolean** |  |  [optional] |
| **damagedByBullets** | **kotlin.Boolean** |  |  [optional] |
| **damagedByMelee** | **kotlin.Boolean** |  |  [optional] |
| **damagedBySlide** | **kotlin.Boolean** |  |  [optional] |
| **expirationDuration** | [**CurveOrFloat**](CurveOrFloat.md) |  |  [optional] |
| **goldAmount** | **kotlin.Double** |  |  [optional] |
| **goldPerMinuteAmount** | **kotlin.Double** |  |  [optional] |
| **health** | **kotlin.Long** |  |  [optional] |
| **heavyMeleeHitCount** | **kotlin.Long** |  |  [optional] |
| **heavyMeleeOnly** | **kotlin.Boolean** |  |  [optional] |
| **initialSpawnDelayInSeconds** | **kotlin.Long** |  |  [optional] |
| **initialSpawnDelaySeconds** | **kotlin.Long** | Duplicate of &#x60;initial_spawn_delay_in_seconds&#x60; for shape parity. |  [optional] |
| **initialSpawnTime** | **kotlin.Double** |  |  [optional] |
| **isMantleable** | **kotlin.Boolean** |  |  [optional] |
| **lifetime** | **kotlin.Double** |  |  [optional] |
| **lootListDeckSize** | **kotlin.Long** |  |  [optional] |
| **mVecPickupsLv2** | [**kotlin.collections.List&lt;Pickup&gt;**](Pickup.md) |  |  [optional] |
| **mVecPickupsLv3** | [**kotlin.collections.List&lt;Pickup&gt;**](Pickup.md) |  |  [optional] |
| **matchTimeMinsForLevel2Pickups** | **kotlin.Long** |  |  [optional] |
| **matchTimeMinsForLevel3Pickups** | **kotlin.Long** |  |  [optional] |
| **modifier** | [**SubclassModifierDefinition**](SubclassModifierDefinition.md) |  |  [optional] |
| **orbSpawnDelayMax** | **kotlin.Double** |  |  [optional] |
| **orbSpawnDelayMin** | **kotlin.Double** |  |  [optional] |
| **pickupChances** | **kotlin.collections.Map&lt;kotlin.String, kotlin.Double&gt;** | Pickup name to relative weight (build 6711+); replaces the &#x60;primary_pickups&#x60; / &#x60;m_vecPickups_lv*&#x60; lists. |  [optional] |
| **pickupRadius** | [**CurveOrFloat**](CurveOrFloat.md) |  |  [optional] |
| **powerupDropChance** | **kotlin.Double** | Drop chance (percent) for build 6711+; replaces &#x60;primary_drop_chance&#x60;. |  [optional] |
| **primaryDropChance** | **kotlin.Double** | Pre-6711 builds only; see &#x60;powerup_drop_chance&#x60;. |  [optional] |
| **primaryPickups** | [**kotlin.collections.List&lt;Pickup&gt;**](Pickup.md) |  |  [optional] |
| **renderAfterDeath** | **kotlin.Boolean** |  |  [optional] |
| **respawnTime** | **kotlin.Double** |  |  [optional] |
| **rollType** | **kotlin.String** | Known values for &#x60;m_eRollType&#x60;. Unknown values pass through unchanged so a newly-introduced roll type doesn&#39;t 500. Known values: &#x60;ECitadelRandomRoll_BreakablePowerupPickup&#x60;, &#x60;ECitadelRandomRoll_BreakableGoldPickup&#x60;. |  [optional] |
| **showOnMinimap** | **kotlin.Boolean** |  |  [optional] |
| **solidAfterDeath** | **kotlin.Boolean** |  |  [optional] |
| **spawnInterval** | **kotlin.Double** |  |  [optional] |
| **spawnIntervalInSeconds** | **kotlin.Long** |  |  [optional] |



