# AssetsBucketApi

All URIs are relative to *https://api.deadlock-api.com*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**fonts**](AssetsBucketApi.md#fonts) | **GET** /v1/assets/fonts | Fonts Index |
| [**icons**](AssetsBucketApi.md#icons) | **GET** /v1/assets/icons | Icons Index |
| [**images**](AssetsBucketApi.md#images) | **GET** /v1/assets/images | Images Index |
| [**sounds**](AssetsBucketApi.md#sounds) | **GET** /v1/assets/sounds | Sounds Index |


<a id="fonts"></a>
# **fonts**
> kotlin.Any fonts()

Fonts Index

Nested file-tree of all hosted fonts, mapping each name to its public CDN URL.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = AssetsBucketApi()
try {
    val result : kotlin.Any = apiInstance.fonts()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AssetsBucketApi#fonts")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AssetsBucketApi#fonts")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="icons"></a>
# **icons**
> kotlin.Any icons()

Icons Index

Nested file-tree of all hosted icons, mapping each name to its public CDN URL.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = AssetsBucketApi()
try {
    val result : kotlin.Any = apiInstance.icons()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AssetsBucketApi#icons")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AssetsBucketApi#icons")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="images"></a>
# **images**
> kotlin.Any images()

Images Index

Nested file-tree of all hosted images, mapping each name to its public CDN URL.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = AssetsBucketApi()
try {
    val result : kotlin.Any = apiInstance.images()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AssetsBucketApi#images")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AssetsBucketApi#images")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a id="sounds"></a>
# **sounds**
> kotlin.Any sounds()

Sounds Index

Nested file-tree of all hosted sounds, mapping each name to its public CDN URL.

### Example
```kotlin
// Import classes:
//import deadlock_api_client.infrastructure.*
//import deadlock_api_client.models.*

val apiInstance = AssetsBucketApi()
try {
    val result : kotlin.Any = apiInstance.sounds()
    println(result)
} catch (e: ClientException) {
    println("4xx response calling AssetsBucketApi#sounds")
    e.printStackTrace()
} catch (e: ServerException) {
    println("5xx response calling AssetsBucketApi#sounds")
    e.printStackTrace()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

