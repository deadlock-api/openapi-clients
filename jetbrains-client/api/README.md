# Deadlock API - Jetbrains API Client

## General API description

 ## API Clients  We have auto generated and updated clients for many languages. You can find them here: [https://github.com/deadlock-api/openapi-clients](https://github.com/deadlock-api/openapi-clients)  ## Support the Deadlock API  Whether you&#39;re building your own database, developing data science projects, or enhancing your website with game and player analytics, the Deadlock API has the data you need.  Your sponsorship helps keep this resource open, free and future-proof for everyone. By supporting the Deadlock API, you will enable continued development, new features and reliable access for developers, analysts and streamers worldwide.  Help us continue to provide the data you need - sponsor the Deadlock API today!  **-&gt; You can Sponsor the Deadlock API on [Patreon](https://www.patreon.com/c/user?u&#x3D;68961896) or [GitHub](https://github.com/sponsors/raimannma)**  ## Disclaimer _deadlock-api.com is not endorsed by Valve and does not reflect the views or opinions of Valve or anyone officially involved in producing or managing Valve properties. Valve and all associated properties are trademarks or registered trademarks of Valve Corporation_         

* API basepath : [https://api.deadlock-api.com](https://api.deadlock-api.com)
* Version : 0.1.0

## Documentation for API Endpoints

All URIs are relative to *https://api.deadlock-api.com*, but will link to the `.http` file that contains the endpoint definition.
There may be multiple requests for a single endpoint, one for each example described in the OpenAPI specification.

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnalyticsApi* | [**abilityOrderStats**](Apis/AnalyticsApi.http#abilityorderstats) | **GET** /v1/analytics/ability-order-stats | Ability Order Stats
*AnalyticsApi* | [**badgeDistribution**](Apis/AnalyticsApi.http#badgedistribution) | **GET** /v1/analytics/badge-distribution | Badge Distribution
*AnalyticsApi* | [**buildItemStats**](Apis/AnalyticsApi.http#builditemstats) | **GET** /v1/analytics/build-item-stats | Build Item Stats
*AnalyticsApi* | [**heroCombStats**](Apis/AnalyticsApi.http#herocombstats) | **GET** /v1/analytics/hero-comb-stats | Hero Comb Stats
*AnalyticsApi* | [**heroCountersStats**](Apis/AnalyticsApi.http#herocountersstats) | **GET** /v1/analytics/hero-counter-stats | Hero Counter Stats
*AnalyticsApi* | [**heroScoreboard**](Apis/AnalyticsApi.http#heroscoreboard) | **GET** /v1/analytics/scoreboards/heroes | Hero Scoreboard
*AnalyticsApi* | [**heroStats**](Apis/AnalyticsApi.http#herostats) | **GET** /v1/analytics/hero-stats | Hero Stats
*AnalyticsApi* | [**heroSynergiesStats**](Apis/AnalyticsApi.http#herosynergiesstats) | **GET** /v1/analytics/hero-synergy-stats | Hero Synergy Stats
*AnalyticsApi* | [**itemPermutationStats**](Apis/AnalyticsApi.http#itempermutationstats) | **GET** /v1/analytics/item-permutation-stats | Item Permutation Stats
*AnalyticsApi* | [**itemStats**](Apis/AnalyticsApi.http#itemstats) | **GET** /v1/analytics/item-stats | Item Stats
*AnalyticsApi* | [**killDeathStats**](Apis/AnalyticsApi.http#killdeathstats) | **GET** /v1/analytics/kill-death-stats | Kill Death Stats
*AnalyticsApi* | [**playerPerformanceCurve**](Apis/AnalyticsApi.http#playerperformancecurve) | **GET** /v1/analytics/player-performance-curve | Player Performance Curve
*AnalyticsApi* | [**playerScoreboard**](Apis/AnalyticsApi.http#playerscoreboard) | **GET** /v1/analytics/scoreboards/players | Player Scoreboard
*AnalyticsApi* | [**playerStatsMetrics**](Apis/AnalyticsApi.http#playerstatsmetrics) | **GET** /v1/analytics/player-stats/metrics | Player Stats Metrics
*BuildsApi* | [**searchBuilds**](Apis/BuildsApi.http#searchbuilds) | **GET** /v1/builds | Search
*CommandsApi* | [**availableVariables**](Apis/CommandsApi.http#availablevariables) | **GET** /v1/commands/variables/available | Available Variables
*CommandsApi* | [**commandResolve**](Apis/CommandsApi.http#commandresolve) | **GET** /v1/commands/resolve | Resolve Command
*CommandsApi* | [**variablesResolve**](Apis/CommandsApi.http#variablesresolve) | **GET** /v1/commands/variables/resolve | Resolve Variables
*CommandsApi* | [**widgetVersions**](Apis/CommandsApi.http#widgetversions) | **GET** /v1/commands/widgets/versions | Widget Versions
*CustomMatchesApi* | [**createCustom**](Apis/CustomMatchesApi.http#createcustom) | **POST** /v1/matches/custom/create | Create Match
*CustomMatchesApi* | [**getCustom**](Apis/CustomMatchesApi.http#getcustom) | **GET** /v1/matches/custom/{party_id}/match-id | Get Match ID
*CustomMatchesApi* | [**leave**](Apis/CustomMatchesApi.http#leave) | **POST** /v1/matches/custom/{lobby_id}/leave | Leave Lobby
*CustomMatchesApi* | [**readyUp**](Apis/CustomMatchesApi.http#readyup) | **POST** /v1/matches/custom/{lobby_id}/ready | Ready Up
*CustomMatchesApi* | [**unready**](Apis/CustomMatchesApi.http#unready) | **POST** /v1/matches/custom/{lobby_id}/unready | Unready
*ESportsApi* | [**ingestMatch**](Apis/ESportsApi.http#ingestmatch) | **POST** /v1/esports/ingest/match | Ingest
*ESportsApi* | [**matches**](Apis/ESportsApi.http#matches) | **GET** /v1/esports/matches | List Matches
*InfoApi* | [**healthCheck**](Apis/InfoApi.http#healthcheck) | **GET** /v1/info/health | Health Check
*InfoApi* | [**info**](Apis/InfoApi.http#info) | **GET** /v1/info | API Info
*InternalApi* | [**ingestSalts**](Apis/InternalApi.http#ingestsalts) | **POST** /v1/matches/salts | Match Salts Ingest
*LeaderboardApi* | [**leaderboard**](Apis/LeaderboardApi.http#leaderboard) | **GET** /v1/leaderboard/{region} | Leaderboard
*LeaderboardApi* | [**leaderboardHero**](Apis/LeaderboardApi.http#leaderboardhero) | **GET** /v1/leaderboard/{region}/{hero_id} | Hero Leaderboard
*LeaderboardApi* | [**leaderboardHeroRaw**](Apis/LeaderboardApi.http#leaderboardheroraw) | **GET** /v1/leaderboard/{region}/{hero_id}/raw | Hero Leaderboard as Protobuf
*LeaderboardApi* | [**leaderboardRaw**](Apis/LeaderboardApi.http#leaderboardraw) | **GET** /v1/leaderboard/{region}/raw | Leaderboard as Protobuf
*MMRApi* | [**heroMmr**](Apis/MMRApi.http#herommr) | **GET** /v1/players/mmr/{hero_id} | Batch Hero MMR
*MMRApi* | [**heroMmrDistribution**](Apis/MMRApi.http#herommrdistribution) | **GET** /v1/players/mmr/distribution/{hero_id} | Hero MMR Distribution
*MMRApi* | [**heroMmrHistory**](Apis/MMRApi.http#herommrhistory) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History
*MMRApi* | [**mmr**](Apis/MMRApi.http#mmr) | **GET** /v1/players/mmr | Batch MMR
*MMRApi* | [**mmrDistribution**](Apis/MMRApi.http#mmrdistribution) | **GET** /v1/players/mmr/distribution | MMR Distribution
*MMRApi* | [**mmrHistory**](Apis/MMRApi.http#mmrhistory) | **GET** /v1/players/{account_id}/mmr-history | MMR History
*MatchesApi* | [**activeMatches**](Apis/MatchesApi.http#activematches) | **GET** /v1/matches/active | Active
*MatchesApi* | [**activeMatchesRaw**](Apis/MatchesApi.http#activematchesraw) | **GET** /v1/matches/active/raw | Active as Protobuf
*MatchesApi* | [**bulkMetadata**](Apis/MatchesApi.http#bulkmetadata) | **GET** /v1/matches/metadata | Bulk Metadata
*MatchesApi* | [**metadata**](Apis/MatchesApi.http#metadata) | **GET** /v1/matches/{match_id}/metadata | Metadata
*MatchesApi* | [**metadataRaw**](Apis/MatchesApi.http#metadataraw) | **GET** /v1/matches/{match_id}/metadata/raw | Metadata as Protobuf
*MatchesApi* | [**recentlyFetched**](Apis/MatchesApi.http#recentlyfetched) | **GET** /v1/matches/recently-fetched | Recently Fetched
*MatchesApi* | [**salts**](Apis/MatchesApi.http#salts) | **GET** /v1/matches/{match_id}/salts | Salts
*MatchesApi* | [**url**](Apis/MatchesApi.http#url) | **GET** /v1/matches/{match_id}/live/url | Live Broadcast URL
*PatchesApi* | [**bigPatchDays**](Apis/PatchesApi.http#bigpatchdays) | **GET** /v1/patches/big-days | Big Days
*PatchesApi* | [**feed**](Apis/PatchesApi.http#feed) | **GET** /v1/patches | Notes
*PlayersApi* | [**enemyStats**](Apis/PlayersApi.http#enemystats) | **GET** /v1/players/{account_id}/enemy-stats | Enemy Stats
*PlayersApi* | [**matchHistory**](Apis/PlayersApi.http#matchhistory) | **GET** /v1/players/{account_id}/match-history | Match History
*PlayersApi* | [**mateStats**](Apis/PlayersApi.http#matestats) | **GET** /v1/players/{account_id}/mate-stats | Mate Stats
*PlayersApi* | [**partyStats**](Apis/PlayersApi.http#partystats) | **GET** /v1/players/{account_id}/party-stats | Party Stats
*PlayersApi* | [**playerHeroStats**](Apis/PlayersApi.http#playerherostats) | **GET** /v1/players/hero-stats | Hero Stats
*PlayersApi* | [**steam**](Apis/PlayersApi.http#steam) | **GET** /v1/players/steam | Batch Steam Profile
*PlayersApi* | [**steamSearch**](Apis/PlayersApi.http#steamsearch) | **GET** /v1/players/steam-search | Steam Profile Search
*SQLApi* | [**listTables**](Apis/SQLApi.http#listtables) | **GET** /v1/sql/tables | List Tables
*SQLApi* | [**sql**](Apis/SQLApi.http#sql) | **GET** /v1/sql | Query
*SQLApi* | [**tableSchema**](Apis/SQLApi.http#tableschema) | **GET** /v1/sql/tables/{table}/schema | Table Schema


## Usage

### Prerequisites

You need [IntelliJ](https://www.jetbrains.com/idea/) to be able to run those queries. More information can be found [here](https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html).
You may have some luck running queries using the [Code REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) as well, but your mileage may vary.

### Variables and Environment files

* Generally speaking, you want queries to be specific using custom variables. All variables in the `.http` files have the `` format.
* You can create [public or private environment files](https://www.jetbrains.com/help/idea/exploring-http-syntax.html#environment-variables) to dynamically replace the variables at runtime.

_Note: don't commit private environment files! They typically will contain sensitive information like API Keys._

### Customizations

If you have control over the generation of the files here, there are two main things you can do

* Select elements to replace as variables during generation. The process is case-sensitive. For example, API_KEY -> 
    * For this, run the generation with the `bodyVariables` property, followed by a "-" separated list of variables
    * Example: `--additional-properties bodyVariables=YOUR_MERCHANT_ACCOUNT-YOUR_COMPANY_ACCOUNT-YOUR_BALANCE_PLATFORM`
* Add custom headers to _all_ requests. This can be useful for example if your specifications are missing [security schemes](https://github.com/github/rest-api-description/issues/237).
    * For this, run the generation with the `customHeaders` property, followed by a "&" separated list of variables
    * Example : `--additional-properties=customHeaders="Cookie:X-API-KEY="&"Accept-Encoding=gzip"`

_This client was generated by the [jetbrains-http-client](https://openapi-generator.tech/docs/generators/jetbrains-http-client) generator of OpenAPI Generator_