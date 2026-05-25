# MetricIngestRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Steam account id (&#x60;UInt32&#x60;) of the player this metric is about |
**game_mode** | **string** | Game mode this metric applies to (e.g. \&quot;speedrun\&quot;) |
**game_mode_version** | **string** | Optional game-mode version tag (e.g. \&quot;v2\&quot;, \&quot;season3\&quot;) for versioning leaderboards | [optional]
**map** | **string** | Optional map identifier the metric was produced on | [optional]
**metadata** | **array<string,string>** | Free-form key/value metadata for game-mode-specific context | [optional]
**metric_name** | **string** | Name of the metric (e.g. &#x60;run_time&#x60;) |
**metric_value** | **float** | The primary numeric measurement for this metric |
**region** | **string** | Region the server is located in (e.g. \&quot;eu\&quot;, \&quot;na\&quot;) |
**server_id** | **string** | Unique identifier for the game server reporting the metric |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
