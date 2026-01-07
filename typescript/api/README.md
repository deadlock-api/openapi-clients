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
*AnalyticsApi* | [**abilityOrderStats**](docs/AnalyticsApi.md#abilityorderstats) | **GET** /v1/analytics/ability-order-stats | Ability Order Stats
*AnalyticsApi* | [**badgeDistribution**](docs/AnalyticsApi.md#badgedistribution) | **GET** /v1/analytics/badge-distribution | Badge Distribution
*AnalyticsApi* | [**buildItemStats**](docs/AnalyticsApi.md#builditemstats) | **GET** /v1/analytics/build-item-stats | Build Item Stats
*AnalyticsApi* | [**heroCombStats**](docs/AnalyticsApi.md#herocombstats) | **GET** /v1/analytics/hero-comb-stats | Hero Comb Stats
*AnalyticsApi* | [**heroCountersStats**](docs/AnalyticsApi.md#herocountersstats) | **GET** /v1/analytics/hero-counter-stats | Hero Counter Stats
*AnalyticsApi* | [**heroScoreboard**](docs/AnalyticsApi.md#heroscoreboard) | **GET** /v1/analytics/scoreboards/heroes | Hero Scoreboard
*AnalyticsApi* | [**heroStats**](docs/AnalyticsApi.md#herostats) | **GET** /v1/analytics/hero-stats | Hero Stats
*AnalyticsApi* | [**heroSynergiesStats**](docs/AnalyticsApi.md#herosynergiesstats) | **GET** /v1/analytics/hero-synergy-stats | Hero Synergy Stats
*AnalyticsApi* | [**itemPermutationStats**](docs/AnalyticsApi.md#itempermutationstats) | **GET** /v1/analytics/item-permutation-stats | Item Permutation Stats
*AnalyticsApi* | [**itemStats**](docs/AnalyticsApi.md#itemstats) | **GET** /v1/analytics/item-stats | Item Stats
*AnalyticsApi* | [**killDeathStats**](docs/AnalyticsApi.md#killdeathstats) | **GET** /v1/analytics/kill-death-stats | Kill Death Stats
*AnalyticsApi* | [**playerPerformanceCurve**](docs/AnalyticsApi.md#playerperformancecurve) | **GET** /v1/analytics/player-performance-curve | Player Performance Curve
*AnalyticsApi* | [**playerScoreboard**](docs/AnalyticsApi.md#playerscoreboard) | **GET** /v1/analytics/scoreboards/players | Player Scoreboard
*AnalyticsApi* | [**playerStatsMetrics**](docs/AnalyticsApi.md#playerstatsmetrics) | **GET** /v1/analytics/player-stats/metrics | Player Stats Metrics
*BuildsApi* | [**searchBuilds**](docs/BuildsApi.md#searchbuilds) | **GET** /v1/builds | Search
*CommandsApi* | [**availableVariables**](docs/CommandsApi.md#availablevariables) | **GET** /v1/commands/variables/available | Available Variables
*CommandsApi* | [**commandResolve**](docs/CommandsApi.md#commandresolve) | **GET** /v1/commands/resolve | Resolve Command
*CommandsApi* | [**variablesResolve**](docs/CommandsApi.md#variablesresolve) | **GET** /v1/commands/variables/resolve | Resolve Variables
*CommandsApi* | [**widgetVersions**](docs/CommandsApi.md#widgetversions) | **GET** /v1/commands/widgets/versions | Widget Versions
*CustomMatchesApi* | [**createCustom**](docs/CustomMatchesApi.md#createcustom) | **POST** /v1/matches/custom/create | Create Match
*CustomMatchesApi* | [**getCustom**](docs/CustomMatchesApi.md#getcustom) | **GET** /v1/matches/custom/{party_id}/match-id | Get Match ID
*CustomMatchesApi* | [**readyUp**](docs/CustomMatchesApi.md#readyup) | **POST** /v1/matches/custom/{lobby_id}/ready | Ready Up
*CustomMatchesApi* | [**unready**](docs/CustomMatchesApi.md#unready) | **POST** /v1/matches/custom/{lobby_id}/unready | Unready
*ESportsApi* | [**ingestMatch**](docs/ESportsApi.md#ingestmatch) | **POST** /v1/esports/ingest/match | Ingest
*ESportsApi* | [**matches**](docs/ESportsApi.md#matches) | **GET** /v1/esports/matches | List Matches
*InfoApi* | [**healthCheck**](docs/InfoApi.md#healthcheck) | **GET** /v1/info/health | Health Check
*InfoApi* | [**info**](docs/InfoApi.md#info) | **GET** /v1/info | API Info
*InternalApi* | [**ingestSalts**](docs/InternalApi.md#ingestsalts) | **POST** /v1/matches/salts | Match Salts Ingest
*LeaderboardApi* | [**leaderboard**](docs/LeaderboardApi.md#leaderboard) | **GET** /v1/leaderboard/{region} | Leaderboard
*LeaderboardApi* | [**leaderboardHero**](docs/LeaderboardApi.md#leaderboardhero) | **GET** /v1/leaderboard/{region}/{hero_id} | Hero Leaderboard
*LeaderboardApi* | [**leaderboardHeroRaw**](docs/LeaderboardApi.md#leaderboardheroraw) | **GET** /v1/leaderboard/{region}/{hero_id}/raw | Hero Leaderboard as Protobuf
*LeaderboardApi* | [**leaderboardRaw**](docs/LeaderboardApi.md#leaderboardraw) | **GET** /v1/leaderboard/{region}/raw | Leaderboard as Protobuf
*MMRApi* | [**heroMmr**](docs/MMRApi.md#herommr) | **GET** /v1/players/mmr/{hero_id} | Batch Hero MMR
*MMRApi* | [**heroMmrDistribution**](docs/MMRApi.md#herommrdistribution) | **GET** /v1/players/mmr/distribution/{hero_id} | Hero MMR Distribution
*MMRApi* | [**heroMmrHistory**](docs/MMRApi.md#herommrhistory) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History
*MMRApi* | [**mmr**](docs/MMRApi.md#mmr) | **GET** /v1/players/mmr | Batch MMR
*MMRApi* | [**mmrDistribution**](docs/MMRApi.md#mmrdistribution) | **GET** /v1/players/mmr/distribution | MMR Distribution
*MMRApi* | [**mmrHistory**](docs/MMRApi.md#mmrhistory) | **GET** /v1/players/{account_id}/mmr-history | MMR History
*MatchesApi* | [**activeMatches**](docs/MatchesApi.md#activematches) | **GET** /v1/matches/active | Active
*MatchesApi* | [**activeMatchesRaw**](docs/MatchesApi.md#activematchesraw) | **GET** /v1/matches/active/raw | Active as Protobuf
*MatchesApi* | [**bulkMetadata**](docs/MatchesApi.md#bulkmetadata) | **GET** /v1/matches/metadata | Bulk Metadata
*MatchesApi* | [**metadata**](docs/MatchesApi.md#metadata) | **GET** /v1/matches/{match_id}/metadata | Metadata
*MatchesApi* | [**metadataRaw**](docs/MatchesApi.md#metadataraw) | **GET** /v1/matches/{match_id}/metadata/raw | Metadata as Protobuf
*MatchesApi* | [**recentlyFetched**](docs/MatchesApi.md#recentlyfetched) | **GET** /v1/matches/recently-fetched | Recently Fetched
*MatchesApi* | [**salts**](docs/MatchesApi.md#salts) | **GET** /v1/matches/{match_id}/salts | Salts
*MatchesApi* | [**url**](docs/MatchesApi.md#url) | **GET** /v1/matches/{match_id}/live/url | Live Broadcast URL
*PatchesApi* | [**bigPatchDays**](docs/PatchesApi.md#bigpatchdays) | **GET** /v1/patches/big-days | Big Days
*PatchesApi* | [**feed**](docs/PatchesApi.md#feed) | **GET** /v1/patches | Notes
*PlayersApi* | [**enemyStats**](docs/PlayersApi.md#enemystats) | **GET** /v1/players/{account_id}/enemy-stats | Enemy Stats
*PlayersApi* | [**matchHistory**](docs/PlayersApi.md#matchhistory) | **GET** /v1/players/{account_id}/match-history | Match History
*PlayersApi* | [**mateStats**](docs/PlayersApi.md#matestats) | **GET** /v1/players/{account_id}/mate-stats | Mate Stats
*PlayersApi* | [**partyStats**](docs/PlayersApi.md#partystats) | **GET** /v1/players/{account_id}/party-stats | Party Stats
*PlayersApi* | [**playerHeroStats**](docs/PlayersApi.md#playerherostats) | **GET** /v1/players/hero-stats | Hero Stats
*PlayersApi* | [**steam**](docs/PlayersApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile
*PlayersApi* | [**steamSearch**](docs/PlayersApi.md#steamsearch) | **GET** /v1/players/steam-search | Steam Profile Search
*SQLApi* | [**listTables**](docs/SQLApi.md#listtables) | **GET** /v1/sql/tables | List Tables
*SQLApi* | [**sql**](docs/SQLApi.md#sql) | **GET** /v1/sql | Query
*SQLApi* | [**tableSchema**](docs/SQLApi.md#tableschema) | **GET** /v1/sql/tables/{table}/schema | Table Schema


### Documentation For Models

 - [APIInfo](docs/APIInfo.md)
 - [ActiveMatch](docs/ActiveMatch.md)
 - [ActiveMatchGameMode](docs/ActiveMatchGameMode.md)
 - [ActiveMatchMode](docs/ActiveMatchMode.md)
 - [ActiveMatchPlayer](docs/ActiveMatchPlayer.md)
 - [ActiveMatchTeam](docs/ActiveMatchTeam.md)
 - [AnalyticsAbilityOrderStats](docs/AnalyticsAbilityOrderStats.md)
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
 - [ClickhouseMatchInfo](docs/ClickhouseMatchInfo.md)
 - [ClickhouseSalts](docs/ClickhouseSalts.md)
 - [CreateCustomRequest](docs/CreateCustomRequest.md)
 - [CreateCustomResponse](docs/CreateCustomResponse.md)
 - [DistributionEntry](docs/DistributionEntry.md)
 - [ESportsMatch](docs/ESportsMatch.md)
 - [ESportsMatchStatus](docs/ESportsMatchStatus.md)
 - [EnemyStats](docs/EnemyStats.md)
 - [Entry](docs/Entry.md)
 - [GetCustomMatchIdResponse](docs/GetCustomMatchIdResponse.md)
 - [HashMapValue](docs/HashMapValue.md)
 - [HeroCombStats](docs/HeroCombStats.md)
 - [HeroCounterStats](docs/HeroCounterStats.md)
 - [HeroStats](docs/HeroStats.md)
 - [HeroSynergyStats](docs/HeroSynergyStats.md)
 - [ItemPermutationStats](docs/ItemPermutationStats.md)
 - [ItemStats](docs/ItemStats.md)
 - [KillDeathStats](docs/KillDeathStats.md)
 - [Leaderboard](docs/Leaderboard.md)
 - [LeaderboardEntry](docs/LeaderboardEntry.md)
 - [MMRHistory](docs/MMRHistory.md)
 - [MatchSaltsResponse](docs/MatchSaltsResponse.md)
 - [MatchSpectateResponse](docs/MatchSpectateResponse.md)
 - [MateStats](docs/MateStats.md)
 - [PartyStats](docs/PartyStats.md)
 - [Patch](docs/Patch.md)
 - [PatchCategory](docs/PatchCategory.md)
 - [PatchGuid](docs/PatchGuid.md)
 - [PlayerMatchHistoryEntry](docs/PlayerMatchHistoryEntry.md)
 - [PlayerPerformanceCurvePoint](docs/PlayerPerformanceCurvePoint.md)
 - [RegionMode](docs/RegionMode.md)
 - [Status](docs/Status.md)
 - [StatusServices](docs/StatusServices.md)
 - [SteamProfile](docs/SteamProfile.md)
 - [TableSize](docs/TableSize.md)
 - [VariableCategory](docs/VariableCategory.md)
 - [VariableDescription](docs/VariableDescription.md)


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

