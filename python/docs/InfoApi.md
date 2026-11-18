# deadlock_api_client.InfoApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check**](InfoApi.md#health_check) | **GET** /v1/info/health | Health Check
[**info**](InfoApi.md#info) | **GET** /v1/info | API Info
[**live_requests**](InfoApi.md#live_requests) | **GET** /v1/info/live-requests | Live Requests (SSE)


# **health_check**
> Status health_check()

Health Check


Checks the health of the services.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |


### Example


```python
import deadlock_api_client
from deadlock_api_client.models.status import Status
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.InfoApi(api_client)

    try:
        # Health Check
        api_response = api_instance.health_check()
        print("The response of InfoApi->health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->health_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info**
> APIInfo info()

API Info


Returns information about the API.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | 100req/s |
| Key | - |
| Global | - |


### Example


```python
import deadlock_api_client
from deadlock_api_client.models.api_info import APIInfo
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.InfoApi(api_client)

    try:
        # API Info
        api_response = api_instance.info()
        print("The response of InfoApi->info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfoApi->info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**APIInfo**](APIInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **live_requests**
> live_requests()

Live Requests (SSE)


A live, sampled feed of the requests the API is serving, as drawn on the website's live map.

Each request carries only its approximate location (rounded to 0.1°), country, the Cloudflare data
center it went through, its route template, status, duration and response size. No IP addresses,
query strings or API keys. Every request is in the feed, up to 512 a batch (sampled beyond that; `n` counts all of them).

Responses Cloudflare serves from its cache never reach the API and are not in the feed.

A client may hold 4 streams at once. A stream ends after 30 minutes.

### Rate Limits:
| Type | Limit |
| ---- | ----- |
| IP | Opening a stream: 30req/10min |
| Key | Opening a stream: - |
| Global | Opening a stream: - |


### Example


```python
import deadlock_api_client
from deadlock_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.deadlock-api.com
# See configuration.py for a list of all supported configuration parameters.
configuration = deadlock_api_client.Configuration(
    host = "https://api.deadlock-api.com"
)


# Enter a context with an instance of the API client
with deadlock_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deadlock_api_client.InfoApi(api_client)

    try:
        # Live Requests (SSE)
        api_instance.live_requests()
    except Exception as e:
        print("Exception when calling InfoApi->live_requests: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSE stream with one &#x60;message&#x60; event every 500 ms. Its &#x60;data&#x60; is a JSON object: &#x60;t&#x60; the tick&#39;s start (unix ms), &#x60;d&#x60; its length (ms), &#x60;n&#x60; the requests served in it, &#x60;q&#x60; the requests in progress at its end and &#x60;qp&#x60; the most at once during it, &#x60;cr&#x60; / &#x60;cw&#x60; the &#x60;ClickHouse&#x60; queries running / waiting for a slot and &#x60;cl&#x60; the current slot limit, &#x60;cq&#x60; / &#x60;rr&#x60; / &#x60;rb&#x60; the &#x60;ClickHouse&#x60; queries the tick&#39;s requests ran and the rows / bytes they read, &#x60;r&#x60; the route templates of this batch, and &#x60;e&#x60; the sampled requests as &#x60;[offset_ms, lat, lon, country, colo, route_index, status, duration_ms, response_bytes, rows_read]&#x60;, where &#x60;colo&#x60; is the IATA code of the Cloudflare data center that handed the request to the API (the Ray id&#39;s, usually one near the API rather than the client&#39;s edge) and &#x60;lat&#x60;, &#x60;lon&#x60;, &#x60;country&#x60; and &#x60;colo&#x60; are null when unknown. &#x60;hm&#x60; carries a minute of the requests Cloudflare answered itself as &#x60;{m: unix_minute, g: [[kind, colo, country, count], ...], s: {tr, cr, tb, cb, at, ac, lr, lb}, d: {lr, lb}}&#x60;: kind 0-4 is API cache hits, website, assets, other subdomains, data lake; &#x60;s&#x60; holds the minute&#39;s requests (&#x60;tr&#x60;) and response bytes (&#x60;tb&#x60;) with the cached ones (&#x60;cr&#x60;, &#x60;cb&#x60;), the API&#39;s requests (&#x60;at&#x60;) with its cached ones (&#x60;ac&#x60;) and the data lake&#39;s requests and bytes (&#x60;lr&#x60;, &#x60;lb&#x60;); &#x60;d&#x60; the data lake&#39;s since midnight UTC (null if unavailable). It comes first on connect and then whenever a new minute is complete, a few minutes behind real time. &#x60;im&#x60; carries the matches the ingest worker just wrote to the database, one entry per flush (about one a minute): &#x60;{t: unix_ms, n: matches_written, m: [[match_id, start_time, duration_s, game_mode, match_mode, average_badge, winning_team, region, team0_hero_ids, team1_hero_ids], ...]}&#x60;, &#x60;m&#x60; a random sample of at most 300 of them and &#x60;region&#x60; the server region (null if unknown). The newest entry comes first on connect, with &#x60;ih&#x60;: &#x60;[t, n]&#x60; of the last 30 flushes. |  -  |
**429** | Rate limit exceeded, or too many streams open |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

