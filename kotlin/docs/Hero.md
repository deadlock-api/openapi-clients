
# Hero

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **assignedPlayersOnly** | **kotlin.Boolean** | &#x60;m_bAssignedPlayersOnly&#x60; was removed in build 6711; always &#x60;false&#x60; since. |  |
| **className** | **kotlin.String** |  |  |
| **colors** | [**HeroColors**](HeroColors.md) |  |  |
| **complexity** | **kotlin.Long** |  |  |
| **description** | [**HeroDescription**](HeroDescription.md) |  |  |
| **disabled** | **kotlin.Boolean** |  |  |
| **heroStatsUi** | [**HeroStatsUI**](HeroStatsUI.md) |  |  |
| **id** | **kotlin.Int** |  |  |
| **images** | [**HeroImages**](HeroImages.md) |  |  |
| **inDevelopment** | **kotlin.Boolean** |  |  |
| **itemSlotInfo** | [**kotlin.collections.Map&lt;kotlin.String, HashMapItemSlotTypeItemSlotInfoValue&gt;**](HashMapItemSlotTypeItemSlotInfoValue.md) |  |  |
| **items** | **kotlin.collections.Map&lt;kotlin.String, kotlin.String&gt;** |  |  |
| **levelInfo** | [**kotlin.collections.Map&lt;kotlin.String, HashMapStringLevelInfoValue&gt;**](HashMapStringLevelInfoValue.md) |  |  |
| **limitedTesting** | **kotlin.Boolean** |  |  |
| **name** | **kotlin.String** |  |  |
| **needsTesting** | **kotlin.Boolean** |  |  |
| **physics** | [**HeroPhysics**](HeroPhysics.md) |  |  |
| **playerSelectable** | **kotlin.Boolean** | Read from &#x60;m_bPlayerSelectable&#x60; on older builds; since build 6711 it is derived as &#x60;development_state &#x3D;&#x3D; release&#x60;. |  |
| **purchaseBonuses** | **kotlin.collections.Map&lt;kotlin.String, kotlin.collections.List&lt;HashMapItemSlotTypeVecPurchaseBonusValueInner&gt;&gt;** | Deprecated: &#x60;m_mapPurchaseBonuses&#x60; was removed in build 6711, so this is always empty for newer builds. |  |
| **scalingStats** | [**kotlin.collections.Map&lt;kotlin.String, HashMapStringScalingStatValue&gt;**](HashMapStringScalingStatValue.md) |  |  |
| **shopStatDisplay** | [**ShopStatDisplay**](ShopStatDisplay.md) |  |  |
| **skin** | **kotlin.Long** |  |  |
| **standardLevelUpUpgrades** | **kotlin.collections.Map&lt;kotlin.String, kotlin.Double&gt;** |  |  |
| **startingStats** | [**StartingStats**](StartingStats.md) |  |  |
| **statsDisplay** | [**StatsDisplay**](StatsDisplay.md) |  |  |
| **tags** | **kotlin.collections.List&lt;kotlin.String&gt;** | Always emitted (empty if the hero declares no &#x60;m_vecHeroTags&#x60;). |  |
| **costBonuses** | **kotlin.collections.Map&lt;kotlin.String, kotlin.collections.List&lt;HashMapItemSlotTypeVecMapModCostBonusValueInner&gt;&gt;** |  |  [optional] |
| **developmentState** | [**HeroDevelopmentState**](HeroDevelopmentState.md) | Hero development state (&#x60;m_eHeroDevelopmentState&#x60;, build 6711+). &#x60;null&#x60; on older builds and on heroes that don&#39;t declare one. |  [optional] |
| **gender** | **kotlin.String** | Hero gender (&#x60;m_strHeroGender&#x60;, build 6711+), e.g. &#x60;male&#x60; / &#x60;female&#x60;. |  [optional] |
| **gunTag** | **kotlin.String** |  |  [optional] |
| **heroType** | [**HeroType**](HeroType.md) |  |  [optional] |
| **hideoutRichPresence** | **kotlin.String** |  |  [optional] |
| **itemDraftBucketing** | [**kotlin.collections.Map&lt;kotlin.String, HashMapStringOptionDraftBucketingValue&gt;**](HashMapStringOptionDraftBucketingValue.md) |  |  [optional] |
| **itemDraftWeights** | **kotlin.collections.Map&lt;kotlin.String, kotlin.Double&gt;** |  |  [optional] |
| **popularItems** | [**HeroPopularItems**](HeroPopularItems.md) | Valve&#39;s generated item pick / win rates per game phase (&#x60;m_PopularItems&#x60;, build 6711+). &#x60;null&#x60; when the hero has no data. |  [optional] |
| **prereleaseOnly** | **kotlin.Boolean** | Read from &#x60;m_bPrereleaseOnly&#x60; on older builds; since build 6711 it is derived as &#x60;development_state &#x3D;&#x3D; pre_release&#x60;. |  [optional] |
| **searchName** | **kotlin.String** | Localized search name (&#x60;m_strHeroSearchName&#x60;, build 6711+). |  [optional] |



