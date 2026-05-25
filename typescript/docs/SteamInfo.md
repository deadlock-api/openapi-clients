# SteamInfo

Per-patch Steam manifest as served by the public assets API.  Field order is load-bearing — it sets the JSON key order, which matches the legacy Python endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **number** |  | [default to undefined]
**client_version** | **number** |  | [default to undefined]
**product_name** | **string** |  | [default to undefined]
**server_app_id** | **number** |  | [default to undefined]
**server_version** | **number** |  | [default to undefined]
**source_revision** | **number** |  | [default to undefined]
**tools_app_id** | **number** |  | [default to undefined]
**version_date** | **string** |  | [default to undefined]
**version_datetime** | **string** | &#x60;version_date&#x60; + &#x60;version_time&#x60; combined into a naive ISO-8601 string (&#x60;YYYY-MM-DDTHH:MM:SS&#x60;, no timezone) — matches the Python output. | [default to undefined]
**version_time** | **string** |  | [default to undefined]

## Example

```typescript
import { SteamInfo } from 'deadlock_api_client';

const instance: SteamInfo = {
    app_id,
    client_version,
    product_name,
    server_app_id,
    server_version,
    source_revision,
    tools_app_id,
    version_date,
    version_datetime,
    version_time,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
