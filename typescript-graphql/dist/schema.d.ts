export type Scalars = {
    Boolean: boolean;
    DateTime: any;
    Float: number;
    ID: string;
    Int: number;
    JSON: any;
    JsonScalar: any;
    String: string;
};
export interface Ability {
    id: Scalars['Int'];
    class_name: Scalars['String'];
    name: Scalars['String'];
    start_trained: (Scalars['Boolean'] | null);
    image: (Scalars['String'] | null);
    image_webp: (Scalars['String'] | null);
    hero: (Scalars['Int'] | null);
    heroes: (Scalars['Int'][] | null);
    update_time: (Scalars['Int'] | null);
    type: ItemType;
    grant_ammo_on_cast: (Scalars['Boolean'] | null);
    behaviours: (Scalars['String'][] | null);
    description: AbilityDescription;
    ability_type: (AbilityType | null);
    boss_damage_scale: (Scalars['Float'] | null);
    dependant_abilities: (Scalars['String'][] | null);
    videos: (AbilityVideos | null);
    properties: Scalars['JSON'];
    weapon_info: Scalars['JSON'];
    tooltip_details: Scalars['JSON'];
    upgrades: Scalars['JSON'];
    dependent_abilities: Scalars['JSON'];
    __typename: 'Ability';
}
export type AbilityActivation = 'HOLD_TOGGLE' | 'INSTANT_CAST' | 'ON_BUTTON_IS_DOWN' | 'PASSIVE' | 'PRESS' | 'PRESS_TOGGLE' | 'INSTANT_CAST_TOGGLE';
export interface AbilityDescription {
    desc: (Scalars['String'] | null);
    quip: (Scalars['String'] | null);
    t_1_desc: (Scalars['String'] | null);
    t_2_desc: (Scalars['String'] | null);
    t_3_desc: (Scalars['String'] | null);
    active: (Scalars['String'] | null);
    passive: (Scalars['String'] | null);
    __typename: 'AbilityDescription';
}
export type AbilityImbue = 'ACTIVE' | 'ACTIVE_NON_ULT' | 'MODIFIER_VALUE';
export type AbilityType = 'INNATE' | 'ITEM' | 'SIGNATURE' | 'ULTIMATE' | 'WEAPON' | 'MELEE' | 'COSMETIC';
export interface AbilityVideos {
    webm: (Scalars['String'] | null);
    mp_4: (Scalars['String'] | null);
    __typename: 'AbilityVideos';
}
export type AssetItem = (Ability | Weapon | Upgrade) & {
    __isUnion?: true;
};
export interface Hero {
    id: Scalars['Int'];
    class_name: Scalars['String'];
    name: Scalars['String'];
    description: HeroDescription;
    player_selectable: Scalars['Boolean'];
    disabled: Scalars['Boolean'];
    in_development: Scalars['Boolean'];
    needs_testing: Scalars['Boolean'];
    assigned_players_only: Scalars['Boolean'];
    /** Always emitted (empty if the hero declares no `m_vecHeroTags`). */
    tags: Scalars['String'][];
    gun_tag: (Scalars['String'] | null);
    hideout_rich_presence: (Scalars['String'] | null);
    hero_type: (HeroType | null);
    prerelease_only: (Scalars['Boolean'] | null);
    limited_testing: Scalars['Boolean'];
    complexity: Scalars['Int'];
    skin: Scalars['Int'];
    images: HeroImages;
    physics: HeroPhysics;
    shop_stat_display: ShopStatDisplay;
    stats_display: StatsDisplay;
    hero_stats_ui: HeroStatsUI;
    item_draft_weights: Scalars['JSON'];
    items: Scalars['JSON'];
    starting_stats: Scalars['JSON'];
    item_slot_info: Scalars['JSON'];
    colors: Scalars['JSON'];
    cost_bonuses: Scalars['JSON'];
    level_info: Scalars['JSON'];
    scaling_stats: Scalars['JSON'];
    purchase_bonuses: Scalars['JSON'];
    standard_level_up_upgrades: Scalars['JSON'];
    item_draft_bucketing: Scalars['JSON'];
    __typename: 'Hero';
}
export interface HeroDescription {
    lore: (Scalars['String'] | null);
    role: (Scalars['String'] | null);
    playstyle: (Scalars['String'] | null);
    __typename: 'HeroDescription';
}
export interface HeroImages {
    icon_hero_card: (Scalars['String'] | null);
    icon_hero_card_webp: (Scalars['String'] | null);
    icon_image_small: (Scalars['String'] | null);
    icon_image_small_webp: (Scalars['String'] | null);
    minimap_image: (Scalars['String'] | null);
    minimap_image_webp: (Scalars['String'] | null);
    hero_card_critical: (Scalars['String'] | null);
    hero_card_critical_webp: (Scalars['String'] | null);
    hero_card_gloat: (Scalars['String'] | null);
    hero_card_gloat_webp: (Scalars['String'] | null);
    top_bar_vertical_image: (Scalars['String'] | null);
    top_bar_vertical_image_webp: (Scalars['String'] | null);
    weapon_image: (Scalars['String'] | null);
    weapon_image_webp: (Scalars['String'] | null);
    background_image: (Scalars['String'] | null);
    background_image_webp: (Scalars['String'] | null);
    name_image: (Scalars['String'] | null);
    __typename: 'HeroImages';
}
export interface HeroPhysics {
    stealth_speed_meters_per_second: Scalars['Float'];
    collision_height: (Scalars['Float'] | null);
    collision_radius: (Scalars['Float'] | null);
    step_height: (Scalars['Float'] | null);
    footstep_sound_travel_distance_meters: (Scalars['Float'] | null);
    step_sound_time: (Scalars['Float'] | null);
    step_sound_time_sprinting: (Scalars['Float'] | null);
    __typename: 'HeroPhysics';
}
export interface HeroStatsUI {
    weapon_stat_display: Scalars['String'];
    display_stats: HeroStatsUIDisplay[];
    __typename: 'HeroStatsUI';
}
export interface HeroStatsUIDisplay {
    category: Scalars['String'];
    stat_type: Scalars['String'];
    __typename: 'HeroStatsUIDisplay';
}
export type HeroType = 'ASSASSIN' | 'BRAWLER' | 'MARKSMAN' | 'MYSTIC';
export interface Item {
    game_time_s: (Scalars['Int'] | null);
    item_id: (Scalars['Int'] | null);
    upgrade_id: (Scalars['Int'] | null);
    sold_time_s: (Scalars['Int'] | null);
    flags: (Scalars['Int'] | null);
    imbued_ability_id: (Scalars['Int'] | null);
    /** Catalog asset for this purchased item, matched by `item_id` then `upgrade_id`. */
    asset: (AssetItem | null);
    __typename: 'Item';
}
export type ItemSlotType = 'WEAPON' | 'SPIRIT' | 'VITALITY';
/** Discriminator for the `type` field on every item variant. */
export type ItemType = 'ABILITY' | 'WEAPON' | 'UPGRADE';
/** Set of languages the upstream `localization/<lang>.json` files are keyed by. */
export type Language = 'BRAZILIAN' | 'BULGARIAN' | 'CZECH' | 'DANISH' | 'DUTCH' | 'ENGLISH' | 'FINNISH' | 'FRENCH' | 'GERMAN' | 'GREEK' | 'HUNGARIAN' | 'INDONESIAN' | 'ITALIAN' | 'JAPANESE' | 'KOREANA' | 'LATAM' | 'NORWEGIAN' | 'POLISH' | 'PORTUGUESE' | 'ROMANIAN' | 'RUSSIAN' | 'SCHINESE' | 'SPANISH' | 'SWEDISH' | 'TCHINESE' | 'THAI' | 'TURKISH' | 'UKRAINIAN' | 'VIETNAMESE';
export interface Match {
    match_id: (Scalars['Int'] | null);
    start_time: (Scalars['Int'] | null);
    duration_s: (Scalars['Int'] | null);
    match_mode: (Scalars['String'] | null);
    game_mode: (Scalars['String'] | null);
    game_mode_version: (Scalars['Int'] | null);
    bot_difficulty: (Scalars['String'] | null);
    winning_team: (Scalars['String'] | null);
    match_outcome: (Scalars['String'] | null);
    average_badge_team_0: (Scalars['Int'] | null);
    average_badge_team_1: (Scalars['Int'] | null);
    average_badge: (Scalars['Int'] | null);
    is_high_skill_range_parties: (Scalars['Boolean'] | null);
    low_pri_pool: (Scalars['Boolean'] | null);
    new_player_pool: (Scalars['Boolean'] | null);
    not_scored: (Scalars['Boolean'] | null);
    ranked_type: (Scalars['String'] | null);
    rank_interval: (Scalars['Int'] | null);
    rewards_eligible: (Scalars['Boolean'] | null);
    earned_holiday_award_2025: (Scalars['Boolean'] | null);
    objectives_mask_team_0: (Scalars['Int'] | null);
    objectives_mask_team_1: (Scalars['Int'] | null);
    team_score: (Scalars['JsonScalar'] | null);
    match_tracked_stats: (Scalars['JsonScalar'] | null);
    team_0_tracked_stats: (Scalars['JsonScalar'] | null);
    team_1_tracked_stats: (Scalars['JsonScalar'] | null);
    objectives: (Scalars['JsonScalar'] | null);
    mid_boss: (Scalars['JsonScalar'] | null);
    street_brawl_rounds: (Scalars['JsonScalar'] | null);
    banned_hero_ids: (Scalars['JsonScalar'] | null);
    first_mid_boss_time_s: (Scalars['Int'] | null);
    first_objective_destroyed_time_s: (Scalars['Int'] | null);
    players: (MatchPlayer[] | null);
    __typename: 'Match';
}
/**
 * One `player_match_history` row per (`account_id`, `match_id`) — the same
 * data as the REST `/v1/players/{account_id}/match-history` endpoint, minus
 * the on-demand Steam fetch (only what `ClickHouse` has stored).
 */
export interface MatchHistoryEntry {
    account_id: (Scalars['Int'] | null);
    match_id: (Scalars['Int'] | null);
    /** See more: <https://api.deadlock-api.com/v1/assets/heroes> */
    hero_id: (Scalars['Int'] | null);
    hero_level: (Scalars['Int'] | null);
    start_time: (Scalars['Int'] | null);
    game_mode: (Scalars['String'] | null);
    match_mode: (Scalars['String'] | null);
    player_team: (Scalars['String'] | null);
    player_kills: (Scalars['Int'] | null);
    player_deaths: (Scalars['Int'] | null);
    player_assists: (Scalars['Int'] | null);
    denies: (Scalars['Int'] | null);
    net_worth: (Scalars['Int'] | null);
    last_hits: (Scalars['Int'] | null);
    team_abandoned: (Scalars['Boolean'] | null);
    abandoned_time_s: (Scalars['Int'] | null);
    match_duration_s: (Scalars['Int'] | null);
    /** The winning team id. */
    match_result: (Scalars['Int'] | null);
    objectives_mask_team_0: (Scalars['Int'] | null);
    objectives_mask_team_1: (Scalars['Int'] | null);
    brawl_score_team_0: (Scalars['Int'] | null);
    brawl_score_team_1: (Scalars['Int'] | null);
    brawl_avg_round_time_s: (Scalars['Int'] | null);
    won: (Scalars['Boolean'] | null);
    /** How the match was scored for the player. */
    player_match_outcome: (Scalars['String'] | null);
    /** The ranked badge shown for the player after the match (tier = first digits, subtier = last digit), capped at Eternus 6. See more: <https://api.deadlock-api.com/v1/assets/ranks> */
    ranked_display_badge: (Scalars['Int'] | null);
    /** The ranked progress change the player got from this match. */
    ranked_delta: (Scalars['Int'] | null);
    /** Non-zero if this match counted towards the player's ranked calibration. */
    ranked_calibration_match: (Scalars['Int'] | null);
    /** Whether the player's demotion protection absorbed a loss in this match. */
    ranked_used_demotion_protection: (Scalars['Boolean'] | null);
    /** Hero asset metadata for this entry's `hero_id` (latest version, English). */
    hero: (Hero | null);
    __typename: 'MatchHistoryEntry';
}
export interface MatchPlayer {
    match_id: (Scalars['Int'] | null);
    account_id: (Scalars['Int'] | null);
    player_slot: (Scalars['Int'] | null);
    team: (Scalars['String'] | null);
    hero_id: (Scalars['Int'] | null);
    party: (Scalars['Int'] | null);
    assigned_lane: (Scalars['Int'] | null);
    start_time: (Scalars['Int'] | null);
    duration_s: (Scalars['Int'] | null);
    match_mode: (Scalars['String'] | null);
    game_mode: (Scalars['String'] | null);
    winning_team: (Scalars['String'] | null);
    match_outcome: (Scalars['String'] | null);
    average_badge_team_0: (Scalars['Int'] | null);
    average_badge_team_1: (Scalars['Int'] | null);
    average_badge: (Scalars['Int'] | null);
    kills: (Scalars['Int'] | null);
    deaths: (Scalars['Int'] | null);
    assists: (Scalars['Int'] | null);
    net_worth: (Scalars['Int'] | null);
    last_hits: (Scalars['Int'] | null);
    denies: (Scalars['Int'] | null);
    ability_points: (Scalars['Int'] | null);
    player_level: (Scalars['Int'] | null);
    abandon_match_time_s: (Scalars['Int'] | null);
    mvp_rank: (Scalars['Int'] | null);
    max_level: (Scalars['Int'] | null);
    max_player_damage: (Scalars['Int'] | null);
    max_player_damage_taken: (Scalars['Int'] | null);
    max_boss_damage: (Scalars['Int'] | null);
    max_creep_damage: (Scalars['Int'] | null);
    max_creep_kills: (Scalars['Int'] | null);
    max_neutral_kills: (Scalars['Int'] | null);
    max_neutral_damage: (Scalars['Int'] | null);
    max_max_health: (Scalars['Int'] | null);
    max_hero_bullets_hit: (Scalars['Int'] | null);
    max_hero_bullets_hit_crit: (Scalars['Int'] | null);
    max_shots_hit: (Scalars['Int'] | null);
    max_shots_missed: (Scalars['Int'] | null);
    rewards_eligible: (Scalars['Boolean'] | null);
    earned_holiday_award_2025: (Scalars['Boolean'] | null);
    player_match_outcome: (Scalars['String'] | null);
    player_rank_initial_display_rank: (Scalars['Int'] | null);
    player_rank_initial_flat_progress: (Scalars['Int'] | null);
    player_rank_final_flat_progress: (Scalars['Int'] | null);
    player_rank_desired_progress_change: (Scalars['Int'] | null);
    player_rank_initial_calibration_games: (Scalars['Int'] | null);
    player_rank_initial_demotion_protection_games: (Scalars['Int'] | null);
    player_rank_consumed_demotion_protection: (Scalars['Boolean'] | null);
    player_rank_initial_win_streak: (Scalars['Int'] | null);
    hero_build_id: (Scalars['Int'] | null);
    /** Hero locked before the pre-game swap window; 0 when unknown. Differs from `hero_id` when the player swapped. */
    pregame_hero_id: (Scalars['Int'] | null);
    items: (Item[] | null);
    stats: (Stat[] | null);
    death_details: (Scalars['JsonScalar'] | null);
    accolades: (Scalars['JsonScalar'] | null);
    book_reward: (Scalars['JsonScalar'] | null);
    power_up_buffs: (Scalars['JsonScalar'] | null);
    ability_stats: (Scalars['JsonScalar'] | null);
    player_tracked_stats: (Scalars['JsonScalar'] | null);
    stats_type_stat: (Scalars['JsonScalar'] | null);
    hero_xp_rewards: (Scalars['JsonScalar'] | null);
    /** Hero asset metadata for this player's `hero_id` (latest version, English). */
    hero: (Hero | null);
    /**
     * Stored Steam profile for this player's `account_id` (no live Steam
     * fetch). `null` for protected users and accounts without a stored
     * profile.
     */
    steam: (SteamProfile | null);
    __typename: 'MatchPlayer';
}
export type OrderByMatch = 'MATCH_ID' | 'START_TIME' | 'AVERAGE_BADGE';
export type OrderByMatchHistory = 'MATCH_ID' | 'ACCOUNT_ID' | 'START_TIME';
export type OrderByMatchPlayer = 'MATCH_ID' | 'ACCOUNT_ID' | 'START_TIME';
export type OrderDirection = 'DESC' | 'ASC';
export interface QueryRoot {
    /** Match-grouped query — one node per match_id with players aggregated. */
    matches: Match[];
    /** Player-row query — one node per (match_id, account_id). */
    match_players: MatchPlayer[];
    /**
     * Player match history — one node per (account_id, match_id), from the
     * stored `player_match_history` table (no on-demand Steam fetch).
     */
    match_history: MatchHistoryEntry[];
    /**
     * All heroes for the given client version (defaults to latest), localized
     * to `language` (defaults to English). Sourced from the versioned assets,
     * not ClickHouse.
     */
    heroes: Hero[];
    /**
     * All items (abilities, weapons, upgrades) for the given client version
     * (defaults to latest), localized to `language` (defaults to English).
     */
    items: AssetItem[];
    /**
     * All rank tiers for the given client version (defaults to latest),
     * localized to `language` (defaults to English).
     */
    ranks: Rank[];
    __typename: 'QueryRoot';
}
export interface Rank {
    tier: Scalars['Int'];
    name: Scalars['String'];
    images: RankImages;
    color: Scalars['String'];
    __typename: 'Rank';
}
/**
 * Image URLs for a single rank tier. Field declaration order is load-bearing:
 * it sets the JSON key order, which is stable across versions of this API.
 */
export interface RankImages {
    large: (Scalars['String'] | null);
    large_webp: (Scalars['String'] | null);
    chalk: (Scalars['String'] | null);
    chalk_webp: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank1`. */
    large_subrank_1: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank1_webp`. */
    large_subrank_1_webp: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank2`. */
    large_subrank_2: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank2_webp`. */
    large_subrank_2_webp: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank3`. */
    large_subrank_3: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank3_webp`. */
    large_subrank_3_webp: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank4`. */
    large_subrank_4: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank4_webp`. */
    large_subrank_4_webp: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank5`. */
    large_subrank_5: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank5_webp`. */
    large_subrank_5_webp: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank6`. */
    large_subrank_6: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank6_webp`. */
    large_subrank_6_webp: (Scalars['String'] | null);
    /** @deprecated No longer produced by the game assets; use `large`/`chalk` instead. */
    small: (Scalars['String'] | null);
    /** @deprecated No longer produced by the game assets; use `large`/`chalk` instead. */
    small_webp: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank1`. */
    small_subrank_1: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank1_webp`. */
    small_subrank_1_webp: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank2`. */
    small_subrank_2: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank2_webp`. */
    small_subrank_2_webp: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank3`. */
    small_subrank_3: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank3_webp`. */
    small_subrank_3_webp: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank4`. */
    small_subrank_4: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank4_webp`. */
    small_subrank_4_webp: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank5`. */
    small_subrank_5: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank5_webp`. */
    small_subrank_5_webp: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank6`. */
    small_subrank_6: (Scalars['String'] | null);
    /** @deprecated Size variants are gone; this is an alias of `subrank6_webp`. */
    small_subrank_6_webp: (Scalars['String'] | null);
    /** Tier badge with the division numeral drawn on it, composed on demand by this API. */
    subrank_1: (Scalars['String'] | null);
    subrank_1_webp: (Scalars['String'] | null);
    subrank_2: (Scalars['String'] | null);
    subrank_2_webp: (Scalars['String'] | null);
    subrank_3: (Scalars['String'] | null);
    subrank_3_webp: (Scalars['String'] | null);
    subrank_4: (Scalars['String'] | null);
    subrank_4_webp: (Scalars['String'] | null);
    subrank_5: (Scalars['String'] | null);
    subrank_5_webp: (Scalars['String'] | null);
    subrank_6: (Scalars['String'] | null);
    subrank_6_webp: (Scalars['String'] | null);
    __typename: 'RankImages';
}
export interface ShopSpiritStatsDisplay {
    display_stats: Scalars['String'][];
    __typename: 'ShopSpiritStatsDisplay';
}
export interface ShopStatDisplay {
    spirit_stats_display: ShopSpiritStatsDisplay;
    vitality_stats_display: ShopVitalityStatsDisplay;
    weapon_stats_display: ShopWeaponStatsDisplay;
    __typename: 'ShopStatDisplay';
}
export interface ShopVitalityStatsDisplay {
    display_stats: Scalars['String'][];
    other_display_stats: Scalars['String'][];
    __typename: 'ShopVitalityStatsDisplay';
}
export interface ShopWeaponStatsDisplay {
    display_stats: Scalars['String'][];
    other_display_stats: Scalars['String'][];
    weapon_attributes: (Scalars['String'][] | null);
    weapon_image: (Scalars['String'] | null);
    weapon_image_webp: (Scalars['String'] | null);
    __typename: 'ShopWeaponStatsDisplay';
}
export interface Stat {
    time_stamp_s: (Scalars['Int'] | null);
    net_worth: (Scalars['Int'] | null);
    gold_player: (Scalars['Int'] | null);
    gold_player_orbs: (Scalars['Int'] | null);
    gold_lane_creep_orbs: (Scalars['Int'] | null);
    gold_neutral_creep_orbs: (Scalars['Int'] | null);
    gold_boss: (Scalars['Int'] | null);
    gold_boss_orb: (Scalars['Int'] | null);
    gold_treasure: (Scalars['Int'] | null);
    gold_denied: (Scalars['Int'] | null);
    gold_death_loss: (Scalars['Int'] | null);
    gold_lane_creep: (Scalars['Int'] | null);
    gold_neutral_creep: (Scalars['Int'] | null);
    kills: (Scalars['Int'] | null);
    deaths: (Scalars['Int'] | null);
    assists: (Scalars['Int'] | null);
    creep_kills: (Scalars['Int'] | null);
    neutral_kills: (Scalars['Int'] | null);
    possible_creeps: (Scalars['Int'] | null);
    creep_damage: (Scalars['Int'] | null);
    player_damage: (Scalars['Int'] | null);
    neutral_damage: (Scalars['Int'] | null);
    boss_damage: (Scalars['Int'] | null);
    denies: (Scalars['Int'] | null);
    player_healing: (Scalars['Int'] | null);
    ability_points: (Scalars['Int'] | null);
    self_healing: (Scalars['Int'] | null);
    player_damage_taken: (Scalars['Int'] | null);
    max_health: (Scalars['Int'] | null);
    weapon_power: (Scalars['Int'] | null);
    tech_power: (Scalars['Int'] | null);
    shots_hit: (Scalars['Int'] | null);
    shots_missed: (Scalars['Int'] | null);
    damage_absorbed: (Scalars['Int'] | null);
    absorption_provided: (Scalars['Int'] | null);
    hero_bullets_hit: (Scalars['Int'] | null);
    hero_bullets_hit_crit: (Scalars['Int'] | null);
    heal_prevented: (Scalars['Int'] | null);
    heal_lost: (Scalars['Int'] | null);
    damage_mitigated: (Scalars['Int'] | null);
    level: (Scalars['Int'] | null);
    player_barriering: (Scalars['Int'] | null);
    teammate_healing: (Scalars['Int'] | null);
    teammate_barriering: (Scalars['Int'] | null);
    __typename: 'Stat';
}
export interface StatsDisplay {
    health_header_stats: Scalars['String'][];
    health_stats: Scalars['String'][];
    magic_header_stats: Scalars['String'][];
    magic_stats: Scalars['String'][];
    weapon_header_stats: Scalars['String'][];
    weapon_stats: Scalars['String'][];
    __typename: 'StatsDisplay';
}
/**
 * Stored Steam profile of a player, from the `steam_profiles` table (no live
 * Steam Web API fetch). Same data as the REST `/v1/players/steam` endpoint.
 */
export interface SteamProfile {
    account_id: Scalars['Int'];
    personaname: Scalars['String'];
    profileurl: Scalars['String'];
    avatar: Scalars['String'];
    avatarmedium: Scalars['String'];
    avatarfull: Scalars['String'];
    realname: (Scalars['String'] | null);
    countrycode: (Scalars['String'] | null);
    last_updated: Scalars['DateTime'];
    __typename: 'SteamProfile';
}
export interface Upgrade {
    id: Scalars['Int'];
    class_name: Scalars['String'];
    name: Scalars['String'];
    start_trained: (Scalars['Boolean'] | null);
    image: (Scalars['String'] | null);
    image_webp: (Scalars['String'] | null);
    hero: (Scalars['Int'] | null);
    heroes: (Scalars['Int'][] | null);
    update_time: (Scalars['Int'] | null);
    type: ItemType;
    shop_image: (Scalars['String'] | null);
    shop_image_webp: (Scalars['String'] | null);
    shop_image_small: (Scalars['String'] | null);
    shop_image_small_webp: (Scalars['String'] | null);
    item_slot_type: ItemSlotType;
    item_tier: Scalars['Int'];
    disabled: (Scalars['Boolean'] | null);
    description: (UpgradeDescription | null);
    activation: AbilityActivation;
    imbue: (AbilityImbue | null);
    component_items: (Scalars['String'][] | null);
    is_active_item: Scalars['Boolean'];
    shopable: Scalars['Boolean'];
    cost: (Scalars['Int'] | null);
    weapon_info: Scalars['JSON'];
    properties: Scalars['JSON'];
    tooltip_sections: Scalars['JSON'];
    upgrades: Scalars['JSON'];
    __typename: 'Upgrade';
}
export interface UpgradeDescription {
    desc: (Scalars['String'] | null);
    desc_2: (Scalars['String'] | null);
    active: (Scalars['String'] | null);
    passive: (Scalars['String'] | null);
    __typename: 'UpgradeDescription';
}
export interface Weapon {
    id: Scalars['Int'];
    class_name: Scalars['String'];
    name: Scalars['String'];
    start_trained: (Scalars['Boolean'] | null);
    image: (Scalars['String'] | null);
    image_webp: (Scalars['String'] | null);
    hero: (Scalars['Int'] | null);
    heroes: (Scalars['Int'][] | null);
    update_time: (Scalars['Int'] | null);
    type: ItemType;
    crosshair_css_class: (Scalars['String'] | null);
    use_custom_crosshair_settings: (Scalars['Boolean'] | null);
    properties: Scalars['JSON'];
    weapon_info: Scalars['JSON'];
    custom_crosshair_settings: Scalars['JSON'];
    __typename: 'Weapon';
}
export type Query = QueryRoot;
export interface AbilityGenqlSelection {
    id?: boolean | number;
    class_name?: boolean | number;
    name?: boolean | number;
    start_trained?: boolean | number;
    image?: boolean | number;
    image_webp?: boolean | number;
    hero?: boolean | number;
    heroes?: boolean | number;
    update_time?: boolean | number;
    type?: boolean | number;
    grant_ammo_on_cast?: boolean | number;
    behaviours?: boolean | number;
    description?: AbilityDescriptionGenqlSelection;
    ability_type?: boolean | number;
    boss_damage_scale?: boolean | number;
    dependant_abilities?: boolean | number;
    videos?: AbilityVideosGenqlSelection;
    properties?: boolean | number;
    weapon_info?: boolean | number;
    tooltip_details?: boolean | number;
    upgrades?: boolean | number;
    dependent_abilities?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface AbilityDescriptionGenqlSelection {
    desc?: boolean | number;
    quip?: boolean | number;
    t_1_desc?: boolean | number;
    t_2_desc?: boolean | number;
    t_3_desc?: boolean | number;
    active?: boolean | number;
    passive?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface AbilityVideosGenqlSelection {
    webm?: boolean | number;
    mp_4?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface AssetItemGenqlSelection {
    on_Ability?: AbilityGenqlSelection;
    on_Weapon?: WeaponGenqlSelection;
    on_Upgrade?: UpgradeGenqlSelection;
    __typename?: boolean | number;
}
export interface BoolFilter {
    eq?: (Scalars['Boolean'] | null);
    is_null?: (Scalars['Boolean'] | null);
}
export interface HeroGenqlSelection {
    id?: boolean | number;
    class_name?: boolean | number;
    name?: boolean | number;
    description?: HeroDescriptionGenqlSelection;
    player_selectable?: boolean | number;
    disabled?: boolean | number;
    in_development?: boolean | number;
    needs_testing?: boolean | number;
    assigned_players_only?: boolean | number;
    /** Always emitted (empty if the hero declares no `m_vecHeroTags`). */
    tags?: boolean | number;
    gun_tag?: boolean | number;
    hideout_rich_presence?: boolean | number;
    hero_type?: boolean | number;
    prerelease_only?: boolean | number;
    limited_testing?: boolean | number;
    complexity?: boolean | number;
    skin?: boolean | number;
    images?: HeroImagesGenqlSelection;
    physics?: HeroPhysicsGenqlSelection;
    shop_stat_display?: ShopStatDisplayGenqlSelection;
    stats_display?: StatsDisplayGenqlSelection;
    hero_stats_ui?: HeroStatsUIGenqlSelection;
    item_draft_weights?: boolean | number;
    items?: boolean | number;
    starting_stats?: boolean | number;
    item_slot_info?: boolean | number;
    colors?: boolean | number;
    cost_bonuses?: boolean | number;
    level_info?: boolean | number;
    scaling_stats?: boolean | number;
    purchase_bonuses?: boolean | number;
    standard_level_up_upgrades?: boolean | number;
    item_draft_bucketing?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface HeroDescriptionGenqlSelection {
    lore?: boolean | number;
    role?: boolean | number;
    playstyle?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface HeroImagesGenqlSelection {
    icon_hero_card?: boolean | number;
    icon_hero_card_webp?: boolean | number;
    icon_image_small?: boolean | number;
    icon_image_small_webp?: boolean | number;
    minimap_image?: boolean | number;
    minimap_image_webp?: boolean | number;
    hero_card_critical?: boolean | number;
    hero_card_critical_webp?: boolean | number;
    hero_card_gloat?: boolean | number;
    hero_card_gloat_webp?: boolean | number;
    top_bar_vertical_image?: boolean | number;
    top_bar_vertical_image_webp?: boolean | number;
    weapon_image?: boolean | number;
    weapon_image_webp?: boolean | number;
    background_image?: boolean | number;
    background_image_webp?: boolean | number;
    name_image?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface HeroPhysicsGenqlSelection {
    stealth_speed_meters_per_second?: boolean | number;
    collision_height?: boolean | number;
    collision_radius?: boolean | number;
    step_height?: boolean | number;
    footstep_sound_travel_distance_meters?: boolean | number;
    step_sound_time?: boolean | number;
    step_sound_time_sprinting?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface HeroStatsUIGenqlSelection {
    weapon_stat_display?: boolean | number;
    display_stats?: HeroStatsUIDisplayGenqlSelection;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface HeroStatsUIDisplayGenqlSelection {
    category?: boolean | number;
    stat_type?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface I32Filter {
    eq?: (Scalars['Int'] | null);
    in?: (Scalars['Int'][] | null);
    gt?: (Scalars['Int'] | null);
    gte?: (Scalars['Int'] | null);
    lt?: (Scalars['Int'] | null);
    lte?: (Scalars['Int'] | null);
    is_null?: (Scalars['Boolean'] | null);
}
export interface I64Filter {
    eq?: (Scalars['Int'] | null);
    in?: (Scalars['Int'][] | null);
    gt?: (Scalars['Int'] | null);
    gte?: (Scalars['Int'] | null);
    lt?: (Scalars['Int'] | null);
    lte?: (Scalars['Int'] | null);
    is_null?: (Scalars['Boolean'] | null);
}
export interface ItemGenqlSelection {
    game_time_s?: boolean | number;
    item_id?: boolean | number;
    upgrade_id?: boolean | number;
    sold_time_s?: boolean | number;
    flags?: boolean | number;
    imbued_ability_id?: boolean | number;
    /** Catalog asset for this purchased item, matched by `item_id` then `upgrade_id`. */
    asset?: AssetItemGenqlSelection;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface MatchGenqlSelection {
    match_id?: boolean | number;
    start_time?: boolean | number;
    duration_s?: boolean | number;
    match_mode?: boolean | number;
    game_mode?: boolean | number;
    game_mode_version?: boolean | number;
    bot_difficulty?: boolean | number;
    winning_team?: boolean | number;
    match_outcome?: boolean | number;
    average_badge_team_0?: boolean | number;
    average_badge_team_1?: boolean | number;
    average_badge?: boolean | number;
    is_high_skill_range_parties?: boolean | number;
    low_pri_pool?: boolean | number;
    new_player_pool?: boolean | number;
    not_scored?: boolean | number;
    ranked_type?: boolean | number;
    rank_interval?: boolean | number;
    rewards_eligible?: boolean | number;
    earned_holiday_award_2025?: boolean | number;
    objectives_mask_team_0?: boolean | number;
    objectives_mask_team_1?: boolean | number;
    team_score?: boolean | number;
    match_tracked_stats?: boolean | number;
    team_0_tracked_stats?: boolean | number;
    team_1_tracked_stats?: boolean | number;
    objectives?: boolean | number;
    mid_boss?: boolean | number;
    street_brawl_rounds?: boolean | number;
    banned_hero_ids?: boolean | number;
    first_mid_boss_time_s?: boolean | number;
    first_objective_destroyed_time_s?: boolean | number;
    players?: MatchPlayerGenqlSelection;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
/**
 * One `player_match_history` row per (`account_id`, `match_id`) — the same
 * data as the REST `/v1/players/{account_id}/match-history` endpoint, minus
 * the on-demand Steam fetch (only what `ClickHouse` has stored).
 */
export interface MatchHistoryEntryGenqlSelection {
    account_id?: boolean | number;
    match_id?: boolean | number;
    /** See more: <https://api.deadlock-api.com/v1/assets/heroes> */
    hero_id?: boolean | number;
    hero_level?: boolean | number;
    start_time?: boolean | number;
    game_mode?: boolean | number;
    match_mode?: boolean | number;
    player_team?: boolean | number;
    player_kills?: boolean | number;
    player_deaths?: boolean | number;
    player_assists?: boolean | number;
    denies?: boolean | number;
    net_worth?: boolean | number;
    last_hits?: boolean | number;
    team_abandoned?: boolean | number;
    abandoned_time_s?: boolean | number;
    match_duration_s?: boolean | number;
    /** The winning team id. */
    match_result?: boolean | number;
    objectives_mask_team_0?: boolean | number;
    objectives_mask_team_1?: boolean | number;
    brawl_score_team_0?: boolean | number;
    brawl_score_team_1?: boolean | number;
    brawl_avg_round_time_s?: boolean | number;
    won?: boolean | number;
    /** How the match was scored for the player. */
    player_match_outcome?: boolean | number;
    /** The ranked badge shown for the player after the match (tier = first digits, subtier = last digit), capped at Eternus 6. See more: <https://api.deadlock-api.com/v1/assets/ranks> */
    ranked_display_badge?: boolean | number;
    /** The ranked progress change the player got from this match. */
    ranked_delta?: boolean | number;
    /** Non-zero if this match counted towards the player's ranked calibration. */
    ranked_calibration_match?: boolean | number;
    /** Whether the player's demotion protection absorbed a loss in this match. */
    ranked_used_demotion_protection?: boolean | number;
    /** Hero asset metadata for this entry's `hero_id` (latest version, English). */
    hero?: HeroGenqlSelection;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
/** Filter input for the `match_history` query. Operations across fields are AND-ed. */
export interface MatchHistoryWhere {
    account_id?: (U32Filter | null);
    match_id?: (U64Filter | null);
    hero_id?: (U32Filter | null);
    hero_level?: (U32Filter | null);
    start_time?: (I64Filter | null);
    game_mode?: (StringFilter | null);
    match_mode?: (StringFilter | null);
    player_team?: (StringFilter | null);
    player_kills?: (U32Filter | null);
    player_deaths?: (U32Filter | null);
    player_assists?: (U32Filter | null);
    denies?: (U32Filter | null);
    net_worth?: (U32Filter | null);
    last_hits?: (U32Filter | null);
    team_abandoned?: (BoolFilter | null);
    match_duration_s?: (U32Filter | null);
    match_result?: (U32Filter | null);
    won?: (BoolFilter | null);
    player_match_outcome?: (StringFilter | null);
    ranked_display_badge?: (U32Filter | null);
    ranked_delta?: (I32Filter | null);
    ranked_calibration_match?: (U32Filter | null);
    ranked_used_demotion_protection?: (BoolFilter | null);
}
export interface MatchPlayerGenqlSelection {
    match_id?: boolean | number;
    account_id?: boolean | number;
    player_slot?: boolean | number;
    team?: boolean | number;
    hero_id?: boolean | number;
    party?: boolean | number;
    assigned_lane?: boolean | number;
    start_time?: boolean | number;
    duration_s?: boolean | number;
    match_mode?: boolean | number;
    game_mode?: boolean | number;
    winning_team?: boolean | number;
    match_outcome?: boolean | number;
    average_badge_team_0?: boolean | number;
    average_badge_team_1?: boolean | number;
    average_badge?: boolean | number;
    kills?: boolean | number;
    deaths?: boolean | number;
    assists?: boolean | number;
    net_worth?: boolean | number;
    last_hits?: boolean | number;
    denies?: boolean | number;
    ability_points?: boolean | number;
    player_level?: boolean | number;
    abandon_match_time_s?: boolean | number;
    mvp_rank?: boolean | number;
    max_level?: boolean | number;
    max_player_damage?: boolean | number;
    max_player_damage_taken?: boolean | number;
    max_boss_damage?: boolean | number;
    max_creep_damage?: boolean | number;
    max_creep_kills?: boolean | number;
    max_neutral_kills?: boolean | number;
    max_neutral_damage?: boolean | number;
    max_max_health?: boolean | number;
    max_hero_bullets_hit?: boolean | number;
    max_hero_bullets_hit_crit?: boolean | number;
    max_shots_hit?: boolean | number;
    max_shots_missed?: boolean | number;
    rewards_eligible?: boolean | number;
    earned_holiday_award_2025?: boolean | number;
    player_match_outcome?: boolean | number;
    player_rank_initial_display_rank?: boolean | number;
    player_rank_initial_flat_progress?: boolean | number;
    player_rank_final_flat_progress?: boolean | number;
    player_rank_desired_progress_change?: boolean | number;
    player_rank_initial_calibration_games?: boolean | number;
    player_rank_initial_demotion_protection_games?: boolean | number;
    player_rank_consumed_demotion_protection?: boolean | number;
    player_rank_initial_win_streak?: boolean | number;
    hero_build_id?: boolean | number;
    /** Hero locked before the pre-game swap window; 0 when unknown. Differs from `hero_id` when the player swapped. */
    pregame_hero_id?: boolean | number;
    items?: ItemGenqlSelection;
    stats?: StatGenqlSelection;
    death_details?: boolean | number;
    accolades?: boolean | number;
    book_reward?: boolean | number;
    power_up_buffs?: boolean | number;
    ability_stats?: boolean | number;
    player_tracked_stats?: boolean | number;
    stats_type_stat?: boolean | number;
    hero_xp_rewards?: boolean | number;
    /** Hero asset metadata for this player's `hero_id` (latest version, English). */
    hero?: HeroGenqlSelection;
    /**
     * Stored Steam profile for this player's `account_id` (no live Steam
     * fetch). `null` for protected users and accounts without a stored
     * profile.
     */
    steam?: SteamProfileGenqlSelection;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
/**
 * Filter input for the `matches` and (transitively) `match_players` queries.
 * All listed columns are filterable. Operations across fields are AND-ed.
 */
export interface MatchPlayerWhere {
    match_id?: (U64Filter | null);
    account_id?: (U32Filter | null);
    hero_id?: (U32Filter | null);
    player_slot?: (U32Filter | null);
    team?: (StringFilter | null);
    start_time?: (I64Filter | null);
    duration_s?: (U32Filter | null);
    match_mode?: (StringFilter | null);
    game_mode?: (StringFilter | null);
    winning_team?: (StringFilter | null);
    match_outcome?: (StringFilter | null);
    average_badge_team_0?: (U32Filter | null);
    average_badge_team_1?: (U32Filter | null);
    average_badge?: (U32Filter | null);
    is_high_skill_range_parties?: (BoolFilter | null);
    low_pri_pool?: (BoolFilter | null);
    new_player_pool?: (BoolFilter | null);
    not_scored?: (BoolFilter | null);
    rewards_eligible?: (BoolFilter | null);
    kills?: (U32Filter | null);
    deaths?: (U32Filter | null);
    assists?: (U32Filter | null);
    net_worth?: (U32Filter | null);
    player_level?: (U32Filter | null);
    assigned_lane?: (U32Filter | null);
}
export interface QueryRootGenqlSelection {
    /** Match-grouped query — one node per match_id with players aggregated. */
    matches?: (MatchGenqlSelection & {
        __args?: {
            where?: (MatchPlayerWhere | null);
            order_by?: (OrderByMatch | null);
            order_direction?: (OrderDirection | null);
            limit?: Scalars['Int'];
            offset?: Scalars['Int'];
        };
    });
    /** Player-row query — one node per (match_id, account_id). */
    match_players?: (MatchPlayerGenqlSelection & {
        __args?: {
            where?: (MatchPlayerWhere | null);
            order_by?: (OrderByMatchPlayer | null);
            order_direction?: (OrderDirection | null);
            limit?: Scalars['Int'];
            offset?: Scalars['Int'];
        };
    });
    /**
     * Player match history — one node per (account_id, match_id), from the
     * stored `player_match_history` table (no on-demand Steam fetch).
     */
    match_history?: (MatchHistoryEntryGenqlSelection & {
        __args?: {
            where?: (MatchHistoryWhere | null);
            order_by?: (OrderByMatchHistory | null);
            order_direction?: (OrderDirection | null);
            limit?: Scalars['Int'];
            offset?: Scalars['Int'];
        };
    });
    /**
     * All heroes for the given client version (defaults to latest), localized
     * to `language` (defaults to English). Sourced from the versioned assets,
     * not ClickHouse.
     */
    heroes?: (HeroGenqlSelection & {
        __args?: {
            client_version?: (Scalars['Int'] | null);
            language?: (Language | null);
        };
    });
    /**
     * All items (abilities, weapons, upgrades) for the given client version
     * (defaults to latest), localized to `language` (defaults to English).
     */
    items?: (AssetItemGenqlSelection & {
        __args?: {
            client_version?: (Scalars['Int'] | null);
            language?: (Language | null);
        };
    });
    /**
     * All rank tiers for the given client version (defaults to latest),
     * localized to `language` (defaults to English).
     */
    ranks?: (RankGenqlSelection & {
        __args?: {
            client_version?: (Scalars['Int'] | null);
            language?: (Language | null);
        };
    });
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface RankGenqlSelection {
    tier?: boolean | number;
    name?: boolean | number;
    images?: RankImagesGenqlSelection;
    color?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
/**
 * Image URLs for a single rank tier. Field declaration order is load-bearing:
 * it sets the JSON key order, which is stable across versions of this API.
 */
export interface RankImagesGenqlSelection {
    large?: boolean | number;
    large_webp?: boolean | number;
    chalk?: boolean | number;
    chalk_webp?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank1`. */
    large_subrank_1?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank1_webp`. */
    large_subrank_1_webp?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank2`. */
    large_subrank_2?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank2_webp`. */
    large_subrank_2_webp?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank3`. */
    large_subrank_3?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank3_webp`. */
    large_subrank_3_webp?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank4`. */
    large_subrank_4?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank4_webp`. */
    large_subrank_4_webp?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank5`. */
    large_subrank_5?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank5_webp`. */
    large_subrank_5_webp?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank6`. */
    large_subrank_6?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank6_webp`. */
    large_subrank_6_webp?: boolean | number;
    /** @deprecated No longer produced by the game assets; use `large`/`chalk` instead. */
    small?: boolean | number;
    /** @deprecated No longer produced by the game assets; use `large`/`chalk` instead. */
    small_webp?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank1`. */
    small_subrank_1?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank1_webp`. */
    small_subrank_1_webp?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank2`. */
    small_subrank_2?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank2_webp`. */
    small_subrank_2_webp?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank3`. */
    small_subrank_3?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank3_webp`. */
    small_subrank_3_webp?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank4`. */
    small_subrank_4?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank4_webp`. */
    small_subrank_4_webp?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank5`. */
    small_subrank_5?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank5_webp`. */
    small_subrank_5_webp?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank6`. */
    small_subrank_6?: boolean | number;
    /** @deprecated Size variants are gone; this is an alias of `subrank6_webp`. */
    small_subrank_6_webp?: boolean | number;
    /** Tier badge with the division numeral drawn on it, composed on demand by this API. */
    subrank_1?: boolean | number;
    subrank_1_webp?: boolean | number;
    subrank_2?: boolean | number;
    subrank_2_webp?: boolean | number;
    subrank_3?: boolean | number;
    subrank_3_webp?: boolean | number;
    subrank_4?: boolean | number;
    subrank_4_webp?: boolean | number;
    subrank_5?: boolean | number;
    subrank_5_webp?: boolean | number;
    subrank_6?: boolean | number;
    subrank_6_webp?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface ShopSpiritStatsDisplayGenqlSelection {
    display_stats?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface ShopStatDisplayGenqlSelection {
    spirit_stats_display?: ShopSpiritStatsDisplayGenqlSelection;
    vitality_stats_display?: ShopVitalityStatsDisplayGenqlSelection;
    weapon_stats_display?: ShopWeaponStatsDisplayGenqlSelection;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface ShopVitalityStatsDisplayGenqlSelection {
    display_stats?: boolean | number;
    other_display_stats?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface ShopWeaponStatsDisplayGenqlSelection {
    display_stats?: boolean | number;
    other_display_stats?: boolean | number;
    weapon_attributes?: boolean | number;
    weapon_image?: boolean | number;
    weapon_image_webp?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface StatGenqlSelection {
    time_stamp_s?: boolean | number;
    net_worth?: boolean | number;
    gold_player?: boolean | number;
    gold_player_orbs?: boolean | number;
    gold_lane_creep_orbs?: boolean | number;
    gold_neutral_creep_orbs?: boolean | number;
    gold_boss?: boolean | number;
    gold_boss_orb?: boolean | number;
    gold_treasure?: boolean | number;
    gold_denied?: boolean | number;
    gold_death_loss?: boolean | number;
    gold_lane_creep?: boolean | number;
    gold_neutral_creep?: boolean | number;
    kills?: boolean | number;
    deaths?: boolean | number;
    assists?: boolean | number;
    creep_kills?: boolean | number;
    neutral_kills?: boolean | number;
    possible_creeps?: boolean | number;
    creep_damage?: boolean | number;
    player_damage?: boolean | number;
    neutral_damage?: boolean | number;
    boss_damage?: boolean | number;
    denies?: boolean | number;
    player_healing?: boolean | number;
    ability_points?: boolean | number;
    self_healing?: boolean | number;
    player_damage_taken?: boolean | number;
    max_health?: boolean | number;
    weapon_power?: boolean | number;
    tech_power?: boolean | number;
    shots_hit?: boolean | number;
    shots_missed?: boolean | number;
    damage_absorbed?: boolean | number;
    absorption_provided?: boolean | number;
    hero_bullets_hit?: boolean | number;
    hero_bullets_hit_crit?: boolean | number;
    heal_prevented?: boolean | number;
    heal_lost?: boolean | number;
    damage_mitigated?: boolean | number;
    level?: boolean | number;
    player_barriering?: boolean | number;
    teammate_healing?: boolean | number;
    teammate_barriering?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface StatsDisplayGenqlSelection {
    health_header_stats?: boolean | number;
    health_stats?: boolean | number;
    magic_header_stats?: boolean | number;
    magic_stats?: boolean | number;
    weapon_header_stats?: boolean | number;
    weapon_stats?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
/**
 * Stored Steam profile of a player, from the `steam_profiles` table (no live
 * Steam Web API fetch). Same data as the REST `/v1/players/steam` endpoint.
 */
export interface SteamProfileGenqlSelection {
    account_id?: boolean | number;
    personaname?: boolean | number;
    profileurl?: boolean | number;
    avatar?: boolean | number;
    avatarmedium?: boolean | number;
    avatarfull?: boolean | number;
    realname?: boolean | number;
    countrycode?: boolean | number;
    last_updated?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface StringFilter {
    eq?: (Scalars['String'] | null);
    in?: (Scalars['String'][] | null);
    is_null?: (Scalars['Boolean'] | null);
}
export interface U32Filter {
    eq?: (Scalars['Int'] | null);
    in?: (Scalars['Int'][] | null);
    gt?: (Scalars['Int'] | null);
    gte?: (Scalars['Int'] | null);
    lt?: (Scalars['Int'] | null);
    lte?: (Scalars['Int'] | null);
    is_null?: (Scalars['Boolean'] | null);
}
export interface U64Filter {
    eq?: (Scalars['Int'] | null);
    in?: (Scalars['Int'][] | null);
    gt?: (Scalars['Int'] | null);
    gte?: (Scalars['Int'] | null);
    lt?: (Scalars['Int'] | null);
    lte?: (Scalars['Int'] | null);
    is_null?: (Scalars['Boolean'] | null);
}
export interface UpgradeGenqlSelection {
    id?: boolean | number;
    class_name?: boolean | number;
    name?: boolean | number;
    start_trained?: boolean | number;
    image?: boolean | number;
    image_webp?: boolean | number;
    hero?: boolean | number;
    heroes?: boolean | number;
    update_time?: boolean | number;
    type?: boolean | number;
    shop_image?: boolean | number;
    shop_image_webp?: boolean | number;
    shop_image_small?: boolean | number;
    shop_image_small_webp?: boolean | number;
    item_slot_type?: boolean | number;
    item_tier?: boolean | number;
    disabled?: boolean | number;
    description?: UpgradeDescriptionGenqlSelection;
    activation?: boolean | number;
    imbue?: boolean | number;
    component_items?: boolean | number;
    is_active_item?: boolean | number;
    shopable?: boolean | number;
    cost?: boolean | number;
    weapon_info?: boolean | number;
    properties?: boolean | number;
    tooltip_sections?: boolean | number;
    upgrades?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface UpgradeDescriptionGenqlSelection {
    desc?: boolean | number;
    desc_2?: boolean | number;
    active?: boolean | number;
    passive?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export interface WeaponGenqlSelection {
    id?: boolean | number;
    class_name?: boolean | number;
    name?: boolean | number;
    start_trained?: boolean | number;
    image?: boolean | number;
    image_webp?: boolean | number;
    hero?: boolean | number;
    heroes?: boolean | number;
    update_time?: boolean | number;
    type?: boolean | number;
    crosshair_css_class?: boolean | number;
    use_custom_crosshair_settings?: boolean | number;
    properties?: boolean | number;
    weapon_info?: boolean | number;
    custom_crosshair_settings?: boolean | number;
    __typename?: boolean | number;
    __scalar?: boolean | number;
}
export type QueryGenqlSelection = QueryRootGenqlSelection;
export declare const isAbility: (obj?: {
    __typename?: any;
} | null) => obj is Ability;
export declare const isAbilityDescription: (obj?: {
    __typename?: any;
} | null) => obj is AbilityDescription;
export declare const isAbilityVideos: (obj?: {
    __typename?: any;
} | null) => obj is AbilityVideos;
export declare const isAssetItem: (obj?: {
    __typename?: any;
} | null) => obj is AssetItem;
export declare const isHero: (obj?: {
    __typename?: any;
} | null) => obj is Hero;
export declare const isHeroDescription: (obj?: {
    __typename?: any;
} | null) => obj is HeroDescription;
export declare const isHeroImages: (obj?: {
    __typename?: any;
} | null) => obj is HeroImages;
export declare const isHeroPhysics: (obj?: {
    __typename?: any;
} | null) => obj is HeroPhysics;
export declare const isHeroStatsUI: (obj?: {
    __typename?: any;
} | null) => obj is HeroStatsUI;
export declare const isHeroStatsUIDisplay: (obj?: {
    __typename?: any;
} | null) => obj is HeroStatsUIDisplay;
export declare const isItem: (obj?: {
    __typename?: any;
} | null) => obj is Item;
export declare const isMatch: (obj?: {
    __typename?: any;
} | null) => obj is Match;
export declare const isMatchHistoryEntry: (obj?: {
    __typename?: any;
} | null) => obj is MatchHistoryEntry;
export declare const isMatchPlayer: (obj?: {
    __typename?: any;
} | null) => obj is MatchPlayer;
export declare const isQueryRoot: (obj?: {
    __typename?: any;
} | null) => obj is QueryRoot;
export declare const isRank: (obj?: {
    __typename?: any;
} | null) => obj is Rank;
export declare const isRankImages: (obj?: {
    __typename?: any;
} | null) => obj is RankImages;
export declare const isShopSpiritStatsDisplay: (obj?: {
    __typename?: any;
} | null) => obj is ShopSpiritStatsDisplay;
export declare const isShopStatDisplay: (obj?: {
    __typename?: any;
} | null) => obj is ShopStatDisplay;
export declare const isShopVitalityStatsDisplay: (obj?: {
    __typename?: any;
} | null) => obj is ShopVitalityStatsDisplay;
export declare const isShopWeaponStatsDisplay: (obj?: {
    __typename?: any;
} | null) => obj is ShopWeaponStatsDisplay;
export declare const isStat: (obj?: {
    __typename?: any;
} | null) => obj is Stat;
export declare const isStatsDisplay: (obj?: {
    __typename?: any;
} | null) => obj is StatsDisplay;
export declare const isSteamProfile: (obj?: {
    __typename?: any;
} | null) => obj is SteamProfile;
export declare const isUpgrade: (obj?: {
    __typename?: any;
} | null) => obj is Upgrade;
export declare const isUpgradeDescription: (obj?: {
    __typename?: any;
} | null) => obj is UpgradeDescription;
export declare const isWeapon: (obj?: {
    __typename?: any;
} | null) => obj is Weapon;
export declare const enumAbilityActivation: {
    HOLD_TOGGLE: "HOLD_TOGGLE";
    INSTANT_CAST: "INSTANT_CAST";
    ON_BUTTON_IS_DOWN: "ON_BUTTON_IS_DOWN";
    PASSIVE: "PASSIVE";
    PRESS: "PRESS";
    PRESS_TOGGLE: "PRESS_TOGGLE";
    INSTANT_CAST_TOGGLE: "INSTANT_CAST_TOGGLE";
};
export declare const enumAbilityImbue: {
    ACTIVE: "ACTIVE";
    ACTIVE_NON_ULT: "ACTIVE_NON_ULT";
    MODIFIER_VALUE: "MODIFIER_VALUE";
};
export declare const enumAbilityType: {
    INNATE: "INNATE";
    ITEM: "ITEM";
    SIGNATURE: "SIGNATURE";
    ULTIMATE: "ULTIMATE";
    WEAPON: "WEAPON";
    MELEE: "MELEE";
    COSMETIC: "COSMETIC";
};
export declare const enumHeroType: {
    ASSASSIN: "ASSASSIN";
    BRAWLER: "BRAWLER";
    MARKSMAN: "MARKSMAN";
    MYSTIC: "MYSTIC";
};
export declare const enumItemSlotType: {
    WEAPON: "WEAPON";
    SPIRIT: "SPIRIT";
    VITALITY: "VITALITY";
};
export declare const enumItemType: {
    ABILITY: "ABILITY";
    WEAPON: "WEAPON";
    UPGRADE: "UPGRADE";
};
export declare const enumLanguage: {
    BRAZILIAN: "BRAZILIAN";
    BULGARIAN: "BULGARIAN";
    CZECH: "CZECH";
    DANISH: "DANISH";
    DUTCH: "DUTCH";
    ENGLISH: "ENGLISH";
    FINNISH: "FINNISH";
    FRENCH: "FRENCH";
    GERMAN: "GERMAN";
    GREEK: "GREEK";
    HUNGARIAN: "HUNGARIAN";
    INDONESIAN: "INDONESIAN";
    ITALIAN: "ITALIAN";
    JAPANESE: "JAPANESE";
    KOREANA: "KOREANA";
    LATAM: "LATAM";
    NORWEGIAN: "NORWEGIAN";
    POLISH: "POLISH";
    PORTUGUESE: "PORTUGUESE";
    ROMANIAN: "ROMANIAN";
    RUSSIAN: "RUSSIAN";
    SCHINESE: "SCHINESE";
    SPANISH: "SPANISH";
    SWEDISH: "SWEDISH";
    TCHINESE: "TCHINESE";
    THAI: "THAI";
    TURKISH: "TURKISH";
    UKRAINIAN: "UKRAINIAN";
    VIETNAMESE: "VIETNAMESE";
};
export declare const enumOrderByMatch: {
    MATCH_ID: "MATCH_ID";
    START_TIME: "START_TIME";
    AVERAGE_BADGE: "AVERAGE_BADGE";
};
export declare const enumOrderByMatchHistory: {
    MATCH_ID: "MATCH_ID";
    ACCOUNT_ID: "ACCOUNT_ID";
    START_TIME: "START_TIME";
};
export declare const enumOrderByMatchPlayer: {
    MATCH_ID: "MATCH_ID";
    ACCOUNT_ID: "ACCOUNT_ID";
    START_TIME: "START_TIME";
};
export declare const enumOrderDirection: {
    DESC: "DESC";
    ASC: "ASC";
};
//# sourceMappingURL=schema.d.ts.map