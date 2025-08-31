/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type PlayerMatchHistoryEntry = {
    abandoned_time_s?: number | null;
    account_id: number;
    denies: number;
    game_mode: number;
    /**
     * See more: <https://assets.deadlock-api.com/v2/heroes>
     */
    hero_id: number;
    hero_level: number;
    last_hits: number;
    match_duration_s: number;
    match_id: number;
    match_mode: number;
    match_result: number;
    net_worth: number;
    objectives_mask_team0: number;
    objectives_mask_team1: number;
    player_assists: number;
    player_deaths: number;
    player_kills: number;
    player_team: number;
    start_time: number;
    team_abandoned?: boolean | null;
};

