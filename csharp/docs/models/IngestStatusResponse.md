# DeadlockApiClient.Model.IngestStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **long** |  | 
**Active** | **bool** | Whether the account&#39;s player tracker is open to everyone: it or one of its Steam friends ran an ingest client within the window, or a patron prioritizes it. | 
**FriendActive** | **bool** | Whether a Steam friend of the account uploaded with an ingest client within the window. | 
**Prioritized** | **bool** | Whether the account is one of a patron&#39;s active prioritized accounts. | 
**WindowDays** | **long** | The window, in days, an upload must fall in to count. | 
**LastUploadAt** | **long** | Unix timestamp of the account&#39;s own most recent verified upload within the window. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

