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