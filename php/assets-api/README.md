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

PHP 8.1 and later.

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
$language = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\Language(); // \OpenAPI\Client\Model\Language
$client_version = new \OpenAPI\Client\Model\\OpenAPI\Client\Model\DeadlockAssetsApiRoutesV1ValidClientVersions(); // \OpenAPI\Client\Model\DeadlockAssetsApiRoutesV1ValidClientVersions

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
- [AbilityTooltipDetailsInfoSectionV2Input](docs/Model/AbilityTooltipDetailsInfoSectionV2Input.md)
- [AbilityTooltipDetailsInfoSectionV2Output](docs/Model/AbilityTooltipDetailsInfoSectionV2Output.md)
- [AbilityTooltipDetailsV2Input](docs/Model/AbilityTooltipDetailsV2Input.md)
- [AbilityTooltipDetailsV2Output](docs/Model/AbilityTooltipDetailsV2Output.md)
- [AbilityTypeV2](docs/Model/AbilityTypeV2.md)
- [AbilityV2Input](docs/Model/AbilityV2Input.md)
- [AbilityV2Output](docs/Model/AbilityV2Output.md)
- [AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty](docs/Model/AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty.md)
- [AbilityVideosV2](docs/Model/AbilityVideosV2.md)
- [AimingShotSpreadPenalty](docs/Model/AimingShotSpreadPenalty.md)
- [Bonus](docs/Model/Bonus.md)
- [BuildTagV2Input](docs/Model/BuildTagV2Input.md)
- [BuildTagV2Output](docs/Model/BuildTagV2Output.md)
- [ColorV1](docs/Model/ColorV1.md)
- [DeadlockAssetsApiRoutesV1ValidClientVersions](docs/Model/DeadlockAssetsApiRoutesV1ValidClientVersions.md)
- [GetItemsV2ItemsGet200ResponseInner](docs/Model/GetItemsV2ItemsGet200ResponseInner.md)
- [HTTPValidationError](docs/Model/HTTPValidationError.md)
- [HeroColorsV2](docs/Model/HeroColorsV2.md)
- [HeroDescriptionV2](docs/Model/HeroDescriptionV2.md)
- [HeroImagesV2](docs/Model/HeroImagesV2.md)
- [HeroItemTypeV2](docs/Model/HeroItemTypeV2.md)
- [HeroLevelInfoV2Input](docs/Model/HeroLevelInfoV2Input.md)
- [HeroLevelInfoV2Output](docs/Model/HeroLevelInfoV2Output.md)
- [HeroPhysicsV2](docs/Model/HeroPhysicsV2.md)
- [HeroShopStatDisplayV2Input](docs/Model/HeroShopStatDisplayV2Input.md)
- [HeroShopStatDisplayV2Output](docs/Model/HeroShopStatDisplayV2Output.md)
- [HeroShopWeaponStatsDisplayV2Input](docs/Model/HeroShopWeaponStatsDisplayV2Input.md)
- [HeroShopWeaponStatsDisplayV2Output](docs/Model/HeroShopWeaponStatsDisplayV2Output.md)
- [HeroStartingStatV2](docs/Model/HeroStartingStatV2.md)
- [HeroStartingStatsV2](docs/Model/HeroStartingStatsV2.md)
- [HeroTypeV2](docs/Model/HeroTypeV2.md)
- [HeroV2](docs/Model/HeroV2.md)
- [ItemPropertyV2Input](docs/Model/ItemPropertyV2Input.md)
- [ItemPropertyV2Output](docs/Model/ItemPropertyV2Output.md)
- [ItemSlotTypeV2](docs/Model/ItemSlotTypeV2.md)
- [ItemTierV2](docs/Model/ItemTierV2.md)
- [ItemTypeV2](docs/Model/ItemTypeV2.md)
- [Language](docs/Model/Language.md)
- [MAimingshootspreadpenalty](docs/Model/MAimingshootspreadpenalty.md)
- [MEstatsusageflags](docs/Model/MEstatsusageflags.md)
- [MRange](docs/Model/MRange.md)
- [MStandingshootspreadpenalty](docs/Model/MStandingshootspreadpenalty.md)
- [MStrbonus](docs/Model/MStrbonus.md)
- [MStrvalue](docs/Model/MStrvalue.md)
- [MapImagesV1](docs/Model/MapImagesV1.md)
- [MapV1](docs/Model/MapV1.md)
- [ObjectivePositionV1](docs/Model/ObjectivePositionV1.md)
- [ObjectivePositionsV1](docs/Model/ObjectivePositionsV1.md)
- [Range](docs/Model/Range.md)
- [RankImagesV2](docs/Model/RankImagesV2.md)
- [RankV2Input](docs/Model/RankV2Input.md)
- [RankV2Output](docs/Model/RankV2Output.md)
- [RawAbilityActivationV2](docs/Model/RawAbilityActivationV2.md)
- [RawAbilityImbueV2](docs/Model/RawAbilityImbueV2.md)
- [RawAbilitySectionTypeV2](docs/Model/RawAbilitySectionTypeV2.md)
- [RawAbilityUpgradePropertyUpgradeV2Input](docs/Model/RawAbilityUpgradePropertyUpgradeV2Input.md)
- [RawAbilityUpgradePropertyUpgradeV2Output](docs/Model/RawAbilityUpgradePropertyUpgradeV2Output.md)
- [RawAbilityUpgradeV2Input](docs/Model/RawAbilityUpgradeV2Input.md)
- [RawAbilityUpgradeV2Output](docs/Model/RawAbilityUpgradeV2Output.md)
- [RawHeroItemSlotInfoValueV2Input](docs/Model/RawHeroItemSlotInfoValueV2Input.md)
- [RawHeroItemSlotInfoValueV2Output](docs/Model/RawHeroItemSlotInfoValueV2Output.md)
- [RawHeroMapModCostBonusesV2Input](docs/Model/RawHeroMapModCostBonusesV2Input.md)
- [RawHeroMapModCostBonusesV2Output](docs/Model/RawHeroMapModCostBonusesV2Output.md)
- [RawHeroPurchaseBonusV2Input](docs/Model/RawHeroPurchaseBonusV2Input.md)
- [RawHeroPurchaseBonusV2Output](docs/Model/RawHeroPurchaseBonusV2Output.md)
- [RawHeroScalingStatV2Input](docs/Model/RawHeroScalingStatV2Input.md)
- [RawHeroScalingStatV2Output](docs/Model/RawHeroScalingStatV2Output.md)
- [RawHeroShopSpiritStatsDisplayV2Input](docs/Model/RawHeroShopSpiritStatsDisplayV2Input.md)
- [RawHeroShopSpiritStatsDisplayV2Output](docs/Model/RawHeroShopSpiritStatsDisplayV2Output.md)
- [RawHeroShopVitalityStatsDisplayV2Input](docs/Model/RawHeroShopVitalityStatsDisplayV2Input.md)
- [RawHeroShopVitalityStatsDisplayV2Output](docs/Model/RawHeroShopVitalityStatsDisplayV2Output.md)
- [RawHeroStatsDisplayV2Input](docs/Model/RawHeroStatsDisplayV2Input.md)
- [RawHeroStatsDisplayV2Output](docs/Model/RawHeroStatsDisplayV2Output.md)
- [RawHeroStatsUIDisplayV2Input](docs/Model/RawHeroStatsUIDisplayV2Input.md)
- [RawHeroStatsUIDisplayV2Output](docs/Model/RawHeroStatsUIDisplayV2Output.md)
- [RawHeroStatsUIV2Input](docs/Model/RawHeroStatsUIV2Input.md)
- [RawHeroStatsUIV2Output](docs/Model/RawHeroStatsUIV2Output.md)
- [RawItemPropertyScaleFunctionSubclassV2Input](docs/Model/RawItemPropertyScaleFunctionSubclassV2Input.md)
- [RawItemPropertyScaleFunctionSubclassV2Output](docs/Model/RawItemPropertyScaleFunctionSubclassV2Output.md)
- [RawItemWeaponInfoBulletSpeedCurveSplineV2Input](docs/Model/RawItemWeaponInfoBulletSpeedCurveSplineV2Input.md)
- [RawItemWeaponInfoBulletSpeedCurveSplineV2Output](docs/Model/RawItemWeaponInfoBulletSpeedCurveSplineV2Output.md)
- [RawItemWeaponInfoBulletSpeedCurveV2Input](docs/Model/RawItemWeaponInfoBulletSpeedCurveV2Input.md)
- [RawItemWeaponInfoBulletSpeedCurveV2Output](docs/Model/RawItemWeaponInfoBulletSpeedCurveV2Output.md)
- [RawItemWeaponInfoV2Input](docs/Model/RawItemWeaponInfoV2Input.md)
- [RawItemWeaponInfoV2Output](docs/Model/RawItemWeaponInfoV2Output.md)
- [RawWeaponInfoHorizontalRecoilV2Input](docs/Model/RawWeaponInfoHorizontalRecoilV2Input.md)
- [RawWeaponInfoHorizontalRecoilV2Output](docs/Model/RawWeaponInfoHorizontalRecoilV2Output.md)
- [RawWeaponInfoV2Input](docs/Model/RawWeaponInfoV2Input.md)
- [RawWeaponInfoV2Output](docs/Model/RawWeaponInfoV2Output.md)
- [RawWeaponInfoVerticalRecoilV2Input](docs/Model/RawWeaponInfoVerticalRecoilV2Input.md)
- [RawWeaponInfoVerticalRecoilV2Output](docs/Model/RawWeaponInfoVerticalRecoilV2Output.md)
- [ResponseGetItemV2ItemsIdOrClassNameGet](docs/Model/ResponseGetItemV2ItemsIdOrClassNameGet.md)
- [StandingShotSpreadPenalty](docs/Model/StandingShotSpreadPenalty.md)
- [StatsUsageFlagV2](docs/Model/StatsUsageFlagV2.md)
- [UpgradeDescriptionV2](docs/Model/UpgradeDescriptionV2.md)
- [UpgradePropertyV2Input](docs/Model/UpgradePropertyV2Input.md)
- [UpgradePropertyV2Output](docs/Model/UpgradePropertyV2Output.md)
- [UpgradeTooltipSectionAttributeV2](docs/Model/UpgradeTooltipSectionAttributeV2.md)
- [UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon](docs/Model/UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon.md)
- [UpgradeTooltipSectionV2Input](docs/Model/UpgradeTooltipSectionV2Input.md)
- [UpgradeTooltipSectionV2Output](docs/Model/UpgradeTooltipSectionV2Output.md)
- [UpgradeV2Input](docs/Model/UpgradeV2Input.md)
- [UpgradeV2Output](docs/Model/UpgradeV2Output.md)
- [UsageFlags](docs/Model/UsageFlags.md)
- [ValidationError](docs/Model/ValidationError.md)
- [ValidationErrorLocInner](docs/Model/ValidationErrorLocInner.md)
- [Value](docs/Model/Value.md)
- [Value1](docs/Model/Value1.md)
- [WeaponV2Input](docs/Model/WeaponV2Input.md)
- [WeaponV2Output](docs/Model/WeaponV2Output.md)
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
    - Generator version: `7.17.0`
- Build package: `org.openapitools.codegen.languages.PhpClientCodegen`
