# InternalApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**addSteamAccount**](InternalApi.md#addSteamAccount) | **POST** /v1/patron/steam-accounts | Add Prioritized Steam Account |
| [**deleteSteamAccount**](InternalApi.md#deleteSteamAccount) | **DELETE** /v1/patron/steam-accounts/{account_id} | Remove Prioritized Steam Account |
| [**ingestSalts**](InternalApi.md#ingestSalts) | **POST** /v1/matches/salts | Match Salts Ingest |
| [**listSteamAccounts**](InternalApi.md#listSteamAccounts) | **GET** /v1/patron/steam-accounts | List Prioritized Steam Accounts |
| [**reactivateSteamAccount**](InternalApi.md#reactivateSteamAccount) | **POST** /v1/patron/steam-accounts/{account_id}/reactivate | Reactivate Prioritized Steam Account |
| [**replaceSteamAccount**](InternalApi.md#replaceSteamAccount) | **PUT** /v1/patron/steam-accounts/{account_id} | Replace Prioritized Steam Account |
| [**submitFeedback**](InternalApi.md#submitFeedback) | **POST** /v1/feedback | Submit Website Feedback |


<a id="addSteamAccount"></a>
# **addSteamAccount**
> SteamAccountResponse addSteamAccount(addSteamAccountRequest)

Add Prioritized Steam Account

 Adds a Steam account to the patron&#39;s prioritized fetching list. Matches of prioritized accounts are fetched first.  Re-adding an account that was removed earlier restores that entry.  ### Authentication Requires an API key linked to an active Patreon membership, sent as &#x60;X-API-Key&#x60; header, &#x60;api_key&#x60; query parameter or &#x60;Authorization: Bearer &lt;key&gt;&#x60;. A &#x60;patron_session&#x60; from the website login works as well. 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = InternalApi()
val addSteamAccountRequest : AddSteamAccountRequest =  // AddSteamAccountRequest | 
try {
    val result : SteamAccountResponse = apiInstance.addSteamAccount(addSteamAccountRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling InternalApi#addSteamAccount")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling InternalApi#addSteamAccount")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **addSteamAccountRequest** | [**AddSteamAccountRequest**](AddSteamAccountRequest.md)|  | |

### Return type

[**SteamAccountResponse**](SteamAccountResponse.md)

### Authorization


Configure api_key_query:
    ApiClient.apiKey["api_key"] = ""
    ApiClient.apiKeyPrefix["api_key"] = ""
Configure api_key_header:
    ApiClient.apiKey["X-API-KEY"] = ""
    ApiClient.apiKeyPrefix["X-API-KEY"] = ""

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a id="deleteSteamAccount"></a>
# **deleteSteamAccount**
> DeleteSteamAccountResponse deleteSteamAccount(accountId)

Remove Prioritized Steam Account

 Removes a Steam account from the patron&#39;s prioritized fetching list. &#x60;account_id&#x60; is the &#x60;steam_id3&#x60; or the entry &#x60;id&#x60;. Its slot stays in a 24 hour cooldown before it can be reused.  ### Authentication Requires an API key linked to an active Patreon membership, sent as &#x60;X-API-Key&#x60; header, &#x60;api_key&#x60; query parameter or &#x60;Authorization: Bearer &lt;key&gt;&#x60;. A &#x60;patron_session&#x60; from the website login works as well. 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = InternalApi()
val accountId : kotlin.String = accountId_example // kotlin.String | The account's `steam_id3`, or the `id` of its entry as returned by the list endpoint
try {
    val result : DeleteSteamAccountResponse = apiInstance.deleteSteamAccount(accountId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling InternalApi#deleteSteamAccount")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling InternalApi#deleteSteamAccount")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.String**| The account&#39;s &#x60;steam_id3&#x60;, or the &#x60;id&#x60; of its entry as returned by the list endpoint | |

### Return type

[**DeleteSteamAccountResponse**](DeleteSteamAccountResponse.md)

### Authorization


Configure api_key_query:
    ApiClient.apiKey["api_key"] = ""
    ApiClient.apiKeyPrefix["api_key"] = ""
Configure api_key_header:
    ApiClient.apiKey["X-API-KEY"] = ""
    ApiClient.apiKeyPrefix["X-API-KEY"] = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="ingestSalts"></a>
# **ingestSalts**
> ingestSalts(clickhouseSalts)

Match Salts Ingest

 You can use this endpoint to help us collecting data.  The endpoint accepts a list of MatchSalts objects, which contain the following fields:  - &#x60;match_id&#x60;: The match ID - &#x60;cluster_id&#x60;: The cluster ID - &#x60;metadata_salt&#x60;: The metadata salt - &#x60;replay_salt&#x60;: The replay salt - &#x60;username&#x60;: The username of the person who submitted the match  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 100req/s | | Key | - | | Global | - |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = InternalApi()
val clickhouseSalts : kotlin.collections.List<ClickhouseSalts> =  // kotlin.collections.List<ClickhouseSalts> | 
try {
    apiInstance.ingestSalts(clickhouseSalts)
} catch (e: ClientException) {
    println("4xx response calling InternalApi#ingestSalts")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling InternalApi#ingestSalts")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **clickhouseSalts** | [**kotlin.collections.List&lt;ClickhouseSalts&gt;**](ClickhouseSalts.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

<a id="listSteamAccounts"></a>
# **listSteamAccounts**
> ListSteamAccountsResponse listSteamAccounts()

List Prioritized Steam Accounts

 Lists the patron&#39;s prioritized Steam accounts, including removed ones still in their 24 hour cooldown, and a summary of slot usage.  ### Authentication Requires an API key linked to an active Patreon membership, sent as &#x60;X-API-Key&#x60; header, &#x60;api_key&#x60; query parameter or &#x60;Authorization: Bearer &lt;key&gt;&#x60;. A &#x60;patron_session&#x60; from the website login works as well. 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = InternalApi()
try {
    val result : ListSteamAccountsResponse = apiInstance.listSteamAccounts()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling InternalApi#listSteamAccounts")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling InternalApi#listSteamAccounts")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListSteamAccountsResponse**](ListSteamAccountsResponse.md)

### Authorization


Configure api_key_query:
    ApiClient.apiKey["api_key"] = ""
    ApiClient.apiKeyPrefix["api_key"] = ""
Configure api_key_header:
    ApiClient.apiKey["X-API-KEY"] = ""
    ApiClient.apiKeyPrefix["X-API-KEY"] = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="reactivateSteamAccount"></a>
# **reactivateSteamAccount**
> SteamAccountResponse reactivateSteamAccount(accountId)

Reactivate Prioritized Steam Account

 Restores a previously removed Steam account to the patron&#39;s prioritized fetching list. &#x60;account_id&#x60; is the &#x60;steam_id3&#x60; or the entry &#x60;id&#x60;.  ### Authentication Requires an API key linked to an active Patreon membership, sent as &#x60;X-API-Key&#x60; header, &#x60;api_key&#x60; query parameter or &#x60;Authorization: Bearer &lt;key&gt;&#x60;. A &#x60;patron_session&#x60; from the website login works as well. 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = InternalApi()
val accountId : kotlin.String = accountId_example // kotlin.String | The account's `steam_id3`, or the `id` of its entry as returned by the list endpoint
try {
    val result : SteamAccountResponse = apiInstance.reactivateSteamAccount(accountId)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling InternalApi#reactivateSteamAccount")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling InternalApi#reactivateSteamAccount")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.String**| The account&#39;s &#x60;steam_id3&#x60;, or the &#x60;id&#x60; of its entry as returned by the list endpoint | |

### Return type

[**SteamAccountResponse**](SteamAccountResponse.md)

### Authorization


Configure api_key_query:
    ApiClient.apiKey["api_key"] = ""
    ApiClient.apiKeyPrefix["api_key"] = ""
Configure api_key_header:
    ApiClient.apiKey["X-API-KEY"] = ""
    ApiClient.apiKeyPrefix["X-API-KEY"] = ""

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="replaceSteamAccount"></a>
# **replaceSteamAccount**
> SteamAccountResponse replaceSteamAccount(accountId, replaceSteamAccountRequest)

Replace Prioritized Steam Account

 Swaps a removed Steam account whose 24 hour cooldown has passed for a new &#x60;steam_id3&#x60;. &#x60;account_id&#x60; is the removed account&#39;s &#x60;steam_id3&#x60; or its entry &#x60;id&#x60;.  ### Authentication Requires an API key linked to an active Patreon membership, sent as &#x60;X-API-Key&#x60; header, &#x60;api_key&#x60; query parameter or &#x60;Authorization: Bearer &lt;key&gt;&#x60;. A &#x60;patron_session&#x60; from the website login works as well. 

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = InternalApi()
val accountId : kotlin.String = accountId_example // kotlin.String | The account's `steam_id3`, or the `id` of its entry as returned by the list endpoint
val replaceSteamAccountRequest : ReplaceSteamAccountRequest =  // ReplaceSteamAccountRequest | 
try {
    val result : SteamAccountResponse = apiInstance.replaceSteamAccount(accountId, replaceSteamAccountRequest)
    println(result)
} catch (e: ClientException) {
    println("4xx response calling InternalApi#replaceSteamAccount")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling InternalApi#replaceSteamAccount")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **accountId** | **kotlin.String**| The account&#39;s &#x60;steam_id3&#x60;, or the &#x60;id&#x60; of its entry as returned by the list endpoint | |
| **replaceSteamAccountRequest** | [**ReplaceSteamAccountRequest**](ReplaceSteamAccountRequest.md)|  | |

### Return type

[**SteamAccountResponse**](SteamAccountResponse.md)

### Authorization


Configure api_key_query:
    ApiClient.apiKey["api_key"] = ""
    ApiClient.apiKeyPrefix["api_key"] = ""
Configure api_key_header:
    ApiClient.apiKey["X-API-KEY"] = ""
    ApiClient.apiKeyPrefix["X-API-KEY"] = ""

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a id="submitFeedback"></a>
# **submitFeedback**
> submitFeedback(feedbackSubmission)

Submit Website Feedback

 Stores a component annotation or general feedback submitted from deadlock-api.com.  ### Rate Limits: | Type | Limit | | ---- | ----- | | IP | 10req/min, 100req/h | | Key | - | | Global | 2000req/h |     

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = InternalApi()
val feedbackSubmission : FeedbackSubmission =  // FeedbackSubmission | 
try {
    apiInstance.submitFeedback(feedbackSubmission)
} catch (e: ClientException) {
    println("4xx response calling InternalApi#submitFeedback")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling InternalApi#submitFeedback")
    e.printStackTrace()
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **feedbackSubmission** | [**FeedbackSubmission**](FeedbackSubmission.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

