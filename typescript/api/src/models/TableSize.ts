/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type TableSize = {
    /**
     * Compressed size of the table in bytes.
     */
    data_compressed_bytes?: number | null;
    /**
     * Uncompressed size of the table in bytes.
     */
    data_uncompressed_bytes?: number | null;
    /**
     * Whether the table is a view.
     */
    is_view: boolean;
    /**
     * Number of rows in the table.
     */
    rows?: number | null;
};

