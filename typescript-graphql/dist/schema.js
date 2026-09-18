// @ts-nocheck
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
const Ability_possibleTypes = ['Ability'];
export const isAbility = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isAbility"');
    return Ability_possibleTypes.includes(obj.__typename);
};
const AbilityDescription_possibleTypes = ['AbilityDescription'];
export const isAbilityDescription = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isAbilityDescription"');
    return AbilityDescription_possibleTypes.includes(obj.__typename);
};
const AbilityVideos_possibleTypes = ['AbilityVideos'];
export const isAbilityVideos = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isAbilityVideos"');
    return AbilityVideos_possibleTypes.includes(obj.__typename);
};
const AssetItem_possibleTypes = ['Ability', 'Weapon', 'Upgrade'];
export const isAssetItem = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isAssetItem"');
    return AssetItem_possibleTypes.includes(obj.__typename);
};
const Build_possibleTypes = ['Build'];
export const isBuild = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isBuild"');
    return Build_possibleTypes.includes(obj.__typename);
};
const BuildHero_possibleTypes = ['BuildHero'];
export const isBuildHero = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isBuildHero"');
    return BuildHero_possibleTypes.includes(obj.__typename);
};
const BuildHeroDetails_possibleTypes = ['BuildHeroDetails'];
export const isBuildHeroDetails = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isBuildHeroDetails"');
    return BuildHeroDetails_possibleTypes.includes(obj.__typename);
};
const BuildHeroDetailsAbilityOrder_possibleTypes = ['BuildHeroDetailsAbilityOrder'];
export const isBuildHeroDetailsAbilityOrder = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isBuildHeroDetailsAbilityOrder"');
    return BuildHeroDetailsAbilityOrder_possibleTypes.includes(obj.__typename);
};
const BuildHeroDetailsAbilityOrderCurrencyChange_possibleTypes = ['BuildHeroDetailsAbilityOrderCurrencyChange'];
export const isBuildHeroDetailsAbilityOrderCurrencyChange = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isBuildHeroDetailsAbilityOrderCurrencyChange"');
    return BuildHeroDetailsAbilityOrderCurrencyChange_possibleTypes.includes(obj.__typename);
};
const BuildHeroDetailsCategory_possibleTypes = ['BuildHeroDetailsCategory'];
export const isBuildHeroDetailsCategory = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isBuildHeroDetailsCategory"');
    return BuildHeroDetailsCategory_possibleTypes.includes(obj.__typename);
};
const BuildHeroDetailsCategoryAbility_possibleTypes = ['BuildHeroDetailsCategoryAbility'];
export const isBuildHeroDetailsCategoryAbility = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isBuildHeroDetailsCategoryAbility"');
    return BuildHeroDetailsCategoryAbility_possibleTypes.includes(obj.__typename);
};
const Hero_possibleTypes = ['Hero'];
export const isHero = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isHero"');
    return Hero_possibleTypes.includes(obj.__typename);
};
const HeroDescription_possibleTypes = ['HeroDescription'];
export const isHeroDescription = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isHeroDescription"');
    return HeroDescription_possibleTypes.includes(obj.__typename);
};
const HeroImages_possibleTypes = ['HeroImages'];
export const isHeroImages = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isHeroImages"');
    return HeroImages_possibleTypes.includes(obj.__typename);
};
const HeroPhysics_possibleTypes = ['HeroPhysics'];
export const isHeroPhysics = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isHeroPhysics"');
    return HeroPhysics_possibleTypes.includes(obj.__typename);
};
const HeroStatsUI_possibleTypes = ['HeroStatsUI'];
export const isHeroStatsUI = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isHeroStatsUI"');
    return HeroStatsUI_possibleTypes.includes(obj.__typename);
};
const HeroStatsUIDisplay_possibleTypes = ['HeroStatsUIDisplay'];
export const isHeroStatsUIDisplay = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isHeroStatsUIDisplay"');
    return HeroStatsUIDisplay_possibleTypes.includes(obj.__typename);
};
const Item_possibleTypes = ['Item'];
export const isItem = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isItem"');
    return Item_possibleTypes.includes(obj.__typename);
};
const Match_possibleTypes = ['Match'];
export const isMatch = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isMatch"');
    return Match_possibleTypes.includes(obj.__typename);
};
const MatchHistoryEntry_possibleTypes = ['MatchHistoryEntry'];
export const isMatchHistoryEntry = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isMatchHistoryEntry"');
    return MatchHistoryEntry_possibleTypes.includes(obj.__typename);
};
const MatchPlayer_possibleTypes = ['MatchPlayer'];
export const isMatchPlayer = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isMatchPlayer"');
    return MatchPlayer_possibleTypes.includes(obj.__typename);
};
const QueryRoot_possibleTypes = ['QueryRoot'];
export const isQueryRoot = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isQueryRoot"');
    return QueryRoot_possibleTypes.includes(obj.__typename);
};
const Rank_possibleTypes = ['Rank'];
export const isRank = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isRank"');
    return Rank_possibleTypes.includes(obj.__typename);
};
const RankImages_possibleTypes = ['RankImages'];
export const isRankImages = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isRankImages"');
    return RankImages_possibleTypes.includes(obj.__typename);
};
const ShopSpiritStatsDisplay_possibleTypes = ['ShopSpiritStatsDisplay'];
export const isShopSpiritStatsDisplay = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isShopSpiritStatsDisplay"');
    return ShopSpiritStatsDisplay_possibleTypes.includes(obj.__typename);
};
const ShopStatDisplay_possibleTypes = ['ShopStatDisplay'];
export const isShopStatDisplay = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isShopStatDisplay"');
    return ShopStatDisplay_possibleTypes.includes(obj.__typename);
};
const ShopVitalityStatsDisplay_possibleTypes = ['ShopVitalityStatsDisplay'];
export const isShopVitalityStatsDisplay = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isShopVitalityStatsDisplay"');
    return ShopVitalityStatsDisplay_possibleTypes.includes(obj.__typename);
};
const ShopWeaponStatsDisplay_possibleTypes = ['ShopWeaponStatsDisplay'];
export const isShopWeaponStatsDisplay = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isShopWeaponStatsDisplay"');
    return ShopWeaponStatsDisplay_possibleTypes.includes(obj.__typename);
};
const Stat_possibleTypes = ['Stat'];
export const isStat = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isStat"');
    return Stat_possibleTypes.includes(obj.__typename);
};
const StatsDisplay_possibleTypes = ['StatsDisplay'];
export const isStatsDisplay = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isStatsDisplay"');
    return StatsDisplay_possibleTypes.includes(obj.__typename);
};
const SteamProfile_possibleTypes = ['SteamProfile'];
export const isSteamProfile = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isSteamProfile"');
    return SteamProfile_possibleTypes.includes(obj.__typename);
};
const Upgrade_possibleTypes = ['Upgrade'];
export const isUpgrade = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isUpgrade"');
    return Upgrade_possibleTypes.includes(obj.__typename);
};
const UpgradeDescription_possibleTypes = ['UpgradeDescription'];
export const isUpgradeDescription = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isUpgradeDescription"');
    return UpgradeDescription_possibleTypes.includes(obj.__typename);
};
const Weapon_possibleTypes = ['Weapon'];
export const isWeapon = (obj) => {
    if (!obj?.__typename)
        throw new Error('__typename is missing in "isWeapon"');
    return Weapon_possibleTypes.includes(obj.__typename);
};
export const enumAbilityActivation = {
    HOLD_TOGGLE: 'HOLD_TOGGLE',
    INSTANT_CAST: 'INSTANT_CAST',
    ON_BUTTON_IS_DOWN: 'ON_BUTTON_IS_DOWN',
    PASSIVE: 'PASSIVE',
    PRESS: 'PRESS',
    PRESS_TOGGLE: 'PRESS_TOGGLE',
    INSTANT_CAST_TOGGLE: 'INSTANT_CAST_TOGGLE'
};
export const enumAbilityImbue = {
    ACTIVE: 'ACTIVE',
    ACTIVE_NON_ULT: 'ACTIVE_NON_ULT',
    MODIFIER_VALUE: 'MODIFIER_VALUE'
};
export const enumAbilityType = {
    INNATE: 'INNATE',
    ITEM: 'ITEM',
    SIGNATURE: 'SIGNATURE',
    ULTIMATE: 'ULTIMATE',
    WEAPON: 'WEAPON',
    MELEE: 'MELEE',
    COSMETIC: 'COSMETIC'
};
export const enumBuildLanguage = {
    ENGLISH: 'ENGLISH',
    GERMAN: 'GERMAN',
    FRENCH: 'FRENCH',
    ITALIAN: 'ITALIAN',
    KOREAN: 'KOREAN',
    SPANISH_SPAIN: 'SPANISH_SPAIN',
    CHINESE_SIMPLIFIED: 'CHINESE_SIMPLIFIED',
    RUSSIAN: 'RUSSIAN',
    THAI: 'THAI',
    JAPANESE: 'JAPANESE',
    PORTUGUESE_PORTUGAL: 'PORTUGUESE_PORTUGAL',
    POLISH: 'POLISH',
    CZECH: 'CZECH',
    TURKISH: 'TURKISH',
    PORTUGUESE_BRAZIL: 'PORTUGUESE_BRAZIL',
    UKRAINIAN: 'UKRAINIAN',
    SPANISH_LATIN_AMERICA: 'SPANISH_LATIN_AMERICA',
    VIETNAMESE: 'VIETNAMESE'
};
export const enumHeroType = {
    ASSASSIN: 'ASSASSIN',
    BRAWLER: 'BRAWLER',
    MARKSMAN: 'MARKSMAN',
    MYSTIC: 'MYSTIC'
};
export const enumItemSlotType = {
    WEAPON: 'WEAPON',
    SPIRIT: 'SPIRIT',
    VITALITY: 'VITALITY'
};
export const enumItemType = {
    ABILITY: 'ABILITY',
    WEAPON: 'WEAPON',
    UPGRADE: 'UPGRADE'
};
export const enumLanguage = {
    BRAZILIAN: 'BRAZILIAN',
    BULGARIAN: 'BULGARIAN',
    CZECH: 'CZECH',
    DANISH: 'DANISH',
    DUTCH: 'DUTCH',
    ENGLISH: 'ENGLISH',
    FINNISH: 'FINNISH',
    FRENCH: 'FRENCH',
    GERMAN: 'GERMAN',
    GREEK: 'GREEK',
    HUNGARIAN: 'HUNGARIAN',
    INDONESIAN: 'INDONESIAN',
    ITALIAN: 'ITALIAN',
    JAPANESE: 'JAPANESE',
    KOREANA: 'KOREANA',
    LATAM: 'LATAM',
    NORWEGIAN: 'NORWEGIAN',
    POLISH: 'POLISH',
    PORTUGUESE: 'PORTUGUESE',
    ROMANIAN: 'ROMANIAN',
    RUSSIAN: 'RUSSIAN',
    SCHINESE: 'SCHINESE',
    SPANISH: 'SPANISH',
    SWEDISH: 'SWEDISH',
    TCHINESE: 'TCHINESE',
    THAI: 'THAI',
    TURKISH: 'TURKISH',
    UKRAINIAN: 'UKRAINIAN',
    VIETNAMESE: 'VIETNAMESE'
};
export const enumOrderByHeroBuild = {
    WEEKLY_FAVORITES: 'WEEKLY_FAVORITES',
    FAVORITES: 'FAVORITES',
    IGNORES: 'IGNORES',
    REPORTS: 'REPORTS',
    UPDATED_AT: 'UPDATED_AT',
    PUBLISHED_AT: 'PUBLISHED_AT',
    VERSION: 'VERSION'
};
export const enumOrderByMatch = {
    MATCH_ID: 'MATCH_ID',
    START_TIME: 'START_TIME',
    AVERAGE_BADGE: 'AVERAGE_BADGE'
};
export const enumOrderByMatchHistory = {
    MATCH_ID: 'MATCH_ID',
    ACCOUNT_ID: 'ACCOUNT_ID',
    START_TIME: 'START_TIME'
};
export const enumOrderByMatchPlayer = {
    MATCH_ID: 'MATCH_ID',
    ACCOUNT_ID: 'ACCOUNT_ID',
    START_TIME: 'START_TIME'
};
export const enumOrderDirection = {
    DESC: 'DESC',
    ASC: 'ASC'
};
//# sourceMappingURL=schema.js.map