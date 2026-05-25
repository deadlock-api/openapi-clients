# MetricIngestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **number** | Steam account id (&#x60;UInt32&#x60;) of the player this metric is about | [default to undefined]
**game_mode** | **string** | Game mode this metric applies to (e.g. \&quot;speedrun\&quot;) | [default to undefined]
**game_mode_version** | **string** | Optional game-mode version tag (e.g. \&quot;v2\&quot;, \&quot;season3\&quot;) for versioning leaderboards | [optional] [default to undefined]
**map** | **string** | Optional map identifier the metric was produced on | [optional] [default to undefined]
**metadata** | **{ [key: string]: string; }** | Free-form key/value metadata for game-mode-specific context | [optional] [default to undefined]
**metric_name** | **string** | Name of the metric (e.g. &#x60;run_time&#x60;) | [default to undefined]
**metric_value** | **number** | The primary numeric measurement for this metric | [default to undefined]
**region** | **string** | Region the server is located in (e.g. \&quot;eu\&quot;, \&quot;na\&quot;) | [default to undefined]
**server_id** | **string** | Unique identifier for the game server reporting the metric | [default to undefined]

## Example

```typescript
import { MetricIngestRequest } from 'deadlock_api_client';

const instance: MetricIngestRequest = {
    account_id,
    game_mode,
    game_mode_version,
    map,
    metadata,
    metric_name,
    metric_value,
    region,
    server_id,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
