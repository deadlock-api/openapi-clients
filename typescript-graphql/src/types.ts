export default {
    "scalars": [
        1,
        3,
        4,
        8,
        16,
        17,
        18,
        26,
        29,
        30,
        32,
        33,
        34,
        35,
        36,
        44,
        45,
        46,
        47,
        48,
        60
    ],
    "types": {
        "Ability": {
            "id": [
                30
            ],
            "class_name": [
                60
            ],
            "name": [
                60
            ],
            "start_trained": [
                8
            ],
            "image": [
                60
            ],
            "image_webp": [
                60
            ],
            "hero": [
                30
            ],
            "heroes": [
                30
            ],
            "update_time": [
                30
            ],
            "type": [
                33
            ],
            "grant_ammo_on_cast": [
                8
            ],
            "behaviours": [
                60
            ],
            "description": [
                2
            ],
            "ability_type": [
                4
            ],
            "boss_damage_scale": [
                18
            ],
            "dependant_abilities": [
                60
            ],
            "videos": [
                5
            ],
            "properties": [
                34
            ],
            "weapon_info": [
                34
            ],
            "tooltip_details": [
                34
            ],
            "upgrades": [
                34
            ],
            "dependent_abilities": [
                34
            ],
            "__typename": [
                60
            ]
        },
        "AbilityActivation": {},
        "AbilityDescription": {
            "desc": [
                60
            ],
            "quip": [
                60
            ],
            "t_1_desc": [
                60
            ],
            "t_2_desc": [
                60
            ],
            "t_3_desc": [
                60
            ],
            "active": [
                60
            ],
            "passive": [
                60
            ],
            "__typename": [
                60
            ]
        },
        "AbilityImbue": {},
        "AbilityType": {},
        "AbilityVideos": {
            "webm": [
                60
            ],
            "mp_4": [
                60
            ],
            "__typename": [
                60
            ]
        },
        "AssetItem": {
            "on_Ability": [
                0
            ],
            "on_Weapon": [
                67
            ],
            "on_Upgrade": [
                64
            ],
            "__typename": [
                60
            ]
        },
        "BoolFilter": {
            "eq": [
                8
            ],
            "is_null": [
                8
            ],
            "__typename": [
                60
            ]
        },
        "Boolean": {},
        "Build": {
            "hero_build": [
                10
            ],
            "num_favorites": [
                30
            ],
            "num_ignores": [
                30
            ],
            "num_reports": [
                30
            ],
            "num_weekly_favorites": [
                30
            ],
            "rollup_category": [
                30
            ],
            "__typename": [
                60
            ]
        },
        "BuildHero": {
            "hero_id": [
                30
            ],
            "hero_build_id": [
                30
            ],
            "author_account_id": [
                30
            ],
            "last_updated_timestamp": [
                30
            ],
            "publish_timestamp": [
                30
            ],
            "name": [
                60
            ],
            "description": [
                60
            ],
            "language": [
                30
            ],
            "version": [
                30
            ],
            "origin_build_id": [
                30
            ],
            "tags": [
                30
            ],
            "development_build": [
                8
            ],
            "details": [
                11
            ],
            "hero": [
                19
            ],
            "author": [
                59
            ],
            "__typename": [
                60
            ]
        },
        "BuildHeroDetails": {
            "mod_categories": [
                14
            ],
            "ability_order": [
                12
            ],
            "__typename": [
                60
            ]
        },
        "BuildHeroDetailsAbilityOrder": {
            "currency_changes": [
                13
            ],
            "__typename": [
                60
            ]
        },
        "BuildHeroDetailsAbilityOrderCurrencyChange": {
            "ability_id": [
                30
            ],
            "currency_type": [
                30
            ],
            "delta": [
                30
            ],
            "annotation": [
                60
            ],
            "asset": [
                6
            ],
            "__typename": [
                60
            ]
        },
        "BuildHeroDetailsCategory": {
            "name": [
                60
            ],
            "width": [
                18
            ],
            "height": [
                18
            ],
            "description": [
                60
            ],
            "mods": [
                15
            ],
            "optional": [
                8
            ],
            "__typename": [
                60
            ]
        },
        "BuildHeroDetailsCategoryAbility": {
            "ability_id": [
                30
            ],
            "annotation": [
                60
            ],
            "required_flex_slots": [
                30
            ],
            "sell_priority": [
                30
            ],
            "imbue_target_ability_id": [
                30
            ],
            "asset": [
                6
            ],
            "__typename": [
                60
            ]
        },
        "BuildLanguage": {},
        "DateTime": {},
        "Float": {},
        "Hero": {
            "id": [
                30
            ],
            "class_name": [
                60
            ],
            "name": [
                60
            ],
            "description": [
                21
            ],
            "player_selectable": [
                8
            ],
            "disabled": [
                8
            ],
            "in_development": [
                8
            ],
            "needs_testing": [
                8
            ],
            "assigned_players_only": [
                8
            ],
            "tags": [
                60
            ],
            "gun_tag": [
                60
            ],
            "hideout_rich_presence": [
                60
            ],
            "hero_type": [
                26
            ],
            "prerelease_only": [
                8
            ],
            "limited_testing": [
                8
            ],
            "complexity": [
                30
            ],
            "skin": [
                30
            ],
            "images": [
                22
            ],
            "physics": [
                23
            ],
            "shop_stat_display": [
                54
            ],
            "stats_display": [
                58
            ],
            "hero_stats_ui": [
                24
            ],
            "item_draft_weights": [
                34
            ],
            "items": [
                34
            ],
            "starting_stats": [
                34
            ],
            "item_slot_info": [
                34
            ],
            "colors": [
                34
            ],
            "cost_bonuses": [
                34
            ],
            "level_info": [
                34
            ],
            "scaling_stats": [
                34
            ],
            "purchase_bonuses": [
                34
            ],
            "standard_level_up_upgrades": [
                34
            ],
            "item_draft_bucketing": [
                34
            ],
            "__typename": [
                60
            ]
        },
        "HeroBuildWhere": {
            "hero_id": [
                30
            ],
            "build_id": [
                30
            ],
            "version": [
                30
            ],
            "author_id": [
                30
            ],
            "language": [
                16
            ],
            "tag": [
                30
            ],
            "rollup_category": [
                30
            ],
            "search_name": [
                60
            ],
            "search_description": [
                60
            ],
            "only_latest": [
                8
            ],
            "min_unix_timestamp": [
                30
            ],
            "max_unix_timestamp": [
                30
            ],
            "min_published_unix_timestamp": [
                30
            ],
            "max_published_unix_timestamp": [
                30
            ],
            "__typename": [
                60
            ]
        },
        "HeroDescription": {
            "lore": [
                60
            ],
            "role": [
                60
            ],
            "playstyle": [
                60
            ],
            "__typename": [
                60
            ]
        },
        "HeroImages": {
            "icon_hero_card": [
                60
            ],
            "icon_hero_card_webp": [
                60
            ],
            "icon_image_small": [
                60
            ],
            "icon_image_small_webp": [
                60
            ],
            "minimap_image": [
                60
            ],
            "minimap_image_webp": [
                60
            ],
            "hero_card_critical": [
                60
            ],
            "hero_card_critical_webp": [
                60
            ],
            "hero_card_gloat": [
                60
            ],
            "hero_card_gloat_webp": [
                60
            ],
            "top_bar_vertical_image": [
                60
            ],
            "top_bar_vertical_image_webp": [
                60
            ],
            "weapon_image": [
                60
            ],
            "weapon_image_webp": [
                60
            ],
            "background_image": [
                60
            ],
            "background_image_webp": [
                60
            ],
            "name_image": [
                60
            ],
            "__typename": [
                60
            ]
        },
        "HeroPhysics": {
            "stealth_speed_meters_per_second": [
                18
            ],
            "collision_height": [
                18
            ],
            "collision_radius": [
                18
            ],
            "step_height": [
                18
            ],
            "footstep_sound_travel_distance_meters": [
                18
            ],
            "step_sound_time": [
                18
            ],
            "step_sound_time_sprinting": [
                18
            ],
            "__typename": [
                60
            ]
        },
        "HeroStatsUI": {
            "weapon_stat_display": [
                60
            ],
            "display_stats": [
                25
            ],
            "__typename": [
                60
            ]
        },
        "HeroStatsUIDisplay": {
            "category": [
                60
            ],
            "stat_type": [
                60
            ],
            "__typename": [
                60
            ]
        },
        "HeroType": {},
        "I32Filter": {
            "eq": [
                30
            ],
            "in": [
                30
            ],
            "gt": [
                30
            ],
            "gte": [
                30
            ],
            "lt": [
                30
            ],
            "lte": [
                30
            ],
            "is_null": [
                8
            ],
            "__typename": [
                60
            ]
        },
        "I64Filter": {
            "eq": [
                30
            ],
            "in": [
                30
            ],
            "gt": [
                30
            ],
            "gte": [
                30
            ],
            "lt": [
                30
            ],
            "lte": [
                30
            ],
            "is_null": [
                8
            ],
            "__typename": [
                60
            ]
        },
        "ID": {},
        "Int": {},
        "Item": {
            "game_time_s": [
                30
            ],
            "item_id": [
                30
            ],
            "upgrade_id": [
                30
            ],
            "sold_time_s": [
                30
            ],
            "flags": [
                30
            ],
            "imbued_ability_id": [
                30
            ],
            "upgrade_info": [
                30
            ],
            "net_worth_at_buy": [
                30
            ],
            "asset": [
                6
            ],
            "__typename": [
                60
            ]
        },
        "ItemSlotType": {},
        "ItemType": {},
        "JSON": {},
        "JsonScalar": {},
        "Language": {},
        "Match": {
            "match_id": [
                30
            ],
            "start_time": [
                30
            ],
            "duration_s": [
                30
            ],
            "match_mode": [
                60
            ],
            "game_mode": [
                60
            ],
            "game_mode_version": [
                30
            ],
            "bot_difficulty": [
                60
            ],
            "winning_team": [
                60
            ],
            "match_outcome": [
                60
            ],
            "average_badge_team_0": [
                30
            ],
            "average_badge_team_1": [
                30
            ],
            "average_badge": [
                30
            ],
            "is_high_skill_range_parties": [
                8
            ],
            "low_pri_pool": [
                8
            ],
            "new_player_pool": [
                8
            ],
            "not_scored": [
                8
            ],
            "ranked_type": [
                60
            ],
            "rank_interval": [
                30
            ],
            "rewards_eligible": [
                8
            ],
            "earned_holiday_award_2025": [
                8
            ],
            "objectives_mask_team_0": [
                30
            ],
            "objectives_mask_team_1": [
                30
            ],
            "team_score": [
                35
            ],
            "match_tracked_stats": [
                35
            ],
            "team_0_tracked_stats": [
                35
            ],
            "team_1_tracked_stats": [
                35
            ],
            "objectives": [
                35
            ],
            "mid_boss": [
                35
            ],
            "street_brawl_rounds": [
                35
            ],
            "banned_hero_ids": [
                35
            ],
            "first_mid_boss_time_s": [
                30
            ],
            "first_objective_destroyed_time_s": [
                30
            ],
            "players": [
                40
            ],
            "salts": [
                42
            ],
            "__typename": [
                60
            ]
        },
        "MatchHistoryEntry": {
            "account_id": [
                30
            ],
            "match_id": [
                30
            ],
            "hero_id": [
                30
            ],
            "hero_level": [
                30
            ],
            "start_time": [
                30
            ],
            "game_mode": [
                60
            ],
            "match_mode": [
                60
            ],
            "player_team": [
                60
            ],
            "player_kills": [
                30
            ],
            "player_deaths": [
                30
            ],
            "player_assists": [
                30
            ],
            "denies": [
                30
            ],
            "net_worth": [
                30
            ],
            "last_hits": [
                30
            ],
            "team_abandoned": [
                8
            ],
            "abandoned_time_s": [
                30
            ],
            "match_duration_s": [
                30
            ],
            "match_result": [
                30
            ],
            "objectives_mask_team_0": [
                30
            ],
            "objectives_mask_team_1": [
                30
            ],
            "brawl_score_team_0": [
                30
            ],
            "brawl_score_team_1": [
                30
            ],
            "brawl_avg_round_time_s": [
                30
            ],
            "won": [
                8
            ],
            "player_match_outcome": [
                60
            ],
            "ranked_display_badge": [
                30
            ],
            "ranked_delta": [
                30
            ],
            "ranked_calibration_match": [
                30
            ],
            "ranked_used_demotion_protection": [
                8
            ],
            "hero": [
                19
            ],
            "__typename": [
                60
            ]
        },
        "MatchHistoryWhere": {
            "account_id": [
                62
            ],
            "match_id": [
                63
            ],
            "hero_id": [
                62
            ],
            "hero_level": [
                62
            ],
            "start_time": [
                28
            ],
            "game_mode": [
                61
            ],
            "match_mode": [
                61
            ],
            "player_team": [
                61
            ],
            "player_kills": [
                62
            ],
            "player_deaths": [
                62
            ],
            "player_assists": [
                62
            ],
            "denies": [
                62
            ],
            "net_worth": [
                62
            ],
            "last_hits": [
                62
            ],
            "team_abandoned": [
                7
            ],
            "match_duration_s": [
                62
            ],
            "match_result": [
                62
            ],
            "won": [
                7
            ],
            "player_match_outcome": [
                61
            ],
            "ranked_display_badge": [
                62
            ],
            "ranked_delta": [
                27
            ],
            "ranked_calibration_match": [
                62
            ],
            "ranked_used_demotion_protection": [
                7
            ],
            "__typename": [
                60
            ]
        },
        "MatchPlayer": {
            "match_id": [
                30
            ],
            "account_id": [
                30
            ],
            "player_slot": [
                30
            ],
            "team": [
                60
            ],
            "hero_id": [
                30
            ],
            "party": [
                30
            ],
            "assigned_lane": [
                30
            ],
            "start_time": [
                30
            ],
            "duration_s": [
                30
            ],
            "match_mode": [
                60
            ],
            "game_mode": [
                60
            ],
            "winning_team": [
                60
            ],
            "match_outcome": [
                60
            ],
            "average_badge_team_0": [
                30
            ],
            "average_badge_team_1": [
                30
            ],
            "average_badge": [
                30
            ],
            "kills": [
                30
            ],
            "deaths": [
                30
            ],
            "assists": [
                30
            ],
            "net_worth": [
                30
            ],
            "last_hits": [
                30
            ],
            "denies": [
                30
            ],
            "ability_points": [
                30
            ],
            "player_level": [
                30
            ],
            "abandon_match_time_s": [
                30
            ],
            "mvp_rank": [
                30
            ],
            "won": [
                8
            ],
            "hero_xp": [
                30
            ],
            "hero_equips": [
                30
            ],
            "abilities": [
                30
            ],
            "created_at": [
                30
            ],
            "max_level": [
                30
            ],
            "max_player_damage": [
                30
            ],
            "max_player_damage_taken": [
                30
            ],
            "max_boss_damage": [
                30
            ],
            "max_creep_damage": [
                30
            ],
            "max_creep_kills": [
                30
            ],
            "max_neutral_kills": [
                30
            ],
            "max_neutral_damage": [
                30
            ],
            "max_max_health": [
                30
            ],
            "max_hero_bullets_hit": [
                30
            ],
            "max_hero_bullets_hit_crit": [
                30
            ],
            "max_shots_hit": [
                30
            ],
            "max_shots_missed": [
                30
            ],
            "max_self_healing": [
                30
            ],
            "max_player_healing": [
                30
            ],
            "max_gold_player": [
                30
            ],
            "max_gold_player_orbs": [
                30
            ],
            "max_gold_lane_creep": [
                30
            ],
            "max_gold_lane_creep_orbs": [
                30
            ],
            "max_gold_neutral_creep": [
                30
            ],
            "max_gold_neutral_creep_orbs": [
                30
            ],
            "max_gold_boss": [
                30
            ],
            "max_gold_boss_orb": [
                30
            ],
            "max_gold_treasure": [
                30
            ],
            "max_gold_denied": [
                30
            ],
            "max_gold_death_loss": [
                30
            ],
            "max_damage_mitigated": [
                30
            ],
            "max_absorption_provided": [
                30
            ],
            "max_heal_prevented": [
                30
            ],
            "max_possible_creeps": [
                30
            ],
            "max_weapon_power": [
                30
            ],
            "max_tech_power": [
                30
            ],
            "max_teammate_healing": [
                30
            ],
            "max_teammate_barriering": [
                30
            ],
            "final_stats": [
                57
            ],
            "rewards_eligible": [
                8
            ],
            "earned_holiday_award_2025": [
                8
            ],
            "player_match_outcome": [
                60
            ],
            "player_rank_initial_display_rank": [
                30
            ],
            "player_rank_initial_flat_progress": [
                30
            ],
            "player_rank_final_flat_progress": [
                30
            ],
            "player_rank_desired_progress_change": [
                30
            ],
            "player_rank_initial_calibration_games": [
                30
            ],
            "player_rank_initial_demotion_protection_games": [
                30
            ],
            "player_rank_consumed_demotion_protection": [
                8
            ],
            "player_rank_initial_win_streak": [
                30
            ],
            "hero_build_id": [
                30
            ],
            "pregame_hero_id": [
                30
            ],
            "items": [
                31
            ],
            "upgrades": [
                66
            ],
            "stats": [
                57
            ],
            "death_details": [
                35
            ],
            "accolades": [
                35
            ],
            "book_reward": [
                35
            ],
            "power_up_buffs": [
                35
            ],
            "ability_stats": [
                35
            ],
            "player_tracked_stats": [
                35
            ],
            "stats_type_stat": [
                35
            ],
            "hero_xp_rewards": [
                35
            ],
            "hero": [
                19
            ],
            "steam": [
                59
            ],
            "hero_build": [
                9
            ],
            "salts": [
                42
            ],
            "__typename": [
                60
            ]
        },
        "MatchPlayerWhere": {
            "match_id": [
                63
            ],
            "account_id": [
                62
            ],
            "hero_id": [
                62
            ],
            "player_slot": [
                62
            ],
            "team": [
                61
            ],
            "start_time": [
                28
            ],
            "duration_s": [
                62
            ],
            "match_mode": [
                61
            ],
            "game_mode": [
                61
            ],
            "winning_team": [
                61
            ],
            "match_outcome": [
                61
            ],
            "average_badge_team_0": [
                62
            ],
            "average_badge_team_1": [
                62
            ],
            "average_badge": [
                62
            ],
            "is_high_skill_range_parties": [
                7
            ],
            "low_pri_pool": [
                7
            ],
            "new_player_pool": [
                7
            ],
            "not_scored": [
                7
            ],
            "rewards_eligible": [
                7
            ],
            "kills": [
                62
            ],
            "deaths": [
                62
            ],
            "assists": [
                62
            ],
            "net_worth": [
                62
            ],
            "player_level": [
                62
            ],
            "assigned_lane": [
                62
            ],
            "last_hits": [
                62
            ],
            "denies": [
                62
            ],
            "mvp_rank": [
                62
            ],
            "player_rank_initial_display_rank": [
                62
            ],
            "player_rank_initial_flat_progress": [
                62
            ],
            "player_rank_final_flat_progress": [
                62
            ],
            "player_rank_desired_progress_change": [
                27
            ],
            "player_rank_initial_calibration_games": [
                62
            ],
            "player_rank_initial_demotion_protection_games": [
                62
            ],
            "player_rank_consumed_demotion_protection": [
                7
            ],
            "player_rank_initial_win_streak": [
                62
            ],
            "__typename": [
                60
            ]
        },
        "MatchSalts": {
            "match_id": [
                30
            ],
            "cluster_id": [
                30
            ],
            "metadata_salt": [
                30
            ],
            "replay_salt": [
                30
            ],
            "created_at": [
                30
            ],
            "metadata_url": [
                60
            ],
            "demo_url": [
                60
            ],
            "__typename": [
                60
            ]
        },
        "MatchSaltsWhere": {
            "match_id": [
                63
            ],
            "cluster_id": [
                62
            ],
            "__typename": [
                60
            ]
        },
        "OrderByHeroBuild": {},
        "OrderByMatch": {},
        "OrderByMatchHistory": {},
        "OrderByMatchPlayer": {},
        "OrderDirection": {},
        "Patch": {
            "source": [
                60
            ],
            "title": [
                60
            ],
            "pub_date": [
                30
            ],
            "end_date": [
                30
            ],
            "link": [
                60
            ],
            "guid": [
                60
            ],
            "category": [
                60
            ],
            "content": [
                60
            ],
            "matches": [
                37,
                {
                    "where": [
                        41
                    ],
                    "order_by": [
                        45
                    ],
                    "order_direction": [
                        48
                    ],
                    "limit": [
                        30,
                        "Int!"
                    ],
                    "offset": [
                        30,
                        "Int!"
                    ]
                }
            ],
            "match_players": [
                40,
                {
                    "where": [
                        41
                    ],
                    "order_by": [
                        47
                    ],
                    "order_direction": [
                        48
                    ],
                    "limit": [
                        30,
                        "Int!"
                    ],
                    "offset": [
                        30,
                        "Int!"
                    ]
                }
            ],
            "match_history": [
                38,
                {
                    "where": [
                        39
                    ],
                    "order_by": [
                        46
                    ],
                    "order_direction": [
                        48
                    ],
                    "limit": [
                        30,
                        "Int!"
                    ],
                    "offset": [
                        30,
                        "Int!"
                    ]
                }
            ],
            "__typename": [
                60
            ]
        },
        "PatchWhere": {
            "source": [
                61
            ],
            "category": [
                61
            ],
            "pub_date": [
                28
            ],
            "end_date": [
                28
            ],
            "__typename": [
                60
            ]
        },
        "Rank": {
            "tier": [
                30
            ],
            "name": [
                60
            ],
            "images": [
                52
            ],
            "color": [
                60
            ],
            "__typename": [
                60
            ]
        },
        "RankImages": {
            "large": [
                60
            ],
            "large_webp": [
                60
            ],
            "chalk": [
                60
            ],
            "chalk_webp": [
                60
            ],
            "large_subrank_1": [
                60
            ],
            "large_subrank_1_webp": [
                60
            ],
            "large_subrank_2": [
                60
            ],
            "large_subrank_2_webp": [
                60
            ],
            "large_subrank_3": [
                60
            ],
            "large_subrank_3_webp": [
                60
            ],
            "large_subrank_4": [
                60
            ],
            "large_subrank_4_webp": [
                60
            ],
            "large_subrank_5": [
                60
            ],
            "large_subrank_5_webp": [
                60
            ],
            "large_subrank_6": [
                60
            ],
            "large_subrank_6_webp": [
                60
            ],
            "small": [
                60
            ],
            "small_webp": [
                60
            ],
            "small_subrank_1": [
                60
            ],
            "small_subrank_1_webp": [
                60
            ],
            "small_subrank_2": [
                60
            ],
            "small_subrank_2_webp": [
                60
            ],
            "small_subrank_3": [
                60
            ],
            "small_subrank_3_webp": [
                60
            ],
            "small_subrank_4": [
                60
            ],
            "small_subrank_4_webp": [
                60
            ],
            "small_subrank_5": [
                60
            ],
            "small_subrank_5_webp": [
                60
            ],
            "small_subrank_6": [
                60
            ],
            "small_subrank_6_webp": [
                60
            ],
            "subrank_1": [
                60
            ],
            "subrank_1_webp": [
                60
            ],
            "subrank_2": [
                60
            ],
            "subrank_2_webp": [
                60
            ],
            "subrank_3": [
                60
            ],
            "subrank_3_webp": [
                60
            ],
            "subrank_4": [
                60
            ],
            "subrank_4_webp": [
                60
            ],
            "subrank_5": [
                60
            ],
            "subrank_5_webp": [
                60
            ],
            "subrank_6": [
                60
            ],
            "subrank_6_webp": [
                60
            ],
            "__typename": [
                60
            ]
        },
        "ShopSpiritStatsDisplay": {
            "display_stats": [
                60
            ],
            "__typename": [
                60
            ]
        },
        "ShopStatDisplay": {
            "spirit_stats_display": [
                53
            ],
            "vitality_stats_display": [
                55
            ],
            "weapon_stats_display": [
                56
            ],
            "__typename": [
                60
            ]
        },
        "ShopVitalityStatsDisplay": {
            "display_stats": [
                60
            ],
            "other_display_stats": [
                60
            ],
            "__typename": [
                60
            ]
        },
        "ShopWeaponStatsDisplay": {
            "display_stats": [
                60
            ],
            "other_display_stats": [
                60
            ],
            "weapon_attributes": [
                60
            ],
            "weapon_image": [
                60
            ],
            "weapon_image_webp": [
                60
            ],
            "__typename": [
                60
            ]
        },
        "Stat": {
            "time_stamp_s": [
                30
            ],
            "net_worth": [
                30
            ],
            "gold_player": [
                30
            ],
            "gold_player_orbs": [
                30
            ],
            "gold_lane_creep_orbs": [
                30
            ],
            "gold_neutral_creep_orbs": [
                30
            ],
            "gold_boss": [
                30
            ],
            "gold_boss_orb": [
                30
            ],
            "gold_treasure": [
                30
            ],
            "gold_denied": [
                30
            ],
            "gold_death_loss": [
                30
            ],
            "gold_lane_creep": [
                30
            ],
            "gold_neutral_creep": [
                30
            ],
            "kills": [
                30
            ],
            "deaths": [
                30
            ],
            "assists": [
                30
            ],
            "creep_kills": [
                30
            ],
            "neutral_kills": [
                30
            ],
            "possible_creeps": [
                30
            ],
            "creep_damage": [
                30
            ],
            "player_damage": [
                30
            ],
            "neutral_damage": [
                30
            ],
            "boss_damage": [
                30
            ],
            "denies": [
                30
            ],
            "player_healing": [
                30
            ],
            "ability_points": [
                30
            ],
            "self_healing": [
                30
            ],
            "player_damage_taken": [
                30
            ],
            "max_health": [
                30
            ],
            "weapon_power": [
                30
            ],
            "tech_power": [
                30
            ],
            "shots_hit": [
                30
            ],
            "shots_missed": [
                30
            ],
            "damage_absorbed": [
                30
            ],
            "absorption_provided": [
                30
            ],
            "hero_bullets_hit": [
                30
            ],
            "hero_bullets_hit_crit": [
                30
            ],
            "heal_prevented": [
                30
            ],
            "heal_lost": [
                30
            ],
            "damage_mitigated": [
                30
            ],
            "level": [
                30
            ],
            "player_barriering": [
                30
            ],
            "teammate_healing": [
                30
            ],
            "teammate_barriering": [
                30
            ],
            "self_damage": [
                30
            ],
            "bullet_kills": [
                30
            ],
            "melee_kills": [
                30
            ],
            "ability_kills": [
                30
            ],
            "headshot_kills": [
                30
            ],
            "custom_user_stats": [
                35
            ],
            "__typename": [
                60
            ]
        },
        "StatsDisplay": {
            "health_header_stats": [
                60
            ],
            "health_stats": [
                60
            ],
            "magic_header_stats": [
                60
            ],
            "magic_stats": [
                60
            ],
            "weapon_header_stats": [
                60
            ],
            "weapon_stats": [
                60
            ],
            "__typename": [
                60
            ]
        },
        "SteamProfile": {
            "account_id": [
                30
            ],
            "personaname": [
                60
            ],
            "profileurl": [
                60
            ],
            "avatar": [
                60
            ],
            "avatarmedium": [
                60
            ],
            "avatarfull": [
                60
            ],
            "realname": [
                60
            ],
            "countrycode": [
                60
            ],
            "last_updated": [
                17
            ],
            "__typename": [
                60
            ]
        },
        "String": {},
        "StringFilter": {
            "eq": [
                60
            ],
            "in": [
                60
            ],
            "is_null": [
                8
            ],
            "__typename": [
                60
            ]
        },
        "U32Filter": {
            "eq": [
                30
            ],
            "in": [
                30
            ],
            "gt": [
                30
            ],
            "gte": [
                30
            ],
            "lt": [
                30
            ],
            "lte": [
                30
            ],
            "is_null": [
                8
            ],
            "__typename": [
                60
            ]
        },
        "U64Filter": {
            "eq": [
                30
            ],
            "in": [
                30
            ],
            "gt": [
                30
            ],
            "gte": [
                30
            ],
            "lt": [
                30
            ],
            "lte": [
                30
            ],
            "is_null": [
                8
            ],
            "__typename": [
                60
            ]
        },
        "Upgrade": {
            "id": [
                30
            ],
            "class_name": [
                60
            ],
            "name": [
                60
            ],
            "start_trained": [
                8
            ],
            "image": [
                60
            ],
            "image_webp": [
                60
            ],
            "hero": [
                30
            ],
            "heroes": [
                30
            ],
            "update_time": [
                30
            ],
            "type": [
                33
            ],
            "shop_image": [
                60
            ],
            "shop_image_webp": [
                60
            ],
            "shop_image_small": [
                60
            ],
            "shop_image_small_webp": [
                60
            ],
            "item_slot_type": [
                32
            ],
            "item_tier": [
                30
            ],
            "disabled": [
                8
            ],
            "description": [
                65
            ],
            "activation": [
                1
            ],
            "imbue": [
                3
            ],
            "component_items": [
                60
            ],
            "is_active_item": [
                8
            ],
            "shopable": [
                8
            ],
            "cost": [
                30
            ],
            "weapon_info": [
                34
            ],
            "properties": [
                34
            ],
            "tooltip_sections": [
                34
            ],
            "upgrades": [
                34
            ],
            "__typename": [
                60
            ]
        },
        "UpgradeDescription": {
            "desc": [
                60
            ],
            "desc_2": [
                60
            ],
            "active": [
                60
            ],
            "passive": [
                60
            ],
            "__typename": [
                60
            ]
        },
        "UpgradePurchase": {
            "item_id": [
                30
            ],
            "game_time_s": [
                30
            ],
            "sold_time_s": [
                30
            ],
            "net_worth_at_buy": [
                30
            ],
            "__typename": [
                60
            ]
        },
        "Weapon": {
            "id": [
                30
            ],
            "class_name": [
                60
            ],
            "name": [
                60
            ],
            "start_trained": [
                8
            ],
            "image": [
                60
            ],
            "image_webp": [
                60
            ],
            "hero": [
                30
            ],
            "heroes": [
                30
            ],
            "update_time": [
                30
            ],
            "type": [
                33
            ],
            "crosshair_css_class": [
                60
            ],
            "use_custom_crosshair_settings": [
                8
            ],
            "properties": [
                34
            ],
            "weapon_info": [
                34
            ],
            "custom_crosshair_settings": [
                34
            ],
            "__typename": [
                60
            ]
        },
        "Query": {
            "matches": [
                37,
                {
                    "where": [
                        41
                    ],
                    "order_by": [
                        45
                    ],
                    "order_direction": [
                        48
                    ],
                    "limit": [
                        30,
                        "Int!"
                    ],
                    "offset": [
                        30,
                        "Int!"
                    ]
                }
            ],
            "match_players": [
                40,
                {
                    "where": [
                        41
                    ],
                    "order_by": [
                        47
                    ],
                    "order_direction": [
                        48
                    ],
                    "limit": [
                        30,
                        "Int!"
                    ],
                    "offset": [
                        30,
                        "Int!"
                    ]
                }
            ],
            "match_history": [
                38,
                {
                    "where": [
                        39
                    ],
                    "order_by": [
                        46
                    ],
                    "order_direction": [
                        48
                    ],
                    "limit": [
                        30,
                        "Int!"
                    ],
                    "offset": [
                        30,
                        "Int!"
                    ]
                }
            ],
            "match_salts": [
                42,
                {
                    "where": [
                        43
                    ],
                    "order_direction": [
                        48
                    ],
                    "limit": [
                        30,
                        "Int!"
                    ],
                    "offset": [
                        30,
                        "Int!"
                    ]
                }
            ],
            "patches": [
                49,
                {
                    "where": [
                        50
                    ],
                    "order_direction": [
                        48
                    ],
                    "limit": [
                        30,
                        "Int!"
                    ],
                    "offset": [
                        30,
                        "Int!"
                    ]
                }
            ],
            "hero_builds": [
                9,
                {
                    "where": [
                        20
                    ],
                    "order_by": [
                        44
                    ],
                    "order_direction": [
                        48
                    ],
                    "limit": [
                        30,
                        "Int!"
                    ],
                    "offset": [
                        30,
                        "Int!"
                    ]
                }
            ],
            "heroes": [
                19,
                {
                    "client_version": [
                        30
                    ],
                    "language": [
                        36
                    ]
                }
            ],
            "items": [
                6,
                {
                    "client_version": [
                        30
                    ],
                    "language": [
                        36
                    ]
                }
            ],
            "ranks": [
                51,
                {
                    "client_version": [
                        30
                    ],
                    "language": [
                        36
                    ]
                }
            ],
            "__typename": [
                60
            ]
        }
    }
}