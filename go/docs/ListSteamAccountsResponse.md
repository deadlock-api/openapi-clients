# ListSteamAccountsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Accounts** | [**[]SteamAccountListItem**](SteamAccountListItem.md) |  | 
**Summary** | [**SlotsSummary**](SlotsSummary.md) |  | 

## Methods

### NewListSteamAccountsResponse

`func NewListSteamAccountsResponse(accounts []SteamAccountListItem, summary SlotsSummary, ) *ListSteamAccountsResponse`

NewListSteamAccountsResponse instantiates a new ListSteamAccountsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListSteamAccountsResponseWithDefaults

`func NewListSteamAccountsResponseWithDefaults() *ListSteamAccountsResponse`

NewListSteamAccountsResponseWithDefaults instantiates a new ListSteamAccountsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccounts

`func (o *ListSteamAccountsResponse) GetAccounts() []SteamAccountListItem`

GetAccounts returns the Accounts field if non-nil, zero value otherwise.

### GetAccountsOk

`func (o *ListSteamAccountsResponse) GetAccountsOk() (*[]SteamAccountListItem, bool)`

GetAccountsOk returns a tuple with the Accounts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccounts

`func (o *ListSteamAccountsResponse) SetAccounts(v []SteamAccountListItem)`

SetAccounts sets Accounts field to given value.


### GetSummary

`func (o *ListSteamAccountsResponse) GetSummary() SlotsSummary`

GetSummary returns the Summary field if non-nil, zero value otherwise.

### GetSummaryOk

`func (o *ListSteamAccountsResponse) GetSummaryOk() (*SlotsSummary, bool)`

GetSummaryOk returns a tuple with the Summary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSummary

`func (o *ListSteamAccountsResponse) SetSummary(v SlotsSummary)`

SetSummary sets Summary field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


