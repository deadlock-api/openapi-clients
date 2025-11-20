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


/// tests for PatchesApi
void main() {
  // final instance = PatchesApi();

  group('tests for PatchesApi', () {
    // Big Days
    //
    //  Returns a list of dates where Deadlock's \"big\" patch days were, usually bi-weekly. The exact date is the time when the announcement forum post was published.  This list is manually maintained, and so new patch dates may be delayed by a few hours.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<String>> bigPatchDays() async
    test('test bigPatchDays', () async {
      // TODO
    });

    // Notes
    //
    //  Returns the parsed result of the RSS Feed from the official Forum.  RSS-Feed: https://forums.playdeadlock.com/forums/changelog.10/index.rss  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<ModelPatch>> feed() async
    test('test feed', () async {
      // TODO
    });

  });
}
