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


/// tests for MatchesApi
void main() {
  // final instance = MatchesApi();

  group('tests for MatchesApi', () {
    // Active
    //
    //  Returns active matches that are currently being played.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<ActiveMatch>> activeMatches({ int accountId, List<int> accountIds }) async
    test('test activeMatches', () async {
      // TODO
    });

    // Active as Protobuf
    //
    //  Returns active matches that are currently being played, serialized as protobuf message.  Fetched from the watch tab in game, which is limited to the **top 200 matches**.  You have to decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Message: - CMsgClientToGcGetActiveMatchesResponse  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<int>> activeMatchesRaw() async
    test('test activeMatchesRaw', () async {
      // TODO
    });

    // Bulk Metadata
    //
    //  This endpoints lets you fetch multiple match metadata at once. The response is a JSON array of match metadata.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 4req/s | | Key | - | | Global | 10req/s |     
    //
    //Future<List<int>> bulkMetadata({ bool includeInfo, bool includeObjectives, bool includeMidBoss, bool includePlayerInfo, bool includePlayerItems, bool includePlayerStats, bool includePlayerDeathDetails, List<int> matchIds, int minUnixTimestamp, int maxUnixTimestamp, int minDurationS, int maxDurationS, int minAverageBadge, int maxAverageBadge, int minMatchId, int maxMatchId, bool isHighSkillRangeParties, bool isLowPriPool, bool isNewPlayerPool, List<int> accountIds, String heroIds, String orderBy, String orderDirection, int limit }) async
    test('test bulkMetadata', () async {
      // TODO
    });

    // Metadata
    //
    //  This endpoint returns the match metadata for the given `match_id` parsed into JSON.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins | | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min | | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |     
    //
    //Future metadata(int matchId, { bool isCustom }) async
    test('test metadata', () async {
      // TODO
    });

    // Metadata as Protobuf
    //
    //  This endpoints returns the raw .meta.bz2 file for the given `match_id`.  You have to decompress it and decode the protobuf message.  Protobuf definitions can be found here: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)  Relevant Protobuf Messages: - CMsgMatchMetaData - CMsgMatchMetaDataContents  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins | | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min | | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |     
    //
    //Future<List<int>> metadataRaw(int matchId, { bool isCustom }) async
    test('test metadataRaw', () async {
      // TODO
    });

    // Recently Fetched
    //
    //  This endpoint returns a list of match ids that have been fetched within the last 10 minutes.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<ClickhouseMatchInfo>> recentlyFetched({ bool playerIngestedOnly }) async
    test('test recentlyFetched', () async {
      // TODO
    });

    // Salts
    //
    //  This endpoints returns salts that can be used to fetch metadata and demofile for a match.  **Note:** We currently fetch many matches without salts, so for these matches we do not have salts stored.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | From DB: 100req/s<br>From Steam: 10req/30mins | | Key | From DB: -<br>From Steam: 10req/min | | Global | From DB: -<br>From Steam: 10req/10s |     
    //
    //Future<MatchSaltsResponse> salts(int matchId) async
    test('test salts', () async {
      // TODO
    });

    // Live Broadcast URL
    //
    //  This endpoints spectates a match and returns the live URL to be used in any demofile broadcast parser.  Example Parsers: - [Demofile-Net](https://github.com/saul/demofile-net) - [Haste](https://github.com/blukai/haste/)  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 10req/30mins | | Key | 60req/min | | Global | 100req/10s |     
    //
    //Future<MatchSpectateResponse> url(int matchId) async
    test('test url', () async {
      // TODO
    });

  });
}
