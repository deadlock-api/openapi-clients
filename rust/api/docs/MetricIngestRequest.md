# MetricIngestRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **u32** | Steam account id (`UInt32`) of the player this metric is about | 
**game_mode** | **String** | Game mode this metric applies to (e.g. \"speedrun\") | 
**game_mode_version** | Option<**String**> | Optional game-mode version tag (e.g. \"v2\", \"season3\") for versioning leaderboards | [optional]
**map** | Option<**String**> | Optional map identifier the metric was produced on | [optional]
**metadata** | Option<**std::collections::HashMap<String, String>**> | Free-form key/value metadata for game-mode-specific context | [optional]
**metric_name** | **String** | Name of the metric (e.g. `run_time`) | 
**metric_value** | **f64** | The primary numeric measurement for this metric | 
**region** | **String** | Region the server is located in (e.g. \"eu\", \"na\") | 
**server_id** | **String** | Unique identifier for the game server reporting the metric | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


