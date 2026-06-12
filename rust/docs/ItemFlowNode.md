# ItemFlowNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjusted_win_rate** | **f64** | Win rate standardized to the stage's net-worth-at-buy distribution, removing the \"richer buyers win more\" confound. See the endpoint description. | 
**avg_net_worth_at_buy** | **f64** | Average net worth of buyers at the moment they bought this item (confound visibility). | 
**column** | **u32** | The phase column (0-based) the item was bought in. | 
**item_id** | **u32** | See more: <https://api.deadlock-api.com/v1/assets/items> | 
**losses** | **u64** |  | 
**matches** | **u64** |  | 
**players** | **u64** |  | 
**total_assists** | **u64** |  | 
**total_deaths** | **u64** |  | 
**total_kills** | **u64** |  | 
**wins** | **u64** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


