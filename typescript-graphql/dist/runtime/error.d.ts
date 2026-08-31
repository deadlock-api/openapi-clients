export declare class GenqlError extends Error {
    errors: Array<GraphqlError>;
    /**
     * Partial data returned by the server
     */
    data?: any;
    constructor(errors: any[], data: any);
}
interface GraphqlError {
    message: string;
    locations?: Array<{
        line: number;
        column: number;
    }>;
    path?: string[];
    extensions?: Record<string, any>;
}
export {};
//# sourceMappingURL=error.d.ts.map