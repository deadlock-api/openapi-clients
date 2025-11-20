//
// AUTO-GENERATED FILE, DO NOT MODIFY!
//
// @dart=2.18

// ignore_for_file: unused_element, unused_import
// ignore_for_file: always_put_required_named_parameters_first
// ignore_for_file: constant_identifier_names
// ignore_for_file: lines_longer_than_80_chars

import 'package:deadlock_api_client/api.dart';
import 'package:test/test.dart';


/// tests for PlayersApi
void main() {
  // final instance = PlayersApi();

  group('tests for PlayersApi', () {
    // Enemy Stats
    //
    //  This endpoint returns the enemy stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<EnemyStats>> enemyStats(int accountId, { int minUnixTimestamp, int maxUnixTimestamp, int minDurationS, int maxDurationS, int minMatchId, int maxMatchId, int minMatchesPlayed, int maxMatchesPlayed }) async
    test('test enemyStats', () async {
      // TODO
    });

    // Match History
    //
    //  This endpoint returns the player match history for the given `account_id`.  The player match history is a combination of the data from **Steam** and **ClickHouse**, so you always get the most up-to-date data and full history.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgClientToGcGetMatchHistory - CMsgClientToGcGetMatchHistoryResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 5req/min<br>With `only_stored_history=true`: 100req/s<br>With `force_refetch=true`: 5req/h | | Key | 50req/min & 1000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 5req/h | | Global | 2000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 10req/h |     
    //
    //Future<List<PlayerMatchHistoryEntry>> matchHistory(int accountId, { bool forceRefetch, bool onlyStoredHistory }) async
    test('test matchHistory', () async {
      // TODO
    });

    // Mate Stats
    //
    //  This endpoint returns the mate stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<MateStats>> mateStats(int accountId, { int minUnixTimestamp, int maxUnixTimestamp, int minDurationS, int maxDurationS, int minMatchId, int maxMatchId, int minMatchesPlayed, int maxMatchesPlayed, bool sameParty }) async
    test('test mateStats', () async {
      // TODO
    });

    // Party Stats
    //
    //  This endpoint returns the party stats.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<PartyStats>> partyStats(int accountId, { int minUnixTimestamp, int maxUnixTimestamp, int minDurationS, int maxDurationS, int minMatchId, int maxMatchId }) async
    test('test partyStats', () async {
      // TODO
    });

    // Hero Stats
    //
    //  This endpoint returns statistics for each hero played by a given player account.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<HeroStats>> playerHeroStats(List<int> accountIds, { String heroIds, int minUnixTimestamp, int maxUnixTimestamp, int minDurationS, int maxDurationS, int minNetworth, int maxNetworth, int minAverageBadge, int maxAverageBadge, int minMatchId, int maxMatchId }) async
    test('test playerHeroStats', () async {
      // TODO
    });

    // Batch Steam Profile
    //
    //  This endpoint returns Steam profiles of players.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<SteamProfile>> steam(List<int> accountIds) async
    test('test steam', () async {
      // TODO
    });

    // Steam Profile Search
    //
    //  This endpoint lets you search for Steam profiles by account_id or personaname.  See: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<SteamProfile>> steamSearch(String searchQuery) async
    test('test steamSearch', () async {
      // TODO
    });

  });
}
