# PlayerRegionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **u32** |  | 
**history** | [**Vec<models::PlayerClusterMonth>**](PlayerClusterMonth.md) | Matches per month and server cluster, newest month first. | 
**region** | Option<**String**> | The region the player played most matches in during their latest month with a known region. `null` if none of their matches has a known region. | [optional]
**region_month** | Option<**u32**> | Unix timestamp of the month `region` was taken from. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


