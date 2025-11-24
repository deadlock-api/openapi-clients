
# NPCUnitV2

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **className** | **kotlin.String** |  |  |
| **id** | **kotlin.Long** |  |  [readonly] |
| **weaponInfo** | [**RawWeaponInfoV2**](RawWeaponInfoV2.md) |  |  [optional] |
| **maxHealth** | **kotlin.Int** |  |  [optional] |
| **phase2Health** | **kotlin.Int** |  |  [optional] |
| **boundAbilities** | **kotlin.collections.Map&lt;kotlin.String, kotlin.String&gt;** |  |  [optional] |
| **maxHealthFinal** | **kotlin.Int** |  |  [optional] |
| **maxHealthGenerator** | **kotlin.Int** |  |  [optional] |
| **enemyTrooperProtectionRange** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **backdoorBulletResistModifier** | [**SubclassBulletResistModifier**](SubclassBulletResistModifier.md) |  |  [optional] |
| **objectiveRegen** | [**SubclassObjectiveRegen**](SubclassObjectiveRegen.md) |  |  [optional] |
| **objectiveHealthGrowthPhase1** | [**SubclassObjectiveHealthGrowthPhase**](SubclassObjectiveHealthGrowthPhase.md) |  |  [optional] |
| **objectiveHealthGrowthPhase2** | [**SubclassObjectiveHealthGrowthPhase**](SubclassObjectiveHealthGrowthPhase.md) |  |  [optional] |
| **enemyTrooperDamageReduction** | [**SubclassTrooperDamageReduction**](SubclassTrooperDamageReduction.md) |  |  [optional] |
| **rangedArmorModifier** | [**SubclassRangedArmorModifier**](SubclassRangedArmorModifier.md) |  |  [optional] |
| **intrinsicModifiers** | [**kotlin.collections.List&lt;SubclassIntrinsicModifiers&gt;**](SubclassIntrinsicModifiers.md) |  |  [optional] |
| **sightRangePlayers** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **sightRangeNpcs** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **goldReward** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **goldRewardBonusPercentPerMinute** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **playerDamageResistPct** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **trooperDamageResistPct** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **t1BossDamageResistPct** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **t2BossDamageResistPct** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **t3BossDamageResistPct** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **barrackGuardianDamageResistPct** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **nearDeathDuration** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **laserDpstoPlayers** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **laserDpsmaxHealth** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **noShieldLaserDpstoPlayers** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **stompDamage** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **stompDamageMaxHealthPercent** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **stunDuration** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **stompImpactRadius** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **walkSpeed** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **runSpeed** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **acceleration** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **meleeDamage** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **meleeAttemptRange** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **meleeHitRange** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **meleeDuration** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **attackT1BossMaxRange** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **attackT3BossMaxRange** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **attackT3BossPhase2MaxRange** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **attackTrooperMaxRange** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **t1BossDps** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **t1BossDpsbaseResist** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **t1BossDpsmaxResist** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **t1BossDpsmaxResistTimeInSeconds** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **t2BossDps** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **t2BossDpsbaseResist** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **t2BossDpsmaxResist** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **t2BossDpsmaxResistTimeInSeconds** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **t3BossDps** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **generatorBossDps** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **barrackBossDps** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **playerDps** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **trooperDps** | [**java.math.BigDecimal**](java.math.BigDecimal.md) |  |  [optional] |
| **healthBarColorFriend** | [**ColorV1**](ColorV1.md) |  |  [optional] |
| **healthBarColorEnemy** | [**ColorV1**](ColorV1.md) |  |  [optional] |
| **healthBarColorTeam1** | [**ColorV1**](ColorV1.md) |  |  [optional] |
| **healthBarColorTeam2** | [**ColorV1**](ColorV1.md) |  |  [optional] |
| **healthBarColorTeamNeutral** | [**ColorV1**](ColorV1.md) |  |  [optional] |
| **glowColorFriend** | [**ColorV1**](ColorV1.md) |  |  [optional] |
| **glowColorEnemy** | [**ColorV1**](ColorV1.md) |  |  [optional] |
| **glowColorTeam1** | [**ColorV1**](ColorV1.md) |  |  [optional] |
| **glowColorTeam2** | [**ColorV1**](ColorV1.md) |  |  [optional] |
| **glowColorTeamNeutral** | [**ColorV1**](ColorV1.md) |  |  [optional] |



