# DeadlockApiClient.Model.Hero

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AssignedPlayersOnly** | **bool** | &#x60;m_bAssignedPlayersOnly&#x60; was removed in build 6711; always &#x60;false&#x60; since. | 
**ClassName** | **string** |  | 
**Colors** | [**HeroColors**](HeroColors.md) |  | 
**Complexity** | **long** |  | 
**Description** | [**HeroDescription**](HeroDescription.md) |  | 
**Disabled** | **bool** |  | 
**HeroStatsUi** | [**HeroStatsUI**](HeroStatsUI.md) |  | 
**Id** | **int** |  | 
**Images** | [**HeroImages**](HeroImages.md) |  | 
**InDevelopment** | **bool** |  | 
**ItemSlotInfo** | [**Dictionary&lt;string, HashMapItemSlotTypeItemSlotInfoValue&gt;**](HashMapItemSlotTypeItemSlotInfoValue.md) |  | 
**Items** | **Dictionary&lt;string, string&gt;** |  | 
**LevelInfo** | [**Dictionary&lt;string, HashMapStringLevelInfoValue&gt;**](HashMapStringLevelInfoValue.md) |  | 
**LimitedTesting** | **bool** |  | 
**Name** | **string** |  | 
**NeedsTesting** | **bool** |  | 
**Physics** | [**HeroPhysics**](HeroPhysics.md) |  | 
**PlayerSelectable** | **bool** | Read from &#x60;m_bPlayerSelectable&#x60; on older builds; since build 6711 it is derived as &#x60;development_state &#x3D;&#x3D; release&#x60;. | 
**PurchaseBonuses** | **Dictionary&lt;string, List&lt;HashMapItemSlotTypeVecPurchaseBonusValueInner&gt;&gt;** | Deprecated: &#x60;m_mapPurchaseBonuses&#x60; was removed in build 6711, so this is always empty for newer builds. | 
**ScalingStats** | [**Dictionary&lt;string, HashMapStringScalingStatValue&gt;**](HashMapStringScalingStatValue.md) |  | 
**ShopStatDisplay** | [**ShopStatDisplay**](ShopStatDisplay.md) |  | 
**Skin** | **long** |  | 
**StandardLevelUpUpgrades** | **Dictionary&lt;string, double&gt;** |  | 
**StartingStats** | [**StartingStats**](StartingStats.md) |  | 
**StatsDisplay** | [**StatsDisplay**](StatsDisplay.md) |  | 
**Tags** | **List&lt;string&gt;** | Always emitted (empty if the hero declares no &#x60;m_vecHeroTags&#x60;). | 
**CostBonuses** | **Dictionary&lt;string, List&lt;HashMapItemSlotTypeVecMapModCostBonusValueInner&gt;&gt;** |  | [optional] 
**DevelopmentState** | **HeroDevelopmentState** | Hero development state (&#x60;m_eHeroDevelopmentState&#x60;, build 6711+). &#x60;null&#x60; on older builds and on heroes that don&#39;t declare one. | [optional] 
**GunTag** | **string** |  | [optional] 
**HeroType** | **HeroType** |  | [optional] 
**HideoutRichPresence** | **string** |  | [optional] 
**ItemDraftBucketing** | [**Dictionary&lt;string, HashMapStringOptionDraftBucketingValue&gt;**](HashMapStringOptionDraftBucketingValue.md) |  | [optional] 
**ItemDraftWeights** | **Dictionary&lt;string, double&gt;** |  | [optional] 
**PrereleaseOnly** | **bool** | Read from &#x60;m_bPrereleaseOnly&#x60; on older builds; since build 6711 it is derived as &#x60;development_state &#x3D;&#x3D; pre_release&#x60;. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

