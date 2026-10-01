
# PlayerPerformanceCurvePoint

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **assistsAvg** | **kotlin.Double** | Average assists at this time point |  |
| **assistsStd** | **kotlin.Double** | Standard deviation of assists at this time point |  |
| **deathsAvg** | **kotlin.Double** | Average deaths at this time point |  |
| **deathsStd** | **kotlin.Double** | Standard deviation of deaths at this time point |  |
| **gameTime** | **kotlin.Int** | The time point of the data. If &#x60;resolution&#x60; (default 10) is &gt; 0, this is a percentage (0, 10, ..., 100). If &#x60;resolution&#x60; is 0, this is the match time in seconds. |  |
| **goldAbilityAssassinateAvg** | **kotlin.Double** | Average souls earned from the Assassinate ability at this time point |  |
| **goldAbilityAssassinateStd** | **kotlin.Double** | Standard deviation of &#x60;gold_ability_assassinate_avg&#x60; at this time point |  |
| **goldAssistsAvg** | **kotlin.Double** | Average souls earned from assists at this time point (part of &#x60;gold_player_avg&#x60;) |  |
| **goldAssistsStd** | **kotlin.Double** | Standard deviation of &#x60;gold_assists_avg&#x60; at this time point |  |
| **goldBossAvg** | **kotlin.Double** | Average souls earned from objectives at this time point |  |
| **goldBossOrbAvg** | **kotlin.Double** | Average souls earned from secured objective orbs at this time point |  |
| **goldBossOrbStd** | **kotlin.Double** | Standard deviation of &#x60;gold_boss_orb_avg&#x60; at this time point |  |
| **goldBossStd** | **kotlin.Double** | Standard deviation of &#x60;gold_boss_avg&#x60; at this time point |  |
| **goldBreakableAvg** | **kotlin.Double** | Average souls earned from breakables (crates, statues) at this time point |  |
| **goldBreakableStd** | **kotlin.Double** | Standard deviation of &#x60;gold_breakable_avg&#x60; at this time point |  |
| **goldDeathLossAvg** | **kotlin.Double** | Average souls lost on death at this time point |  |
| **goldDeathLossStd** | **kotlin.Double** | Standard deviation of &#x60;gold_death_loss_avg&#x60; at this time point |  |
| **goldDeniedAvg** | **kotlin.Double** | Average souls denied to enemies at this time point |  |
| **goldDeniedStd** | **kotlin.Double** | Standard deviation of &#x60;gold_denied_avg&#x60; at this time point |  |
| **goldItemCultistSacrificeAvg** | **kotlin.Double** | Average souls earned from the Cultist Sacrifice item at this time point |  |
| **goldItemCultistSacrificeStd** | **kotlin.Double** | Standard deviation of &#x60;gold_item_cultist_sacrifice_avg&#x60; at this time point |  |
| **goldItemGooseEggAvg** | **kotlin.Double** | Average souls earned from the Golden Goose Egg item at this time point |  |
| **goldItemGooseEggStd** | **kotlin.Double** | Standard deviation of &#x60;gold_item_goose_egg_avg&#x60; at this time point |  |
| **goldItemTrophyCollectorAvg** | **kotlin.Double** | Average souls earned from the Trophy Collector item at this time point |  |
| **goldItemTrophyCollectorStd** | **kotlin.Double** | Standard deviation of &#x60;gold_item_trophy_collector_avg&#x60; at this time point |  |
| **goldLaneCreepAvg** | **kotlin.Double** | Average souls earned from lane creeps at this time point |  |
| **goldLaneCreepOrbsAvg** | **kotlin.Double** | Average souls earned from secured lane-creep orbs at this time point |  |
| **goldLaneCreepOrbsStd** | **kotlin.Double** | Standard deviation of &#x60;gold_lane_creep_orbs_avg&#x60; at this time point |  |
| **goldLaneCreepStd** | **kotlin.Double** | Standard deviation of &#x60;gold_lane_creep_avg&#x60; at this time point |  |
| **goldNeutralCreepAvg** | **kotlin.Double** | Average souls earned from neutral (jungle) creeps at this time point |  |
| **goldNeutralCreepOrbsAvg** | **kotlin.Double** | Average souls earned from secured neutral-creep orbs at this time point |  |
| **goldNeutralCreepOrbsStd** | **kotlin.Double** | Standard deviation of &#x60;gold_neutral_creep_orbs_avg&#x60; at this time point |  |
| **goldNeutralCreepStd** | **kotlin.Double** | Standard deviation of &#x60;gold_neutral_creep_avg&#x60; at this time point |  |
| **goldPlayerAvg** | **kotlin.Double** | Average souls earned from hero kills at this time point, including assist souls (see &#x60;gold_assists_avg&#x60;) |  |
| **goldPlayerOrbsAvg** | **kotlin.Double** | Average souls earned from secured hero-kill orbs at this time point |  |
| **goldPlayerOrbsStd** | **kotlin.Double** | Standard deviation of &#x60;gold_player_orbs_avg&#x60; at this time point |  |
| **goldPlayerStd** | **kotlin.Double** | Standard deviation of &#x60;gold_player_avg&#x60; at this time point |  |
| **goldTeamBonusAvg** | **kotlin.Double** | Average souls earned from the team bonus at this time point |  |
| **goldTeamBonusStd** | **kotlin.Double** | Standard deviation of &#x60;gold_team_bonus_avg&#x60; at this time point |  |
| **goldTreasureAvg** | **kotlin.Double** | Average souls earned from the urn at this time point |  |
| **goldTreasureStd** | **kotlin.Double** | Standard deviation of &#x60;gold_treasure_avg&#x60; at this time point |  |
| **killsAvg** | **kotlin.Double** | Average kills at this time point |  |
| **killsStd** | **kotlin.Double** | Standard deviation of kills at this time point |  |
| **netWorthAvg** | **kotlin.Double** | Average net worth at this time point |  |
| **netWorthStd** | **kotlin.Double** | Standard deviation of net worth at this time point |  |
| **permanentBuffsAvg** | **kotlin.Double** | Average permanent buff (power-up) pickups collected up to this time point. Only matches since build 6712 (2026-09-29) record pickup times, so only players with at least one timed permanent pickup count; &#x60;null&#x60; when there are none. |  [optional] |
| **permanentBuffsStd** | **kotlin.Double** | Standard deviation of &#x60;permanent_buffs_avg&#x60; at this time point; &#x60;null&#x60; when there are no players with timed permanent pickups. |  [optional] |



