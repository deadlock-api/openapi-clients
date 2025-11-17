# Assets - Deadlock API - Jetbrains API Client

## General API description

 ## API Clients  We have auto generated and updated clients for many languages. You can find them here: [https://github.com/deadlock-api/openapi-clients](https://github.com/deadlock-api/openapi-clients)  ## Support the Deadlock API  Whether you&#39;re building your own database, developing data science projects, or enhancing your website with game and player analytics, the Deadlock API has the data you need.  Your sponsorship helps keep this resource open, free and future-proof for everyone. By supporting the Deadlock API, you will enable continued development, new features and reliable access for developers, analysts and streamers worldwide.  Help us continue to provide the data you need - sponsor the Deadlock API today!  **-&gt; You can Sponsor the Deadlock API on [Patreon](https://www.patreon.com/c/user?u&#x3D;68961896) or [GitHub](https://github.com/sponsors/raimannma)**  ## Disclaimer _deadlock-api.com is not endorsed by Valve and does not reflect the views or opinions of Valve or anyone officially involved in producing or managing Valve properties. Valve and all associated properties are trademarks or registered trademarks of Valve Corporation_ 

* API basepath : [https://assets.deadlock-api.com](https://assets.deadlock-api.com)
* Version : 0.1.0

## Documentation for API Endpoints

All URIs are relative to *https://assets.deadlock-api.com*, but will link to the `.http` file that contains the endpoint definition.
There may be multiple requests for a single endpoint, one for each example described in the OpenAPI specification.

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**getBuildTagsV2BuildTagsGet**](Apis/DefaultApi.http#getbuildtagsv2buildtagsget) | **GET** /v2/build-tags | Get Build Tags
*DefaultApi* | [**getClientVersionsV2ClientVersionsGet**](Apis/DefaultApi.http#getclientversionsv2clientversionsget) | **GET** /v2/client-versions | Get Client Versions
*DefaultApi* | [**getColorsV1ColorsGet**](Apis/DefaultApi.http#getcolorsv1colorsget) | **GET** /v1/colors | Get Colors
*DefaultApi* | [**getIconsV1IconsGet**](Apis/DefaultApi.http#geticonsv1iconsget) | **GET** /v1/icons | Get Icons
*DefaultApi* | [**getMapV1MapGet**](Apis/DefaultApi.http#getmapv1mapget) | **GET** /v1/map | Get Map
*DefaultApi* | [**getRanksV2RanksGet**](Apis/DefaultApi.http#getranksv2ranksget) | **GET** /v2/ranks | Get Ranks
*DefaultApi* | [**getSoundsV1SoundsGet**](Apis/DefaultApi.http#getsoundsv1soundsget) | **GET** /v1/sounds | Get Sounds
*DefaultApi* | [**getSteamInfoV1SteamInfoGet**](Apis/DefaultApi.http#getsteaminfov1steaminfoget) | **GET** /v1/steam-info | Get Steam Info
*HeroesApi* | [**getHeroByNameV2HeroesByNameNameGet**](Apis/HeroesApi.http#getherobynamev2heroesbynamenameget) | **GET** /v2/heroes/by-name/{name} | Get Hero By Name
*HeroesApi* | [**getHeroV2HeroesIdGet**](Apis/HeroesApi.http#getherov2heroesidget) | **GET** /v2/heroes/{id} | Get Hero
*HeroesApi* | [**getHeroesV2HeroesGet**](Apis/HeroesApi.http#getheroesv2heroesget) | **GET** /v2/heroes | Get Heroes
*ItemsApi* | [**getItemV2ItemsIdOrClassNameGet**](Apis/ItemsApi.http#getitemv2itemsidorclassnameget) | **GET** /v2/items/{id_or_class_name} | Get Item
*ItemsApi* | [**getItemsByHeroIdV2ItemsByHeroIdIdGet**](Apis/ItemsApi.http#getitemsbyheroidv2itemsbyheroididget) | **GET** /v2/items/by-hero-id/{id} | Get Items By Hero Id
*ItemsApi* | [**getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet**](Apis/ItemsApi.http#getitemsbyslottypev2itemsbyslottypeslottypeget) | **GET** /v2/items/by-slot-type/{slot_type} | Get Items By Slot Type
*ItemsApi* | [**getItemsByTypeV2ItemsByTypeTypeGet**](Apis/ItemsApi.http#getitemsbytypev2itemsbytypetypeget) | **GET** /v2/items/by-type/{type} | Get Items By Type
*ItemsApi* | [**getItemsV2ItemsGet**](Apis/ItemsApi.http#getitemsv2itemsget) | **GET** /v2/items | Get Items
*RawApi* | [**getGenericDataRawGenericDataGet**](Apis/RawApi.http#getgenericdatarawgenericdataget) | **GET** /raw/generic_data | Get Generic Data
*RawApi* | [**getRawHeroesRawHeroesGet**](Apis/RawApi.http#getrawheroesrawheroesget) | **GET** /raw/heroes | Get Raw Heroes
*RawApi* | [**getRawItemsRawItemsGet**](Apis/RawApi.http#getrawitemsrawitemsget) | **GET** /raw/items | Get Raw Items


## Usage

### Prerequisites

You need [IntelliJ](https://www.jetbrains.com/idea/) to be able to run those queries. More information can be found [here](https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html).
You may have some luck running queries using the [Code REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) as well, but your mileage may vary.

### Variables and Environment files

* Generally speaking, you want queries to be specific using custom variables. All variables in the `.http` files have the `` format.
* You can create [public or private environment files](https://www.jetbrains.com/help/idea/exploring-http-syntax.html#environment-variables) to dynamically replace the variables at runtime.

_Note: don't commit private environment files! They typically will contain sensitive information like API Keys._

### Customizations

If you have control over the generation of the files here, there are two main things you can do

* Select elements to replace as variables during generation. The process is case-sensitive. For example, API_KEY -> 
    * For this, run the generation with the `bodyVariables` property, followed by a "-" separated list of variables
    * Example: `--additional-properties bodyVariables=YOUR_MERCHANT_ACCOUNT-YOUR_COMPANY_ACCOUNT-YOUR_BALANCE_PLATFORM`
* Add custom headers to _all_ requests. This can be useful for example if your specifications are missing [security schemes](https://github.com/github/rest-api-description/issues/237).
    * For this, run the generation with the `customHeaders` property, followed by a "&" separated list of variables
    * Example : `--additional-properties=customHeaders="Cookie:X-API-KEY="&"Accept-Encoding=gzip"`

_This client was generated by the [jetbrains-http-client](https://openapi-generator.tech/docs/generators/jetbrains-http-client) generator of OpenAPI Generator_