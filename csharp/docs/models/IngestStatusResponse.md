# DeadlockApiClient.Model.IngestStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccountId** | **int** |  | 
**Active** | **bool** | Whether the ingest tool uploaded a salt for this account within the window that was then verified. | 
**WindowDays** | **int** | The window, in days, an upload must fall in to count. | 
**LastUploadAt** | **int** | Unix timestamp of the most recent verified upload within the window. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

