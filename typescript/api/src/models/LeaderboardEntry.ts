/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type LeaderboardEntry = {
    /**
     * The account name of the player.
     */
    account_name?: string | null;
    /**
     * The badge level of the player. See more: <https://assets.deadlock-api.com/v2/ranks>
     */
    badge_level?: number | null;
    /**
     * The possible account IDs of the player. **CAVEAT: This is not always correct, as Steam account names are not unique.**
     */
    possible_account_ids?: Array<number>;
    /**
     * The rank of the player. See more: <https://assets.deadlock-api.com/v2/ranks>
     */
    rank?: number | null;
    /**
     * The ranked rank of the player. See more: <https://assets.deadlock-api.com/v2/ranks>
     */
    ranked_rank?: number | null;
    /**
     * The ranked subrank of the player. See more: <https://assets.deadlock-api.com/v2/ranks>
     */
    ranked_subrank?: number | null;
    /**
     * The top hero IDs of the player. See more: <https://assets.deadlock-api.com/v2/heroes>
     */
    top_hero_ids?: Array<number>;
};

