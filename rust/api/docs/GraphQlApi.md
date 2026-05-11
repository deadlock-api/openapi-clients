# \GraphQlApi

All URIs are relative to *https://api.deadlock-api.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**playground**](GraphQlApi.md#playground) | **GET** /v1/graphql | GraphQL Playground



## playground

> playground()
GraphQL Playground

 Interactive GraphiQL playground for exploring the GraphQL API.  Open this endpoint in a browser to access the playground. Send GraphQL queries via `POST /v1/graphql` with a JSON body of the form `{ \"query\": \"...\", \"variables\": {...} }`.  ### Rate Limits (POST): | Type | Limit | | ---- | ----- | | IP | 10req/min | | Key | 10req/10s | | Global | 100req/min |     

### Parameters

This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

