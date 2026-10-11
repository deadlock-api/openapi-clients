# IngestStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **u32** |  | 
**active** | **bool** | Whether the ingest tool uploaded a salt for this account within the window that was then verified. | 
**last_upload_at** | Option<**u32**> | Unix timestamp of the most recent verified upload within the window. | [optional]
**window_days** | **u32** | The window, in days, an upload must fall in to count. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


