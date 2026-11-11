# DeadlockApiClient.Model.PlayerClusterMonth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClusterId** | **int** | The server cluster the matches were played on. | 
**Matches** | **long** | Number of the player&#39;s matches on this cluster in this month. | 
**Month** | **int** | Unix timestamp of the first day of the month (UTC). | 
**Datacenter** | **string** | Datacenter(s) of the cluster&#39;s servers, e.g. &#x60;fra2&#x60;; comma-separated if the cluster spans several. &#x60;null&#x60; if the cluster has not been seen in a replay yet. | [optional] 
**Region** | **string** | Region of the cluster&#39;s servers, e.g. &#x60;eu_west&#x60; or &#x60;us_north_central&#x60;. &#x60;null&#x60; if the cluster has not been seen in a replay yet. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

