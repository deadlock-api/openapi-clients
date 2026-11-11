# PlayerClusterMonth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **u32** | The server cluster the matches were played on. | 
**datacenter** | Option<**String**> | Datacenter(s) of the cluster's servers, e.g. `fra2`; comma-separated if the cluster spans several. `null` if the cluster has not been seen in a replay yet. | [optional]
**matches** | **u64** | Number of the player's matches on this cluster in this month. | 
**month** | **u32** | Unix timestamp of the first day of the month (UTC). | 
**region** | Option<**String**> | Region of the cluster's servers, e.g. `eu_west` or `us_north_central`. `null` if the cluster has not been seen in a replay yet. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


