
# PlayerClusterMonth

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **clusterId** | **kotlin.Int** | The server cluster the matches were played on. |  |
| **matches** | **kotlin.Long** | Number of the player&#39;s matches on this cluster in this month. |  |
| **month** | **kotlin.Int** | Unix timestamp of the first day of the month (UTC). |  |
| **datacenter** | **kotlin.String** | Datacenter(s) of the cluster&#39;s servers, e.g. &#x60;fra2&#x60;; comma-separated if the cluster spans several. &#x60;null&#x60; if the cluster has not been seen in a replay yet. |  [optional] |
| **region** | **kotlin.String** | Region of the cluster&#39;s servers, e.g. &#x60;eu_west&#x60; or &#x60;us_north_central&#x60;. &#x60;null&#x60; if the cluster has not been seen in a replay yet. |  [optional] |



