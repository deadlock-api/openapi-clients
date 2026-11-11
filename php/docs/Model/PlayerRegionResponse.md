# PlayerRegionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  |
**history** | [**\OpenAPI\Client\Model\PlayerClusterMonth[]**](PlayerClusterMonth.md) | Matches per month and server cluster, newest month first. |
**region** | **string** | The region the player played most matches in during their latest month with a known region. &#x60;null&#x60; if none of their matches has a known region. | [optional]
**region_month** | **int** | Unix timestamp of the month &#x60;region&#x60; was taken from. | [optional]

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
