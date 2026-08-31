// @ts-nocheck
import { createFetcher } from './fetcher';
import { generateGraphqlOperation, } from './generateGraphqlOperation';
export const createClient = ({ queryRoot, mutationRoot, subscriptionRoot, ...options }) => {
    const fetcher = createFetcher(options);
    const client = {};
    if (queryRoot) {
        client.query = (request) => {
            if (!queryRoot)
                throw new Error('queryRoot argument is missing');
            const resultPromise = fetcher(generateGraphqlOperation('query', queryRoot, request));
            return resultPromise;
        };
    }
    if (mutationRoot) {
        client.mutation = (request) => {
            if (!mutationRoot)
                throw new Error('mutationRoot argument is missing');
            const resultPromise = fetcher(generateGraphqlOperation('mutation', mutationRoot, request));
            return resultPromise;
        };
    }
    return client;
};
//# sourceMappingURL=createClient.js.map