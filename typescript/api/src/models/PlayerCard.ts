/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { PlayerCardSlot } from './PlayerCardSlot';
export type PlayerCard = {
    account_id: number;
    /**
     * See more: <https://assets.deadlock-api.com/v2/ranks>
     */
    ranked_badge_level?: number | null;
    /**
     * See more: <https://assets.deadlock-api.com/v2/ranks>
     */
    ranked_rank?: number | null;
    /**
     * See more: <https://assets.deadlock-api.com/v2/ranks>
     */
    ranked_subrank?: number | null;
    slots: Array<PlayerCardSlot>;
};

