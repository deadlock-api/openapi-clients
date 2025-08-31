/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type MMRHistory = {
    account_id: number;
    /**
     * Extracted from the rank the division (rank // 10)
     */
    division: number;
    /**
     * Extracted from the rank the division tier (rank % 10)
     */
    division_tier: number;
    match_id: number;
    /**
     * Player Score is the index for the rank array (internally used for the rank regression)
     */
    player_score: number;
    /**
     * The Player Rank. See more: <https://assets.deadlock-api.com/v2/ranks>
     */
    rank: number;
    /**
     * Start time of the match
     */
    start_time: number;
};

