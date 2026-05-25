
# MetricIngestRequest

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.Int** | Steam account id (&#x60;UInt32&#x60;) of the player this metric is about |  |
| **gameMode** | **kotlin.String** | Game mode this metric applies to (e.g. \&quot;speedrun\&quot;) |  |
| **metricName** | **kotlin.String** | Name of the metric (e.g. &#x60;run_time&#x60;) |  |
| **metricValue** | **kotlin.Double** | The primary numeric measurement for this metric |  |
| **region** | **kotlin.String** | Region the server is located in (e.g. \&quot;eu\&quot;, \&quot;na\&quot;) |  |
| **serverId** | **kotlin.String** | Unique identifier for the game server reporting the metric |  |
| **gameModeVersion** | **kotlin.String** | Optional game-mode version tag (e.g. \&quot;v2\&quot;, \&quot;season3\&quot;) for versioning leaderboards |  [optional] |
| **map** | **kotlin.String** | Optional map identifier the metric was produced on |  [optional] |
| **metadata** | **kotlin.collections.Map&lt;kotlin.String, kotlin.String&gt;** | Free-form key/value metadata for game-mode-specific context |  [optional] |



