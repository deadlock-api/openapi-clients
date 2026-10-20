# AnalyticsAbilityOrderTreeNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Abilities** | **[]int32** | The order prefix: one entry per ability point spent, unlocks included. Its parent node is the prefix one entry shorter. See more: &lt;https://api.deadlock-api.com/v1/assets/heroes&gt; | 
**AvgUpgradeTimeS** | **float64** | Average game time (in seconds) at which the last upgrade in &#x60;abilities&#x60; was bought. | 
**Losses** | **int64** |  | 
**Matches** | **int64** |  | 
**Players** | **int64** | Distinct players, counted exactly. | 
**TotalAssists** | **int64** |  | 
**TotalDeaths** | **int64** |  | 
**TotalKills** | **int64** |  | 
**Wins** | **int64** |  | 

## Methods

### NewAnalyticsAbilityOrderTreeNode

`func NewAnalyticsAbilityOrderTreeNode(abilities []int32, avgUpgradeTimeS float64, losses int64, matches int64, players int64, totalAssists int64, totalDeaths int64, totalKills int64, wins int64, ) *AnalyticsAbilityOrderTreeNode`

NewAnalyticsAbilityOrderTreeNode instantiates a new AnalyticsAbilityOrderTreeNode object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAnalyticsAbilityOrderTreeNodeWithDefaults

`func NewAnalyticsAbilityOrderTreeNodeWithDefaults() *AnalyticsAbilityOrderTreeNode`

NewAnalyticsAbilityOrderTreeNodeWithDefaults instantiates a new AnalyticsAbilityOrderTreeNode object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAbilities

`func (o *AnalyticsAbilityOrderTreeNode) GetAbilities() []int32`

GetAbilities returns the Abilities field if non-nil, zero value otherwise.

### GetAbilitiesOk

`func (o *AnalyticsAbilityOrderTreeNode) GetAbilitiesOk() (*[]int32, bool)`

GetAbilitiesOk returns a tuple with the Abilities field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAbilities

`func (o *AnalyticsAbilityOrderTreeNode) SetAbilities(v []int32)`

SetAbilities sets Abilities field to given value.


### GetAvgUpgradeTimeS

`func (o *AnalyticsAbilityOrderTreeNode) GetAvgUpgradeTimeS() float64`

GetAvgUpgradeTimeS returns the AvgUpgradeTimeS field if non-nil, zero value otherwise.

### GetAvgUpgradeTimeSOk

`func (o *AnalyticsAbilityOrderTreeNode) GetAvgUpgradeTimeSOk() (*float64, bool)`

GetAvgUpgradeTimeSOk returns a tuple with the AvgUpgradeTimeS field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAvgUpgradeTimeS

`func (o *AnalyticsAbilityOrderTreeNode) SetAvgUpgradeTimeS(v float64)`

SetAvgUpgradeTimeS sets AvgUpgradeTimeS field to given value.


### GetLosses

`func (o *AnalyticsAbilityOrderTreeNode) GetLosses() int64`

GetLosses returns the Losses field if non-nil, zero value otherwise.

### GetLossesOk

`func (o *AnalyticsAbilityOrderTreeNode) GetLossesOk() (*int64, bool)`

GetLossesOk returns a tuple with the Losses field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLosses

`func (o *AnalyticsAbilityOrderTreeNode) SetLosses(v int64)`

SetLosses sets Losses field to given value.


### GetMatches

`func (o *AnalyticsAbilityOrderTreeNode) GetMatches() int64`

GetMatches returns the Matches field if non-nil, zero value otherwise.

### GetMatchesOk

`func (o *AnalyticsAbilityOrderTreeNode) GetMatchesOk() (*int64, bool)`

GetMatchesOk returns a tuple with the Matches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMatches

`func (o *AnalyticsAbilityOrderTreeNode) SetMatches(v int64)`

SetMatches sets Matches field to given value.


### GetPlayers

`func (o *AnalyticsAbilityOrderTreeNode) GetPlayers() int64`

GetPlayers returns the Players field if non-nil, zero value otherwise.

### GetPlayersOk

`func (o *AnalyticsAbilityOrderTreeNode) GetPlayersOk() (*int64, bool)`

GetPlayersOk returns a tuple with the Players field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPlayers

`func (o *AnalyticsAbilityOrderTreeNode) SetPlayers(v int64)`

SetPlayers sets Players field to given value.


### GetTotalAssists

`func (o *AnalyticsAbilityOrderTreeNode) GetTotalAssists() int64`

GetTotalAssists returns the TotalAssists field if non-nil, zero value otherwise.

### GetTotalAssistsOk

`func (o *AnalyticsAbilityOrderTreeNode) GetTotalAssistsOk() (*int64, bool)`

GetTotalAssistsOk returns a tuple with the TotalAssists field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalAssists

`func (o *AnalyticsAbilityOrderTreeNode) SetTotalAssists(v int64)`

SetTotalAssists sets TotalAssists field to given value.


### GetTotalDeaths

`func (o *AnalyticsAbilityOrderTreeNode) GetTotalDeaths() int64`

GetTotalDeaths returns the TotalDeaths field if non-nil, zero value otherwise.

### GetTotalDeathsOk

`func (o *AnalyticsAbilityOrderTreeNode) GetTotalDeathsOk() (*int64, bool)`

GetTotalDeathsOk returns a tuple with the TotalDeaths field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalDeaths

`func (o *AnalyticsAbilityOrderTreeNode) SetTotalDeaths(v int64)`

SetTotalDeaths sets TotalDeaths field to given value.


### GetTotalKills

`func (o *AnalyticsAbilityOrderTreeNode) GetTotalKills() int64`

GetTotalKills returns the TotalKills field if non-nil, zero value otherwise.

### GetTotalKillsOk

`func (o *AnalyticsAbilityOrderTreeNode) GetTotalKillsOk() (*int64, bool)`

GetTotalKillsOk returns a tuple with the TotalKills field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalKills

`func (o *AnalyticsAbilityOrderTreeNode) SetTotalKills(v int64)`

SetTotalKills sets TotalKills field to given value.


### GetWins

`func (o *AnalyticsAbilityOrderTreeNode) GetWins() int64`

GetWins returns the Wins field if non-nil, zero value otherwise.

### GetWinsOk

`func (o *AnalyticsAbilityOrderTreeNode) GetWinsOk() (*int64, bool)`

GetWinsOk returns a tuple with the Wins field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWins

`func (o *AnalyticsAbilityOrderTreeNode) SetWins(v int64)`

SetWins sets Wins field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


