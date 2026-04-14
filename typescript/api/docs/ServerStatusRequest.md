# ServerStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_player_count** | **number** | Current number of players on this server | [default to undefined]
**game_mode** | **string** | Game mode this server is running (e.g. \&quot;ranked\&quot;, \&quot;unranked\&quot;) | [default to undefined]
**ip** | **string** | IP address of the game server | [default to undefined]
**port** | **number** | Port the game server is listening on | [default to undefined]
**region** | **string** | Region the server is located in (e.g. \&quot;eu\&quot;, \&quot;na\&quot;, \&quot;sa\&quot;, \&quot;asia\&quot;, \&quot;oceania\&quot;) | [default to undefined]
**server_id** | **string** | Unique identifier for the game server | [default to undefined]

## Example

```typescript
import { ServerStatusRequest } from 'deadlock_api_client';

const instance: ServerStatusRequest = {
    current_player_count,
    game_mode,
    ip,
    port,
    region,
    server_id,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
