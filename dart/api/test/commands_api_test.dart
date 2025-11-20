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


/// tests for CommandsApi
void main() {
  // final instance = CommandsApi();

  group('tests for CommandsApi', () {
    // Available Variables
    //
    //  Returns a list of available variables that can be used in the command endpoint.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     
    //
    //Future<List<VariableDescription>> availableVariables() async
    test('test availableVariables', () async {
      // TODO
    });

    // Resolve Command
    //
    //      Resolves a command and returns the resolved command.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 60req/60s | | Key | - | | Global | 300req/60s |     
    //
    //Future<String> commandResolve(int accountId, { String region, String template, String heroName }) async
    test('test commandResolve', () async {
      // TODO
    });

    // Resolve Variables
    //
    //  Resolves variables and returns a map of variable name to resolved value.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 60req/min | | Key | - | | Global | 300req/min |     
    //
    //Future<Map<String, String>> variablesResolve(int accountId, { String region, String variables, String heroName }) async
    test('test variablesResolve', () async {
      // TODO
    });

    // Widget Versions
    //
    //  Returns a map of str->int of widget versions.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - | 
    //
    //Future<Map<String, int>> widgetVersions() async
    test('test widgetVersions', () async {
      // TODO
    });

  });
}
