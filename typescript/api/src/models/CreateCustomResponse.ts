/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type CreateCustomResponse = {
    /**
     * If a callback url is provided, this is the secret that should be used to verify the callback.
     * The secret is a base64 encoded random string. To verify it you should compare it with the X-Callback-Secret header.
     * If no callback url is provided, this will be None.
     */
    callback_secret?: string | null;
    party_code: string;
    party_id: string;
};

