/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ActiveMatchGameMode } from './ActiveMatchGameMode';
import type { ActiveMatchMode } from './ActiveMatchMode';
import type { ActiveMatchPlayer } from './ActiveMatchPlayer';
import type { ActiveMatchRegionMode } from './ActiveMatchRegionMode';
import type { ActiveMatchTeam } from './ActiveMatchTeam';
export type ActiveMatch = {
    compat_version?: number | null;
    duration_s?: number | null;
    game_mode?: number | null;
    game_mode_parsed?: (null | ActiveMatchGameMode);
    game_mode_version?: number | null;
    lobby_id?: number | null;
    match_id?: number | null;
    match_mode?: number | null;
    match_mode_parsed?: (null | ActiveMatchMode);
    match_score?: number | null;
    net_worth_team_0?: number | null;
    net_worth_team_1?: number | null;
    objectives_mask_team0?: number | null;
    objectives_mask_team1?: number | null;
    open_spectator_slots?: number | null;
    players: Array<ActiveMatchPlayer>;
    region_mode?: number | null;
    region_mode_parsed?: (null | ActiveMatchRegionMode);
    spectators?: number | null;
    start_time?: number | null;
    winning_team?: number | null;
    winning_team_parsed?: (null | ActiveMatchTeam);
};

