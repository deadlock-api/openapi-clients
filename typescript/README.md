## deadlock_api_client@0.1.0

This generator creates TypeScript/JavaScript client that utilizes [axios](https://github.com/axios/axios). The generated Node module can be used in the following environments:

Environment
* Node.js
* Webpack
* Browserify

Language level
* ES5 - you must have a Promises/A+ library installed
* ES6

Module system
* CommonJS
* ES6 module system

It can be used in both TypeScript and JavaScript. In TypeScript, the definition will be automatically resolved via `package.json`. ([Reference](https://www.typescriptlang.org/docs/handbook/declaration-files/consumption.html))

### Building

To build and compile the typescript sources to javascript use:
```
npm install
npm run build
```

### Publishing

First build the package then run `npm publish`

### Consuming

navigate to the folder of your consuming project and run one of the following commands.

_published:_

```
npm install deadlock_api_client@0.1.0 --save
```

_unPublished (not recommended):_

```
npm install PATH_TO_GENERATED_PACKAGE --save
```

### Documentation for API Endpoints

All URIs are relative to *https://api.deadlock-api.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccoladesApi* | [**getAccolade**](docs/AccoladesApi.md#getaccolade) | **GET** /v1/assets/accolades/{accolade_id} | Get Accolade
*AccoladesApi* | [**getAccoladeByName**](docs/AccoladesApi.md#getaccoladebyname) | **GET** /v1/assets/accolades/by-name/{name} | Get Accolade By Name
*AccoladesApi* | [**listAccolades**](docs/AccoladesApi.md#listaccolades) | **GET** /v1/assets/accolades | List Accolades
*AnalyticsApi* | [**abilityOrderStats**](docs/AnalyticsApi.md#abilityorderstats) | **GET** /v1/analytics/ability-order-stats | Ability Order Stats
*AnalyticsApi* | [**badgeDistribution**](docs/AnalyticsApi.md#badgedistribution) | **GET** /v1/analytics/badge-distribution | Badge Distribution
*AnalyticsApi* | [**buildItemStats**](docs/AnalyticsApi.md#builditemstats) | **GET** /v1/analytics/build-item-stats | Build Item Stats
*AnalyticsApi* | [**gameStats**](docs/AnalyticsApi.md#gamestats) | **GET** /v1/analytics/game-stats | Game Stats
*AnalyticsApi* | [**heroBanStats**](docs/AnalyticsApi.md#herobanstats) | **GET** /v1/analytics/hero-ban-stats | Hero Ban Stats
*AnalyticsApi* | [**heroBuildStats**](docs/AnalyticsApi.md#herobuildstats) | **GET** /v1/analytics/hero-build-stats/{hero_id} | Hero Build Stats
*AnalyticsApi* | [**heroCombStats**](docs/AnalyticsApi.md#herocombstats) | **GET** /v1/analytics/hero-comb-stats | Hero Comb Stats
*AnalyticsApi* | [**heroCountersStats**](docs/AnalyticsApi.md#herocountersstats) | **GET** /v1/analytics/hero-counter-stats | Hero Counter Stats
*AnalyticsApi* | [**heroScoreboard**](docs/AnalyticsApi.md#heroscoreboard) | **GET** /v1/analytics/scoreboards/heroes | Hero Scoreboard
*AnalyticsApi* | [**heroStats**](docs/AnalyticsApi.md#herostats) | **GET** /v1/analytics/hero-stats | Hero Stats
*AnalyticsApi* | [**heroSynergiesStats**](docs/AnalyticsApi.md#herosynergiesstats) | **GET** /v1/analytics/hero-synergy-stats | Hero Synergy Stats
*AnalyticsApi* | [**itemFlowStats**](docs/AnalyticsApi.md#itemflowstats) | **GET** /v1/analytics/item-flow-stats | Item Flow Stats
*AnalyticsApi* | [**itemPermutationStats**](docs/AnalyticsApi.md#itempermutationstats) | **GET** /v1/analytics/item-permutation-stats | Item Permutation Stats
*AnalyticsApi* | [**itemStats**](docs/AnalyticsApi.md#itemstats) | **GET** /v1/analytics/item-stats | Item Stats
*AnalyticsApi* | [**killDeathStats**](docs/AnalyticsApi.md#killdeathstats) | **GET** /v1/analytics/kill-death-stats | Kill Death Stats
*AnalyticsApi* | [**playerPerformanceCurve**](docs/AnalyticsApi.md#playerperformancecurve) | **GET** /v1/analytics/player-performance-curve | Player Performance Curve
*AnalyticsApi* | [**playerScoreboard**](docs/AnalyticsApi.md#playerscoreboard) | **GET** /v1/analytics/scoreboards/players | Player Scoreboard
*AnalyticsApi* | [**playerStatsMetrics**](docs/AnalyticsApi.md#playerstatsmetrics) | **GET** /v1/analytics/player-stats/metrics | Player Stats Metrics
*AssetsBucketApi* | [**fonts**](docs/AssetsBucketApi.md#fonts) | **GET** /v1/assets/fonts | Fonts Index
*AssetsBucketApi* | [**icons**](docs/AssetsBucketApi.md#icons) | **GET** /v1/assets/icons | Icons Index
*AssetsBucketApi* | [**images**](docs/AssetsBucketApi.md#images) | **GET** /v1/assets/images | Images Index
*AssetsBucketApi* | [**sounds**](docs/AssetsBucketApi.md#sounds) | **GET** /v1/assets/sounds | Sounds Index
*BuildTagsApi* | [**getBuildTag**](docs/BuildTagsApi.md#getbuildtag) | **GET** /v1/assets/build-tags/{build_tag_id} | Get Build Tag
*BuildTagsApi* | [**getBuildTagByName**](docs/BuildTagsApi.md#getbuildtagbyname) | **GET** /v1/assets/build-tags/by-name/{name} | Get Build Tag By Name
*BuildTagsApi* | [**listBuildTags**](docs/BuildTagsApi.md#listbuildtags) | **GET** /v1/assets/build-tags | List Build Tags
*BuildsApi* | [**searchBuilds**](docs/BuildsApi.md#searchbuilds) | **GET** /v1/builds | Search
*ClientVersionsApi* | [**listClientVersions**](docs/ClientVersionsApi.md#listclientversions) | **GET** /v1/assets/client-versions | List Client Versions
*ColorsApi* | [**listColors**](docs/ColorsApi.md#listcolors) | **GET** /v1/assets/colors | List Colors
*CommandsApi* | [**availableVariables**](docs/CommandsApi.md#availablevariables) | **GET** /v1/commands/variables/available | Available Variables
*CommandsApi* | [**commandResolve**](docs/CommandsApi.md#commandresolve) | **GET** /v1/commands/resolve | Resolve Command
*CommandsApi* | [**variablesResolve**](docs/CommandsApi.md#variablesresolve) | **GET** /v1/commands/variables/resolve | Resolve Variables
*CommandsApi* | [**widgetVersions**](docs/CommandsApi.md#widgetversions) | **GET** /v1/commands/widgets/versions | Widget Versions
*CustomMatchesApi* | [**createCustom**](docs/CustomMatchesApi.md#createcustom) | **POST** /v1/matches/custom/create | Create Match
*CustomMatchesApi* | [**getCustom**](docs/CustomMatchesApi.md#getcustom) | **GET** /v1/matches/custom/{party_id}/match-id | Get Match ID
*CustomMatchesApi* | [**leave**](docs/CustomMatchesApi.md#leave) | **POST** /v1/matches/custom/{lobby_id}/leave | Leave Lobby
*CustomMatchesApi* | [**readyUp**](docs/CustomMatchesApi.md#readyup) | **POST** /v1/matches/custom/{lobby_id}/ready | Ready Up
*CustomMatchesApi* | [**start**](docs/CustomMatchesApi.md#start) | **POST** /v1/matches/custom/{lobby_id}/start | Start Match
*CustomMatchesApi* | [**unready**](docs/CustomMatchesApi.md#unready) | **POST** /v1/matches/custom/{lobby_id}/unready | Unready
*DemoApi* | [**liveQuery**](docs/DemoApi.md#livequery) | **GET** /v1/matches/demo/live/query | Live Demo Query (SSE)
*DemoApi* | [**schema**](docs/DemoApi.md#schema) | **GET** /v1/matches/demo/schema | Demo Schema
*DemoApi* | [**status**](docs/DemoApi.md#status) | **GET** /v1/matches/demo/query/{job_id} | Demo Query Status
*DemoApi* | [**submit**](docs/DemoApi.md#submit) | **POST** /v1/matches/demo/query | Demo Query
*GenericDataApi* | [**getGenericData**](docs/GenericDataApi.md#getgenericdata) | **GET** /v1/assets/generic-data | Get Generic Data
*GraphQLApi* | [**playground**](docs/GraphQLApi.md#playground) | **GET** /v1/graphql | GraphQL Playground
*HeroesApi* | [**getHero**](docs/HeroesApi.md#gethero) | **GET** /v1/assets/heroes/{hero_id} | Get Hero
*HeroesApi* | [**getHeroByName**](docs/HeroesApi.md#getherobyname) | **GET** /v1/assets/heroes/by-name/{name} | Get Hero By Name
*HeroesApi* | [**listHeroes**](docs/HeroesApi.md#listheroes) | **GET** /v1/assets/heroes | List Heroes
*InfoApi* | [**healthCheck**](docs/InfoApi.md#healthcheck) | **GET** /v1/info/health | Health Check
*InfoApi* | [**info**](docs/InfoApi.md#info) | **GET** /v1/info | API Info
*InternalApi* | [**ingestSalts**](docs/InternalApi.md#ingestsalts) | **POST** /v1/matches/salts | Match Salts Ingest
*ItemsApi* | [**getItem**](docs/ItemsApi.md#getitem) | **GET** /v1/assets/items/{id_or_class_name} | Get Item
*ItemsApi* | [**getItemsByHeroId**](docs/ItemsApi.md#getitemsbyheroid) | **GET** /v1/assets/items/by-hero-id/{id} | List Items By Hero
*ItemsApi* | [**getItemsBySlotType**](docs/ItemsApi.md#getitemsbyslottype) | **GET** /v1/assets/items/by-slot-type/{slot_type} | List Items By Slot Type
*ItemsApi* | [**getItemsByType**](docs/ItemsApi.md#getitemsbytype) | **GET** /v1/assets/items/by-type/{type} | List Items By Type
*ItemsApi* | [**listItems**](docs/ItemsApi.md#listitems) | **GET** /v1/assets/items | List Items
*LeaderboardApi* | [**leaderboard**](docs/LeaderboardApi.md#leaderboard) | **GET** /v1/leaderboard/{region} | Leaderboard
*LeaderboardApi* | [**leaderboardHero**](docs/LeaderboardApi.md#leaderboardhero) | **GET** /v1/leaderboard/{region}/{hero_id} | Hero Leaderboard
*LeaderboardApi* | [**leaderboardHeroRaw**](docs/LeaderboardApi.md#leaderboardheroraw) | **GET** /v1/leaderboard/{region}/{hero_id}/raw | Hero Leaderboard as Protobuf
*LeaderboardApi* | [**leaderboardRaw**](docs/LeaderboardApi.md#leaderboardraw) | **GET** /v1/leaderboard/{region}/raw | Leaderboard as Protobuf
*LootTablesApi* | [**listLootTables**](docs/LootTablesApi.md#listloottables) | **GET** /v1/assets/loot-tables | List Loot Tables
*MMRApi* | [**heroMmr**](docs/MMRApi.md#herommr) | **GET** /v1/players/mmr/{hero_id} | Batch Hero MMR
*MMRApi* | [**heroMmrDistribution**](docs/MMRApi.md#herommrdistribution) | **GET** /v1/players/mmr/distribution/{hero_id} | Hero MMR Distribution
*MMRApi* | [**heroMmrHistory**](docs/MMRApi.md#herommrhistory) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History
*MMRApi* | [**mmr**](docs/MMRApi.md#mmr) | **GET** /v1/players/mmr | Batch MMR
*MMRApi* | [**mmrDistribution**](docs/MMRApi.md#mmrdistribution) | **GET** /v1/players/mmr/distribution | MMR Distribution
*MMRApi* | [**mmrHistory**](docs/MMRApi.md#mmrhistory) | **GET** /v1/players/{account_id}/mmr-history | MMR History
*MapApi* | [**getMap**](docs/MapApi.md#getmap) | **GET** /v1/assets/map | Map
*MatchesApi* | [**activeMatches**](docs/MatchesApi.md#activematches) | **GET** /v1/matches/active | Active
*MatchesApi* | [**activeMatchesRaw**](docs/MatchesApi.md#activematchesraw) | **GET** /v1/matches/active/raw | Active as Protobuf
*MatchesApi* | [**bulkMetadata**](docs/MatchesApi.md#bulkmetadata) | **GET** /v1/matches/metadata | Bulk Metadata
*MatchesApi* | [**ingestUrls**](docs/MatchesApi.md#ingesturls) | **POST** /v1/matches/live/urls | Ingest Live Broadcast URLs
*MatchesApi* | [**metadata**](docs/MatchesApi.md#metadata) | **GET** /v1/matches/{match_id}/metadata | Metadata
*MatchesApi* | [**metadataRaw**](docs/MatchesApi.md#metadataraw) | **GET** /v1/matches/{match_id}/metadata/raw | Metadata as Protobuf
*MatchesApi* | [**recentlyFetched**](docs/MatchesApi.md#recentlyfetched) | **GET** /v1/matches/recently-fetched | Recently Fetched
*MatchesApi* | [**salts**](docs/MatchesApi.md#salts) | **GET** /v1/matches/{match_id}/salts | Salts
*MatchesApi* | [**url**](docs/MatchesApi.md#url) | **GET** /v1/matches/{match_id}/live/url | Live Broadcast URL
*MatchesApi* | [**urls**](docs/MatchesApi.md#urls) | **GET** /v1/matches/live/urls | Live Broadcast URLs
*MiscEntitiesApi* | [**getMiscEntity**](docs/MiscEntitiesApi.md#getmiscentity) | **GET** /v1/assets/misc-entities/{id_or_classname} | Get Misc Entity
*MiscEntitiesApi* | [**listMiscEntities**](docs/MiscEntitiesApi.md#listmiscentities) | **GET** /v1/assets/misc-entities | List Misc Entities
*NPCUnitsApi* | [**getNpcUnit**](docs/NPCUnitsApi.md#getnpcunit) | **GET** /v1/assets/npc-units/{id_or_classname} | Get NPC Unit
*NPCUnitsApi* | [**listNpcUnits**](docs/NPCUnitsApi.md#listnpcunits) | **GET** /v1/assets/npc-units | List NPC Units
*PatchesApi* | [**bigPatchDays**](docs/PatchesApi.md#bigpatchdays) | **GET** /v1/patches/big-days | Big Days
*PatchesApi* | [**feed**](docs/PatchesApi.md#feed) | **GET** /v1/patches | Notes
*PatchesApi* | [**feed_0**](docs/PatchesApi.md#feed_0) | **GET** /v2/patches | Notes
*PlayersApi* | [**accountStats**](docs/PlayersApi.md#accountstats) | **GET** /v1/players/{account_id}/account-stats | Account Stats
*PlayersApi* | [**card**](docs/PlayersApi.md#card) | **GET** /v1/players/{account_id}/card | Card
*PlayersApi* | [**enemyStats**](docs/PlayersApi.md#enemystats) | **GET** /v1/players/{account_id}/enemy-stats | Enemy Stats
*PlayersApi* | [**matchHistory**](docs/PlayersApi.md#matchhistory) | **GET** /v1/players/{account_id}/match-history | Match History
*PlayersApi* | [**mateStats**](docs/PlayersApi.md#matestats) | **GET** /v1/players/{account_id}/mate-stats | Mate Stats
*PlayersApi* | [**playerHeroStats**](docs/PlayersApi.md#playerherostats) | **GET** /v1/players/hero-stats | Hero Stats
*PlayersApi* | [**rankPredict**](docs/PlayersApi.md#rankpredict) | **GET** /v1/players/{account_id}/rank-predict | Rank Predict
*PlayersApi* | [**rankPredictAvgImage**](docs/PlayersApi.md#rankpredictavgimage) | **GET** /v1/players/rank-predict/image | Rank Predict Avg Image
*PlayersApi* | [**rankPredictImage**](docs/PlayersApi.md#rankpredictimage) | **GET** /v1/players/{account_id}/rank-predict/image | Rank Predict Image
*RanksApi* | [**getRank**](docs/RanksApi.md#getrank) | **GET** /v1/assets/ranks/{tier} | Get Rank
*RanksApi* | [**listRanks**](docs/RanksApi.md#listranks) | **GET** /v1/assets/ranks | List Ranks
*SQLApi* | [**listTables**](docs/SQLApi.md#listtables) | **GET** /v1/sql/tables | List Tables
*SQLApi* | [**sql**](docs/SQLApi.md#sql) | **GET** /v1/sql | Query
*SQLApi* | [**tableSchema**](docs/SQLApi.md#tableschema) | **GET** /v1/sql/tables/{table}/schema | Table Schema
*ServersApi* | [**ingest**](docs/ServersApi.md#ingest) | **POST** /v1/servers/metrics | Game Server Metric Ingest
*ServersApi* | [**list**](docs/ServersApi.md#list) | **GET** /v1/servers | List Game Servers
*ServersApi* | [**status**](docs/ServersApi.md#status) | **POST** /v1/servers/status | Game Server Status
*ServersApi* | [**steamList**](docs/ServersApi.md#steamlist) | **GET** /v1/servers/steam | List Steam Game Servers
*SteamApi* | [**steam**](docs/SteamApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile
*SteamApi* | [**steamSearch**](docs/SteamApi.md#steamsearch) | **GET** /v1/players/steam-search | Steam Profile Search
*SteamInfoApi* | [**getAllSteamInfo**](docs/SteamInfoApi.md#getallsteaminfo) | **GET** /v1/assets/steam-info/all | Get All Steam Infos
*SteamInfoApi* | [**getSteamInfo**](docs/SteamInfoApi.md#getsteaminfo) | **GET** /v1/assets/steam-info | Get Steam Info


### Documentation For Models

 - [APIInfo](docs/APIInfo.md)
 - [Ability](docs/Ability.md)
 - [AbilityActivation](docs/AbilityActivation.md)
 - [AbilityDescription](docs/AbilityDescription.md)
 - [AbilityImbue](docs/AbilityImbue.md)
 - [AbilitySectionType](docs/AbilitySectionType.md)
 - [AbilityTooltipDetails](docs/AbilityTooltipDetails.md)
 - [AbilityType](docs/AbilityType.md)
 - [AbilityVideos](docs/AbilityVideos.md)
 - [Accolade](docs/Accolade.md)
 - [ActiveMatch](docs/ActiveMatch.md)
 - [ActiveMatchGameMode](docs/ActiveMatchGameMode.md)
 - [ActiveMatchMode](docs/ActiveMatchMode.md)
 - [ActiveMatchPlayer](docs/ActiveMatchPlayer.md)
 - [ActiveMatchTeam](docs/ActiveMatchTeam.md)
 - [AnalyticsAbilityOrderStats](docs/AnalyticsAbilityOrderStats.md)
 - [AnalyticsGameStats](docs/AnalyticsGameStats.md)
 - [AnalyticsHeroStats](docs/AnalyticsHeroStats.md)
 - [BadgeDistribution](docs/BadgeDistribution.md)
 - [Build](docs/Build.md)
 - [BuildHero](docs/BuildHero.md)
 - [BuildHeroDetails](docs/BuildHeroDetails.md)
 - [BuildHeroDetailsAbilityOrder](docs/BuildHeroDetailsAbilityOrder.md)
 - [BuildHeroDetailsAbilityOrderCurrencyChange](docs/BuildHeroDetailsAbilityOrderCurrencyChange.md)
 - [BuildHeroDetailsCategory](docs/BuildHeroDetailsCategory.md)
 - [BuildHeroDetailsCategoryAbility](docs/BuildHeroDetailsCategoryAbility.md)
 - [BuildItemStats](docs/BuildItemStats.md)
 - [BuildTag](docs/BuildTag.md)
 - [ClickhouseMatchInfo](docs/ClickhouseMatchInfo.md)
 - [ClickhouseSalts](docs/ClickhouseSalts.md)
 - [Color](docs/Color.md)
 - [ColumnSchema](docs/ColumnSchema.md)
 - [CreateCustomRequest](docs/CreateCustomRequest.md)
 - [CreateCustomResponse](docs/CreateCustomResponse.md)
 - [Curve](docs/Curve.md)
 - [CurveOrFloat](docs/CurveOrFloat.md)
 - [DamageFlash](docs/DamageFlash.md)
 - [DemoQueryJobResponse](docs/DemoQueryJobResponse.md)
 - [DemoQueryRequest](docs/DemoQueryRequest.md)
 - [DemoQueryStatusResponse](docs/DemoQueryStatusResponse.md)
 - [DemoSchemaResponse](docs/DemoSchemaResponse.md)
 - [DependantAbilities](docs/DependantAbilities.md)
 - [DistributionEntry](docs/DistributionEntry.md)
 - [DraftBucket](docs/DraftBucket.md)
 - [DraftBuckets](docs/DraftBuckets.md)
 - [EnemyStats](docs/EnemyStats.md)
 - [FeedItem](docs/FeedItem.md)
 - [FeedItemOneOf](docs/FeedItemOneOf.md)
 - [FeedItemOneOf1](docs/FeedItemOneOf1.md)
 - [FlashData](docs/FlashData.md)
 - [ForumPatch](docs/ForumPatch.md)
 - [GameMode](docs/GameMode.md)
 - [GameServerInfo](docs/GameServerInfo.md)
 - [GenericData](docs/GenericData.md)
 - [GetCustomMatchIdResponse](docs/GetCustomMatchIdResponse.md)
 - [GlitchSettings](docs/GlitchSettings.md)
 - [HashMapItemSlotTypeItemSlotInfoValue](docs/HashMapItemSlotTypeItemSlotInfoValue.md)
 - [HashMapItemSlotTypeVecMapModCostBonusValueInner](docs/HashMapItemSlotTypeVecMapModCostBonusValueInner.md)
 - [HashMapItemSlotTypeVecPurchaseBonusValueInner](docs/HashMapItemSlotTypeVecPurchaseBonusValueInner.md)
 - [HashMapStringLevelInfoValue](docs/HashMapStringLevelInfoValue.md)
 - [HashMapStringOptionDraftBucketingValue](docs/HashMapStringOptionDraftBucketingValue.md)
 - [HashMapStringOptionDraftBucketingValueOneOf](docs/HashMapStringOptionDraftBucketingValueOneOf.md)
 - [HashMapStringScalingStatValue](docs/HashMapStringScalingStatValue.md)
 - [HashMapValue](docs/HashMapValue.md)
 - [Hero](docs/Hero.md)
 - [HeroBanStats](docs/HeroBanStats.md)
 - [HeroBuildStats](docs/HeroBuildStats.md)
 - [HeroColors](docs/HeroColors.md)
 - [HeroCombStats](docs/HeroCombStats.md)
 - [HeroCounterStats](docs/HeroCounterStats.md)
 - [HeroDescription](docs/HeroDescription.md)
 - [HeroEntry](docs/HeroEntry.md)
 - [HeroImages](docs/HeroImages.md)
 - [HeroPhysics](docs/HeroPhysics.md)
 - [HeroStats](docs/HeroStats.md)
 - [HeroStatsUI](docs/HeroStatsUI.md)
 - [HeroStatsUIDisplay](docs/HeroStatsUIDisplay.md)
 - [HeroSynergyStats](docs/HeroSynergyStats.md)
 - [HeroType](docs/HeroType.md)
 - [HorizontalRecoil](docs/HorizontalRecoil.md)
 - [IngestLiveUrl](docs/IngestLiveUrl.md)
 - [Item](docs/Item.md)
 - [ItemDraftRound](docs/ItemDraftRound.md)
 - [ItemDraftRoundPerGameRound](docs/ItemDraftRoundPerGameRound.md)
 - [ItemFlowEdge](docs/ItemFlowEdge.md)
 - [ItemFlowNode](docs/ItemFlowNode.md)
 - [ItemFlowStats](docs/ItemFlowStats.md)
 - [ItemFlowSummary](docs/ItemFlowSummary.md)
 - [ItemGroup](docs/ItemGroup.md)
 - [ItemPermutationStats](docs/ItemPermutationStats.md)
 - [ItemProperty](docs/ItemProperty.md)
 - [ItemSlotType](docs/ItemSlotType.md)
 - [ItemStats](docs/ItemStats.md)
 - [ItemType](docs/ItemType.md)
 - [JobStatus](docs/JobStatus.md)
 - [KillDeathStats](docs/KillDeathStats.md)
 - [LaneInfo](docs/LaneInfo.md)
 - [Leaderboard](docs/Leaderboard.md)
 - [LeaderboardEntry](docs/LeaderboardEntry.md)
 - [ListServersResponse](docs/ListServersResponse.md)
 - [LiveUrl](docs/LiveUrl.md)
 - [LootEntry](docs/LootEntry.md)
 - [LootTable](docs/LootTable.md)
 - [MMRHistory](docs/MMRHistory.md)
 - [MapData](docs/MapData.md)
 - [MapImages](docs/MapImages.md)
 - [MatchPlayer](docs/MatchPlayer.md)
 - [MatchSaltsResponse](docs/MatchSaltsResponse.md)
 - [MatchSpectateResponse](docs/MatchSpectateResponse.md)
 - [MateStats](docs/MateStats.md)
 - [MetricIngestRequest](docs/MetricIngestRequest.md)
 - [MiniMapOffsets](docs/MiniMapOffsets.md)
 - [MiscEntity](docs/MiscEntity.md)
 - [ModifierValue](docs/ModifierValue.md)
 - [NewPlayerMetrics](docs/NewPlayerMetrics.md)
 - [NpcUnit](docs/NpcUnit.md)
 - [ObjectiveParams](docs/ObjectiveParams.md)
 - [ObjectivePosition](docs/ObjectivePosition.md)
 - [OutcomeToWeights](docs/OutcomeToWeights.md)
 - [OutputFormat](docs/OutputFormat.md)
 - [Patch](docs/Patch.md)
 - [PatchCategory](docs/PatchCategory.md)
 - [PatchGuid](docs/PatchGuid.md)
 - [Pickup](docs/Pickup.md)
 - [PlayerAccountHeroStats](docs/PlayerAccountHeroStats.md)
 - [PlayerAccountStats](docs/PlayerAccountStats.md)
 - [PlayerCard](docs/PlayerCard.md)
 - [PlayerCardSlot](docs/PlayerCardSlot.md)
 - [PlayerCardSlotHero](docs/PlayerCardSlotHero.md)
 - [PlayerCardSlotStat](docs/PlayerCardSlotStat.md)
 - [PlayerEntry](docs/PlayerEntry.md)
 - [PlayerMatchHistoryEntry](docs/PlayerMatchHistoryEntry.md)
 - [PlayerPerformanceCurvePoint](docs/PlayerPerformanceCurvePoint.md)
 - [Rank](docs/Rank.md)
 - [RankImages](docs/RankImages.md)
 - [RankPredictResponse](docs/RankPredictResponse.md)
 - [RankPrediction](docs/RankPrediction.md)
 - [RawAbilityUpgrade](docs/RawAbilityUpgrade.md)
 - [RawAbilityUpgradePropertyUpgrade](docs/RawAbilityUpgradePropertyUpgrade.md)
 - [RawCustomCrosshairSettings](docs/RawCustomCrosshairSettings.md)
 - [RawItemPropertyScaleFunctionSubclass](docs/RawItemPropertyScaleFunctionSubclass.md)
 - [RawItemWeaponInfoBulletSpeedCurve](docs/RawItemWeaponInfoBulletSpeedCurve.md)
 - [RawItemWeaponInfoBulletSpeedCurveSpline](docs/RawItemWeaponInfoBulletSpeedCurveSpline.md)
 - [RawItemWeaponInfoInner](docs/RawItemWeaponInfoInner.md)
 - [RawWeaponInfoHorizontalRecoil](docs/RawWeaponInfoHorizontalRecoil.md)
 - [RawWeaponInfoVerticalRecoil](docs/RawWeaponInfoVerticalRecoil.md)
 - [RecoilRange](docs/RecoilRange.md)
 - [RegionMode](docs/RegionMode.md)
 - [RejuvParams](docs/RejuvParams.md)
 - [RollType](docs/RollType.md)
 - [RollTypeOneOf](docs/RollTypeOneOf.md)
 - [ScriptValues](docs/ScriptValues.md)
 - [ServerRegion](docs/ServerRegion.md)
 - [ServerStatusRequest](docs/ServerStatusRequest.md)
 - [ServerStatusResponse](docs/ServerStatusResponse.md)
 - [ShopSpiritStatsDisplay](docs/ShopSpiritStatsDisplay.md)
 - [ShopStatDisplay](docs/ShopStatDisplay.md)
 - [ShopVitalityStatsDisplay](docs/ShopVitalityStatsDisplay.md)
 - [ShopWeaponStatsDisplay](docs/ShopWeaponStatsDisplay.md)
 - [SpreadPenalty](docs/SpreadPenalty.md)
 - [StartingStat](docs/StartingStat.md)
 - [StartingStats](docs/StartingStats.md)
 - [StatsDisplay](docs/StatsDisplay.md)
 - [StatsUsageFlag](docs/StatsUsageFlag.md)
 - [Status](docs/Status.md)
 - [StatusServices](docs/StatusServices.md)
 - [SteamFriend](docs/SteamFriend.md)
 - [SteamInfo](docs/SteamInfo.md)
 - [SteamNews](docs/SteamNews.md)
 - [SteamProfile](docs/SteamProfile.md)
 - [SteamServer](docs/SteamServer.md)
 - [StreetBrawl](docs/StreetBrawl.md)
 - [SubclassBulletResistModifier](docs/SubclassBulletResistModifier.md)
 - [SubclassBulletResistModifierSubclass](docs/SubclassBulletResistModifierSubclass.md)
 - [SubclassEmpoweredModifierLevel](docs/SubclassEmpoweredModifierLevel.md)
 - [SubclassEmpoweredModifierLevelSubclass](docs/SubclassEmpoweredModifierLevelSubclass.md)
 - [SubclassIntrinsicModifiers](docs/SubclassIntrinsicModifiers.md)
 - [SubclassIntrinsicModifiersSubclass](docs/SubclassIntrinsicModifiersSubclass.md)
 - [SubclassModifierDefinition](docs/SubclassModifierDefinition.md)
 - [SubclassModifierDefinitionSubclass](docs/SubclassModifierDefinitionSubclass.md)
 - [SubclassObjectiveHealthGrowthPhase](docs/SubclassObjectiveHealthGrowthPhase.md)
 - [SubclassObjectiveHealthGrowthPhaseSubclass](docs/SubclassObjectiveHealthGrowthPhaseSubclass.md)
 - [SubclassObjectiveRegen](docs/SubclassObjectiveRegen.md)
 - [SubclassObjectiveRegenSubclass](docs/SubclassObjectiveRegenSubclass.md)
 - [SubclassRangedArmorModifier](docs/SubclassRangedArmorModifier.md)
 - [SubclassRangedArmorModifierSubclass](docs/SubclassRangedArmorModifierSubclass.md)
 - [SubclassTrooperDamageReduction](docs/SubclassTrooperDamageReduction.md)
 - [SubclassTrooperDamageReductionSubclass](docs/SubclassTrooperDamageReductionSubclass.md)
 - [TableSchemaResponse](docs/TableSchemaResponse.md)
 - [TableSize](docs/TableSize.md)
 - [TooltipDetailsBlock](docs/TooltipDetailsBlock.md)
 - [TooltipDetailsBlockProperty](docs/TooltipDetailsBlockProperty.md)
 - [TooltipDetailsInfoSection](docs/TooltipDetailsInfoSection.md)
 - [Upgrade](docs/Upgrade.md)
 - [UpgradeDescription](docs/UpgradeDescription.md)
 - [UpgradeProperty](docs/UpgradeProperty.md)
 - [UpgradeTooltipImportantPropertyWithIcon](docs/UpgradeTooltipImportantPropertyWithIcon.md)
 - [UpgradeTooltipSection](docs/UpgradeTooltipSection.md)
 - [UpgradeTooltipSectionAttribute](docs/UpgradeTooltipSectionAttribute.md)
 - [VariableCategory](docs/VariableCategory.md)
 - [VariableDescription](docs/VariableDescription.md)
 - [VerticalRecoil](docs/VerticalRecoil.md)
 - [Weapon](docs/Weapon.md)
 - [WeaponInfo](docs/WeaponInfo.md)
 - [ZiplanePath](docs/ZiplanePath.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="api_key_header"></a>
### api_key_header

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header

<a id="api_key_query"></a>
### api_key_query

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: URL query string

