/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { VariableCategory } from './VariableCategory';
export type VariableDescription = {
    /**
     * The category of the variable.
     */
    category: VariableCategory;
    /**
     * The default label for the variable.
     */
    default_label?: string | null;
    /**
     * The description of the variable.
     */
    description: string;
    /**
     * Extra arguments that can be passed to the variable.
     */
    extra_args: Array<string>;
    /**
     * The name of the variable.
     */
    name: string;
};

