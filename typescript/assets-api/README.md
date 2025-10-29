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
 - [AbilityTooltipDetailsInfoSectionV2Input](docs/AbilityTooltipDetailsInfoSectionV2Input.md)
 - [AbilityTooltipDetailsInfoSectionV2Output](docs/AbilityTooltipDetailsInfoSectionV2Output.md)
 - [AbilityTooltipDetailsV2Input](docs/AbilityTooltipDetailsV2Input.md)
 - [AbilityTooltipDetailsV2Output](docs/AbilityTooltipDetailsV2Output.md)
 - [AbilityTypeV2](docs/AbilityTypeV2.md)
 - [AbilityV2Input](docs/AbilityV2Input.md)
 - [AbilityV2Output](docs/AbilityV2Output.md)
 - [AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty](docs/AbilityV2TooltipDetailsInfoSectionPropertyBlockProperty.md)
 - [AbilityVideosV2](docs/AbilityVideosV2.md)
 - [AimingShotSpreadPenalty](docs/AimingShotSpreadPenalty.md)
 - [Bonus](docs/Bonus.md)
 - [BuildTagV2Input](docs/BuildTagV2Input.md)
 - [BuildTagV2Output](docs/BuildTagV2Output.md)
 - [ColorV1](docs/ColorV1.md)
 - [DeadlockAssetsApiRoutesV1ValidClientVersions](docs/DeadlockAssetsApiRoutesV1ValidClientVersions.md)
 - [GetItemsV2ItemsGet200ResponseInner](docs/GetItemsV2ItemsGet200ResponseInner.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [HeroColorsV2](docs/HeroColorsV2.md)
 - [HeroDescriptionV2](docs/HeroDescriptionV2.md)
 - [HeroImagesV2](docs/HeroImagesV2.md)
 - [HeroItemTypeV2](docs/HeroItemTypeV2.md)
 - [HeroLevelInfoV2Input](docs/HeroLevelInfoV2Input.md)
 - [HeroLevelInfoV2Output](docs/HeroLevelInfoV2Output.md)
 - [HeroPhysicsV2](docs/HeroPhysicsV2.md)
 - [HeroShopStatDisplayV2Input](docs/HeroShopStatDisplayV2Input.md)
 - [HeroShopStatDisplayV2Output](docs/HeroShopStatDisplayV2Output.md)
 - [HeroShopWeaponStatsDisplayV2Input](docs/HeroShopWeaponStatsDisplayV2Input.md)
 - [HeroShopWeaponStatsDisplayV2Output](docs/HeroShopWeaponStatsDisplayV2Output.md)
 - [HeroStartingStatV2](docs/HeroStartingStatV2.md)
 - [HeroStartingStatsV2](docs/HeroStartingStatsV2.md)
 - [HeroTypeV2](docs/HeroTypeV2.md)
 - [HeroV2](docs/HeroV2.md)
 - [ItemPropertyV2Input](docs/ItemPropertyV2Input.md)
 - [ItemPropertyV2Output](docs/ItemPropertyV2Output.md)
 - [ItemSlotTypeV2](docs/ItemSlotTypeV2.md)
 - [ItemTierV2](docs/ItemTierV2.md)
 - [ItemTypeV2](docs/ItemTypeV2.md)
 - [Language](docs/Language.md)
 - [MAimingshootspreadpenalty](docs/MAimingshootspreadpenalty.md)
 - [MEstatsusageflags](docs/MEstatsusageflags.md)
 - [MRange](docs/MRange.md)
 - [MStandingshootspreadpenalty](docs/MStandingshootspreadpenalty.md)
 - [MStrbonus](docs/MStrbonus.md)
 - [MStrvalue](docs/MStrvalue.md)
 - [MapImagesV1](docs/MapImagesV1.md)
 - [MapV1](docs/MapV1.md)
 - [ObjectivePositionV1](docs/ObjectivePositionV1.md)
 - [ObjectivePositionsV1](docs/ObjectivePositionsV1.md)
 - [Range](docs/Range.md)
 - [RankImagesV2](docs/RankImagesV2.md)
 - [RankV2Input](docs/RankV2Input.md)
 - [RankV2Output](docs/RankV2Output.md)
 - [RawAbilityActivationV2](docs/RawAbilityActivationV2.md)
 - [RawAbilityImbueV2](docs/RawAbilityImbueV2.md)
 - [RawAbilitySectionTypeV2](docs/RawAbilitySectionTypeV2.md)
 - [RawAbilityUpgradePropertyUpgradeV2Input](docs/RawAbilityUpgradePropertyUpgradeV2Input.md)
 - [RawAbilityUpgradePropertyUpgradeV2Output](docs/RawAbilityUpgradePropertyUpgradeV2Output.md)
 - [RawAbilityUpgradeV2Input](docs/RawAbilityUpgradeV2Input.md)
 - [RawAbilityUpgradeV2Output](docs/RawAbilityUpgradeV2Output.md)
 - [RawHeroItemSlotInfoValueV2Input](docs/RawHeroItemSlotInfoValueV2Input.md)
 - [RawHeroItemSlotInfoValueV2Output](docs/RawHeroItemSlotInfoValueV2Output.md)
 - [RawHeroMapModCostBonusesV2Input](docs/RawHeroMapModCostBonusesV2Input.md)
 - [RawHeroMapModCostBonusesV2Output](docs/RawHeroMapModCostBonusesV2Output.md)
 - [RawHeroPurchaseBonusV2Input](docs/RawHeroPurchaseBonusV2Input.md)
 - [RawHeroPurchaseBonusV2Output](docs/RawHeroPurchaseBonusV2Output.md)
 - [RawHeroScalingStatV2Input](docs/RawHeroScalingStatV2Input.md)
 - [RawHeroScalingStatV2Output](docs/RawHeroScalingStatV2Output.md)
 - [RawHeroShopSpiritStatsDisplayV2Input](docs/RawHeroShopSpiritStatsDisplayV2Input.md)
 - [RawHeroShopSpiritStatsDisplayV2Output](docs/RawHeroShopSpiritStatsDisplayV2Output.md)
 - [RawHeroShopVitalityStatsDisplayV2Input](docs/RawHeroShopVitalityStatsDisplayV2Input.md)
 - [RawHeroShopVitalityStatsDisplayV2Output](docs/RawHeroShopVitalityStatsDisplayV2Output.md)
 - [RawHeroStatsDisplayV2Input](docs/RawHeroStatsDisplayV2Input.md)
 - [RawHeroStatsDisplayV2Output](docs/RawHeroStatsDisplayV2Output.md)
 - [RawHeroStatsUIDisplayV2Input](docs/RawHeroStatsUIDisplayV2Input.md)
 - [RawHeroStatsUIDisplayV2Output](docs/RawHeroStatsUIDisplayV2Output.md)
 - [RawHeroStatsUIV2Input](docs/RawHeroStatsUIV2Input.md)
 - [RawHeroStatsUIV2Output](docs/RawHeroStatsUIV2Output.md)
 - [RawItemPropertyScaleFunctionSubclassV2Input](docs/RawItemPropertyScaleFunctionSubclassV2Input.md)
 - [RawItemPropertyScaleFunctionSubclassV2Output](docs/RawItemPropertyScaleFunctionSubclassV2Output.md)
 - [RawItemWeaponInfoBulletSpeedCurveSplineV2Input](docs/RawItemWeaponInfoBulletSpeedCurveSplineV2Input.md)
 - [RawItemWeaponInfoBulletSpeedCurveSplineV2Output](docs/RawItemWeaponInfoBulletSpeedCurveSplineV2Output.md)
 - [RawItemWeaponInfoBulletSpeedCurveV2Input](docs/RawItemWeaponInfoBulletSpeedCurveV2Input.md)
 - [RawItemWeaponInfoBulletSpeedCurveV2Output](docs/RawItemWeaponInfoBulletSpeedCurveV2Output.md)
 - [RawItemWeaponInfoV2Input](docs/RawItemWeaponInfoV2Input.md)
 - [RawItemWeaponInfoV2Output](docs/RawItemWeaponInfoV2Output.md)
 - [RawWeaponInfoHorizontalRecoilV2Input](docs/RawWeaponInfoHorizontalRecoilV2Input.md)
 - [RawWeaponInfoHorizontalRecoilV2Output](docs/RawWeaponInfoHorizontalRecoilV2Output.md)
 - [RawWeaponInfoV2Input](docs/RawWeaponInfoV2Input.md)
 - [RawWeaponInfoV2Output](docs/RawWeaponInfoV2Output.md)
 - [RawWeaponInfoVerticalRecoilV2Input](docs/RawWeaponInfoVerticalRecoilV2Input.md)
 - [RawWeaponInfoVerticalRecoilV2Output](docs/RawWeaponInfoVerticalRecoilV2Output.md)
 - [ResponseGetItemV2ItemsIdOrClassNameGet](docs/ResponseGetItemV2ItemsIdOrClassNameGet.md)
 - [StandingShotSpreadPenalty](docs/StandingShotSpreadPenalty.md)
 - [StatsUsageFlagV2](docs/StatsUsageFlagV2.md)
 - [UpgradeDescriptionV2](docs/UpgradeDescriptionV2.md)
 - [UpgradePropertyV2Input](docs/UpgradePropertyV2Input.md)
 - [UpgradePropertyV2Output](docs/UpgradePropertyV2Output.md)
 - [UpgradeTooltipSectionAttributeV2](docs/UpgradeTooltipSectionAttributeV2.md)
 - [UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon](docs/UpgradeTooltipSectionAttributeV2ImportantPropertyWithIcon.md)
 - [UpgradeTooltipSectionV2Input](docs/UpgradeTooltipSectionV2Input.md)
 - [UpgradeTooltipSectionV2Output](docs/UpgradeTooltipSectionV2Output.md)
 - [UpgradeV2Input](docs/UpgradeV2Input.md)
 - [UpgradeV2Output](docs/UpgradeV2Output.md)
 - [UsageFlags](docs/UsageFlags.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)
 - [Value](docs/Value.md)
 - [Value1](docs/Value1.md)
 - [WeaponV2Input](docs/WeaponV2Input.md)
 - [WeaponV2Output](docs/WeaponV2Output.md)
 - [ZiplanePathV1](docs/ZiplanePathV1.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.

