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
**Models** | **Dictionary&lt;string, string&gt;** | 3D model of the hero as a self-contained glTF binary (&#x60;.glb&#x60;), keyed by pose (e.g. &#x60;hero_select&#x60;, the hero select screen pose). Each file holds the skinned mesh, its skeleton and that pose&#39;s animation clip; weapons and props only sit in the hero&#39;s hands once the clip is applied. Uses &#x60;EXT_meshopt_compression&#x60; and &#x60;EXT_texture_webp&#x60;. Empty when the game files don&#39;t ship the hero&#39;s model. | 
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
**Gender** | **string** | Hero gender (&#x60;m_strHeroGender&#x60;, build 6711+), e.g. &#x60;male&#x60; / &#x60;female&#x60;. | [optional] 
**GunTag** | **string** |  | [optional] 
**HeroType** | **HeroType** |  | [optional] 
**HideoutRichPresence** | **string** |  | [optional] 
**ItemDraftBucketing** | [**Dictionary&lt;string, HashMapStringOptionDraftBucketingValue&gt;**](HashMapStringOptionDraftBucketingValue.md) |  | [optional] 
**ItemDraftWeights** | **Dictionary&lt;string, double&gt;** |  | [optional] 
**PopularItems** | [**HeroPopularItems**](HeroPopularItems.md) | Valve&#39;s generated item pick / win rates per game phase (&#x60;m_PopularItems&#x60;, build 6711+). &#x60;null&#x60; when the hero has no data. | [optional] 
**PrereleaseOnly** | **bool** | Read from &#x60;m_bPrereleaseOnly&#x60; on older builds; since build 6711 it is derived as &#x60;development_state &#x3D;&#x3D; pre_release&#x60;. | [optional] 
**SearchName** | **string** | Localized search name (&#x60;m_strHeroSearchName&#x60;, build 6711+). | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

