# deadlock-api-client


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
      "url": "https://github.com/GIT_USER_ID/GIT_REPO_ID.git"
    }
  ],
  "require": {
    "GIT_USER_ID/GIT_REPO_ID": "*@dev"
  }
}
```

Then run `composer install`

### Manual Installation

Download the files and include `autoload.php`:

```php
<?php
require_once('/path/to/deadlock-api-client/vendor/autoload.php');
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');




$apiInstance = new OpenAPI\Client\Api\AnalyticsApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$hero_id = 56; // int | See more: <https://assets.deadlock-api.com/v2/heroes>
$min_unix_timestamp = 1756166400; // int | Filter matches based on their start time (Unix timestamp). **Default:** 30 days ago.
$max_unix_timestamp = 56; // int | Filter matches based on their start time (Unix timestamp).
$min_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$max_duration_s = 56; // int | Filter matches based on their duration in seconds (up to 7000s).
$min_ability_upgrades = 56; // int | Filter players based on their minimum number of ability upgrades over the whole match.
$max_ability_upgrades = 56; // int | Filter players based on their maximum number of ability upgrades over the whole match.
$min_networth = 56; // int | Filter players based on their net worth.
$max_networth = 56; // int | Filter players based on their net worth.
$min_average_badge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$max_average_badge = 56; // int | Filter matches based on the average badge level (0-116) of *both* teams involved. See more: <https://assets.deadlock-api.com/v2/ranks>
$min_match_id = 56; // int | Filter matches based on their ID.
$max_match_id = 56; // int | Filter matches based on their ID.
$min_matches = 20; // int | The minimum number of matches played for an ability order to be included in the response.
$account_id = 56; // int | Filter for matches with a specific player account ID.
$account_ids = array(56); // int[] | Comma separated list of account ids to include

try {
    $result = $apiInstance->abilityOrderStats($hero_id, $min_unix_timestamp, $max_unix_timestamp, $min_duration_s, $max_duration_s, $min_ability_upgrades, $max_ability_upgrades, $min_networth, $max_networth, $min_average_badge, $max_average_badge, $min_match_id, $max_match_id, $min_matches, $account_id, $account_ids);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling AnalyticsApi->abilityOrderStats: ', $e->getMessage(), PHP_EOL;
}

```

## API Endpoints

All URIs are relative to *https://api.deadlock-api.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnalyticsApi* | [**abilityOrderStats**](docs/Api/AnalyticsApi.md#abilityorderstats) | **GET** /v1/analytics/ability-order-stats | Ability Order Stats
*AnalyticsApi* | [**badgeDistribution**](docs/Api/AnalyticsApi.md#badgedistribution) | **GET** /v1/analytics/badge-distribution | Badge Distribution
*AnalyticsApi* | [**buildItemStats**](docs/Api/AnalyticsApi.md#builditemstats) | **GET** /v1/analytics/build-item-stats | Build Item Stats
*AnalyticsApi* | [**heroCombStats**](docs/Api/AnalyticsApi.md#herocombstats) | **GET** /v1/analytics/hero-comb-stats | Hero Comb Stats
*AnalyticsApi* | [**heroCountersStats**](docs/Api/AnalyticsApi.md#herocountersstats) | **GET** /v1/analytics/hero-counter-stats | Hero Counter Stats
*AnalyticsApi* | [**heroScoreboard**](docs/Api/AnalyticsApi.md#heroscoreboard) | **GET** /v1/analytics/scoreboards/heroes | Hero Scoreboard
*AnalyticsApi* | [**heroStats**](docs/Api/AnalyticsApi.md#herostats) | **GET** /v1/analytics/hero-stats | Hero Stats
*AnalyticsApi* | [**heroSynergiesStats**](docs/Api/AnalyticsApi.md#herosynergiesstats) | **GET** /v1/analytics/hero-synergy-stats | Hero Synergy Stats
*AnalyticsApi* | [**itemPermutationStats**](docs/Api/AnalyticsApi.md#itempermutationstats) | **GET** /v1/analytics/item-permutation-stats | Item Permutation Stats
*AnalyticsApi* | [**itemStats**](docs/Api/AnalyticsApi.md#itemstats) | **GET** /v1/analytics/item-stats | Item Stats
*AnalyticsApi* | [**playerScoreboard**](docs/Api/AnalyticsApi.md#playerscoreboard) | **GET** /v1/analytics/scoreboards/players | Player Scoreboard
*AnalyticsApi* | [**playerStatsMetrics**](docs/Api/AnalyticsApi.md#playerstatsmetrics) | **GET** /v1/analytics/player-stats/metrics | Player Stats Metrics
*BuildsApi* | [**searchBuilds**](docs/Api/BuildsApi.md#searchbuilds) | **GET** /v1/builds | Search
*CommandsApi* | [**availableVariables**](docs/Api/CommandsApi.md#availablevariables) | **GET** /v1/commands/variables/available | Available Variables
*CommandsApi* | [**commandResolve**](docs/Api/CommandsApi.md#commandresolve) | **GET** /v1/commands/resolve | Resolve Command
*CommandsApi* | [**variablesResolve**](docs/Api/CommandsApi.md#variablesresolve) | **GET** /v1/commands/variables/resolve | Resolve Variables
*CommandsApi* | [**widgetVersions**](docs/Api/CommandsApi.md#widgetversions) | **GET** /v1/commands/widgets/versions | Widget Versions
*CustomMatchesApi* | [**createCustom**](docs/Api/CustomMatchesApi.md#createcustom) | **POST** /v1/matches/custom/create | Create Match
*CustomMatchesApi* | [**getCustom**](docs/Api/CustomMatchesApi.md#getcustom) | **GET** /v1/matches/custom/{party_id}/match-id | Get Match ID
*ESportsApi* | [**ingestMatch**](docs/Api/ESportsApi.md#ingestmatch) | **POST** /v1/esports/ingest/match | Ingest
*ESportsApi* | [**matches**](docs/Api/ESportsApi.md#matches) | **GET** /v1/esports/matches | List Matches
*InfoApi* | [**healthCheck**](docs/Api/InfoApi.md#healthcheck) | **GET** /v1/info/health | Health Check
*InfoApi* | [**info**](docs/Api/InfoApi.md#info) | **GET** /v1/info | API Info
*InternalApi* | [**ingestSalts**](docs/Api/InternalApi.md#ingestsalts) | **POST** /v1/matches/salts | Match Salts Ingest
*LeaderboardApi* | [**leaderboard**](docs/Api/LeaderboardApi.md#leaderboard) | **GET** /v1/leaderboard/{region} | Leaderboard
*LeaderboardApi* | [**leaderboardHero**](docs/Api/LeaderboardApi.md#leaderboardhero) | **GET** /v1/leaderboard/{region}/{hero_id} | Hero Leaderboard
*LeaderboardApi* | [**leaderboardHeroRaw**](docs/Api/LeaderboardApi.md#leaderboardheroraw) | **GET** /v1/leaderboard/{region}/{hero_id}/raw | Hero Leaderboard as Protobuf
*LeaderboardApi* | [**leaderboardRaw**](docs/Api/LeaderboardApi.md#leaderboardraw) | **GET** /v1/leaderboard/{region}/raw | Leaderboard as Protobuf
*MMRApi* | [**heroMmr**](docs/Api/MMRApi.md#herommr) | **GET** /v1/players/mmr/{hero_id} | Hero MMR
*MMRApi* | [**heroMmrHistory**](docs/Api/MMRApi.md#herommrhistory) | **GET** /v1/players/{account_id}/mmr-history/{hero_id} | Hero MMR History
*MMRApi* | [**mmr**](docs/Api/MMRApi.md#mmr) | **GET** /v1/players/mmr | MMR
*MMRApi* | [**mmrHistory**](docs/Api/MMRApi.md#mmrhistory) | **GET** /v1/players/{account_id}/mmr-history | MMR History
*MatchesApi* | [**activeMatches**](docs/Api/MatchesApi.md#activematches) | **GET** /v1/matches/active | Active
*MatchesApi* | [**activeMatchesRaw**](docs/Api/MatchesApi.md#activematchesraw) | **GET** /v1/matches/active/raw | Active as Protobuf
*MatchesApi* | [**bulkMetadata**](docs/Api/MatchesApi.md#bulkmetadata) | **GET** /v1/matches/metadata | Bulk Metadata
*MatchesApi* | [**metadata**](docs/Api/MatchesApi.md#metadata) | **GET** /v1/matches/{match_id}/metadata | Metadata
*MatchesApi* | [**metadataRaw**](docs/Api/MatchesApi.md#metadataraw) | **GET** /v1/matches/{match_id}/metadata/raw | Metadata as Protobuf
*MatchesApi* | [**recentlyFetched**](docs/Api/MatchesApi.md#recentlyfetched) | **GET** /v1/matches/recently-fetched | Recently Fetched
*MatchesApi* | [**salts**](docs/Api/MatchesApi.md#salts) | **GET** /v1/matches/{match_id}/salts | Salts
*MatchesApi* | [**url**](docs/Api/MatchesApi.md#url) | **GET** /v1/matches/{match_id}/live/url | Live Broadcast URL
*PatchesApi* | [**bigPatchDays**](docs/Api/PatchesApi.md#bigpatchdays) | **GET** /v1/patches/big-days | Big Days
*PatchesApi* | [**feed**](docs/Api/PatchesApi.md#feed) | **GET** /v1/patches | Notes
*PlayersApi* | [**card**](docs/Api/PlayersApi.md#card) | **GET** /v1/players/{account_id}/card | Card
*PlayersApi* | [**enemyStats**](docs/Api/PlayersApi.md#enemystats) | **GET** /v1/players/{account_id}/enemy-stats | Enemy Stats
*PlayersApi* | [**matchHistory**](docs/Api/PlayersApi.md#matchhistory) | **GET** /v1/players/{account_id}/match-history | Match History
*PlayersApi* | [**mateStats**](docs/Api/PlayersApi.md#matestats) | **GET** /v1/players/{account_id}/mate-stats | Mate Stats
*PlayersApi* | [**partyStats**](docs/Api/PlayersApi.md#partystats) | **GET** /v1/players/{account_id}/party-stats | Party Stats
*PlayersApi* | [**playerHeroStats**](docs/Api/PlayersApi.md#playerherostats) | **GET** /v1/players/hero-stats | Hero Stats
*PlayersApi* | [**steam**](docs/Api/PlayersApi.md#steam) | **GET** /v1/players/steam | Batch Steam Profile
*PlayersApi* | [**steamSearch**](docs/Api/PlayersApi.md#steamsearch) | **GET** /v1/players/steam-search | Steam Profile Search
*SQLApi* | [**listTables**](docs/Api/SQLApi.md#listtables) | **GET** /v1/sql/tables | List Tables
*SQLApi* | [**sql**](docs/Api/SQLApi.md#sql) | **GET** /v1/sql | Query
*SQLApi* | [**tableSchema**](docs/Api/SQLApi.md#tableschema) | **GET** /v1/sql/tables/{table}/schema | Table Schema

## Models

- [APIInfo](docs/Model/APIInfo.md)
- [ActiveMatch](docs/Model/ActiveMatch.md)
- [ActiveMatchGameMode](docs/Model/ActiveMatchGameMode.md)
- [ActiveMatchMode](docs/Model/ActiveMatchMode.md)
- [ActiveMatchPlayer](docs/Model/ActiveMatchPlayer.md)
- [ActiveMatchRegionMode](docs/Model/ActiveMatchRegionMode.md)
- [ActiveMatchTeam](docs/Model/ActiveMatchTeam.md)
- [AnalyticsAbilityOrderStats](docs/Model/AnalyticsAbilityOrderStats.md)
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
- [ClickhouseMatchInfo](docs/Model/ClickhouseMatchInfo.md)
- [ClickhouseSalts](docs/Model/ClickhouseSalts.md)
- [CreateCustomRequest](docs/Model/CreateCustomRequest.md)
- [CreateCustomResponse](docs/Model/CreateCustomResponse.md)
- [ESportsMatch](docs/Model/ESportsMatch.md)
- [ESportsMatchStatus](docs/Model/ESportsMatchStatus.md)
- [EnemyStats](docs/Model/EnemyStats.md)
- [Entry](docs/Model/Entry.md)
- [GetCustomMatchIdResponse](docs/Model/GetCustomMatchIdResponse.md)
- [HashMapValue](docs/Model/HashMapValue.md)
- [HeroCombStats](docs/Model/HeroCombStats.md)
- [HeroCounterStats](docs/Model/HeroCounterStats.md)
- [HeroStats](docs/Model/HeroStats.md)
- [HeroSynergyStats](docs/Model/HeroSynergyStats.md)
- [ItemPermutationStats](docs/Model/ItemPermutationStats.md)
- [ItemStats](docs/Model/ItemStats.md)
- [Leaderboard](docs/Model/Leaderboard.md)
- [LeaderboardEntry](docs/Model/LeaderboardEntry.md)
- [MMRHistory](docs/Model/MMRHistory.md)
- [MatchSaltsResponse](docs/Model/MatchSaltsResponse.md)
- [MatchSpectateResponse](docs/Model/MatchSpectateResponse.md)
- [MateStats](docs/Model/MateStats.md)
- [PartyStats](docs/Model/PartyStats.md)
- [Patch](docs/Model/Patch.md)
- [PatchCategory](docs/Model/PatchCategory.md)
- [PatchGuid](docs/Model/PatchGuid.md)
- [PlayerCard](docs/Model/PlayerCard.md)
- [PlayerCardSlot](docs/Model/PlayerCardSlot.md)
- [PlayerCardSlotHero](docs/Model/PlayerCardSlotHero.md)
- [PlayerCardSlotStat](docs/Model/PlayerCardSlotStat.md)
- [PlayerMatchHistoryEntry](docs/Model/PlayerMatchHistoryEntry.md)
- [RegionMode](docs/Model/RegionMode.md)
- [Status](docs/Model/Status.md)
- [StatusServices](docs/Model/StatusServices.md)
- [SteamProfile](docs/Model/SteamProfile.md)
- [TableSize](docs/Model/TableSize.md)
- [VariableCategory](docs/Model/VariableCategory.md)
- [VariableDescription](docs/Model/VariableDescription.md)

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
    - Generator version: `7.14.0`
- Build package: `org.openapitools.codegen.languages.PhpClientCodegen`
