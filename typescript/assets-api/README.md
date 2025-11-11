## assets-deadlock-api-client@0.1.0

This generator creates TypeScript/JavaScript client that utilizes [axios](https://github.com/axios/axios). The generated Node module can be used in the following environments:

Environment
* Node.js
* Webpack
* Browserify

Language level
* ES5 - you must have a Promises/A+ library installed
* ES6

Module system
* CommonJS
* ES6 module system

It can be used in both TypeScript and JavaScript. In TypeScript, the definition will be automatically resolved via `package.json`. ([Reference](https://www.typescriptlang.org/docs/handbook/declaration-files/consumption.html))

### Building

To build and compile the typescript sources to javascript use:
```
npm install
npm run build
```

### Publishing

First build the package then run `npm publish`

### Consuming

navigate to the folder of your consuming project and run one of the following commands.

_published:_

```
npm install assets-deadlock-api-client@0.1.0 --save
```

_unPublished (not recommended):_

```
npm install PATH_TO_GENERATED_PACKAGE --save
```

### Documentation for API Endpoints

All URIs are relative to *https://assets.deadlock-api.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**getBuildTagsV2BuildTagsGet**](docs/DefaultApi.md#getbuildtagsv2buildtagsget) | **GET** /v2/build-tags | Get Build Tags
*DefaultApi* | [**getClientVersionsV2ClientVersionsGet**](docs/DefaultApi.md#getclientversionsv2clientversionsget) | **GET** /v2/client-versions | Get Client Versions
*DefaultApi* | [**getColorsV1ColorsGet**](docs/DefaultApi.md#getcolorsv1colorsget) | **GET** /v1/colors | Get Colors
*DefaultApi* | [**getIconsV1IconsGet**](docs/DefaultApi.md#geticonsv1iconsget) | **GET** /v1/icons | Get Icons
*DefaultApi* | [**getMapV1MapGet**](docs/DefaultApi.md#getmapv1mapget) | **GET** /v1/map | Get Map
*DefaultApi* | [**getRanksV2RanksGet**](docs/DefaultApi.md#getranksv2ranksget) | **GET** /v2/ranks | Get Ranks
*DefaultApi* | [**getSoundsV1SoundsGet**](docs/DefaultApi.md#getsoundsv1soundsget) | **GET** /v1/sounds | Get Sounds
*DefaultApi* | [**getSteamInfoV1SteamInfoGet**](docs/DefaultApi.md#getsteaminfov1steaminfoget) | **GET** /v1/steam-info | Get Steam Info
*HeroesApi* | [**getHeroByNameV2HeroesByNameNameGet**](docs/HeroesApi.md#getherobynamev2heroesbynamenameget) | **GET** /v2/heroes/by-name/{name} | Get Hero By Name
*HeroesApi* | [**getHeroV2HeroesIdGet**](docs/HeroesApi.md#getherov2heroesidget) | **GET** /v2/heroes/{id} | Get Hero
*HeroesApi* | [**getHeroesV2HeroesGet**](docs/HeroesApi.md#getheroesv2heroesget) | **GET** /v2/heroes | Get Heroes
*ItemsApi* | [**getItemV2ItemsIdOrClassNameGet**](docs/ItemsApi.md#getitemv2itemsidorclassnameget) | **GET** /v2/items/{id_or_class_name} | Get Item
*ItemsApi* | [**getItemsByHeroIdV2ItemsByHeroIdIdGet**](docs/ItemsApi.md#getitemsbyheroidv2itemsbyheroididget) | **GET** /v2/items/by-hero-id/{id} | Get Items By Hero Id
*ItemsApi* | [**getItemsBySlotTypeV2ItemsBySlotTypeSlotTypeGet**](docs/ItemsApi.md#getitemsbyslottypev2itemsbyslottypeslottypeget) | **GET** /v2/items/by-slot-type/{slot_type} | Get Items By Slot Type
*ItemsApi* | [**getItemsByTypeV2ItemsByTypeTypeGet**](docs/ItemsApi.md#getitemsbytypev2itemsbytypetypeget) | **GET** /v2/items/by-type/{type} | Get Items By Type
*ItemsApi* | [**getItemsV2ItemsGet**](docs/ItemsApi.md#getitemsv2itemsget) | **GET** /v2/items | Get Items
*RawApi* | [**getGenericDataRawGenericDataGet**](docs/RawApi.md#getgenericdatarawgenericdataget) | **GET** /raw/generic_data | Get Generic Data
*RawApi* | [**getRawHeroesRawHeroesGet**](docs/RawApi.md#getrawheroesrawheroesget) | **GET** /raw/heroes | Get Raw Heroes
*RawApi* | [**getRawItemsRawItemsGet**](docs/RawApi.md#getrawitemsrawitemsget) | **GET** /raw/items | Get Raw Items


### Documentation For Models

 - [AbilityDescriptionV2](docs/AbilityDescriptionV2.md)
 - [AbilityTooltipDetailsInfoSectionPropertyBlockV2](docs/AbilityTooltipDetailsInfoSectionPropertyBlockV2.md)
 - [AbilityTooltipDetailsInfoSectionV2](docs/AbilityTooltipDetailsInfoSectionV2.md)
 - [AbilityTooltipDetailsV2](docs/AbilityTooltipDetailsV2.md)
 - [AbilityTypeV2](docs/AbilityTypeV2.md)
 - [AbilityV2](docs/AbilityV2.md)
 - [AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty](docs/AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty.md)
 - [AbilityVideosV2](docs/AbilityVideosV2.md)
 - [AimingShotSpreadPenalty](docs/AimingShotSpreadPenalty.md)
 - [Bonus](docs/Bonus.md)
 - [BuildTagV2](docs/BuildTagV2.md)
 - [ColorV1](docs/ColorV1.md)
 - [DeadlockAssetsApiRoutesRawValidClientVersions](docs/DeadlockAssetsApiRoutesRawValidClientVersions.md)
 - [GetItemsV2ItemsGet200ResponseInner](docs/GetItemsV2ItemsGet200ResponseInner.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [HeroColorsV2](docs/HeroColorsV2.md)
 - [HeroDescriptionV2](docs/HeroDescriptionV2.md)
 - [HeroImagesV2](docs/HeroImagesV2.md)
 - [HeroItemTypeV2](docs/HeroItemTypeV2.md)
 - [HeroLevelInfoV2](docs/HeroLevelInfoV2.md)
 - [HeroPhysicsV2](docs/HeroPhysicsV2.md)
 - [HeroShopStatDisplayV2](docs/HeroShopStatDisplayV2.md)
 - [HeroShopWeaponStatsDisplayV2](docs/HeroShopWeaponStatsDisplayV2.md)
 - [HeroStartingStatV2](docs/HeroStartingStatV2.md)
 - [HeroStartingStatsV2](docs/HeroStartingStatsV2.md)
 - [HeroTypeV2](docs/HeroTypeV2.md)
 - [HeroV2](docs/HeroV2.md)
 - [ItemPropertyV2](docs/ItemPropertyV2.md)
 - [ItemSlotTypeV2](docs/ItemSlotTypeV2.md)
 - [ItemTierV2](docs/ItemTierV2.md)
 - [ItemTypeV2](docs/ItemTypeV2.md)
 - [Language](docs/Language.md)
 - [MapImagesV1](docs/MapImagesV1.md)
 - [MapV1](docs/MapV1.md)
 - [ObjectivePositionV1](docs/ObjectivePositionV1.md)
 - [ObjectivePositionsV1](docs/ObjectivePositionsV1.md)
 - [Range](docs/Range.md)
 - [RankImagesV2](docs/RankImagesV2.md)
 - [RankV2](docs/RankV2.md)
 - [RawAbilityActivationV2](docs/RawAbilityActivationV2.md)
 - [RawAbilityImbueV2](docs/RawAbilityImbueV2.md)
 - [RawAbilitySectionTypeV2](docs/RawAbilitySectionTypeV2.md)
 - [RawAbilityUpgradePropertyUpgradeV2](docs/RawAbilityUpgradePropertyUpgradeV2.md)
 - [RawAbilityUpgradeV2](docs/RawAbilityUpgradeV2.md)
 - [RawHeroItemSlotInfoValueV2](docs/RawHeroItemSlotInfoValueV2.md)
 - [RawHeroMapModCostBonusesV2](docs/RawHeroMapModCostBonusesV2.md)
 - [RawHeroPurchaseBonusV2](docs/RawHeroPurchaseBonusV2.md)
 - [RawHeroScalingStatV2](docs/RawHeroScalingStatV2.md)
 - [RawHeroShopSpiritStatsDisplayV2](docs/RawHeroShopSpiritStatsDisplayV2.md)
 - [RawHeroShopVitalityStatsDisplayV2](docs/RawHeroShopVitalityStatsDisplayV2.md)
 - [RawHeroStatsDisplayV2](docs/RawHeroStatsDisplayV2.md)
 - [RawHeroStatsUIDisplayV2](docs/RawHeroStatsUIDisplayV2.md)
 - [RawHeroStatsUIV2](docs/RawHeroStatsUIV2.md)
 - [RawItemPropertyScaleFunctionSubclassV2](docs/RawItemPropertyScaleFunctionSubclassV2.md)
 - [RawItemWeaponInfoBulletSpeedCurveSplineV2](docs/RawItemWeaponInfoBulletSpeedCurveSplineV2.md)
 - [RawItemWeaponInfoBulletSpeedCurveV2](docs/RawItemWeaponInfoBulletSpeedCurveV2.md)
 - [RawItemWeaponInfoV2](docs/RawItemWeaponInfoV2.md)
 - [RawWeaponInfoHorizontalRecoilV2](docs/RawWeaponInfoHorizontalRecoilV2.md)
 - [RawWeaponInfoV2](docs/RawWeaponInfoV2.md)
 - [RawWeaponInfoVerticalRecoilV2](docs/RawWeaponInfoVerticalRecoilV2.md)
 - [ResponseGetItemV2ItemsIdOrClassNameGet](docs/ResponseGetItemV2ItemsIdOrClassNameGet.md)
 - [StandingShotSpreadPenalty](docs/StandingShotSpreadPenalty.md)
 - [StatsUsageFlagV2](docs/StatsUsageFlagV2.md)
 - [UpgradeDescriptionV2](docs/UpgradeDescriptionV2.md)
 - [UpgradePropertyV2](docs/UpgradePropertyV2.md)
 - [UpgradeTooltipSectionAttributeV2](docs/UpgradeTooltipSectionAttributeV2.md)
 - [UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon](docs/UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon.md)
 - [UpgradeTooltipSectionV2](docs/UpgradeTooltipSectionV2.md)
 - [UpgradeV2](docs/UpgradeV2.md)
 - [UsageFlags](docs/UsageFlags.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)
 - [Value](docs/Value.md)
 - [Value1](docs/Value1.md)
 - [WeaponV2](docs/WeaponV2.md)
 - [ZiplanePathV1](docs/ZiplanePathV1.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.

