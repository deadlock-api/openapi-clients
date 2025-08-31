/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ActiveMatchTeam } from './ActiveMatchTeam';
export type ActiveMatchPlayer = {
    abandoned?: boolean | null;
    account_id?: number | null;
    /**
     * See more: <https://assets.deadlock-api.com/v2/heroes>
     */
    hero_id?: number | null;
    team?: number | null;
    team_parsed?: (null | ActiveMatchTeam);
};

