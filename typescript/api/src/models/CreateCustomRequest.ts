/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type CreateCustomRequest = {
    /**
     * If a callback url is provided, we will send a POST request to this url when the match starts.
     */
    callback_url?: string | null;
    cheats_enabled?: boolean | null;
    duplicate_heroes_enabled?: boolean | null;
    experimental_heroes_enabled?: boolean | null;
    is_publicly_visible?: boolean | null;
    min_roster_size?: number | null;
    randomize_lanes?: boolean | null;
};

