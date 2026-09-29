export default {
    "scalars": [
        1,
        3,
        4,
        8,
        16,
        17,
        18,
        22,
        27,
        30,
        31,
        33,
        34,
        35,
        36,
        37,
        45,
        46,
        47,
        48,
        49,
        61
    ],
    "types": {
        "Ability": {
            "id": [
                31
            ],
            "class_name": [
                61
            ],
            "name": [
                61
            ],
            "start_trained": [
                8
            ],
            "image": [
                61
            ],
            "image_webp": [
                61
            ],
            "hero": [
                31
            ],
            "heroes": [
                31
            ],
            "update_time": [
                31
            ],
            "type": [
                34
            ],
            "grant_ammo_on_cast": [
                8
            ],
            "behaviours": [
                61
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
                61
            ],
            "videos": [
                5
            ],
            "properties": [
                35
            ],
            "weapon_info": [
                35
            ],
            "tooltip_details": [
                35
            ],
            "upgrades": [
                35
            ],
            "dependent_abilities": [
                35
            ],
            "__typename": [
                61
            ]
        },
        "AbilityActivation": {},
        "AbilityDescription": {
            "desc": [
                61
            ],
            "quip": [
                61
            ],
            "t_1_desc": [
                61
            ],
            "t_2_desc": [
                61
            ],
            "t_3_desc": [
                61
            ],
            "active": [
                61
            ],
            "passive": [
                61
            ],
            "__typename": [
                61
            ]
        },
        "AbilityImbue": {},
        "AbilityType": {},
        "AbilityVideos": {
            "webm": [
                61
            ],
            "mp_4": [
                61
            ],
            "__typename": [
                61
            ]
        },
        "AssetItem": {
            "on_Ability": [
                0
            ],
            "on_Weapon": [
                68
            ],
            "on_Upgrade": [
                65
            ],
            "__typename": [
                61
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
                61
            ]
        },
        "Boolean": {},
        "Build": {
            "hero_build": [
                10
            ],
            "num_favorites": [
                31
            ],
            "num_ignores": [
                31
            ],
            "num_reports": [
                31
            ],
            "num_weekly_favorites": [
                31
            ],
            "rollup_category": [
                31
            ],
            "__typename": [
                61
            ]
        },
        "BuildHero": {
            "hero_id": [
                31
            ],
            "hero_build_id": [
                31
            ],
            "author_account_id": [
                31
            ],
            "last_updated_timestamp": [
                31
            ],
            "publish_timestamp": [
                31
            ],
            "name": [
                61
            ],
            "description": [
                61
            ],
            "language": [
                31
            ],
            "version": [
                31
            ],
            "origin_build_id": [
                31
            ],
            "tags": [
                31
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
                60
            ],
            "__typename": [
                61
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
                61
            ]
        },
        "BuildHeroDetailsAbilityOrder": {
            "currency_changes": [
                13
            ],
            "__typename": [
                61
            ]
        },
        "BuildHeroDetailsAbilityOrderCurrencyChange": {
            "ability_id": [
                31
            ],
            "currency_type": [
                31
            ],
            "delta": [
                31
            ],
            "annotation": [
                61
            ],
            "asset": [
                6
            ],
            "__typename": [
                61
            ]
        },
        "BuildHeroDetailsCategory": {
            "name": [
                61
            ],
            "width": [
                18
            ],
            "height": [
                18
            ],
            "description": [
                61
            ],
            "mods": [
                15
            ],
            "optional": [
                8
            ],
            "__typename": [
                61
            ]
        },
        "BuildHeroDetailsCategoryAbility": {
            "ability_id": [
                31
            ],
            "annotation": [
                61
            ],
            "required_flex_slots": [
                31
            ],
            "sell_priority": [
                31
            ],
            "imbue_target_ability_id": [
                31
            ],
            "asset": [
                6
            ],
            "__typename": [
                61
            ]
        },
        "BuildLanguage": {},
        "DateTime": {},
        "Float": {},
        "Hero": {
            "id": [
                31
            ],
            "class_name": [
                61
            ],
            "name": [
                61
            ],
            "description": [
                21
            ],
            "player_selectable": [
                8
            ],
            "development_state": [
                22
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
                61
            ],
            "gun_tag": [
                61
            ],
            "hideout_rich_presence": [
                61
            ],
            "hero_type": [
                27
            ],
            "prerelease_only": [
                8
            ],
            "limited_testing": [
                8
            ],
            "complexity": [
                31
            ],
            "skin": [
                31
            ],
            "images": [
                23
            ],
            "physics": [
                24
            ],
            "shop_stat_display": [
                55
            ],
            "stats_display": [
                59
            ],
            "hero_stats_ui": [
                25
            ],
            "item_draft_weights": [
                35
            ],
            "items": [
                35
            ],
            "starting_stats": [
                35
            ],
            "item_slot_info": [
                35
            ],
            "colors": [
                35
            ],
            "cost_bonuses": [
                35
            ],
            "level_info": [
                35
            ],
            "scaling_stats": [
                35
            ],
            "purchase_bonuses": [
                35
            ],
            "standard_level_up_upgrades": [
                35
            ],
            "item_draft_bucketing": [
                35
            ],
            "__typename": [
                61
            ]
        },
        "HeroBuildWhere": {
            "hero_id": [
                31
            ],
            "build_id": [
                31
            ],
            "version": [
                31
            ],
            "author_id": [
                31
            ],
            "language": [
                16
            ],
            "tag": [
                31
            ],
            "rollup_category": [
                31
            ],
            "search_name": [
                61
            ],
            "search_description": [
                61
            ],
            "only_latest": [
                8
            ],
            "min_unix_timestamp": [
                31
            ],
            "max_unix_timestamp": [
                31
            ],
            "min_published_unix_timestamp": [
                31
            ],
            "max_published_unix_timestamp": [
                31
            ],
            "__typename": [
                61
            ]
        },
        "HeroDescription": {
            "lore": [
                61
            ],
            "role": [
                61
            ],
            "playstyle": [
                61
            ],
            "__typename": [
                61
            ]
        },
        "HeroDevelopmentState": {},
        "HeroImages": {
            "icon_hero_card": [
                61
            ],
            "icon_hero_card_webp": [
                61
            ],
            "icon_image_small": [
                61
            ],
            "icon_image_small_webp": [
                61
            ],
            "minimap_image": [
                61
            ],
            "minimap_image_webp": [
                61
            ],
            "hero_card_critical": [
                61
            ],
            "hero_card_critical_webp": [
                61
            ],
            "hero_card_gloat": [
                61
            ],
            "hero_card_gloat_webp": [
                61
            ],
            "top_bar_vertical_image": [
                61
            ],
            "top_bar_vertical_image_webp": [
                61
            ],
            "weapon_image": [
                61
            ],
            "weapon_image_webp": [
                61
            ],
            "background_image": [
                61
            ],
            "background_image_webp": [
                61
            ],
            "name_image": [
                61
            ],
            "__typename": [
                61
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
                61
            ]
        },
        "HeroStatsUI": {
            "weapon_stat_display": [
                61
            ],
            "display_stats": [
                26
            ],
            "__typename": [
                61
            ]
        },
        "HeroStatsUIDisplay": {
            "category": [
                61
            ],
            "stat_type": [
                61
            ],
            "__typename": [
                61
            ]
        },
        "HeroType": {},
        "I32Filter": {
            "eq": [
                31
            ],
            "in": [
                31
            ],
            "gt": [
                31
            ],
            "gte": [
                31
            ],
            "lt": [
                31
            ],
            "lte": [
                31
            ],
            "is_null": [
                8
            ],
            "__typename": [
                61
            ]
        },
        "I64Filter": {
            "eq": [
                31
            ],
            "in": [
                31
            ],
            "gt": [
                31
            ],
            "gte": [
                31
            ],
            "lt": [
                31
            ],
            "lte": [
                31
            ],
            "is_null": [
                8
            ],
            "__typename": [
                61
            ]
        },
        "ID": {},
        "Int": {},
        "Item": {
            "game_time_s": [
                31
            ],
            "item_id": [
                31
            ],
            "upgrade_id": [
                31
            ],
            "sold_time_s": [
                31
            ],
            "flags": [
                31
            ],
            "imbued_ability_id": [
                31
            ],
            "upgrade_info": [
                31
            ],
            "net_worth_at_buy": [
                31
            ],
            "asset": [
                6
            ],
            "__typename": [
                61
            ]
        },
        "ItemSlotType": {},
        "ItemType": {},
        "JSON": {},
        "JsonScalar": {},
        "Language": {},
        "Match": {
            "match_id": [
                31
            ],
            "start_time": [
                31
            ],
            "duration_s": [
                31
            ],
            "match_mode": [
                61
            ],
            "game_mode": [
                61
            ],
            "game_mode_version": [
                31
            ],
            "bot_difficulty": [
                61
            ],
            "winning_team": [
                61
            ],
            "match_outcome": [
                61
            ],
            "average_badge_team_0": [
                31
            ],
            "average_badge_team_1": [
                31
            ],
            "average_badge": [
                31
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
                61
            ],
            "rank_interval": [
                31
            ],
            "corrupted_penalty_seed": [
                31
            ],
            "rewards_eligible": [
                8
            ],
            "earned_holiday_award_2025": [
                8
            ],
            "objectives_mask_team_0": [
                31
            ],
            "objectives_mask_team_1": [
                31
            ],
            "team_score": [
                36
            ],
            "match_tracked_stats": [
                36
            ],
            "team_0_tracked_stats": [
                36
            ],
            "team_1_tracked_stats": [
                36
            ],
            "objectives": [
                36
            ],
            "mid_boss": [
                36
            ],
            "street_brawl_rounds": [
                36
            ],
            "banned_hero_ids": [
                36
            ],
            "first_mid_boss_time_s": [
                31
            ],
            "first_objective_destroyed_time_s": [
                31
            ],
            "players": [
                41
            ],
            "salts": [
                43
            ],
            "__typename": [
                61
            ]
        },
        "MatchHistoryEntry": {
            "account_id": [
                31
            ],
            "match_id": [
                31
            ],
            "hero_id": [
                31
            ],
            "hero_level": [
                31
            ],
            "start_time": [
                31
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
                31
            ],
            "player_deaths": [
                31
            ],
            "player_assists": [
                31
            ],
            "denies": [
                31
            ],
            "net_worth": [
                31
            ],
            "last_hits": [
                31
            ],
            "team_abandoned": [
                8
            ],
            "abandoned_time_s": [
                31
            ],
            "match_duration_s": [
                31
            ],
            "match_result": [
                31
            ],
            "objectives_mask_team_0": [
                31
            ],
            "objectives_mask_team_1": [
                31
            ],
            "brawl_score_team_0": [
                31
            ],
            "brawl_score_team_1": [
                31
            ],
            "brawl_avg_round_time_s": [
                31
            ],
            "won": [
                8
            ],
            "player_match_outcome": [
                61
            ],
            "ranked_display_badge": [
                31
            ],
            "ranked_delta": [
                31
            ],
            "ranked_calibration_match": [
                31
            ],
            "ranked_used_demotion_protection": [
                8
            ],
            "hero": [
                19
            ],
            "__typename": [
                61
            ]
        },
        "MatchHistoryWhere": {
            "account_id": [
                63
            ],
            "match_id": [
                64
            ],
            "hero_id": [
                63
            ],
            "hero_level": [
                63
            ],
            "start_time": [
                29
            ],
            "game_mode": [
                62
            ],
            "match_mode": [
                62
            ],
            "player_team": [
                62
            ],
            "player_kills": [
                63
            ],
            "player_deaths": [
                63
            ],
            "player_assists": [
                63
            ],
            "denies": [
                63
            ],
            "net_worth": [
                63
            ],
            "last_hits": [
                63
            ],
            "team_abandoned": [
                7
            ],
            "match_duration_s": [
                63
            ],
            "match_result": [
                63
            ],
            "won": [
                7
            ],
            "player_match_outcome": [
                62
            ],
            "ranked_display_badge": [
                63
            ],
            "ranked_delta": [
                28
            ],
            "ranked_calibration_match": [
                63
            ],
            "ranked_used_demotion_protection": [
                7
            ],
            "__typename": [
                61
            ]
        },
        "MatchPlayer": {
            "match_id": [
                31
            ],
            "account_id": [
                31
            ],
            "player_slot": [
                31
            ],
            "team": [
                61
            ],
            "hero_id": [
                31
            ],
            "party": [
                31
            ],
            "assigned_lane": [
                31
            ],
            "start_time": [
                31
            ],
            "duration_s": [
                31
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
                31
            ],
            "average_badge_team_1": [
                31
            ],
            "average_badge": [
                31
            ],
            "kills": [
                31
            ],
            "deaths": [
                31
            ],
            "assists": [
                31
            ],
            "net_worth": [
                31
            ],
            "last_hits": [
                31
            ],
            "denies": [
                31
            ],
            "ability_points": [
                31
            ],
            "player_level": [
                31
            ],
            "abandon_match_time_s": [
                31
            ],
            "mvp_rank": [
                31
            ],
            "won": [
                8
            ],
            "hero_xp": [
                31
            ],
            "hero_equips": [
                31
            ],
            "abilities": [
                31
            ],
            "created_at": [
                31
            ],
            "max_level": [
                31
            ],
            "max_player_damage": [
                31
            ],
            "max_player_damage_taken": [
                31
            ],
            "max_boss_damage": [
                31
            ],
            "max_creep_damage": [
                31
            ],
            "max_creep_kills": [
                31
            ],
            "max_neutral_kills": [
                31
            ],
            "max_neutral_damage": [
                31
            ],
            "max_max_health": [
                31
            ],
            "max_hero_bullets_hit": [
                31
            ],
            "max_hero_bullets_hit_crit": [
                31
            ],
            "max_shots_hit": [
                31
            ],
            "max_shots_missed": [
                31
            ],
            "max_self_healing": [
                31
            ],
            "max_player_healing": [
                31
            ],
            "max_gold_player": [
                31
            ],
            "max_gold_player_orbs": [
                31
            ],
            "max_gold_lane_creep": [
                31
            ],
            "max_gold_lane_creep_orbs": [
                31
            ],
            "max_gold_neutral_creep": [
                31
            ],
            "max_gold_neutral_creep_orbs": [
                31
            ],
            "max_gold_boss": [
                31
            ],
            "max_gold_boss_orb": [
                31
            ],
            "max_gold_treasure": [
                31
            ],
            "max_gold_denied": [
                31
            ],
            "max_gold_death_loss": [
                31
            ],
            "max_damage_mitigated": [
                31
            ],
            "max_absorption_provided": [
                31
            ],
            "max_heal_prevented": [
                31
            ],
            "max_possible_creeps": [
                31
            ],
            "max_weapon_power": [
                31
            ],
            "max_tech_power": [
                31
            ],
            "max_teammate_healing": [
                31
            ],
            "max_teammate_barriering": [
                31
            ],
            "final_stats": [
                58
            ],
            "rewards_eligible": [
                8
            ],
            "earned_holiday_award_2025": [
                8
            ],
            "player_match_outcome": [
                61
            ],
            "player_rank_initial_display_rank": [
                31
            ],
            "player_rank_initial_flat_progress": [
                31
            ],
            "player_rank_final_flat_progress": [
                31
            ],
            "player_rank_desired_progress_change": [
                31
            ],
            "player_rank_initial_calibration_games": [
                31
            ],
            "player_rank_initial_demotion_protection_games": [
                31
            ],
            "player_rank_consumed_demotion_protection": [
                8
            ],
            "player_rank_initial_win_streak": [
                31
            ],
            "hero_build_id": [
                31
            ],
            "pregame_hero_id": [
                31
            ],
            "items": [
                32
            ],
            "upgrades": [
                67
            ],
            "stats": [
                58
            ],
            "death_details": [
                36
            ],
            "accolades": [
                36
            ],
            "book_reward": [
                36
            ],
            "power_up_buffs": [
                36
            ],
            "ability_stats": [
                36
            ],
            "player_tracked_stats": [
                36
            ],
            "stats_type_stat": [
                36
            ],
            "hero_xp_rewards": [
                36
            ],
            "hero_release_votes": [
                36
            ],
            "hero": [
                19
            ],
            "steam": [
                60
            ],
            "hero_build": [
                9
            ],
            "salts": [
                43
            ],
            "__typename": [
                61
            ]
        },
        "MatchPlayerWhere": {
            "match_id": [
                64
            ],
            "account_id": [
                63
            ],
            "hero_id": [
                63
            ],
            "player_slot": [
                63
            ],
            "team": [
                62
            ],
            "start_time": [
                29
            ],
            "duration_s": [
                63
            ],
            "match_mode": [
                62
            ],
            "game_mode": [
                62
            ],
            "winning_team": [
                62
            ],
            "match_outcome": [
                62
            ],
            "average_badge_team_0": [
                63
            ],
            "average_badge_team_1": [
                63
            ],
            "average_badge": [
                63
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
                63
            ],
            "deaths": [
                63
            ],
            "assists": [
                63
            ],
            "net_worth": [
                63
            ],
            "player_level": [
                63
            ],
            "assigned_lane": [
                63
            ],
            "last_hits": [
                63
            ],
            "denies": [
                63
            ],
            "mvp_rank": [
                63
            ],
            "player_rank_initial_display_rank": [
                63
            ],
            "player_rank_initial_flat_progress": [
                63
            ],
            "player_rank_final_flat_progress": [
                63
            ],
            "player_rank_desired_progress_change": [
                28
            ],
            "player_rank_initial_calibration_games": [
                63
            ],
            "player_rank_initial_demotion_protection_games": [
                63
            ],
            "player_rank_consumed_demotion_protection": [
                7
            ],
            "player_rank_initial_win_streak": [
                63
            ],
            "__typename": [
                61
            ]
        },
        "MatchSalts": {
            "match_id": [
                31
            ],
            "cluster_id": [
                31
            ],
            "metadata_salt": [
                31
            ],
            "replay_salt": [
                31
            ],
            "created_at": [
                31
            ],
            "metadata_url": [
                61
            ],
            "demo_url": [
                61
            ],
            "__typename": [
                61
            ]
        },
        "MatchSaltsWhere": {
            "match_id": [
                64
            ],
            "cluster_id": [
                63
            ],
            "__typename": [
                61
            ]
        },
        "OrderByHeroBuild": {},
        "OrderByMatch": {},
        "OrderByMatchHistory": {},
        "OrderByMatchPlayer": {},
        "OrderDirection": {},
        "Patch": {
            "source": [
                61
            ],
            "title": [
                61
            ],
            "pub_date": [
                31
            ],
            "end_date": [
                31
            ],
            "link": [
                61
            ],
            "guid": [
                61
            ],
            "category": [
                61
            ],
            "content": [
                61
            ],
            "matches": [
                38,
                {
                    "where": [
                        42
                    ],
                    "order_by": [
                        46
                    ],
                    "order_direction": [
                        49
                    ],
                    "limit": [
                        31,
                        "Int!"
                    ],
                    "offset": [
                        31,
                        "Int!"
                    ]
                }
            ],
            "match_players": [
                41,
                {
                    "where": [
                        42
                    ],
                    "order_by": [
                        48
                    ],
                    "order_direction": [
                        49
                    ],
                    "limit": [
                        31,
                        "Int!"
                    ],
                    "offset": [
                        31,
                        "Int!"
                    ]
                }
            ],
            "match_history": [
                39,
                {
                    "where": [
                        40
                    ],
                    "order_by": [
                        47
                    ],
                    "order_direction": [
                        49
                    ],
                    "limit": [
                        31,
                        "Int!"
                    ],
                    "offset": [
                        31,
                        "Int!"
                    ]
                }
            ],
            "__typename": [
                61
            ]
        },
        "PatchWhere": {
            "source": [
                62
            ],
            "category": [
                62
            ],
            "pub_date": [
                29
            ],
            "end_date": [
                29
            ],
            "__typename": [
                61
            ]
        },
        "Rank": {
            "tier": [
                31
            ],
            "name": [
                61
            ],
            "images": [
                53
            ],
            "color": [
                61
            ],
            "__typename": [
                61
            ]
        },
        "RankImages": {
            "large": [
                61
            ],
            "large_webp": [
                61
            ],
            "chalk": [
                61
            ],
            "chalk_webp": [
                61
            ],
            "large_subrank_1": [
                61
            ],
            "large_subrank_1_webp": [
                61
            ],
            "large_subrank_2": [
                61
            ],
            "large_subrank_2_webp": [
                61
            ],
            "large_subrank_3": [
                61
            ],
            "large_subrank_3_webp": [
                61
            ],
            "large_subrank_4": [
                61
            ],
            "large_subrank_4_webp": [
                61
            ],
            "large_subrank_5": [
                61
            ],
            "large_subrank_5_webp": [
                61
            ],
            "large_subrank_6": [
                61
            ],
            "large_subrank_6_webp": [
                61
            ],
            "small": [
                61
            ],
            "small_webp": [
                61
            ],
            "small_subrank_1": [
                61
            ],
            "small_subrank_1_webp": [
                61
            ],
            "small_subrank_2": [
                61
            ],
            "small_subrank_2_webp": [
                61
            ],
            "small_subrank_3": [
                61
            ],
            "small_subrank_3_webp": [
                61
            ],
            "small_subrank_4": [
                61
            ],
            "small_subrank_4_webp": [
                61
            ],
            "small_subrank_5": [
                61
            ],
            "small_subrank_5_webp": [
                61
            ],
            "small_subrank_6": [
                61
            ],
            "small_subrank_6_webp": [
                61
            ],
            "subrank_1": [
                61
            ],
            "subrank_1_webp": [
                61
            ],
            "subrank_2": [
                61
            ],
            "subrank_2_webp": [
                61
            ],
            "subrank_3": [
                61
            ],
            "subrank_3_webp": [
                61
            ],
            "subrank_4": [
                61
            ],
            "subrank_4_webp": [
                61
            ],
            "subrank_5": [
                61
            ],
            "subrank_5_webp": [
                61
            ],
            "subrank_6": [
                61
            ],
            "subrank_6_webp": [
                61
            ],
            "__typename": [
                61
            ]
        },
        "ShopSpiritStatsDisplay": {
            "display_stats": [
                61
            ],
            "__typename": [
                61
            ]
        },
        "ShopStatDisplay": {
            "spirit_stats_display": [
                54
            ],
            "vitality_stats_display": [
                56
            ],
            "weapon_stats_display": [
                57
            ],
            "__typename": [
                61
            ]
        },
        "ShopVitalityStatsDisplay": {
            "display_stats": [
                61
            ],
            "other_display_stats": [
                61
            ],
            "__typename": [
                61
            ]
        },
        "ShopWeaponStatsDisplay": {
            "display_stats": [
                61
            ],
            "other_display_stats": [
                61
            ],
            "weapon_attributes": [
                61
            ],
            "weapon_image": [
                61
            ],
            "weapon_image_webp": [
                61
            ],
            "__typename": [
                61
            ]
        },
        "Stat": {
            "time_stamp_s": [
                31
            ],
            "net_worth": [
                31
            ],
            "gold_player": [
                31
            ],
            "gold_player_orbs": [
                31
            ],
            "gold_lane_creep_orbs": [
                31
            ],
            "gold_neutral_creep_orbs": [
                31
            ],
            "gold_boss": [
                31
            ],
            "gold_boss_orb": [
                31
            ],
            "gold_treasure": [
                31
            ],
            "gold_denied": [
                31
            ],
            "gold_death_loss": [
                31
            ],
            "gold_lane_creep": [
                31
            ],
            "gold_neutral_creep": [
                31
            ],
            "kills": [
                31
            ],
            "deaths": [
                31
            ],
            "assists": [
                31
            ],
            "creep_kills": [
                31
            ],
            "neutral_kills": [
                31
            ],
            "possible_creeps": [
                31
            ],
            "creep_damage": [
                31
            ],
            "player_damage": [
                31
            ],
            "neutral_damage": [
                31
            ],
            "boss_damage": [
                31
            ],
            "denies": [
                31
            ],
            "player_healing": [
                31
            ],
            "ability_points": [
                31
            ],
            "self_healing": [
                31
            ],
            "player_damage_taken": [
                31
            ],
            "max_health": [
                31
            ],
            "weapon_power": [
                31
            ],
            "tech_power": [
                31
            ],
            "shots_hit": [
                31
            ],
            "shots_missed": [
                31
            ],
            "damage_absorbed": [
                31
            ],
            "absorption_provided": [
                31
            ],
            "hero_bullets_hit": [
                31
            ],
            "hero_bullets_hit_crit": [
                31
            ],
            "heal_prevented": [
                31
            ],
            "heal_lost": [
                31
            ],
            "damage_mitigated": [
                31
            ],
            "level": [
                31
            ],
            "player_barriering": [
                31
            ],
            "teammate_healing": [
                31
            ],
            "teammate_barriering": [
                31
            ],
            "self_damage": [
                31
            ],
            "bullet_kills": [
                31
            ],
            "melee_kills": [
                31
            ],
            "ability_kills": [
                31
            ],
            "headshot_kills": [
                31
            ],
            "custom_user_stats": [
                36
            ],
            "__typename": [
                61
            ]
        },
        "StatsDisplay": {
            "health_header_stats": [
                61
            ],
            "health_stats": [
                61
            ],
            "magic_header_stats": [
                61
            ],
            "magic_stats": [
                61
            ],
            "weapon_header_stats": [
                61
            ],
            "weapon_stats": [
                61
            ],
            "__typename": [
                61
            ]
        },
        "SteamProfile": {
            "account_id": [
                31
            ],
            "personaname": [
                61
            ],
            "profileurl": [
                61
            ],
            "avatar": [
                61
            ],
            "avatarmedium": [
                61
            ],
            "avatarfull": [
                61
            ],
            "realname": [
                61
            ],
            "countrycode": [
                61
            ],
            "last_updated": [
                17
            ],
            "__typename": [
                61
            ]
        },
        "String": {},
        "StringFilter": {
            "eq": [
                61
            ],
            "in": [
                61
            ],
            "is_null": [
                8
            ],
            "__typename": [
                61
            ]
        },
        "U32Filter": {
            "eq": [
                31
            ],
            "in": [
                31
            ],
            "gt": [
                31
            ],
            "gte": [
                31
            ],
            "lt": [
                31
            ],
            "lte": [
                31
            ],
            "is_null": [
                8
            ],
            "__typename": [
                61
            ]
        },
        "U64Filter": {
            "eq": [
                31
            ],
            "in": [
                31
            ],
            "gt": [
                31
            ],
            "gte": [
                31
            ],
            "lt": [
                31
            ],
            "lte": [
                31
            ],
            "is_null": [
                8
            ],
            "__typename": [
                61
            ]
        },
        "Upgrade": {
            "id": [
                31
            ],
            "class_name": [
                61
            ],
            "name": [
                61
            ],
            "start_trained": [
                8
            ],
            "image": [
                61
            ],
            "image_webp": [
                61
            ],
            "hero": [
                31
            ],
            "heroes": [
                31
            ],
            "update_time": [
                31
            ],
            "type": [
                34
            ],
            "shop_image": [
                61
            ],
            "shop_image_webp": [
                61
            ],
            "shop_image_small": [
                61
            ],
            "shop_image_small_webp": [
                61
            ],
            "item_slot_type": [
                33
            ],
            "item_tier": [
                31
            ],
            "disabled": [
                8
            ],
            "description": [
                66
            ],
            "activation": [
                1
            ],
            "imbue": [
                3
            ],
            "component_items": [
                61
            ],
            "is_active_item": [
                8
            ],
            "shopable": [
                8
            ],
            "cost": [
                31
            ],
            "weapon_info": [
                35
            ],
            "properties": [
                35
            ],
            "tooltip_sections": [
                35
            ],
            "upgrades": [
                35
            ],
            "__typename": [
                61
            ]
        },
        "UpgradeDescription": {
            "desc": [
                61
            ],
            "desc_2": [
                61
            ],
            "active": [
                61
            ],
            "passive": [
                61
            ],
            "__typename": [
                61
            ]
        },
        "UpgradePurchase": {
            "item_id": [
                31
            ],
            "game_time_s": [
                31
            ],
            "sold_time_s": [
                31
            ],
            "net_worth_at_buy": [
                31
            ],
            "__typename": [
                61
            ]
        },
        "Weapon": {
            "id": [
                31
            ],
            "class_name": [
                61
            ],
            "name": [
                61
            ],
            "start_trained": [
                8
            ],
            "image": [
                61
            ],
            "image_webp": [
                61
            ],
            "hero": [
                31
            ],
            "heroes": [
                31
            ],
            "update_time": [
                31
            ],
            "type": [
                34
            ],
            "crosshair_css_class": [
                61
            ],
            "use_custom_crosshair_settings": [
                8
            ],
            "properties": [
                35
            ],
            "weapon_info": [
                35
            ],
            "custom_crosshair_settings": [
                35
            ],
            "__typename": [
                61
            ]
        },
        "Query": {
            "matches": [
                38,
                {
                    "where": [
                        42
                    ],
                    "order_by": [
                        46
                    ],
                    "order_direction": [
                        49
                    ],
                    "limit": [
                        31,
                        "Int!"
                    ],
                    "offset": [
                        31,
                        "Int!"
                    ]
                }
            ],
            "match_players": [
                41,
                {
                    "where": [
                        42
                    ],
                    "order_by": [
                        48
                    ],
                    "order_direction": [
                        49
                    ],
                    "limit": [
                        31,
                        "Int!"
                    ],
                    "offset": [
                        31,
                        "Int!"
                    ]
                }
            ],
            "match_history": [
                39,
                {
                    "where": [
                        40
                    ],
                    "order_by": [
                        47
                    ],
                    "order_direction": [
                        49
                    ],
                    "limit": [
                        31,
                        "Int!"
                    ],
                    "offset": [
                        31,
                        "Int!"
                    ]
                }
            ],
            "match_salts": [
                43,
                {
                    "where": [
                        44
                    ],
                    "order_direction": [
                        49
                    ],
                    "limit": [
                        31,
                        "Int!"
                    ],
                    "offset": [
                        31,
                        "Int!"
                    ]
                }
            ],
            "patches": [
                50,
                {
                    "where": [
                        51
                    ],
                    "order_direction": [
                        49
                    ],
                    "limit": [
                        31,
                        "Int!"
                    ],
                    "offset": [
                        31,
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
                        45
                    ],
                    "order_direction": [
                        49
                    ],
                    "limit": [
                        31,
                        "Int!"
                    ],
                    "offset": [
                        31,
                        "Int!"
                    ]
                }
            ],
            "heroes": [
                19,
                {
                    "client_version": [
                        31
                    ],
                    "language": [
                        37
                    ]
                }
            ],
            "items": [
                6,
                {
                    "client_version": [
                        31
                    ],
                    "language": [
                        37
                    ]
                }
            ],
            "ranks": [
                52,
                {
                    "client_version": [
                        31
                    ],
                    "language": [
                        37
                    ]
                }
            ],
            "__typename": [
                61
            ]
        }
    }
}