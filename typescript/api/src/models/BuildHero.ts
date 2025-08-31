/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { BuildHeroDetails } from './BuildHeroDetails';
export type BuildHero = {
    author_account_id: number;
    description?: string | null;
    details: BuildHeroDetails;
    development_build?: boolean | null;
    hero_build_id: number;
    /**
     * See more: <https://assets.deadlock-api.com/v2/heroes>
     */
    hero_id: number;
    language: number;
    last_updated_timestamp?: number | null;
    name: string;
    origin_build_id: number;
    publish_timestamp?: number | null;
    tags?: Array<number>;
    version: number;
};

