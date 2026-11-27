
# IngestStatusResponse

## Properties
| Name | Type | Description | Notes |
| ------------ | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.Long** |  |  |
| **active** | **kotlin.Boolean** | Whether the account&#39;s player tracker is open to everyone: it or one of its Steam friends ran an ingest client within the window, or a patron prioritizes it. |  |
| **friendActive** | **kotlin.Boolean** | Whether a Steam friend of the account uploaded with an ingest client within the window. |  |
| **prioritized** | **kotlin.Boolean** | Whether the account is one of a patron&#39;s active prioritized accounts. |  |
| **windowDays** | **kotlin.Long** | The window, in days, an upload must fall in to count. |  |
| **lastUploadAt** | **kotlin.Long** | Unix timestamp of the account&#39;s own most recent verified upload within the window. |  [optional] |



