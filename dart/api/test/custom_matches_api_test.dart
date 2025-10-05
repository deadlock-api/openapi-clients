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


/// tests for CustomMatchesApi
void main() {
  // final instance = CustomMatchesApi();

  group('tests for CustomMatchesApi', () {
    // Create Match
    //
    //  This endpoint creates a custom match using a bot account.  **Process:** 1. A party is created with your provided settings. 2. The system waits for the party code to be generated. 3. The party code is returned in the response. 4. The bot switches to spectator mode. 5. The bot marks itself as ready. 6. You and other players join, ready up, and start the match.  **Callbacks:** If a callback URL is provided, POST requests will be sent to it: - **settings:** When lobby settings change, a POST is sent to `{callback_url}/settings` with the `CsoCitadelParty` protobuf message as JSON. - **match start:** When the match starts, a POST is sent to `{callback_url}` with the match ID.  _Protobuf definitions: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)_  **Note:** The bot will leave the match 15 minutes after creation, regardless of match state.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | API-Key ONLY | | Key | 100req/30min | | Global | 1000req/h | 
    //
    //Future<CreateCustomResponse> createCustom(CreateCustomRequest createCustomRequest) async
    test('test createCustom', () async {
      // TODO
    });

    // Get Match ID
    //
    //  This endpoint allows you to get the match id of a custom match.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 
    //
    //Future<GetCustomMatchIdResponse> getCustom(int partyId) async
    test('test getCustom', () async {
      // TODO
    });

  });
}
