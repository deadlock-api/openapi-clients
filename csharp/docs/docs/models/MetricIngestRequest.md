# DeadlockApiClient.Model.MetricIngestRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **int** | Steam account id (&#x60;UInt32&#x60;) of the player this metric is about | 
**GameMode** | **string** | Game mode this metric applies to (e.g. \&quot;speedrun\&quot;) | 
**MetricName** | **string** | Name of the metric (e.g. &#x60;run_time&#x60;) | 
**MetricValue** | **double** | The primary numeric measurement for this metric | 
**Region** | **string** | Region the server is located in (e.g. \&quot;eu\&quot;, \&quot;na\&quot;) | 
**ServerId** | **string** | Unique identifier for the game server reporting the metric | 
**GameModeVersion** | **string** | Optional game-mode version tag (e.g. \&quot;v2\&quot;, \&quot;season3\&quot;) for versioning leaderboards | [optional] 
**Map** | **string** | Optional map identifier the metric was produced on | [optional] 
**Metadata** | **Dictionary&lt;string, string&gt;** | Free-form key/value metadata for game-mode-specific context | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

