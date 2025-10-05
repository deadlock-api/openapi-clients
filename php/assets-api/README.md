# assets-deadlock-api-client


## Support the Deadlock API

Whether you're building your own database, developing data science projects, or enhancing your website with game and player analytics, the Deadlock API has the data you need.

Your sponsorship helps keep this resource open, free and future-proof for everyone. By supporting the Deadlock API, you will enable continued development, new features and reliable access for developers, analysts and streamers worldwide.

Help us continue to provide the data you need - sponsor the Deadlock API today!

**-> You can Sponsor the Deadlock API on [Patreon](https://www.patreon.com/c/user?u=68961896) or [GitHub](https://github.com/sponsors/raimannma)**

## Disclaimer
_deadlock-api.com is not endorsed by Valve and does not reflect the views or opinions of Valve or anyone officially involved in producing or managing Valve properties. Valve and all associated properties are trademarks or registered trademarks of Valve Corporation_


For more information, please visit [https://discord.gg/XMF9Xrgfqu](https://discord.gg/XMF9Xrgfqu).

## Installation & Usage

### Requirements

PHP 7.4 and later.
Should also work with PHP 8.0.

### Composer

To install the bindings via [Composer](https://getcomposer.org/), add the following to `composer.json`:

```json
{
  "repositories": [
    {
      "type": "vcs",
      "url": "https://github.com/GIT_USER_ID/GIT_REPO_ID.git"
    }
  ],
  "require": {
    "GIT_USER_ID/GIT_REPO_ID": "*@dev"
  }
}
```

Then run `composer install`

### Manual Installation

Download the files and include `autoload.php`:

```php
<?php
require_once('/path/to/assets-deadlock-api-client/vendor/autoload.php');
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');




$apiInstance = new OpenAPI\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$language = new \OpenAPI\Client\Model\Language(); // Language
$client_version = new \OpenAPI\Client\Model\ValidClientVersions(); // ValidClientVersions

try {
    $result = $apiInstance->getBuildTagsV2BuildTagsGet($language, $client_version);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getBuildTagsV2BuildTagsGet: ', $e->getMessage(), PHP_EOL;
}

```

## API Endpoints

All URIs are relative to *https://assets.deadlock-api.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**getBuildTagsV2BuildTagsGet**](docs/Api/DefaultApi.md#getbuildtagsv2buildtagsget) | **GET** /v2/build-tags | Get Build Tags
*DefaultApi* | [**getClientVersionsV2ClientVersionsGet**](docs/Api/DefaultApi.md#getclientversionsv2clientversionsget) | **GET** /v2/client-versions | Get Client Versions
*DefaultApi* | [**getColorsV1ColorsGet**](docs/Api/DefaultApi.md#getcolorsv1colorsget) | **GET** /v1/colors | Get Colors
*DefaultApi* | [**getIconsV1IconsGet**](docs/Api/DefaultApi.md#geticonsv1iconsget) | **GET** /v1/icons | Get Icons
*DefaultApi* | [**getMapV1MapGet**](docs/Api/DefaultApi.md#getmapv1mapget) | **GET** /v1/map | Get Map
*DefaultApi* | [**getRanksV2RanksGet**](docs/Api/DefaultApi.md#getranksv2ranksget) | **GET** /v2/ranks | Get Ranks
*DefaultApi* | [**getSoundsV1SoundsGet**](docs/Api/DefaultApi.md#getsoundsv1soundsget) | **GET** /v1/sounds | Get Sounds
*DefaultApi* | [**getSteamInfoV1SteamInfoGet**](docs/Api/DefaultApi.md#getsteaminfov1steaminfoget) | **GET** /v1/steam-info | Get Steam Info
*HeroesApi* | [**getHeroByNameV2HeroesByNameNameGet**](docs/Api/HeroesApi.md#getherobynamev2heroesbynamenameget) | **GET** /v2/heroes/by-name/{name} | Get Hero By Name
*HeroesApi* | [**getHeroV2HeroesIdGet**](docs/Api/HeroesApi.md#getherov2heroesidget) | **GET** /v2/heroes/{id} | Get Hero
*HeroesApi* | [**getHeroesV2HeroesGet**](docs/Api/HeroesApi.md#getheroesv2heroesget) | **GET** /v2/heroes | Get Heroes
*ItemsApi* | [**getItemV2ItemsIdOrClassNameGet**](docs/Api/ItemsApi.md#getitemv2itemsidorclassnameget) | **GET** /v2/items/{id_or_class_name} | Get Item
*ItemsApi* | [**getItemsByHeroIdV2ItemsByHeroIdIdGet**](docs/Api/ItemsApi.md#getitemsbyheroidv2itemsbyheroididget) | **GET** /v2/items/by-hero-id/{id} | Get Items By Hero Id
*ItemsApi* | [**getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet**](docs/Api/ItemsApi.md#getitemsbyslottypev2itemsbyslottypeslottypeget) | **GET** /v2/items/by-slot-type/{slot_type} | Get Items By Slot Type
*ItemsApi* | [**getItemsByTypeV2ItemsByTypeTypeGet**](docs/Api/ItemsApi.md#getitemsbytypev2itemsbytypetypeget) | **GET** /v2/items/by-type/{type} | Get Items By Type
*ItemsApi* | [**getItemsV2ItemsGet**](docs/Api/ItemsApi.md#getitemsv2itemsget) | **GET** /v2/items | Get Items
*RawApi* | [**getGenericDataRawGenericDataGet**](docs/Api/RawApi.md#getgenericdatarawgenericdataget) | **GET** /raw/generic_data | Get Generic Data
*RawApi* | [**getRawHeroesRawHeroesGet**](docs/Api/RawApi.md#getrawheroesrawheroesget) | **GET** /raw/heroes | Get Raw Heroes
*RawApi* | [**getRawItemsRawItemsGet**](docs/Api/RawApi.md#getrawitemsrawitemsget) | **GET** /raw/items | Get Raw Items

## Models

- [AbilityDescriptionV2](docs/Model/AbilityDescriptionV2.md)
- [AbilityTooltipDetailsInfoSectionPropertyBlockV2](docs/Model/AbilityTooltipDetailsInfoSectionPropertyBlockV2.md)
- [AbilityTooltipDetailsInfoSectionV2](docs/Model/AbilityTooltipDetailsInfoSectionV2.md)
- [AbilityTooltipDetailsV2](docs/Model/AbilityTooltipDetailsV2.md)
- [AbilityTypeV2](docs/Model/AbilityTypeV2.md)
- [AbilityV2](docs/Model/AbilityV2.md)
- [AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty](docs/Model/AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty.md)
- [AbilityVideosV2](docs/Model/AbilityVideosV2.md)
- [AimingShotSpreadPenalty](docs/Model/AimingShotSpreadPenalty.md)
- [Bonus](docs/Model/Bonus.md)
- [BuildTagV2](docs/Model/BuildTagV2.md)
- [ColorV1](docs/Model/ColorV1.md)
- [GetItemsV2ItemsGet200ResponseInner](docs/Model/GetItemsV2ItemsGet200ResponseInner.md)
- [HTTPValidationError](docs/Model/HTTPValidationError.md)
- [HeroColorsV2](docs/Model/HeroColorsV2.md)
- [HeroDescriptionV2](docs/Model/HeroDescriptionV2.md)
- [HeroImagesV2](docs/Model/HeroImagesV2.md)
- [HeroItemTypeV2](docs/Model/HeroItemTypeV2.md)
- [HeroLevelInfoV2](docs/Model/HeroLevelInfoV2.md)
- [HeroPhysicsV2](docs/Model/HeroPhysicsV2.md)
- [HeroShopStatDisplayV2](docs/Model/HeroShopStatDisplayV2.md)
- [HeroShopWeaponStatsDisplayV2](docs/Model/HeroShopWeaponStatsDisplayV2.md)
- [HeroStartingStatV2](docs/Model/HeroStartingStatV2.md)
- [HeroStartingStatsV2](docs/Model/HeroStartingStatsV2.md)
- [HeroTypeV2](docs/Model/HeroTypeV2.md)
- [HeroV2](docs/Model/HeroV2.md)
- [ItemPropertyV2](docs/Model/ItemPropertyV2.md)
- [ItemSlotTypeV2](docs/Model/ItemSlotTypeV2.md)
- [ItemTierV2](docs/Model/ItemTierV2.md)
- [ItemTypeV2](docs/Model/ItemTypeV2.md)
- [Language](docs/Model/Language.md)
- [MapImagesV1](docs/Model/MapImagesV1.md)
- [MapV1](docs/Model/MapV1.md)
- [ObjectivePositionV1](docs/Model/ObjectivePositionV1.md)
- [ObjectivePositionsV1](docs/Model/ObjectivePositionsV1.md)
- [Range](docs/Model/Range.md)
- [RankImagesV2](docs/Model/RankImagesV2.md)
- [RankV2](docs/Model/RankV2.md)
- [RawAbilityActivationV2](docs/Model/RawAbilityActivationV2.md)
- [RawAbilityImbueV2](docs/Model/RawAbilityImbueV2.md)
- [RawAbilitySectionTypeV2](docs/Model/RawAbilitySectionTypeV2.md)
- [RawAbilityUpgradePropertyUpgradeV2](docs/Model/RawAbilityUpgradePropertyUpgradeV2.md)
- [RawAbilityUpgradeV2](docs/Model/RawAbilityUpgradeV2.md)
- [RawHeroItemSlotInfoValueV2](docs/Model/RawHeroItemSlotInfoValueV2.md)
- [RawHeroMapModCostBonusesV2](docs/Model/RawHeroMapModCostBonusesV2.md)
- [RawHeroPurchaseBonusV2](docs/Model/RawHeroPurchaseBonusV2.md)
- [RawHeroScalingStatV2](docs/Model/RawHeroScalingStatV2.md)
- [RawHeroShopSpiritStatsDisplayV2](docs/Model/RawHeroShopSpiritStatsDisplayV2.md)
- [RawHeroShopVitalityStatsDisplayV2](docs/Model/RawHeroShopVitalityStatsDisplayV2.md)
- [RawHeroStatsDisplayV2](docs/Model/RawHeroStatsDisplayV2.md)
- [RawHeroStatsUIDisplayV2](docs/Model/RawHeroStatsUIDisplayV2.md)
- [RawHeroStatsUIV2](docs/Model/RawHeroStatsUIV2.md)
- [RawItemPropertyScaleFunctionSubclassV2](docs/Model/RawItemPropertyScaleFunctionSubclassV2.md)
- [RawItemWeaponInfoBulletSpeedCurveSplineV2](docs/Model/RawItemWeaponInfoBulletSpeedCurveSplineV2.md)
- [RawItemWeaponInfoBulletSpeedCurveV2](docs/Model/RawItemWeaponInfoBulletSpeedCurveV2.md)
- [RawItemWeaponInfoV2](docs/Model/RawItemWeaponInfoV2.md)
- [RawWeaponInfoHorizontalRecoilV2](docs/Model/RawWeaponInfoHorizontalRecoilV2.md)
- [RawWeaponInfoV2](docs/Model/RawWeaponInfoV2.md)
- [RawWeaponInfoVerticalRecoilV2](docs/Model/RawWeaponInfoVerticalRecoilV2.md)
- [ResponseGetItemV2ItemsIdOrClassNameGet](docs/Model/ResponseGetItemV2ItemsIdOrClassNameGet.md)
- [StandingShotSpreadPenalty](docs/Model/StandingShotSpreadPenalty.md)
- [StatsUsageFlagV2](docs/Model/StatsUsageFlagV2.md)
- [UpgradeDescriptionV2](docs/Model/UpgradeDescriptionV2.md)
- [UpgradePropertyV2](docs/Model/UpgradePropertyV2.md)
- [UpgradeTooltipSectionAttributeV2](docs/Model/UpgradeTooltipSectionAttributeV2.md)
- [UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon](docs/Model/UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon.md)
- [UpgradeTooltipSectionV2](docs/Model/UpgradeTooltipSectionV2.md)
- [UpgradeV2](docs/Model/UpgradeV2.md)
- [UsageFlags](docs/Model/UsageFlags.md)
- [ValidClientVersions](docs/Model/ValidClientVersions.md)
- [ValidationError](docs/Model/ValidationError.md)
- [ValidationErrorLocInner](docs/Model/ValidationErrorLocInner.md)
- [Value](docs/Model/Value.md)
- [Value1](docs/Model/Value1.md)
- [WeaponV2](docs/Model/WeaponV2.md)
- [ZiplanePathV1](docs/Model/ZiplanePathV1.md)

## Authorization
Endpoints do not require authorization.

## Tests

To run the tests, use:

```bash
composer install
vendor/bin/phpunit
```

## Author



## About this package

This PHP package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: `0.1.0`
    - Generator version: `7.5.0`
- Build package: `org.openapitools.codegen.languages.PhpClientCodegen`
