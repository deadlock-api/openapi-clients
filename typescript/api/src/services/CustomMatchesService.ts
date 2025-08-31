/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CreateCustomRequest } from '../models/CreateCustomRequest';
import type { CreateCustomResponse } from '../models/CreateCustomResponse';
import type { GetCustomMatchIdResponse } from '../models/GetCustomMatchIdResponse';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class CustomMatchesService {
    /**
     * Create Match
     *
     * This endpoint creates a custom match using a bot account.
     *
     * **Process:**
     * 1. A party is created with your provided settings.
     * 2. The system waits for the party code to be generated.
     * 3. The party code is returned in the response.
     * 4. The bot switches to spectator mode.
     * 5. The bot marks itself as ready.
     * 6. You and other players join, ready up, and start the match.
     *
     * **Callbacks:**
     * If a callback URL is provided, POST requests will be sent to it:
     * - **settings:** When lobby settings change, a POST is sent to `{callback_url}/settings` with the `CsoCitadelParty` protobuf message as JSON.
     * - **match start:** When the match starts, a POST is sent to `{callback_url}` with the match ID.
     *
     * _Protobuf definitions: [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)_
     *
     * **Note:**
     * The bot will leave the match 15 minutes after creation, regardless of match state.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | API-Key ONLY |
     * | Key | 100req/30min |
     * | Global | 1000req/h |
     *
     * @param requestBody
     * @returns CreateCustomResponse Successfully fetched custom match id.
     * @throws ApiError
     */
    public static createCustom(
        requestBody: CreateCustomRequest,
    ): CancelablePromise<CreateCustomResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/v1/matches/custom/create',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                400: `Provided parameters are invalid.`,
                429: `Rate limit exceeded`,
                500: `Creating custom match failed`,
            },
        });
    }
    /**
     * Get Match ID
     *
     * This endpoint allows you to get the match id of a custom match.
     *
     * ### Rate Limits:
     * | Type | Limit |
     * | ---- | ----- |
     * | IP | 100req/s |
     * | Key | - |
     * | Global | - |
     *
     * @param partyId
     * @returns GetCustomMatchIdResponse Successfully fetched custom match id.
     * @throws ApiError
     */
    public static getCustom(
        partyId: number,
    ): CancelablePromise<GetCustomMatchIdResponse> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/v1/matches/custom/{party_id}/match-id',
            path: {
                'party_id': partyId,
            },
            errors: {
                400: `Provided parameters are invalid.`,
                429: `Rate limit exceeded`,
                500: `Fetch Custom Match ID failed`,
            },
        });
    }
}
