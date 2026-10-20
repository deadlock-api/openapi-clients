# DeadlockApiClient.Model.AnalyticsAbilityOrderTreeNode
One node of the ability order tree: the players whose upgrade order starts with `abilities`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Abilities** | **List&lt;int&gt;** | The order prefix: one entry per ability point spent, unlocks included. Its parent node is the prefix one entry shorter. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**AvgUpgradeTimeS** | **double** | Average game time (in seconds) at which the last upgrade in &#x60;abilities&#x60; was bought. | 
**Losses** | **long** |  | 
**Matches** | **long** |  | 
**Players** | **long** | Distinct players, counted exactly. | 
**TotalAssists** | **long** |  | 
**TotalDeaths** | **long** |  | 
**TotalKills** | **long** |  | 
**Wins** | **long** |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

