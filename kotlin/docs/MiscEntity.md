
# MiscEntity

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **className** | **kotlin.String** |  |  |
| **id** | **kotlin.Int** |  |  |
| **breakOnDodgeTouch** | **kotlin.Boolean** |  |  [optional] |
| **buffTypeGraphColor** | [**Color**](Color.md) | Permanent pickups: color used for the buff in the stat graph. |  [optional] |
| **buffTypeLocString** | **kotlin.String** | Permanent pickups: localization token of the stat the buff raises. |  [optional] |
| **buffTypeName** | **kotlin.String** | Permanent pickups: &#x60;buff_type_loc_string&#x60; localized into the requested language (e.g. &#x60;Fire Rate&#x60;). |  [optional] |
| **buffTypeValueUnit** | **kotlin.String** | Permanent pickups: unit of the buff value (e.g. &#x60;Percent&#x60;, &#x60;Meters&#x60;). The modifier value itself is in game units (&#x60;Meters&#x60; values are inches, 39.37 per meter). |  [optional] |
| **collectionMethod** | **kotlin.String** | How the pickup is collected, e.g. &#x60;Punch&#x60; or &#x60;VacuumTrigger&#x60;. |  [optional] |
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
| **hitsRequired** | **kotlin.Long** | Punchable pickups: hits needed to collect. |  [optional] |
| **inShopModifier** | [**SubclassModifierDefinition**](SubclassModifierDefinition.md) | Corrupted item shop (Broker) trigger: modifier applied while inside. |  [optional] |
| **initialSpawnDelayInSeconds** | **kotlin.Long** |  |  [optional] |
| **initialSpawnDelaySeconds** | **kotlin.Long** | Duplicate of &#x60;initial_spawn_delay_in_seconds&#x60; for shape parity. |  [optional] |
| **initialSpawnTime** | **kotlin.Double** |  |  [optional] |
| **isMantleable** | **kotlin.Boolean** |  |  [optional] |
| **isPermanentPickup** | **kotlin.Boolean** |  |  [optional] |
| **lifetime** | **kotlin.Double** |  |  [optional] |
| **lootListDeckSize** | **kotlin.Long** |  |  [optional] |
| **mVecPickupsLv2** | [**kotlin.collections.List&lt;Pickup&gt;**](Pickup.md) |  |  [optional] |
| **mVecPickupsLv3** | [**kotlin.collections.List&lt;Pickup&gt;**](Pickup.md) |  |  [optional] |
| **matchTimeMinsForLevel2Pickups** | **kotlin.Long** |  |  [optional] |
| **matchTimeMinsForLevel3Pickups** | **kotlin.Long** |  |  [optional] |
| **minimapClass** | **kotlin.String** |  |  [optional] |
| **modifier** | [**SubclassModifierDefinition**](SubclassModifierDefinition.md) |  |  [optional] |
| **name** | **kotlin.String** | &#x60;name_loc_string&#x60; localized into the requested language (e.g. &#x60;+1.5% Fire Rate&#x60;). Gold pickups use an ICU plural pattern (&#x60;{amount, plural, one{Soul} other{Souls}}&#x60;). |  [optional] |
| **nameLocString** | **kotlin.String** | Localization token of the pickup&#39;s world label. |  [optional] |
| **orbSpawnDelayMax** | **kotlin.Double** |  |  [optional] |
| **orbSpawnDelayMin** | **kotlin.Double** |  |  [optional] |
| **pickup** | **kotlin.String** | Pickup spawners: class name of the spawned pickup. |  [optional] |
| **pickupChances** | **kotlin.collections.Map&lt;kotlin.String, kotlin.Double&gt;** | Pickup name to relative weight (build 6711+); replaces the &#x60;primary_pickups&#x60; / &#x60;m_vecPickups_lv*&#x60; lists. |  [optional] |
| **pickupRadius** | [**CurveOrFloat**](CurveOrFloat.md) |  |  [optional] |
| **powerupDropChance** | **kotlin.Double** | Drop chance (percent) for build 6711+; replaces &#x60;primary_drop_chance&#x60;. |  [optional] |
| **primaryDropChance** | **kotlin.Double** | Pre-6711 builds only; see &#x60;powerup_drop_chance&#x60;. |  [optional] |
| **primaryPickups** | [**kotlin.collections.List&lt;Pickup&gt;**](Pickup.md) |  |  [optional] |
| **regenDuration** | **kotlin.Double** | Health pickups: seconds over which the healing is applied to heroes. |  [optional] |
| **regenDurationTroopers** | **kotlin.Double** | Health pickups: seconds over which the healing is applied to troopers. |  [optional] |
| **regenMaxHealthPercent** | [**CurveOrFloat**](CurveOrFloat.md) | Health pickups: healing as percent of max health. |  [optional] |
| **regenTrooperMulti** | **kotlin.Double** | Health pickups: healing multiplier for troopers. |  [optional] |
| **renderAfterDeath** | **kotlin.Boolean** |  |  [optional] |
| **respawnTime** | **kotlin.Double** |  |  [optional] |
| **rollType** | **kotlin.String** | Known values for &#x60;m_eRollType&#x60;. Unknown values pass through unchanged so a newly-introduced roll type doesn&#39;t 500. Known values: &#x60;ECitadelRandomRoll_BreakablePowerupPickup&#x60;, &#x60;ECitadelRandomRoll_BreakableGoldPickup&#x60;. |  [optional] |
| **showOnMinimap** | **kotlin.Boolean** |  |  [optional] |
| **singlePickupOverride** | **kotlin.String** | Powerup spawners: class name of the only pickup spawned, overriding &#x60;pickup_chances&#x60;. |  [optional] |
| **solidAfterDeath** | **kotlin.Boolean** |  |  [optional] |
| **spawnDelay** | **kotlin.Double** | Pickup spawners: delay (seconds) before the first spawn. |  [optional] |
| **spawnInterval** | **kotlin.Double** |  |  [optional] |
| **spawnIntervalInSeconds** | **kotlin.Long** |  |  [optional] |
| **spawnMusicState** | **kotlin.String** | Corrupted item shop (Broker) trigger: music cue played on spawn. |  [optional] |



