from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.build import Build
from ...models.search_builds_sort_by import SearchBuildsSortBy
from ...models.search_builds_sort_direction import SearchBuildsSortDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    min_unix_timestamp: Union[Unset, int] = UNSET,
    max_unix_timestamp: Union[Unset, int] = UNSET,
    min_published_unix_timestamp: Union[Unset, int] = UNSET,
    max_published_unix_timestamp: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, SearchBuildsSortBy] = UNSET,
    start: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 100,
    sort_direction: Union[Unset, SearchBuildsSortDirection] = UNSET,
    search_name: Union[Unset, str] = UNSET,
    search_description: Union[Unset, str] = UNSET,
    only_latest: Union[Unset, bool] = UNSET,
    language: Union[Unset, int] = UNSET,
    build_id: Union[Unset, int] = UNSET,
    version: Union[Unset, int] = UNSET,
    hero_id: Union[Unset, int] = UNSET,
    tag: Union[Unset, int] = UNSET,
    rollup_category: Union[Unset, int] = UNSET,
    author_id: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["min_unix_timestamp"] = min_unix_timestamp

    params["max_unix_timestamp"] = max_unix_timestamp

    params["min_published_unix_timestamp"] = min_published_unix_timestamp

    params["max_published_unix_timestamp"] = max_published_unix_timestamp

    json_sort_by: Union[Unset, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sort_by"] = json_sort_by

    params["start"] = start

    params["limit"] = limit

    json_sort_direction: Union[Unset, str] = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sort_direction"] = json_sort_direction

    params["search_name"] = search_name

    params["search_description"] = search_description

    params["only_latest"] = only_latest

    params["language"] = language

    params["build_id"] = build_id

    params["version"] = version

    params["hero_id"] = hero_id

    params["tag"] = tag

    params["rollup_category"] = rollup_category

    params["author_id"] = author_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/builds",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["Build"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Build.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, list["Build"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    min_unix_timestamp: Union[Unset, int] = UNSET,
    max_unix_timestamp: Union[Unset, int] = UNSET,
    min_published_unix_timestamp: Union[Unset, int] = UNSET,
    max_published_unix_timestamp: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, SearchBuildsSortBy] = UNSET,
    start: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 100,
    sort_direction: Union[Unset, SearchBuildsSortDirection] = UNSET,
    search_name: Union[Unset, str] = UNSET,
    search_description: Union[Unset, str] = UNSET,
    only_latest: Union[Unset, bool] = UNSET,
    language: Union[Unset, int] = UNSET,
    build_id: Union[Unset, int] = UNSET,
    version: Union[Unset, int] = UNSET,
    hero_id: Union[Unset, int] = UNSET,
    tag: Union[Unset, int] = UNSET,
    rollup_category: Union[Unset, int] = UNSET,
    author_id: Union[Unset, int] = UNSET,
) -> Response[Union[Any, list["Build"]]]:
    """Search


    Search for builds based on various criteria.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        min_unix_timestamp (Union[Unset, int]):
        max_unix_timestamp (Union[Unset, int]):
        min_published_unix_timestamp (Union[Unset, int]):
        max_published_unix_timestamp (Union[Unset, int]):
        sort_by (Union[Unset, SearchBuildsSortBy]):
        start (Union[Unset, int]):
        limit (Union[Unset, int]):  Default: 100.
        sort_direction (Union[Unset, SearchBuildsSortDirection]):
        search_name (Union[Unset, str]):
        search_description (Union[Unset, str]):
        only_latest (Union[Unset, bool]):
        language (Union[Unset, int]):
        build_id (Union[Unset, int]):
        version (Union[Unset, int]):
        hero_id (Union[Unset, int]):
        tag (Union[Unset, int]):
        rollup_category (Union[Unset, int]):
        author_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['Build']]]
    """

    kwargs = _get_kwargs(
        min_unix_timestamp=min_unix_timestamp,
        max_unix_timestamp=max_unix_timestamp,
        min_published_unix_timestamp=min_published_unix_timestamp,
        max_published_unix_timestamp=max_published_unix_timestamp,
        sort_by=sort_by,
        start=start,
        limit=limit,
        sort_direction=sort_direction,
        search_name=search_name,
        search_description=search_description,
        only_latest=only_latest,
        language=language,
        build_id=build_id,
        version=version,
        hero_id=hero_id,
        tag=tag,
        rollup_category=rollup_category,
        author_id=author_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    min_unix_timestamp: Union[Unset, int] = UNSET,
    max_unix_timestamp: Union[Unset, int] = UNSET,
    min_published_unix_timestamp: Union[Unset, int] = UNSET,
    max_published_unix_timestamp: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, SearchBuildsSortBy] = UNSET,
    start: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 100,
    sort_direction: Union[Unset, SearchBuildsSortDirection] = UNSET,
    search_name: Union[Unset, str] = UNSET,
    search_description: Union[Unset, str] = UNSET,
    only_latest: Union[Unset, bool] = UNSET,
    language: Union[Unset, int] = UNSET,
    build_id: Union[Unset, int] = UNSET,
    version: Union[Unset, int] = UNSET,
    hero_id: Union[Unset, int] = UNSET,
    tag: Union[Unset, int] = UNSET,
    rollup_category: Union[Unset, int] = UNSET,
    author_id: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, list["Build"]]]:
    """Search


    Search for builds based on various criteria.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        min_unix_timestamp (Union[Unset, int]):
        max_unix_timestamp (Union[Unset, int]):
        min_published_unix_timestamp (Union[Unset, int]):
        max_published_unix_timestamp (Union[Unset, int]):
        sort_by (Union[Unset, SearchBuildsSortBy]):
        start (Union[Unset, int]):
        limit (Union[Unset, int]):  Default: 100.
        sort_direction (Union[Unset, SearchBuildsSortDirection]):
        search_name (Union[Unset, str]):
        search_description (Union[Unset, str]):
        only_latest (Union[Unset, bool]):
        language (Union[Unset, int]):
        build_id (Union[Unset, int]):
        version (Union[Unset, int]):
        hero_id (Union[Unset, int]):
        tag (Union[Unset, int]):
        rollup_category (Union[Unset, int]):
        author_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['Build']]
    """

    return sync_detailed(
        client=client,
        min_unix_timestamp=min_unix_timestamp,
        max_unix_timestamp=max_unix_timestamp,
        min_published_unix_timestamp=min_published_unix_timestamp,
        max_published_unix_timestamp=max_published_unix_timestamp,
        sort_by=sort_by,
        start=start,
        limit=limit,
        sort_direction=sort_direction,
        search_name=search_name,
        search_description=search_description,
        only_latest=only_latest,
        language=language,
        build_id=build_id,
        version=version,
        hero_id=hero_id,
        tag=tag,
        rollup_category=rollup_category,
        author_id=author_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    min_unix_timestamp: Union[Unset, int] = UNSET,
    max_unix_timestamp: Union[Unset, int] = UNSET,
    min_published_unix_timestamp: Union[Unset, int] = UNSET,
    max_published_unix_timestamp: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, SearchBuildsSortBy] = UNSET,
    start: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 100,
    sort_direction: Union[Unset, SearchBuildsSortDirection] = UNSET,
    search_name: Union[Unset, str] = UNSET,
    search_description: Union[Unset, str] = UNSET,
    only_latest: Union[Unset, bool] = UNSET,
    language: Union[Unset, int] = UNSET,
    build_id: Union[Unset, int] = UNSET,
    version: Union[Unset, int] = UNSET,
    hero_id: Union[Unset, int] = UNSET,
    tag: Union[Unset, int] = UNSET,
    rollup_category: Union[Unset, int] = UNSET,
    author_id: Union[Unset, int] = UNSET,
) -> Response[Union[Any, list["Build"]]]:
    """Search


    Search for builds based on various criteria.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        min_unix_timestamp (Union[Unset, int]):
        max_unix_timestamp (Union[Unset, int]):
        min_published_unix_timestamp (Union[Unset, int]):
        max_published_unix_timestamp (Union[Unset, int]):
        sort_by (Union[Unset, SearchBuildsSortBy]):
        start (Union[Unset, int]):
        limit (Union[Unset, int]):  Default: 100.
        sort_direction (Union[Unset, SearchBuildsSortDirection]):
        search_name (Union[Unset, str]):
        search_description (Union[Unset, str]):
        only_latest (Union[Unset, bool]):
        language (Union[Unset, int]):
        build_id (Union[Unset, int]):
        version (Union[Unset, int]):
        hero_id (Union[Unset, int]):
        tag (Union[Unset, int]):
        rollup_category (Union[Unset, int]):
        author_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['Build']]]
    """

    kwargs = _get_kwargs(
        min_unix_timestamp=min_unix_timestamp,
        max_unix_timestamp=max_unix_timestamp,
        min_published_unix_timestamp=min_published_unix_timestamp,
        max_published_unix_timestamp=max_published_unix_timestamp,
        sort_by=sort_by,
        start=start,
        limit=limit,
        sort_direction=sort_direction,
        search_name=search_name,
        search_description=search_description,
        only_latest=only_latest,
        language=language,
        build_id=build_id,
        version=version,
        hero_id=hero_id,
        tag=tag,
        rollup_category=rollup_category,
        author_id=author_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    min_unix_timestamp: Union[Unset, int] = UNSET,
    max_unix_timestamp: Union[Unset, int] = UNSET,
    min_published_unix_timestamp: Union[Unset, int] = UNSET,
    max_published_unix_timestamp: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, SearchBuildsSortBy] = UNSET,
    start: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = 100,
    sort_direction: Union[Unset, SearchBuildsSortDirection] = UNSET,
    search_name: Union[Unset, str] = UNSET,
    search_description: Union[Unset, str] = UNSET,
    only_latest: Union[Unset, bool] = UNSET,
    language: Union[Unset, int] = UNSET,
    build_id: Union[Unset, int] = UNSET,
    version: Union[Unset, int] = UNSET,
    hero_id: Union[Unset, int] = UNSET,
    tag: Union[Unset, int] = UNSET,
    rollup_category: Union[Unset, int] = UNSET,
    author_id: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, list["Build"]]]:
    """Search


    Search for builds based on various criteria.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        min_unix_timestamp (Union[Unset, int]):
        max_unix_timestamp (Union[Unset, int]):
        min_published_unix_timestamp (Union[Unset, int]):
        max_published_unix_timestamp (Union[Unset, int]):
        sort_by (Union[Unset, SearchBuildsSortBy]):
        start (Union[Unset, int]):
        limit (Union[Unset, int]):  Default: 100.
        sort_direction (Union[Unset, SearchBuildsSortDirection]):
        search_name (Union[Unset, str]):
        search_description (Union[Unset, str]):
        only_latest (Union[Unset, bool]):
        language (Union[Unset, int]):
        build_id (Union[Unset, int]):
        version (Union[Unset, int]):
        hero_id (Union[Unset, int]):
        tag (Union[Unset, int]):
        rollup_category (Union[Unset, int]):
        author_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['Build']]
    """

    return (
        await asyncio_detailed(
            client=client,
            min_unix_timestamp=min_unix_timestamp,
            max_unix_timestamp=max_unix_timestamp,
            min_published_unix_timestamp=min_published_unix_timestamp,
            max_published_unix_timestamp=max_published_unix_timestamp,
            sort_by=sort_by,
            start=start,
            limit=limit,
            sort_direction=sort_direction,
            search_name=search_name,
            search_description=search_description,
            only_latest=only_latest,
            language=language,
            build_id=build_id,
            version=version,
            hero_id=hero_id,
            tag=tag,
            rollup_category=rollup_category,
            author_id=author_id,
        )
    ).parsed
