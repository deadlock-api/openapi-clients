# SteamServer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addr** | **String** | Full address of the server including port (e.g. `1.2.3.4:27015`) | 
**appid** | **u32** | Steam appid of the game running on this server | 
**bots** | **u32** | Number of bots on the server | 
**dedicated** | **bool** | Whether this is a dedicated server | 
**gamedir** | **String** | Internal game directory name | 
**gameport** | **u32** | Game port the server is listening on | 
**gametype** | **String** | Steam gametype tags | 
**map** | **String** | Current map | 
**max_players** | **u32** | Maximum player count | 
**name** | **String** | Server name as advertised to Steam | 
**os** | **String** | Operating system the server is running on (e.g. `l` for Linux, `w` for Windows) | 
**players** | **u32** | Current player count | 
**product** | **String** | Product identifier reported by the server | 
**region** | **i32** | Steam region code reported by the server | 
**secure** | **bool** | Whether the server is VAC-secured | 
**steamid** | **String** | `SteamID` of the server | 
**version** | **String** | Server build version | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


