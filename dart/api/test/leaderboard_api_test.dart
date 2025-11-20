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


/// tests for LeaderboardApi
void main() {
  // final instance = LeaderboardApi();

  group('tests for LeaderboardApi', () {
    // Leaderboard
    //
    //  Returns the leaderboard.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<Leaderboard> leaderboard(String region) async
    test('test leaderboard', () async {
      // TODO
    });

    // Hero Leaderboard
    //
    //  Returns the leaderboard for a specific hero.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<Leaderboard> leaderboardHero(String region, int heroId) async
    test('test leaderboardHero', () async {
      // TODO
    });

    // Hero Leaderboard as Protobuf
    //
    //  Returns the leaderboard for a specific hero, serialized as protobuf message.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetLeaderboardResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<int>> leaderboardHeroRaw(String region, int heroId) async
    test('test leaderboardHeroRaw', () async {
      // TODO
    });

    // Leaderboard as Protobuf
    //
    //  Returns the leaderboard, serialized as protobuf message.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetLeaderboardResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<int>> leaderboardRaw(String region) async
    test('test leaderboardRaw', () async {
      // TODO
    });

  });
}
