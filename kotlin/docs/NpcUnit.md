
# NpcUnit

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **className** | **kotlin.String** |  |  |
| **id** | **kotlin.Int** |  |  |
| **acceleration** | **kotlin.Double** |  |  [optional] |
| **attackT1BossMaxRange** | **kotlin.Double** |  |  [optional] |
| **attackT3BossMaxRange** | **kotlin.Double** |  |  [optional] |
| **attackT3BossPhase2MaxRange** | **kotlin.Double** |  |  [optional] |
| **attackTrooperMaxRange** | **kotlin.Double** |  |  [optional] |
| **backdoorBulletResistModifier** | [**SubclassBulletResistModifier**](SubclassBulletResistModifier.md) |  |  [optional] |
| **barrackBossDps** | **kotlin.Double** |  |  [optional] |
| **barrackGuardianDamageResistPct** | **kotlin.Double** |  |  [optional] |
| **bossWeaponInfo** | [**WeaponInfo**](WeaponInfo.md) | Secondary weapon the unit uses against bosses (builds 6711+). |  [optional] |
| **boundAbilities** | **kotlin.collections.Map&lt;kotlin.String, kotlin.String&gt;** |  |  [optional] |
| **empoweredModifierLevel1** | [**SubclassEmpoweredModifierLevel**](SubclassEmpoweredModifierLevel.md) |  |  [optional] |
| **empoweredModifierLevel2** | [**SubclassEmpoweredModifierLevel**](SubclassEmpoweredModifierLevel.md) |  |  [optional] |
| **enemyTrooperDamageReduction** | [**SubclassTrooperDamageReduction**](SubclassTrooperDamageReduction.md) |  |  [optional] |
| **enemyTrooperProtectionRange** | **kotlin.Double** |  |  [optional] |
| **generatorBossDps** | **kotlin.Double** |  |  [optional] |
| **goldReward** | **kotlin.Double** |  |  [optional] |
| **goldRewardBonusPercentPerMinute** | **kotlin.Double** |  |  [optional] |
| **healthBarColorEnemy** | [**Color**](Color.md) |  |  [optional] |
| **healthBarColorFriend** | [**Color**](Color.md) |  |  [optional] |
| **healthBarColorTeam1** | [**Color**](Color.md) |  |  [optional] |
| **healthBarColorTeam2** | [**Color**](Color.md) |  |  [optional] |
| **healthBarColorTeamNeutral** | [**Color**](Color.md) |  |  [optional] |
| **image** | **kotlin.String** | Unit icon (&#x60;m_strCustomUnitIcon&#x60;) as png. |  [optional] |
| **imageWebp** | **kotlin.String** | Unit icon (&#x60;m_strCustomUnitIcon&#x60;) as webp. |  [optional] |
| **intrinsicModifiers** | [**kotlin.collections.List&lt;SubclassIntrinsicModifiers&gt;**](SubclassIntrinsicModifiers.md) |  |  [optional] |
| **laserDpsMaxHealth** | **kotlin.Double** |  |  [optional] |
| **laserDpsToPlayers** | **kotlin.Double** |  |  [optional] |
| **maxHealth** | **kotlin.Long** |  |  [optional] |
| **maxHealthFinal** | **kotlin.Long** |  |  [optional] |
| **maxHealthGenerator** | **kotlin.Long** |  |  [optional] |
| **meleeAttemptRange** | **kotlin.Double** |  |  [optional] |
| **meleeDamage** | **kotlin.Double** |  |  [optional] |
| **meleeDuration** | **kotlin.Double** |  |  [optional] |
| **meleeHitRange** | **kotlin.Double** |  |  [optional] |
| **name** | **kotlin.String** | Localized unit name (&#x60;m_sLocUnitName&#x60;), e.g. &#x60;Gutter Ghoul I&#x60;. |  [optional] |
| **nearDeathDuration** | **kotlin.Double** |  |  [optional] |
| **neutralAbilities** | **kotlin.collections.List&lt;kotlin.String&gt;** | Neutral ability class names; see &#x60;/v1/assets/modifiers&#x60; (builds 6711+). |  [optional] |
| **neutralDamageGrowth** | [**SubclassNeutralDamageGrowth**](SubclassNeutralDamageGrowth.md) |  |  [optional] |
| **neutralMelee** | **kotlin.String** | Neutral melee ability class name; see &#x60;/v1/assets/modifiers&#x60; (builds 6711+). |  [optional] |
| **neutralType** | **kotlin.String** | Neutral tier, e.g. &#x60;NEUTRAL_NPC_WEAK&#x60; (builds 6711+). |  [optional] |
| **noShieldLaserDpsToPlayers** | **kotlin.Double** |  |  [optional] |
| **objectiveHealthGrowthPhase1** | [**SubclassObjectiveHealthGrowthPhase**](SubclassObjectiveHealthGrowthPhase.md) |  |  [optional] |
| **objectiveHealthGrowthPhase2** | [**SubclassObjectiveHealthGrowthPhase**](SubclassObjectiveHealthGrowthPhase.md) |  |  [optional] |
| **objectiveRegen** | [**SubclassObjectiveRegen**](SubclassObjectiveRegen.md) |  |  [optional] |
| **phase2Health** | **kotlin.Long** |  |  [optional] |
| **playerDamageResistPct** | **kotlin.Double** |  |  [optional] |
| **playerDps** | **kotlin.Double** |  |  [optional] |
| **rangedArmorModifier** | [**SubclassRangedArmorModifier**](SubclassRangedArmorModifier.md) |  |  [optional] |
| **runSpeed** | **kotlin.Double** |  |  [optional] |
| **sightRangeNpcs** | **kotlin.Double** |  |  [optional] |
| **sightRangePlayers** | **kotlin.Double** |  |  [optional] |
| **spawnBreakablesOnDeath** | **kotlin.Boolean** |  |  [optional] |
| **stompDamage** | **kotlin.Double** |  |  [optional] |
| **stompDamageMaxHealthPercent** | **kotlin.Double** |  |  [optional] |
| **stompImpactRadius** | **kotlin.Double** |  |  [optional] |
| **stunDuration** | **kotlin.Double** |  |  [optional] |
| **t1BossDamageResistPct** | **kotlin.Double** |  |  [optional] |
| **t1BossDps** | **kotlin.Double** |  |  [optional] |
| **t1BossDpsbaseResist** | **kotlin.Double** |  |  [optional] |
| **t1BossDpsmaxResist** | **kotlin.Double** |  |  [optional] |
| **t1BossDpsmaxResistTimeInSeconds** | **kotlin.Double** |  |  [optional] |
| **t2BossDamageResistPct** | **kotlin.Double** |  |  [optional] |
| **t2BossDps** | **kotlin.Double** |  |  [optional] |
| **t2BossDpsbaseResist** | **kotlin.Double** |  |  [optional] |
| **t2BossDpsmaxResist** | **kotlin.Double** |  |  [optional] |
| **t2BossDpsmaxResistTimeInSeconds** | **kotlin.Double** |  |  [optional] |
| **t3BossDamageResistPct** | **kotlin.Double** |  |  [optional] |
| **t3BossDps** | **kotlin.Double** |  |  [optional] |
| **trooperDamageResistPct** | **kotlin.Double** |  |  [optional] |
| **trooperDps** | **kotlin.Double** |  |  [optional] |
| **viewerSoulsClass** | **kotlin.collections.Map&lt;kotlin.String, kotlin.String&gt;** | Distance threshold (as string key) → soul orb class shown to the viewer. |  [optional] |
| **walkSpeed** | **kotlin.Double** |  |  [optional] |
| **weaponInfo** | [**WeaponInfo**](WeaponInfo.md) |  |  [optional] |



