# SteamServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addr** | **string** | Full address of the server including port (e.g. &#x60;1.2.3.4:27015&#x60;) | [default to undefined]
**appid** | **number** | Steam appid of the game running on this server | [default to undefined]
**bots** | **number** | Number of bots on the server | [default to undefined]
**dedicated** | **boolean** | Whether this is a dedicated server | [default to undefined]
**gamedir** | **string** | Internal game directory name | [default to undefined]
**gameport** | **number** | Game port the server is listening on | [default to undefined]
**gametype** | **string** | Steam gametype tags | [default to undefined]
**map** | **string** | Current map | [default to undefined]
**max_players** | **number** | Maximum player count | [default to undefined]
**name** | **string** | Server name as advertised to Steam | [default to undefined]
**os** | **string** | Operating system the server is running on (e.g. &#x60;l&#x60; for Linux, &#x60;w&#x60; for Windows) | [default to undefined]
**players** | **number** | Current player count | [default to undefined]
**product** | **string** | Product identifier reported by the server | [default to undefined]
**region** | **number** | Steam region code reported by the server | [default to undefined]
**secure** | **boolean** | Whether the server is VAC-secured | [default to undefined]
**steamid** | **string** | &#x60;SteamID&#x60; of the server | [default to undefined]
**version** | **string** | Server build version | [default to undefined]

## Example

```typescript
import { SteamServer } from 'deadlock_api_client';

const instance: SteamServer = {
    addr,
    appid,
    bots,
    dedicated,
    gamedir,
    gameport,
    gametype,
    map,
    max_players,
    name,
    os,
    players,
    product,
    region,
    secure,
    steamid,
    version,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
