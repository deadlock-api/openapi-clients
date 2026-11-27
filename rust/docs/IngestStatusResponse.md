# IngestStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **u32** |  | 
**active** | **bool** | Whether the account's player tracker is open to everyone: it or one of its Steam friends ran an ingest client within the window, or a patron prioritizes it. | 
**friend_active** | **bool** | Whether a Steam friend of the account uploaded with an ingest client within the window. | 
**last_upload_at** | Option<**u32**> | Unix timestamp of the account's own most recent verified upload within the window. | [optional]
**prioritized** | **bool** | Whether the account is one of a patron's active prioritized accounts. | 
**window_days** | **u32** | The window, in days, an upload must fall in to count. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


