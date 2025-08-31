/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ESportsMatchStatus } from './ESportsMatchStatus';
export type ESportsMatch = {
    /**
     * Valve's match id of the match.
     */
    match_id?: number | null;
    /**
     * The provider of the match data. Some string that identifies the source of the data.
     */
    provider: string;
    /**
     * The scheduled date of the match.
     */
    scheduled_date?: string | null;
    status?: (null | ESportsMatchStatus);
    /**
     * The name of the first team.
     */
    team0_name?: string | null;
    /**
     * The name of the second team.
     */
    team1_name?: string | null;
    /**
     * The name of the tournament.
     */
    tournament_name?: string | null;
    /**
     * The stage of the tournament.
     */
    tournament_stage?: string | null;
    /**
     * If you want to update an existing match, you can provide an update id.
     */
    update_id?: string | null;
};

