# deadlock_api_client


## API Clients

We have auto generated and updated clients for many languages. You can find them here: [https://github.com/deadlock-api/openapi-clients](https://github.com/deadlock-api/openapi-clients)

## Support the Deadlock API

Whether you're building your own database, developing data science projects, or enhancing your website with game and player analytics, the Deadlock API has the data you need.

Your sponsorship helps keep this resource open, free and future-proof for everyone. By supporting the Deadlock API, you will enable continued development, new features and reliable access for developers, analysts and streamers worldwide.

Help us continue to provide the data you need - sponsor the Deadlock API today!

**-> You can Sponsor the Deadlock API on [Patreon](https://www.patreon.com/c/user?u=68961896) or [GitHub](https://github.com/sponsors/raimannma)**

## Disclaimer
_deadlock-api.com is not endorsed by Valve and does not reflect the views or opinions of Valve or anyone officially involved in producing or managing Valve properties. Valve and all associated properties are trademarks or registered trademarks of Valve Corporation_
        

For more information, please visit [https://discord.gg/XMF9Xrgfqu](https://discord.gg/XMF9Xrgfqu).

## Installation & Usage

### Requirements

PHP 8.1 and later.

### Composer

To install the bindings via [Composer](https://getcomposer.org/), add the following to `composer.json`:

```json
{
  "repositories": [
    {
      "type": "vcs",
      "url": "https://github.com/deadlock-api/openapi-clients.git"
    }
  ],
  "require": {
    "deadlock-api/openapi-clients": "*@dev"
  }
}
```

Then run `composer install`

### Manual Installation

Download the files and include `autoload.php`:

```php
<?php
require_once('/path/to/deadlock_api_client/vendor/autoload.php');
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');




$apiInstance = new OpenAPI\Client\Api\AccoladesApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$accolade_id = 56; // int | Accolade id (`m_unAccoladeID`)
$language = 'language_example'; // string | Language code. Defaults to `english`.
$client_version = 56; // int | Client/game version (e.g. `6518`). Defaults to the latest known version.

try {
    $result = $apiInstance->getAccolade($accolade_id, $language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AccoladesApi->getAccolade: ', $e->getMessage(), PHP_EOL;
}

```

## API Endpoints

All URIs are relative to *https://api.deadlock-api.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccoladesApi* | [**getAccolade**](docs/Api/AccoladesApi.md#getaccolade) | **GET** /v1/assets/accolades/{accolade_id} | Get Accolade
*AccoladesApi* | [**getAccoladeByName**](docs/Api/AccoladesApi.md#getaccoladebyname) | **GET** /v1/assets/accolades/by-name/{name} | Get Accolade By Name
*AccoladesApi* | [**listAccolades**](docs/Api/AccoladesApi.md#listaccolades) | **GET** /v1/assets/accolades | List Accolades
*AnalyticsApi* | [**abilityOrderStats**](docs/Api/AnalyticsApi.md#abilityorderstats) | **GET** /v1/analytics/ability-order-stats | Ability Order Stats
*AnalyticsApi* | [**badgeDistribution**](docs/Api/AnalyticsApi.md#badgedistribution) | **GET** /v1/analytics/badge-distribution | Badge Distribution
*AnalyticsApi* | [**buildItemStats**](docs/Api/AnalyticsApi.md#builditemstats) | **GET** /v1/analytics/build-item-stats | Build Item Stats
*AnalyticsApi* | [**gameStats**](docs/Api/AnalyticsApi.md#gamestats) | **GET** /v1/analytics/game-stats | Game Stats
*AnalyticsApi* | [**heroBanStats**](docs/Api/AnalyticsApi.md#herobanstats) | **GET** /v1/analytics/hero-ban-stats | Hero Ban Stats
*AnalyticsApi* | [**heroBuildStats**](docs/Api/AnalyticsApi.md#herobuildstats) | **GET** /v1/analytics/hero-build-stats/{hero_id} | Hero Build Stats
*AnalyticsApi* | [**heroCombStats**](docs/Api/AnalyticsApi.md#herocombstats) | **GET** /v1/analytics/hero-comb-stats | Hero Comb Stats
*AnalyticsApi* | [**heroCountersStats**](docs/Api/AnalyticsApi.md#herocountersstats) | **GET** /v1/analytics/hero-counter-stats | Hero Counter Stats
*AnalyticsApi* | [**heroScoreboard**](docs/Api/AnalyticsApi.md#heroscoreboard) | **GET** /v1/analytics/scoreboards/heroes | Hero Scoreboard
*AnalyticsApi* | [**heroStats**](docs/Api/AnalyticsApi.md#herostats) | **GET** /v1/analytics/hero-stats | Hero Stats
*AnalyticsApi* | [**heroSynergiesStats**](docs/Api/AnalyticsApi.md#herosynergiesstats) | **GET** /v1/analytics/hero-synergy-stats | Hero Synergy Stats
*AnalyticsApi* | [**itemFlowStats**](docs/Api/AnalyticsApi.md#itemflowstats) | **GET** /v1/analytics/item-flow-stats | Item Flow Stats
*AnalyticsApi* | [**itemPermutationStats**](docs/Api/AnalyticsApi.md#itempermutationstats) | **GET** /v1/analytics/item-permutation-stats | Item Permutation Stats
*AnalyticsApi* | [**itemStats**](docs/Api/AnalyticsApi.md#itemstats) | **GET** /v1/analytics/item-stats | Item Stats
*AnalyticsApi* | [**killDeathStats**](docs/Api/AnalyticsApi.md#killdeathstats) | **GET** /v1/analytics/kill-death-stats | Kill Death Stats
*AnalyticsApi* | [**playerPerformanceCurve**](docs/Api/AnalyticsApi.md#playerperformancecurve) | **GET** /v1/analytics/player-performance-curve | Player Performance Curve
*AnalyticsApi* | [**playerScoreboard**](docs/Api/AnalyticsApi.md#playerscoreboard) | **GET** /v1/analytics/scoreboards/players | Player Scoreboard
*AnalyticsApi* | [**playerStatsMetrics**](docs/Api/AnalyticsApi.md#playerstatsmetrics) | **GET** /v1/analytics/player-stats/metrics | Player Stats Metrics
*AssetsBucketApi* | [**fonts**](docs/Api/AssetsBucketApi.md#fonts) | **GET** /v1/assets/fonts | Fonts Index
*AssetsBucketApi* | [**icons**](docs/Api/AssetsBucketApi.md#icons) | **GET** /v1/assets/icons | Icons Index
*AssetsBucketApi* | [**images**](docs/Api/AssetsBucketApi.md#images) | **GET** /v1/assets/images | Images Index
*AssetsBucketApi* | [**sounds**](docs/Api/AssetsBucketApi.md#sounds) | **GET** /v1/assets/sounds | Sounds Index
*BuildTagsApi* | [**getBuildTag**](docs/Api/BuildTagsApi.md#getbuildtag) | **GET** /v1/assets/build-tags/{build_tag_id} | Get Build Tag
*BuildTagsApi* | [**getBuildTagByName**](docs/Api/BuildTagsApi.md#getbuildtagbyname) | **GET** /v1/assets/build-tags/by-name/{name} | Get Build Tag By Name
*BuildTagsApi* | [**listBuildTags**](docs/Api/BuildTagsApi.md#listbuildtags) | **GET** /v1/assets/build-tags | List Build Tags
*BuildsApi* | [**searchBuilds**](docs/Api/BuildsApi.md#searchbuilds) | **GET** /v1/builds | Search
*ClientVersionsApi* | [**listClientVersions**](docs/Api/ClientVersionsApi.md#listclientversions) | **GET** /v1/assets/client-versions | List Client Versions
*ColorsApi* | [**listColors**](docs/Api/ColorsApi.md#listcolors) | **GET** /v1/assets/colors | List Colors
*CommandsApi* | [**availableVariables**](docs/Api/CommandsApi.md#availablevariables) | **GET** /v1/commands/variables/available | Available Variables
*CommandsApi* | [**commandResolve**](docs/Api/CommandsApi.md#commandresolve) | **GET** /v1/commands/resolve | Resolve Command
*CommandsApi* | [**variablesResolve**](docs/Api/CommandsApi.md#variablesresolve) | **GET** /v1/commands/variables/resolve | Resolve Variables
*CommandsApi* | [**widgetVersions**](docs/Api/CommandsApi.md#widgetversions) | **GET** /v1/commands/widgets/versions | Widget Versions
*CustomMatchesApi* | [**createCustom**](docs/Api/CustomMatchesApi.md#createcustom) | **POST** /v1/matches/custom/create | Create Match
*CustomMatchesApi* | [**getCustom**](docs/Api/CustomMatchesApi.md#getcustom) | **GET** /v1/matches/custom/{party_id}/match-id | Get Match ID
*CustomMatchesApi* | [**leave**](docs/Api/CustomMatchesApi.md#leave) | **POST** /v1/matches/custom/{lobby_id}/leave | Leave Lobby
*CustomMatchesApi* | [**readyUp**](docs/Api/CustomMatchesApi.md#readyup) | **POST** /v1/matches/custom/{lobby_id}/ready | Ready Up
*CustomMatchesApi* | [**start**](docs/Api/CustomMatchesApi.md#start) | **POST** /v1/matches/custom/{lobby_id}/start | Start Match
*CustomMatchesApi* | [**unready**](docs/Api/CustomMatchesApi.md#unready) | **POST** /v1/matches/custom/{lobby_id}/unready | Unready
*DemoApi* | [**liveQuery**](docs/Api/DemoApi.md#livequery) | **GET** /v1/matches/demo/live/query | Live Demo Query (SSE)
*DemoApi* | [**schema**](docs/Api/DemoApi.md#schema) | **GET** /v1/matches/demo/schema | Demo Schema
*DemoApi* | [**status**](docs/Api/DemoApi.md#status) | **GET** /v1/matches/demo/query/{job_id} | Demo Query Status
*DemoApi* | [**submit**](docs/Api/DemoApi.md#submit) | **POST** /v1/matches/demo/query | Demo Query
*GenericDataApi* | [**getGenericData**](docs/Api/GenericDataApi.md#getgenericdata) | **GET** /v1/assets/generic-data | Get Generic Data
*GraphQLApi* | [**playground**](docs/Api/GraphQLApi.md#playground) | **GET** /v1/graphql | GraphQL Playground
*HeroesApi* | [**getHero**](docs/Api/HeroesApi.md#gethero) | **GET** /v1/assets/heroes/{hero_id} | Get Hero
*HeroesApi* | [**getHeroByName**](docs/Api/HeroesApi.md#getherobyname) | **GET** /v1/assets/heroes/by-name/{name} | Get Hero By Name
*HeroesApi* | [**listHeroes**](docs/Api/HeroesApi.md#listheroes) | **GET** /v1/assets/heroes | List Heroes
*InfoApi* | [**healthCheck**](docs/Api/InfoApi.md#healthcheck) | **GET** /v1/info/health | Health Check
*InfoApi* | [**info**](docs/Api/InfoApi.md#info) | **GET** /v1/info | API Info
*InternalApi* | [**ingestSalts**](docs/Api/InternalApi.md#ingestsalts) | **POST** /v1/matches/salts | Match Salts Ingest
*ItemsApi* | [**getItem**](docs/Api/ItemsApi.md#getitem) | **GET** /v1/assets/items/{id_or_class_name} | Get Item
*ItemsApi* | [**getItemsByHeroId**](docs/Api/ItemsApi.md#getitemsbyheroid) | **GET** /v1/assets/items/by-hero-id/{id} | List Items By Hero
*ItemsApi* | [**getItemsBySlotType**](docs/Api/ItemsApi.md#getitemsbyslottype) | **GET** /v1/assets/items/by-slot-type/{slot_type} | List Items By Slot Type
*ItemsApi* | [**getItemsByType**](docs/Api/ItemsApi.md#getitemsbytype) | **GET** /v1/assets/items/by-type/{type} | List Items By Type
*ItemsApi* | [**listItems**](docs/Api/ItemsApi.md#listitems) | **GET** /v1/assets/items | List Items
*LeaderboardApi* | [**leaderboard**](docs/Api/LeaderboardApi.md#leaderboard) | **GET** /v1/leaderboard/{region} | Leaderboard
*LeaderboardApi* | [**leaderboardHero**](docs/Api/LeaderboardApi.md#leaderboardhero) | **GET** /v1/leaderboard/{region}/{hero_id} | Hero Leaderboard
*LeaderboardApi* | [**leaderboardHeroRaw**](docs/Api/LeaderboardApi.md#leaderboardheroraw) | **GET** /v1/leaderboard/{region}/{hero_id}/raw | Hero Leaderboard as Protobuf
*LeaderboardApi* | [**leaderboardRaw**](docs/Api/LeaderboardApi.md#leaderboardraw) | **GET** /v1/leaderboard/{region}/raw | Leaderboard as Protobuf
*LootTablesApi* | [**listLootTables**](docs/Api/LootTablesApi.md#listloottables) | **GET** /v1/assets/loot-tables | List Loot Tables
*MMRApi* | [**heroMmr**](docs/Api/MMRApi.md#herommr) | **GET** /v1/players/mmr/{hero_id} | Batch Hero MMR
*MMRApi* | [**heroMmrDistribution**](docs/Api/MMRApi.md#herommrdistribution) | **GET** /v1/players/mmr/distribution/{hero_id} | Hero MMR Distribution
*MMRApi* | [**heroMmrHistory**](docs/Api/MMRApi.md#herommrhistory) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History
*MMRApi* | [**mmr**](docs/Api/MMRApi.md#mmr) | **GET** /v1/players/mmr | Batch MMR
*MMRApi* | [**mmrDistribution**](docs/Api/MMRApi.md#mmrdistribution) | **GET** /v1/players/mmr/distribution | MMR Distribution
*MMRApi* | [**mmrHistory**](docs/Api/MMRApi.md#mmrhistory) | **GET** /v1/players/{account_id}/mmr-history | MMR History
*MapApi* | [**getMap**](docs/Api/MapApi.md#getmap) | **GET** /v1/assets/map | Map
*MatchesApi* | [**activeMatches**](docs/Api/MatchesApi.md#activematches) | **GET** /v1/matches/active | Active
*MatchesApi* | [**activeMatchesRaw**](docs/Api/MatchesApi.md#activematchesraw) | **GET** /v1/matches/active/raw | Active as Protobuf
*MatchesApi* | [**bulkMetadata**](docs/Api/MatchesApi.md#bulkmetadata) | **GET** /v1/matches/metadata | Bulk Metadata
*MatchesApi* | [**ingestUrls**](docs/Api/MatchesApi.md#ingesturls) | **POST** /v1/matches/live/urls | Ingest Live Broadcast URLs
*MatchesApi* | [**metadata**](docs/Api/MatchesApi.md#metadata) | **GET** /v1/matches/{match_id}/metadata | Metadata
*MatchesApi* | [**metadataRaw**](docs/Api/MatchesApi.md#metadataraw) | **GET** /v1/matches/{match_id}/metadata/raw | Metadata as Protobuf
*MatchesApi* | [**recentlyFetched**](docs/Api/MatchesApi.md#recentlyfetched) | **GET** /v1/matches/recently-fetched | Recently Fetched
*MatchesApi* | [**salts**](docs/Api/MatchesApi.md#salts) | **GET** /v1/matches/{match_id}/salts | Salts
*MatchesApi* | [**url**](docs/Api/MatchesApi.md#url) | **GET** /v1/matches/{match_id}/live/url | Live Broadcast URL
*MatchesApi* | [**urls**](docs/Api/MatchesApi.md#urls) | **GET** /v1/matches/live/urls | Live Broadcast URLs
*MiscEntitiesApi* | [**getMiscEntity**](docs/Api/MiscEntitiesApi.md#getmiscentity) | **GET** /v1/assets/misc-entities/{id_or_classname} | Get Misc Entity
*MiscEntitiesApi* | [**listMiscEntities**](docs/Api/MiscEntitiesApi.md#listmiscentities) | **GET** /v1/assets/misc-entities | List Misc Entities
*NPCUnitsApi* | [**getNpcUnit**](docs/Api/NPCUnitsApi.md#getnpcunit) | **GET** /v1/assets/npc-units/{id_or_classname} | Get NPC Unit
*NPCUnitsApi* | [**listNpcUnits**](docs/Api/NPCUnitsApi.md#listnpcunits) | **GET** /v1/assets/npc-units | List NPC Units
*PatchesApi* | [**bigPatchDays**](docs/Api/PatchesApi.md#bigpatchdays) | **GET** /v1/patches/big-days | Big Days
*PatchesApi* | [**feed**](docs/Api/PatchesApi.md#feed) | **GET** /v1/patches | Notes
*PatchesApi* | [**feed_0**](docs/Api/PatchesApi.md#feed_0) | **GET** /v2/patches | Notes
*PlayersApi* | [**accountStats**](docs/Api/PlayersApi.md#accountstats) | **GET** /v1/players/{account_id}/account-stats | Account Stats
*PlayersApi* | [**card**](docs/Api/PlayersApi.md#card) | **GET** /v1/players/{account_id}/card | Card
*PlayersApi* | [**enemyStats**](docs/Api/PlayersApi.md#enemystats) | **GET** /v1/players/{account_id}/enemy-stats | Enemy Stats
*PlayersApi* | [**matchHistory**](docs/Api/PlayersApi.md#matchhistory) | **GET** /v1/players/{account_id}/match-history | Match History
*PlayersApi* | [**mateStats**](docs/Api/PlayersApi.md#matestats) | **GET** /v1/players/{account_id}/mate-stats | Mate Stats
*PlayersApi* | [**playerHeroStats**](docs/Api/PlayersApi.md#playerherostats) | **GET** /v1/players/hero-stats | Hero Stats
*PlayersApi* | [**rankPredict**](docs/Api/PlayersApi.md#rankpredict) | **GET** /v1/players/{account_id}/rank-predict | Rank Predict
*PlayersApi* | [**rankPredictAvgImage**](docs/Api/PlayersApi.md#rankpredictavgimage) | **GET** /v1/players/rank-predict/image | Rank Predict Avg Image
*PlayersApi* | [**rankPredictImage**](docs/Api/PlayersApi.md#rankpredictimage) | **GET** /v1/players/{account_id}/rank-predict/image | Rank Predict Image
*RanksApi* | [**getRank**](docs/Api/RanksApi.md#getrank) | **GET** /v1/assets/ranks/{tier} | Get Rank
*RanksApi* | [**listRanks**](docs/Api/RanksApi.md#listranks) | **GET** /v1/assets/ranks | List Ranks
*SQLApi* | [**listTables**](docs/Api/SQLApi.md#listtables) | **GET** /v1/sql/tables | List Tables
*SQLApi* | [**sql**](docs/Api/SQLApi.md#sql) | **GET** /v1/sql | Query
*SQLApi* | [**tableSchema**](docs/Api/SQLApi.md#tableschema) | **GET** /v1/sql/tables/{table}/schema | Table Schema
*ServersApi* | [**callList**](docs/Api/ServersApi.md#calllist) | **GET** /v1/servers | List Game Servers
*ServersApi* | [**ingest**](docs/Api/ServersApi.md#ingest) | **POST** /v1/servers/metrics | Game Server Metric Ingest
*ServersApi* | [**status**](docs/Api/ServersApi.md#status) | **POST** /v1/servers/status | Game Server Status
*ServersApi* | [**steamList**](docs/Api/ServersApi.md#steamlist) | **GET** /v1/servers/steam | List Steam Game Servers
*SteamApi* | [**steam**](docs/Api/SteamApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile
*SteamApi* | [**steamSearch**](docs/Api/SteamApi.md#steamsearch) | **GET** /v1/players/steam-search | Steam Profile Search
*SteamInfoApi* | [**getAllSteamInfo**](docs/Api/SteamInfoApi.md#getallsteaminfo) | **GET** /v1/assets/steam-info/all | Get All Steam Infos
*SteamInfoApi* | [**getSteamInfo**](docs/Api/SteamInfoApi.md#getsteaminfo) | **GET** /v1/assets/steam-info | Get Steam Info

## Models

- [APIInfo](docs/Model/APIInfo.md)
- [Ability](docs/Model/Ability.md)
- [AbilityActivation](docs/Model/AbilityActivation.md)
- [AbilityDescription](docs/Model/AbilityDescription.md)
- [AbilityImbue](docs/Model/AbilityImbue.md)
- [AbilitySectionType](docs/Model/AbilitySectionType.md)
- [AbilityTooltipDetails](docs/Model/AbilityTooltipDetails.md)
- [AbilityType](docs/Model/AbilityType.md)
- [AbilityVideos](docs/Model/AbilityVideos.md)
- [Accolade](docs/Model/Accolade.md)
- [ActiveMatch](docs/Model/ActiveMatch.md)
- [ActiveMatchGameMode](docs/Model/ActiveMatchGameMode.md)
- [ActiveMatchMode](docs/Model/ActiveMatchMode.md)
- [ActiveMatchPlayer](docs/Model/ActiveMatchPlayer.md)
- [ActiveMatchTeam](docs/Model/ActiveMatchTeam.md)
- [AnalyticsAbilityOrderStats](docs/Model/AnalyticsAbilityOrderStats.md)
- [AnalyticsGameStats](docs/Model/AnalyticsGameStats.md)
- [AnalyticsHeroStats](docs/Model/AnalyticsHeroStats.md)
- [BadgeDistribution](docs/Model/BadgeDistribution.md)
- [Build](docs/Model/Build.md)
- [BuildHero](docs/Model/BuildHero.md)
- [BuildHeroDetails](docs/Model/BuildHeroDetails.md)
- [BuildHeroDetailsAbilityOrder](docs/Model/BuildHeroDetailsAbilityOrder.md)
- [BuildHeroDetailsAbilityOrderCurrencyChange](docs/Model/BuildHeroDetailsAbilityOrderCurrencyChange.md)
- [BuildHeroDetailsCategory](docs/Model/BuildHeroDetailsCategory.md)
- [BuildHeroDetailsCategoryAbility](docs/Model/BuildHeroDetailsCategoryAbility.md)
- [BuildItemStats](docs/Model/BuildItemStats.md)
- [BuildTag](docs/Model/BuildTag.md)
- [ClickhouseMatchInfo](docs/Model/ClickhouseMatchInfo.md)
- [ClickhouseSalts](docs/Model/ClickhouseSalts.md)
- [Color](docs/Model/Color.md)
- [ColumnSchema](docs/Model/ColumnSchema.md)
- [CreateCustomRequest](docs/Model/CreateCustomRequest.md)
- [CreateCustomResponse](docs/Model/CreateCustomResponse.md)
- [Curve](docs/Model/Curve.md)
- [CurveOrFloat](docs/Model/CurveOrFloat.md)
- [DamageFlash](docs/Model/DamageFlash.md)
- [DemoQueryJobResponse](docs/Model/DemoQueryJobResponse.md)
- [DemoQueryRequest](docs/Model/DemoQueryRequest.md)
- [DemoQueryStatusResponse](docs/Model/DemoQueryStatusResponse.md)
- [DemoSchemaResponse](docs/Model/DemoSchemaResponse.md)
- [DependantAbilities](docs/Model/DependantAbilities.md)
- [DistributionEntry](docs/Model/DistributionEntry.md)
- [DraftBucket](docs/Model/DraftBucket.md)
- [DraftBuckets](docs/Model/DraftBuckets.md)
- [EnemyStats](docs/Model/EnemyStats.md)
- [FeedItem](docs/Model/FeedItem.md)
- [FeedItemOneOf](docs/Model/FeedItemOneOf.md)
- [FeedItemOneOf1](docs/Model/FeedItemOneOf1.md)
- [FlashData](docs/Model/FlashData.md)
- [ForumPatch](docs/Model/ForumPatch.md)
- [GameMode](docs/Model/GameMode.md)
- [GameServerInfo](docs/Model/GameServerInfo.md)
- [GenericData](docs/Model/GenericData.md)
- [GetCustomMatchIdResponse](docs/Model/GetCustomMatchIdResponse.md)
- [GlitchSettings](docs/Model/GlitchSettings.md)
- [HashMapItemSlotTypeItemSlotInfoValue](docs/Model/HashMapItemSlotTypeItemSlotInfoValue.md)
- [HashMapItemSlotTypeVecMapModCostBonusValueInner](docs/Model/HashMapItemSlotTypeVecMapModCostBonusValueInner.md)
- [HashMapItemSlotTypeVecPurchaseBonusValueInner](docs/Model/HashMapItemSlotTypeVecPurchaseBonusValueInner.md)
- [HashMapStringLevelInfoValue](docs/Model/HashMapStringLevelInfoValue.md)
- [HashMapStringOptionDraftBucketingValue](docs/Model/HashMapStringOptionDraftBucketingValue.md)
- [HashMapStringScalingStatValue](docs/Model/HashMapStringScalingStatValue.md)
- [HashMapValue](docs/Model/HashMapValue.md)
- [Hero](docs/Model/Hero.md)
- [HeroBanStats](docs/Model/HeroBanStats.md)
- [HeroBuildStats](docs/Model/HeroBuildStats.md)
- [HeroColors](docs/Model/HeroColors.md)
- [HeroCombStats](docs/Model/HeroCombStats.md)
- [HeroCounterStats](docs/Model/HeroCounterStats.md)
- [HeroDescription](docs/Model/HeroDescription.md)
- [HeroEntry](docs/Model/HeroEntry.md)
- [HeroImages](docs/Model/HeroImages.md)
- [HeroPhysics](docs/Model/HeroPhysics.md)
- [HeroStats](docs/Model/HeroStats.md)
- [HeroStatsUI](docs/Model/HeroStatsUI.md)
- [HeroStatsUIDisplay](docs/Model/HeroStatsUIDisplay.md)
- [HeroSynergyStats](docs/Model/HeroSynergyStats.md)
- [HeroType](docs/Model/HeroType.md)
- [HorizontalRecoil](docs/Model/HorizontalRecoil.md)
- [IngestLiveUrl](docs/Model/IngestLiveUrl.md)
- [Item](docs/Model/Item.md)
- [ItemDraftRound](docs/Model/ItemDraftRound.md)
- [ItemDraftRoundPerGameRound](docs/Model/ItemDraftRoundPerGameRound.md)
- [ItemFlowEdge](docs/Model/ItemFlowEdge.md)
- [ItemFlowNode](docs/Model/ItemFlowNode.md)
- [ItemFlowStats](docs/Model/ItemFlowStats.md)
- [ItemFlowSummary](docs/Model/ItemFlowSummary.md)
- [ItemGroup](docs/Model/ItemGroup.md)
- [ItemPermutationStats](docs/Model/ItemPermutationStats.md)
- [ItemProperty](docs/Model/ItemProperty.md)
- [ItemSlotType](docs/Model/ItemSlotType.md)
- [ItemStats](docs/Model/ItemStats.md)
- [ItemType](docs/Model/ItemType.md)
- [JobStatus](docs/Model/JobStatus.md)
- [KillDeathStats](docs/Model/KillDeathStats.md)
- [LaneInfo](docs/Model/LaneInfo.md)
- [Leaderboard](docs/Model/Leaderboard.md)
- [LeaderboardEntry](docs/Model/LeaderboardEntry.md)
- [ListServersResponse](docs/Model/ListServersResponse.md)
- [LiveUrl](docs/Model/LiveUrl.md)
- [LootEntry](docs/Model/LootEntry.md)
- [LootTable](docs/Model/LootTable.md)
- [MMRHistory](docs/Model/MMRHistory.md)
- [MapData](docs/Model/MapData.md)
- [MapImages](docs/Model/MapImages.md)
- [MatchPlayer](docs/Model/MatchPlayer.md)
- [MatchSaltsResponse](docs/Model/MatchSaltsResponse.md)
- [MatchSpectateResponse](docs/Model/MatchSpectateResponse.md)
- [MateStats](docs/Model/MateStats.md)
- [MetricIngestRequest](docs/Model/MetricIngestRequest.md)
- [MiniMapOffsets](docs/Model/MiniMapOffsets.md)
- [MiscEntity](docs/Model/MiscEntity.md)
- [ModifierValue](docs/Model/ModifierValue.md)
- [NewPlayerMetrics](docs/Model/NewPlayerMetrics.md)
- [NpcUnit](docs/Model/NpcUnit.md)
- [ObjectiveParams](docs/Model/ObjectiveParams.md)
- [ObjectivePosition](docs/Model/ObjectivePosition.md)
- [OutcomeToWeights](docs/Model/OutcomeToWeights.md)
- [OutputFormat](docs/Model/OutputFormat.md)
- [Patch](docs/Model/Patch.md)
- [PatchCategory](docs/Model/PatchCategory.md)
- [PatchGuid](docs/Model/PatchGuid.md)
- [Pickup](docs/Model/Pickup.md)
- [PlayerAccountHeroStats](docs/Model/PlayerAccountHeroStats.md)
- [PlayerAccountStats](docs/Model/PlayerAccountStats.md)
- [PlayerCard](docs/Model/PlayerCard.md)
- [PlayerCardSlot](docs/Model/PlayerCardSlot.md)
- [PlayerCardSlotHero](docs/Model/PlayerCardSlotHero.md)
- [PlayerCardSlotStat](docs/Model/PlayerCardSlotStat.md)
- [PlayerEntry](docs/Model/PlayerEntry.md)
- [PlayerMatchHistoryEntry](docs/Model/PlayerMatchHistoryEntry.md)
- [PlayerPerformanceCurvePoint](docs/Model/PlayerPerformanceCurvePoint.md)
- [Rank](docs/Model/Rank.md)
- [RankImages](docs/Model/RankImages.md)
- [RankPredictResponse](docs/Model/RankPredictResponse.md)
- [RankPrediction](docs/Model/RankPrediction.md)
- [RawAbilityUpgrade](docs/Model/RawAbilityUpgrade.md)
- [RawAbilityUpgradePropertyUpgrade](docs/Model/RawAbilityUpgradePropertyUpgrade.md)
- [RawCustomCrosshairSettings](docs/Model/RawCustomCrosshairSettings.md)
- [RawItemPropertyScaleFunctionSubclass](docs/Model/RawItemPropertyScaleFunctionSubclass.md)
- [RawItemWeaponInfoBulletSpeedCurve](docs/Model/RawItemWeaponInfoBulletSpeedCurve.md)
- [RawItemWeaponInfoBulletSpeedCurveSpline](docs/Model/RawItemWeaponInfoBulletSpeedCurveSpline.md)
- [RawItemWeaponInfoInner](docs/Model/RawItemWeaponInfoInner.md)
- [RawWeaponInfoHorizontalRecoil](docs/Model/RawWeaponInfoHorizontalRecoil.md)
- [RawWeaponInfoVerticalRecoil](docs/Model/RawWeaponInfoVerticalRecoil.md)
- [RecoilRange](docs/Model/RecoilRange.md)
- [RegionMode](docs/Model/RegionMode.md)
- [RejuvParams](docs/Model/RejuvParams.md)
- [ScriptValues](docs/Model/ScriptValues.md)
- [ServerRegion](docs/Model/ServerRegion.md)
- [ServerStatusRequest](docs/Model/ServerStatusRequest.md)
- [ServerStatusResponse](docs/Model/ServerStatusResponse.md)
- [ShopSpiritStatsDisplay](docs/Model/ShopSpiritStatsDisplay.md)
- [ShopStatDisplay](docs/Model/ShopStatDisplay.md)
- [ShopVitalityStatsDisplay](docs/Model/ShopVitalityStatsDisplay.md)
- [ShopWeaponStatsDisplay](docs/Model/ShopWeaponStatsDisplay.md)
- [SpreadPenalty](docs/Model/SpreadPenalty.md)
- [StartingStat](docs/Model/StartingStat.md)
- [StartingStats](docs/Model/StartingStats.md)
- [StatsDisplay](docs/Model/StatsDisplay.md)
- [StatsUsageFlag](docs/Model/StatsUsageFlag.md)
- [Status](docs/Model/Status.md)
- [StatusServices](docs/Model/StatusServices.md)
- [SteamFriend](docs/Model/SteamFriend.md)
- [SteamInfo](docs/Model/SteamInfo.md)
- [SteamNews](docs/Model/SteamNews.md)
- [SteamProfile](docs/Model/SteamProfile.md)
- [SteamServer](docs/Model/SteamServer.md)
- [StreetBrawl](docs/Model/StreetBrawl.md)
- [SubclassBulletResistModifier](docs/Model/SubclassBulletResistModifier.md)
- [SubclassBulletResistModifierSubclass](docs/Model/SubclassBulletResistModifierSubclass.md)
- [SubclassEmpoweredModifierLevel](docs/Model/SubclassEmpoweredModifierLevel.md)
- [SubclassEmpoweredModifierLevelSubclass](docs/Model/SubclassEmpoweredModifierLevelSubclass.md)
- [SubclassIntrinsicModifiers](docs/Model/SubclassIntrinsicModifiers.md)
- [SubclassIntrinsicModifiersSubclass](docs/Model/SubclassIntrinsicModifiersSubclass.md)
- [SubclassModifierDefinition](docs/Model/SubclassModifierDefinition.md)
- [SubclassModifierDefinitionSubclass](docs/Model/SubclassModifierDefinitionSubclass.md)
- [SubclassObjectiveHealthGrowthPhase](docs/Model/SubclassObjectiveHealthGrowthPhase.md)
- [SubclassObjectiveHealthGrowthPhaseSubclass](docs/Model/SubclassObjectiveHealthGrowthPhaseSubclass.md)
- [SubclassObjectiveRegen](docs/Model/SubclassObjectiveRegen.md)
- [SubclassObjectiveRegenSubclass](docs/Model/SubclassObjectiveRegenSubclass.md)
- [SubclassRangedArmorModifier](docs/Model/SubclassRangedArmorModifier.md)
- [SubclassRangedArmorModifierSubclass](docs/Model/SubclassRangedArmorModifierSubclass.md)
- [SubclassTrooperDamageReduction](docs/Model/SubclassTrooperDamageReduction.md)
- [SubclassTrooperDamageReductionSubclass](docs/Model/SubclassTrooperDamageReductionSubclass.md)
- [TableSchemaResponse](docs/Model/TableSchemaResponse.md)
- [TableSize](docs/Model/TableSize.md)
- [TooltipDetailsBlock](docs/Model/TooltipDetailsBlock.md)
- [TooltipDetailsBlockProperty](docs/Model/TooltipDetailsBlockProperty.md)
- [TooltipDetailsInfoSection](docs/Model/TooltipDetailsInfoSection.md)
- [Upgrade](docs/Model/Upgrade.md)
- [UpgradeDescription](docs/Model/UpgradeDescription.md)
- [UpgradeProperty](docs/Model/UpgradeProperty.md)
- [UpgradeTooltipImportantPropertyWithIcon](docs/Model/UpgradeTooltipImportantPropertyWithIcon.md)
- [UpgradeTooltipSection](docs/Model/UpgradeTooltipSection.md)
- [UpgradeTooltipSectionAttribute](docs/Model/UpgradeTooltipSectionAttribute.md)
- [VariableCategory](docs/Model/VariableCategory.md)
- [VariableDescription](docs/Model/VariableDescription.md)
- [VerticalRecoil](docs/Model/VerticalRecoil.md)
- [Weapon](docs/Model/Weapon.md)
- [WeaponInfo](docs/Model/WeaponInfo.md)
- [ZiplanePath](docs/Model/ZiplanePath.md)

## Authorization

Authentication schemes defined for the API:
### api_key_header

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header


### api_key_query

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: URL query string


## Tests

To run the tests, use:

```bash
composer install
vendor/bin/phpunit
```

## Author



## About this package

This PHP package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: `0.1.0`
    - Generator version: `7.24.0`
- Build package: `org.openapitools.codegen.languages.PhpClientCodegen`
