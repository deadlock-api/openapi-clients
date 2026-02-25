# # CreateCustomRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **string** | If a callback url is provided, we will send a POST request to this url when the match starts. | [optional]
**cheats_enabled** | **bool** |  | [optional]
**disable_auto_ready** | **bool** | If auto-ready is disabled, the bot will not automatically ready up. You need to call the &#x60;ready&#x60; endpoint to ready up. | [optional]
**duplicate_heroes_enabled** | **bool** |  | [optional]
**game_mode** | [**\OpenAPI\Client\Model\GameMode**](GameMode.md) |  | [optional]
**is_publicly_visible** | **bool** |  | [optional]
**min_roster_size** | **int** |  | [optional]
**randomize_lanes** | **bool** |  | [optional]
**server_region** | [**\OpenAPI\Client\Model\ServerRegion**](ServerRegion.md) |  | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
