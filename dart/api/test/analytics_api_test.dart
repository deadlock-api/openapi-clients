//
// AUTO-GENERATED FILE, DO NOT MODIFY!
//
// @dart=2.18

// ignore_for_file: unused_element, unused_import
// ignore_for_file: always_put_required_named_parameters_first
// ignore_for_file: constant_identifier_names
// ignore_for_file: lines_longer_than_80_chars

import 'package:deadlock-api-client/api.dart';
import 'package:test/test.dart';


/// tests for AnalyticsApi
void main() {
  // final instance = AnalyticsApi();

  group('tests for AnalyticsApi', () {
    // Ability Order Stats
    //
    //  Retrieves statistics for the ability order of a hero.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<AnalyticsAbilityOrderStats>> abilityOrderStats(int heroId, { int minUnixTimestamp, int maxUnixTimestamp, int minDurationS, int maxDurationS, int minAbilityUpgrades, int maxAbilityUpgrades, int minNetworth, int maxNetworth, int minAverageBadge, int maxAverageBadge, int minMatchId, int maxMatchId, int minMatches, int accountId, List<int> accountIds }) async
    test('test abilityOrderStats', () async {
      // TODO
    });

    // Badge Distribution
    //
    //  This endpoint returns the player badge distribution.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<BadgeDistribution>> badgeDistribution({ int minUnixTimestamp, int maxUnixTimestamp, int minDurationS, int maxDurationS, bool isHighSkillRangeParties, bool isLowPriPool, bool isNewPlayerPool, int minMatchId, int maxMatchId }) async
    test('test badgeDistribution', () async {
      // TODO
    });

    // Build Item Stats
    //
    //  Retrieves item statistics from hero builds.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<BuildItemStats>> buildItemStats({ int heroId, int minLastUpdatedUnixTimestamp, int maxLastUpdatedUnixTimestamp }) async
    test('test buildItemStats', () async {
      // TODO
    });

    // Hero Comb Stats
    //
    //  Retrieves overall statistics for each hero combination.  Results are cached for **1 hour**. The cache key is determined by the specific combination of filter parameters used in the query. Subsequent requests using the exact same filters within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<HeroCombStats>> heroCombStats({ int minUnixTimestamp, int maxUnixTimestamp, int minDurationS, int maxDurationS, int minNetworth, int maxNetworth, int minAverageBadge, int maxAverageBadge, int minMatchId, int maxMatchId, List<int> includeHeroIds, List<int> excludeHeroIds, int minMatches, int maxMatches, int combSize, int accountId, List<int> accountIds }) async
    test('test heroCombStats', () async {
      // TODO
    });

    // Hero Counter Stats
    //
    //  Retrieves hero-versus-hero matchup statistics based on historical match data.  This endpoint analyzes completed matches to calculate how often a specific hero (`hero_id`) wins against an enemy hero (`enemy_hero_id`) and the total number of times they have faced each other under the specified filter conditions.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<HeroCounterStats>> heroCountersStats({ int minUnixTimestamp, int maxUnixTimestamp, int minDurationS, int maxDurationS, int minNetworth, int maxNetworth, int minEnemyNetworth, int maxEnemyNetworth, int minAverageBadge, int maxAverageBadge, int minMatchId, int maxMatchId, bool sameLaneFilter, int minMatches, int maxMatches, int accountId, List<int> accountIds }) async
    test('test heroCountersStats', () async {
      // TODO
    });

    // Hero Scoreboard
    //
    //  This endpoint returns the hero scoreboard.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<Entry>> heroScoreboard(String sortBy, { String sortDirection, int minMatches, int minUnixTimestamp, int maxUnixTimestamp, int minDurationS, int maxDurationS, int minNetworth, int maxNetworth, int minAverageBadge, int maxAverageBadge, int minMatchId, int maxMatchId, int accountId, List<int> accountIds }) async
    test('test heroScoreboard', () async {
      // TODO
    });

    // Hero Stats
    //
    //  Retrieves performance statistics for each hero based on historical match data.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<AnalyticsHeroStats>> heroStats({ String bucket, int minUnixTimestamp, int maxUnixTimestamp, int minDurationS, int maxDurationS, int minNetworth, int maxNetworth, int minAverageBadge, int maxAverageBadge, int minMatchId, int maxMatchId, int minHeroMatches, int maxHeroMatches, List<int> includeItemIds, List<int> excludeItemIds, int accountId, List<int> accountIds }) async
    test('test heroStats', () async {
      // TODO
    });

    // Hero Synergy Stats
    //
    //  Retrieves hero pair synergy statistics based on historical match data.  This endpoint analyzes completed matches to calculate how often a specific pair of heroes (`hero_id1` and `hero_id2`) won when playing *together on the same team*, and the total number of times they have played together under the specified filter conditions.  Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<HeroSynergyStats>> heroSynergiesStats({ int minUnixTimestamp, int maxUnixTimestamp, int minDurationS, int maxDurationS, int minNetworth, int maxNetworth, int minAverageBadge, int maxAverageBadge, int minMatchId, int maxMatchId, bool sameLaneFilter, bool samePartyFilter, int minMatches, int maxMatches, int accountId, List<int> accountIds }) async
    test('test heroSynergiesStats', () async {
      // TODO
    });

    // Item Permutation Stats
    //
    //  Retrieves item permutation statistics based on historical match data.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<ItemPermutationStats>> itemPermutationStats({ List<int> itemIds, int combSize, String heroIds, int heroId, int minUnixTimestamp, int maxUnixTimestamp, int minDurationS, int maxDurationS, int minNetworth, int maxNetworth, int minAverageBadge, int maxAverageBadge, int minMatchId, int maxMatchId, int accountId, List<int> accountIds }) async
    test('test itemPermutationStats', () async {
      // TODO
    });

    // Item Stats
    //
    //  Retrieves item statistics based on historical match data.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<ItemStats>> itemStats({ String bucket, String heroIds, int heroId, int minUnixTimestamp, int maxUnixTimestamp, int minDurationS, int maxDurationS, int minNetworth, int maxNetworth, int minAverageBadge, int maxAverageBadge, int minMatchId, int maxMatchId, List<int> includeItemIds, List<int> excludeItemIds, int minMatches, int maxMatches, int accountId, List<int> accountIds }) async
    test('test itemStats', () async {
      // TODO
    });

    // Player Scoreboard
    //
    //  This endpoint returns the player scoreboard.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<Entry>> playerScoreboard(String sortBy, { String sortDirection, int heroId, int minMatches, int maxMatches, int minUnixTimestamp, int maxUnixTimestamp, int minDurationS, int maxDurationS, int minNetworth, int maxNetworth, int minAverageBadge, int maxAverageBadge, int minMatchId, int maxMatchId, int start, int limit, List<int> accountIds }) async
    test('test playerScoreboard', () async {
      // TODO
    });

    // Player Stats Metrics
    //
    //  Returns comprehensive statistical analysis of player performance.  Results are cached for **1 hour** based on the unique combination of query parameters provided. Subsequent identical requests within this timeframe will receive the cached response.  > Note: Quantiles are calculated using the [DDSketch](https://www.vldb.org/pvldb/vol12/p2195-masson.pdf) algorithm, so they are not exact but have a maximum relative error of 0.01.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<Object> playerStatsMetrics({ String heroIds, int minUnixTimestamp, int maxUnixTimestamp, int minDurationS, int maxDurationS, int minNetworth, int maxNetworth, int minAverageBadge, int maxAverageBadge, int minMatchId, int maxMatchId, int maxMatches, List<int> includeItemIds, List<int> excludeItemIds, List<int> accountIds }) async
    test('test playerStatsMetrics', () async {
      // TODO
    });

  });
}
