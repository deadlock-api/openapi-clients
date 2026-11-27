# IngestStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  |
**active** | **bool** | Whether the account&#39;s player tracker is open to everyone: it or one of its Steam friends ran an ingest client within the window, or a patron prioritizes it. |
**friend_active** | **bool** | Whether a Steam friend of the account uploaded with an ingest client within the window. |
**last_upload_at** | **int** | Unix timestamp of the account&#39;s own most recent verified upload within the window. | [optional]
**prioritized** | **bool** | Whether the account is one of a patron&#39;s active prioritized accounts. |
**window_days** | **int** | The window, in days, an upload must fall in to count. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
