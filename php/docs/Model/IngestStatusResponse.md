# IngestStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  |
**active** | **bool** | Whether the ingest tool uploaded a salt for this account within the window that was then verified. |
**last_upload_at** | **int** | Unix timestamp of the most recent verified upload within the window. | [optional]
**window_days** | **int** | The window, in days, an upload must fall in to count. |

[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)
