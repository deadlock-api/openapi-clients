
# IngestStatusResponse

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.Long** |  |  |
| **active** | **kotlin.Boolean** | Whether the ingest tool uploaded a salt for this account within the window that was then verified. |  |
| **windowDays** | **kotlin.Long** | The window, in days, an upload must fall in to count. |  |
| **lastUploadAt** | **kotlin.Long** | Unix timestamp of the most recent verified upload within the window. |  [optional] |



