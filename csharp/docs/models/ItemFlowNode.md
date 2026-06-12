# DeadlockApiClient.Model.ItemFlowNode
A single item, aggregated within one column of the flow graph.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AdjustedWinRate** | **double** | Win rate standardized to the stage&#39;s net-worth-at-buy distribution, removing the \&quot;richer buyers win more\&quot; confound. See the endpoint description. | 
**AvgNetWorthAtBuy** | **double** | Average net worth of buyers at the moment they bought this item (confound visibility). | 
**Column** | **int** | The phase column (0-based) the item was bought in. | 
**ItemId** | **int** | See more: &lt;https://api.deadlock-api.com/v1/assets/items&gt; | 
**Losses** | **long** |  | 
**Matches** | **long** |  | 
**Players** | **long** |  | 
**TotalAssists** | **long** |  | 
**TotalDeaths** | **long** |  | 
**TotalKills** | **long** |  | 
**Wins** | **long** |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

