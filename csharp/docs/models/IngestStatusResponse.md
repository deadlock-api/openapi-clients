# DeadlockApiClient.Model.IngestStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **long** |  | 
**Active** | **bool** | Whether the ingest tool uploaded a salt for this account within the window that was then verified. | 
**WindowDays** | **long** | The window, in days, an upload must fall in to count. | 
**LastUploadAt** | **long** | Unix timestamp of the most recent verified upload within the window. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

