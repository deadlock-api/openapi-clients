
# IngestStatusResponse

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.Int** |  |  |
| **active** | **kotlin.Boolean** | Whether the ingest tool uploaded a salt for this account within the window that was then verified. |  |
| **windowDays** | **kotlin.Int** | The window, in days, an upload must fall in to count. |  |
| **lastUploadAt** | **kotlin.Int** | Unix timestamp of the most recent verified upload within the window. |  [optional] |



