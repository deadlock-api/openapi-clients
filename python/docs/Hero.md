# Hero


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_players_only** | **bool** |  | 
**class_name** | **str** |  | 
**colors** | [**HeroColors**](HeroColors.md) |  | 
**complexity** | **int** |  | 
**cost_bonuses** | **Dict[str, List[HashMapItemSlotTypeVecMapModCostBonusValueInner]]** |  | [optional] 
**description** | [**HeroDescription**](HeroDescription.md) |  | 
**disabled** | **bool** |  | 
**gun_tag** | **str** |  | [optional] 
**hero_stats_ui** | [**HeroStatsUI**](HeroStatsUI.md) |  | 
**hero_type** | [**HeroType**](HeroType.md) |  | [optional] 
**hideout_rich_presence** | **str** |  | [optional] 
**id** | **int** |  | 
**images** | [**HeroImages**](HeroImages.md) |  | 
**in_development** | **bool** |  | 
**item_draft_bucketing** | [**Dict[str, HashMapStringOptionDraftBucketingValue]**](HashMapStringOptionDraftBucketingValue.md) |  | [optional] 
**item_draft_weights** | **Dict[str, float]** |  | [optional] 
**item_slot_info** | [**Dict[str, HashMapItemSlotTypeItemSlotInfoValue]**](HashMapItemSlotTypeItemSlotInfoValue.md) |  | 
**items** | **Dict[str, str]** |  | 
**level_info** | [**Dict[str, HashMapStringLevelInfoValue]**](HashMapStringLevelInfoValue.md) |  | 
**limited_testing** | **bool** |  | 
**name** | **str** |  | 
**needs_testing** | **bool** |  | 
**physics** | [**HeroPhysics**](HeroPhysics.md) |  | 
**player_selectable** | **bool** |  | 
**prerelease_only** | **bool** |  | [optional] 
**purchase_bonuses** | **Dict[str, List[HashMapItemSlotTypeVecPurchaseBonusValueInner]]** |  | 
**scaling_stats** | [**Dict[str, HashMapStringScalingStatValue]**](HashMapStringScalingStatValue.md) |  | 
**shop_stat_display** | [**ShopStatDisplay**](ShopStatDisplay.md) |  | 
**skin** | **int** |  | 
**standard_level_up_upgrades** | **Dict[str, float]** |  | 
**starting_stats** | [**StartingStats**](StartingStats.md) |  | 
**stats_display** | [**StatsDisplay**](StatsDisplay.md) |  | 
**tags** | **List[str]** | Always emitted (empty if the hero declares no &#x60;m_vecHeroTags&#x60;). | 

## Example

```python
from deadlock_api_client.models.hero import Hero

# TODO update the JSON string below
json = "{}"
# create an instance of Hero from a JSON string
hero_instance = Hero.from_json(json)
# print the JSON string representation of the object
print(Hero.to_json())

# convert the object into a dict
hero_dict = hero_instance.to_dict()
# create an instance of Hero from a dict
hero_from_dict = Hero.from_dict(hero_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


