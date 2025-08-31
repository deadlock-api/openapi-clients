/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { MapImagesV1 } from './MapImagesV1';
import type { ObjectivePositionsV1 } from './ObjectivePositionsV1';
import type { ZiplanePathV1 } from './ZiplanePathV1';
export type MapV1 = {
    /**
     * The radius of the map.
     */
    radius?: number;
    /**
     * The images of the map.
     */
    images: MapImagesV1;
    readonly objective_positions: ObjectivePositionsV1;
    /**
     * The ziplane paths of the map. Each path is a list of P0, P1, and P2 points, describing the cubic spline.
     */
    readonly zipline_paths: Array<ZiplanePathV1>;
};

