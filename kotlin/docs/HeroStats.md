
# HeroStats

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.Int** |  |  |
| **accuracy** | **kotlin.Double** |  |  |
| **assists** | **kotlin.Long** |  |  |
| **assistsPerMin** | **kotlin.Double** |  |  |
| **creepsPerMin** | **kotlin.Double** |  |  |
| **critShotRate** | **kotlin.Double** |  |  |
| **damageMitigatedPerMin** | **kotlin.Double** |  |  |
| **damagePerMin** | **kotlin.Double** |  |  |
| **damagePerSoul** | **kotlin.Double** |  |  |
| **damageTakenPerMin** | **kotlin.Double** |  |  |
| **damageTakenPerSoul** | **kotlin.Double** |  |  |
| **deaths** | **kotlin.Long** |  |  |
| **deathsPerMin** | **kotlin.Double** |  |  |
| **deniesPerMatch** | **kotlin.Double** |  |  |
| **deniesPerMin** | **kotlin.Double** |  |  |
| **endingLevel** | **kotlin.Double** |  |  |
| **heroId** | **kotlin.Int** | See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; |  |
| **kills** | **kotlin.Long** |  |  |
| **killsPerMin** | **kotlin.Double** |  |  |
| **lastHitsPerMin** | **kotlin.Double** |  |  |
| **lastPlayed** | **kotlin.Int** |  |  |
| **matches** | **kotlin.collections.List&lt;kotlin.Long&gt;** |  |  |
| **matchesPlayed** | **kotlin.Long** |  |  |
| **mvpRankCounts** | **kotlin.collections.List&lt;kotlin.Long&gt;** | Matches by the MVP rank Valve awarded the player: index 0 is rank 1 (MVP), index 1 is rank 2, index 2 is rank 3. Only the top three players of a match get a rank. |  |
| **mvpRatedMatches** | **kotlin.Long** | Matches played since Valve started reporting MVP ranks (2026-01-06). Divide &#x60;mvp_rank_counts&#x60; by this, not by &#x60;matches_played&#x60;, when the time range reaches further back. |  |
| **networthPerMin** | **kotlin.Double** |  |  |
| **objDamagePerMin** | **kotlin.Double** |  |  |
| **objDamagePerSoul** | **kotlin.Double** |  |  |
| **permanentBuffMatches** | **kotlin.Long** | Matches that carry buff pickup counts. Only matches ingested since build 6712 (late September 2026) have them here, so divide by this rather than &#x60;matches_played&#x60;. |  |
| **permanentBuffs** | **kotlin.Long** | Permanent buff (power-up) pickups over the &#x60;permanent_buff_matches&#x60; matches. Buff types: &lt;https://api.deadlock-api.com/v1/assets/misc-entities&gt; |  |
| **timePlayed** | **kotlin.Long** |  |  |
| **totalBossDamage** | **kotlin.Long** |  |  |
| **totalCreepDamage** | **kotlin.Long** |  |  |
| **totalNeutralDamage** | **kotlin.Long** |  |  |
| **totalPlayerDamage** | **kotlin.Long** |  |  |
| **totalPlayerDamageTaken** | **kotlin.Long** |  |  |
| **wins** | **kotlin.Long** |  |  |
| **avgFirstPermanentBuffTimeS** | **kotlin.Double** | Average game time (seconds) of the first permanent buff pickup, over matches with pickup timings (build 6712+, at least one permanent pickup), &#x60;null&#x60; without any. |  [optional] |
| **permanentBuffsPerMin** | **kotlin.Double** | Permanent buff pickups per minute over the &#x60;permanent_buff_matches&#x60; matches, &#x60;null&#x60; without any. |  [optional] |



