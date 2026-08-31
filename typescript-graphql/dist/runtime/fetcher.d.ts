import type { ClientOptions } from './createClient';
import type { GraphqlOperation } from './generateGraphqlOperation';
export interface Fetcher {
    (gql: GraphqlOperation): Promise<any>;
}
export type BatchOptions = {
    batchInterval?: number;
    maxBatchSize?: number;
};
export declare const createFetcher: ({ url, headers, fetcher, fetch: _fetch, batch, ...rest }: ClientOptions) => Fetcher;
//# sourceMappingURL=fetcher.d.ts.map