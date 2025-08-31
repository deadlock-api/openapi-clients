from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_metadata_order_by import BulkMetadataOrderBy
from ...models.bulk_metadata_order_direction import BulkMetadataOrderDirection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_info: Union[Unset, bool] = True,
    include_objectives: Union[Unset, bool] = UNSET,
    include_mid_boss: Union[Unset, bool] = UNSET,
    include_player_info: Union[Unset, bool] = UNSET,
    include_player_items: Union[Unset, bool] = UNSET,
    include_player_stats: Union[Unset, bool] = UNSET,
    include_player_death_details: Union[Unset, bool] = UNSET,
    match_ids: Union[None, Unset, list[int]] = UNSET,
    min_unix_timestamp: Union[None, Unset, int] = UNSET,
    max_unix_timestamp: Union[None, Unset, int] = UNSET,
    min_duration_s: Union[None, Unset, int] = UNSET,
    max_duration_s: Union[None, Unset, int] = UNSET,
    min_average_badge: Union[None, Unset, int] = UNSET,
    max_average_badge: Union[None, Unset, int] = UNSET,
    min_match_id: Union[None, Unset, int] = UNSET,
    max_match_id: Union[None, Unset, int] = UNSET,
    is_high_skill_range_parties: Union[None, Unset, bool] = UNSET,
    is_low_pri_pool: Union[None, Unset, bool] = UNSET,
    is_new_player_pool: Union[None, Unset, bool] = UNSET,
    account_ids: Union[None, Unset, list[int]] = UNSET,
    order_by: Union[Unset, BulkMetadataOrderBy] = UNSET,
    order_direction: Union[Unset, BulkMetadataOrderDirection] = UNSET,
    limit: Union[Unset, int] = 1000,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["include_info"] = include_info

    params["include_objectives"] = include_objectives

    params["include_mid_boss"] = include_mid_boss

    params["include_player_info"] = include_player_info

    params["include_player_items"] = include_player_items

    params["include_player_stats"] = include_player_stats

    params["include_player_death_details"] = include_player_death_details

    json_match_ids: Union[None, Unset, list[int]]
    if isinstance(match_ids, Unset):
        json_match_ids = UNSET
    elif isinstance(match_ids, list):
        json_match_ids = match_ids

    else:
        json_match_ids = match_ids
    params["match_ids"] = json_match_ids

    json_min_unix_timestamp: Union[None, Unset, int]
    if isinstance(min_unix_timestamp, Unset):
        json_min_unix_timestamp = UNSET
    else:
        json_min_unix_timestamp = min_unix_timestamp
    params["min_unix_timestamp"] = json_min_unix_timestamp

    json_max_unix_timestamp: Union[None, Unset, int]
    if isinstance(max_unix_timestamp, Unset):
        json_max_unix_timestamp = UNSET
    else:
        json_max_unix_timestamp = max_unix_timestamp
    params["max_unix_timestamp"] = json_max_unix_timestamp

    json_min_duration_s: Union[None, Unset, int]
    if isinstance(min_duration_s, Unset):
        json_min_duration_s = UNSET
    else:
        json_min_duration_s = min_duration_s
    params["min_duration_s"] = json_min_duration_s

    json_max_duration_s: Union[None, Unset, int]
    if isinstance(max_duration_s, Unset):
        json_max_duration_s = UNSET
    else:
        json_max_duration_s = max_duration_s
    params["max_duration_s"] = json_max_duration_s

    json_min_average_badge: Union[None, Unset, int]
    if isinstance(min_average_badge, Unset):
        json_min_average_badge = UNSET
    else:
        json_min_average_badge = min_average_badge
    params["min_average_badge"] = json_min_average_badge

    json_max_average_badge: Union[None, Unset, int]
    if isinstance(max_average_badge, Unset):
        json_max_average_badge = UNSET
    else:
        json_max_average_badge = max_average_badge
    params["max_average_badge"] = json_max_average_badge

    json_min_match_id: Union[None, Unset, int]
    if isinstance(min_match_id, Unset):
        json_min_match_id = UNSET
    else:
        json_min_match_id = min_match_id
    params["min_match_id"] = json_min_match_id

    json_max_match_id: Union[None, Unset, int]
    if isinstance(max_match_id, Unset):
        json_max_match_id = UNSET
    else:
        json_max_match_id = max_match_id
    params["max_match_id"] = json_max_match_id

    json_is_high_skill_range_parties: Union[None, Unset, bool]
    if isinstance(is_high_skill_range_parties, Unset):
        json_is_high_skill_range_parties = UNSET
    else:
        json_is_high_skill_range_parties = is_high_skill_range_parties
    params["is_high_skill_range_parties"] = json_is_high_skill_range_parties

    json_is_low_pri_pool: Union[None, Unset, bool]
    if isinstance(is_low_pri_pool, Unset):
        json_is_low_pri_pool = UNSET
    else:
        json_is_low_pri_pool = is_low_pri_pool
    params["is_low_pri_pool"] = json_is_low_pri_pool

    json_is_new_player_pool: Union[None, Unset, bool]
    if isinstance(is_new_player_pool, Unset):
        json_is_new_player_pool = UNSET
    else:
        json_is_new_player_pool = is_new_player_pool
    params["is_new_player_pool"] = json_is_new_player_pool

    json_account_ids: Union[None, Unset, list[int]]
    if isinstance(account_ids, Unset):
        json_account_ids = UNSET
    elif isinstance(account_ids, list):
        json_account_ids = account_ids

    else:
        json_account_ids = account_ids
    params["account_ids"] = json_account_ids

    json_order_by: Union[Unset, str] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["order_by"] = json_order_by

    json_order_direction: Union[Unset, str] = UNSET
    if not isinstance(order_direction, Unset):
        json_order_direction = order_direction.value

    params["order_direction"] = json_order_direction

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/matches/metadata",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list[int]]]:
    if response.status_code == 200:
        response_200 = cast(list[int], response.content)

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, list[int]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    include_info: Union[Unset, bool] = True,
    include_objectives: Union[Unset, bool] = UNSET,
    include_mid_boss: Union[Unset, bool] = UNSET,
    include_player_info: Union[Unset, bool] = UNSET,
    include_player_items: Union[Unset, bool] = UNSET,
    include_player_stats: Union[Unset, bool] = UNSET,
    include_player_death_details: Union[Unset, bool] = UNSET,
    match_ids: Union[None, Unset, list[int]] = UNSET,
    min_unix_timestamp: Union[None, Unset, int] = UNSET,
    max_unix_timestamp: Union[None, Unset, int] = UNSET,
    min_duration_s: Union[None, Unset, int] = UNSET,
    max_duration_s: Union[None, Unset, int] = UNSET,
    min_average_badge: Union[None, Unset, int] = UNSET,
    max_average_badge: Union[None, Unset, int] = UNSET,
    min_match_id: Union[None, Unset, int] = UNSET,
    max_match_id: Union[None, Unset, int] = UNSET,
    is_high_skill_range_parties: Union[None, Unset, bool] = UNSET,
    is_low_pri_pool: Union[None, Unset, bool] = UNSET,
    is_new_player_pool: Union[None, Unset, bool] = UNSET,
    account_ids: Union[None, Unset, list[int]] = UNSET,
    order_by: Union[Unset, BulkMetadataOrderBy] = UNSET,
    order_direction: Union[Unset, BulkMetadataOrderDirection] = UNSET,
    limit: Union[Unset, int] = 1000,
) -> Response[Union[Any, list[int]]]:
    """Bulk Metadata


    This endpoints lets you fetch multiple match metadata at once. The response is a JSON array of match
    metadata.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 4req/s |
    | Key | - |
    | Global | 10req/s |


    Args:
        include_info (Union[Unset, bool]):  Default: True.
        include_objectives (Union[Unset, bool]):
        include_mid_boss (Union[Unset, bool]):
        include_player_info (Union[Unset, bool]):
        include_player_items (Union[Unset, bool]):
        include_player_stats (Union[Unset, bool]):
        include_player_death_details (Union[Unset, bool]):
        match_ids (Union[None, Unset, list[int]]):
        min_unix_timestamp (Union[None, Unset, int]):
        max_unix_timestamp (Union[None, Unset, int]):
        min_duration_s (Union[None, Unset, int]):
        max_duration_s (Union[None, Unset, int]):
        min_average_badge (Union[None, Unset, int]):
        max_average_badge (Union[None, Unset, int]):
        min_match_id (Union[None, Unset, int]):
        max_match_id (Union[None, Unset, int]):
        is_high_skill_range_parties (Union[None, Unset, bool]):
        is_low_pri_pool (Union[None, Unset, bool]):
        is_new_player_pool (Union[None, Unset, bool]):
        account_ids (Union[None, Unset, list[int]]):
        order_by (Union[Unset, BulkMetadataOrderBy]):
        order_direction (Union[Unset, BulkMetadataOrderDirection]):
        limit (Union[Unset, int]):  Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list[int]]]
    """

    kwargs = _get_kwargs(
        include_info=include_info,
        include_objectives=include_objectives,
        include_mid_boss=include_mid_boss,
        include_player_info=include_player_info,
        include_player_items=include_player_items,
        include_player_stats=include_player_stats,
        include_player_death_details=include_player_death_details,
        match_ids=match_ids,
        min_unix_timestamp=min_unix_timestamp,
        max_unix_timestamp=max_unix_timestamp,
        min_duration_s=min_duration_s,
        max_duration_s=max_duration_s,
        min_average_badge=min_average_badge,
        max_average_badge=max_average_badge,
        min_match_id=min_match_id,
        max_match_id=max_match_id,
        is_high_skill_range_parties=is_high_skill_range_parties,
        is_low_pri_pool=is_low_pri_pool,
        is_new_player_pool=is_new_player_pool,
        account_ids=account_ids,
        order_by=order_by,
        order_direction=order_direction,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    include_info: Union[Unset, bool] = True,
    include_objectives: Union[Unset, bool] = UNSET,
    include_mid_boss: Union[Unset, bool] = UNSET,
    include_player_info: Union[Unset, bool] = UNSET,
    include_player_items: Union[Unset, bool] = UNSET,
    include_player_stats: Union[Unset, bool] = UNSET,
    include_player_death_details: Union[Unset, bool] = UNSET,
    match_ids: Union[None, Unset, list[int]] = UNSET,
    min_unix_timestamp: Union[None, Unset, int] = UNSET,
    max_unix_timestamp: Union[None, Unset, int] = UNSET,
    min_duration_s: Union[None, Unset, int] = UNSET,
    max_duration_s: Union[None, Unset, int] = UNSET,
    min_average_badge: Union[None, Unset, int] = UNSET,
    max_average_badge: Union[None, Unset, int] = UNSET,
    min_match_id: Union[None, Unset, int] = UNSET,
    max_match_id: Union[None, Unset, int] = UNSET,
    is_high_skill_range_parties: Union[None, Unset, bool] = UNSET,
    is_low_pri_pool: Union[None, Unset, bool] = UNSET,
    is_new_player_pool: Union[None, Unset, bool] = UNSET,
    account_ids: Union[None, Unset, list[int]] = UNSET,
    order_by: Union[Unset, BulkMetadataOrderBy] = UNSET,
    order_direction: Union[Unset, BulkMetadataOrderDirection] = UNSET,
    limit: Union[Unset, int] = 1000,
) -> Optional[Union[Any, list[int]]]:
    """Bulk Metadata


    This endpoints lets you fetch multiple match metadata at once. The response is a JSON array of match
    metadata.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 4req/s |
    | Key | - |
    | Global | 10req/s |


    Args:
        include_info (Union[Unset, bool]):  Default: True.
        include_objectives (Union[Unset, bool]):
        include_mid_boss (Union[Unset, bool]):
        include_player_info (Union[Unset, bool]):
        include_player_items (Union[Unset, bool]):
        include_player_stats (Union[Unset, bool]):
        include_player_death_details (Union[Unset, bool]):
        match_ids (Union[None, Unset, list[int]]):
        min_unix_timestamp (Union[None, Unset, int]):
        max_unix_timestamp (Union[None, Unset, int]):
        min_duration_s (Union[None, Unset, int]):
        max_duration_s (Union[None, Unset, int]):
        min_average_badge (Union[None, Unset, int]):
        max_average_badge (Union[None, Unset, int]):
        min_match_id (Union[None, Unset, int]):
        max_match_id (Union[None, Unset, int]):
        is_high_skill_range_parties (Union[None, Unset, bool]):
        is_low_pri_pool (Union[None, Unset, bool]):
        is_new_player_pool (Union[None, Unset, bool]):
        account_ids (Union[None, Unset, list[int]]):
        order_by (Union[Unset, BulkMetadataOrderBy]):
        order_direction (Union[Unset, BulkMetadataOrderDirection]):
        limit (Union[Unset, int]):  Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list[int]]
    """

    return sync_detailed(
        client=client,
        include_info=include_info,
        include_objectives=include_objectives,
        include_mid_boss=include_mid_boss,
        include_player_info=include_player_info,
        include_player_items=include_player_items,
        include_player_stats=include_player_stats,
        include_player_death_details=include_player_death_details,
        match_ids=match_ids,
        min_unix_timestamp=min_unix_timestamp,
        max_unix_timestamp=max_unix_timestamp,
        min_duration_s=min_duration_s,
        max_duration_s=max_duration_s,
        min_average_badge=min_average_badge,
        max_average_badge=max_average_badge,
        min_match_id=min_match_id,
        max_match_id=max_match_id,
        is_high_skill_range_parties=is_high_skill_range_parties,
        is_low_pri_pool=is_low_pri_pool,
        is_new_player_pool=is_new_player_pool,
        account_ids=account_ids,
        order_by=order_by,
        order_direction=order_direction,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    include_info: Union[Unset, bool] = True,
    include_objectives: Union[Unset, bool] = UNSET,
    include_mid_boss: Union[Unset, bool] = UNSET,
    include_player_info: Union[Unset, bool] = UNSET,
    include_player_items: Union[Unset, bool] = UNSET,
    include_player_stats: Union[Unset, bool] = UNSET,
    include_player_death_details: Union[Unset, bool] = UNSET,
    match_ids: Union[None, Unset, list[int]] = UNSET,
    min_unix_timestamp: Union[None, Unset, int] = UNSET,
    max_unix_timestamp: Union[None, Unset, int] = UNSET,
    min_duration_s: Union[None, Unset, int] = UNSET,
    max_duration_s: Union[None, Unset, int] = UNSET,
    min_average_badge: Union[None, Unset, int] = UNSET,
    max_average_badge: Union[None, Unset, int] = UNSET,
    min_match_id: Union[None, Unset, int] = UNSET,
    max_match_id: Union[None, Unset, int] = UNSET,
    is_high_skill_range_parties: Union[None, Unset, bool] = UNSET,
    is_low_pri_pool: Union[None, Unset, bool] = UNSET,
    is_new_player_pool: Union[None, Unset, bool] = UNSET,
    account_ids: Union[None, Unset, list[int]] = UNSET,
    order_by: Union[Unset, BulkMetadataOrderBy] = UNSET,
    order_direction: Union[Unset, BulkMetadataOrderDirection] = UNSET,
    limit: Union[Unset, int] = 1000,
) -> Response[Union[Any, list[int]]]:
    """Bulk Metadata


    This endpoints lets you fetch multiple match metadata at once. The response is a JSON array of match
    metadata.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 4req/s |
    | Key | - |
    | Global | 10req/s |


    Args:
        include_info (Union[Unset, bool]):  Default: True.
        include_objectives (Union[Unset, bool]):
        include_mid_boss (Union[Unset, bool]):
        include_player_info (Union[Unset, bool]):
        include_player_items (Union[Unset, bool]):
        include_player_stats (Union[Unset, bool]):
        include_player_death_details (Union[Unset, bool]):
        match_ids (Union[None, Unset, list[int]]):
        min_unix_timestamp (Union[None, Unset, int]):
        max_unix_timestamp (Union[None, Unset, int]):
        min_duration_s (Union[None, Unset, int]):
        max_duration_s (Union[None, Unset, int]):
        min_average_badge (Union[None, Unset, int]):
        max_average_badge (Union[None, Unset, int]):
        min_match_id (Union[None, Unset, int]):
        max_match_id (Union[None, Unset, int]):
        is_high_skill_range_parties (Union[None, Unset, bool]):
        is_low_pri_pool (Union[None, Unset, bool]):
        is_new_player_pool (Union[None, Unset, bool]):
        account_ids (Union[None, Unset, list[int]]):
        order_by (Union[Unset, BulkMetadataOrderBy]):
        order_direction (Union[Unset, BulkMetadataOrderDirection]):
        limit (Union[Unset, int]):  Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list[int]]]
    """

    kwargs = _get_kwargs(
        include_info=include_info,
        include_objectives=include_objectives,
        include_mid_boss=include_mid_boss,
        include_player_info=include_player_info,
        include_player_items=include_player_items,
        include_player_stats=include_player_stats,
        include_player_death_details=include_player_death_details,
        match_ids=match_ids,
        min_unix_timestamp=min_unix_timestamp,
        max_unix_timestamp=max_unix_timestamp,
        min_duration_s=min_duration_s,
        max_duration_s=max_duration_s,
        min_average_badge=min_average_badge,
        max_average_badge=max_average_badge,
        min_match_id=min_match_id,
        max_match_id=max_match_id,
        is_high_skill_range_parties=is_high_skill_range_parties,
        is_low_pri_pool=is_low_pri_pool,
        is_new_player_pool=is_new_player_pool,
        account_ids=account_ids,
        order_by=order_by,
        order_direction=order_direction,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    include_info: Union[Unset, bool] = True,
    include_objectives: Union[Unset, bool] = UNSET,
    include_mid_boss: Union[Unset, bool] = UNSET,
    include_player_info: Union[Unset, bool] = UNSET,
    include_player_items: Union[Unset, bool] = UNSET,
    include_player_stats: Union[Unset, bool] = UNSET,
    include_player_death_details: Union[Unset, bool] = UNSET,
    match_ids: Union[None, Unset, list[int]] = UNSET,
    min_unix_timestamp: Union[None, Unset, int] = UNSET,
    max_unix_timestamp: Union[None, Unset, int] = UNSET,
    min_duration_s: Union[None, Unset, int] = UNSET,
    max_duration_s: Union[None, Unset, int] = UNSET,
    min_average_badge: Union[None, Unset, int] = UNSET,
    max_average_badge: Union[None, Unset, int] = UNSET,
    min_match_id: Union[None, Unset, int] = UNSET,
    max_match_id: Union[None, Unset, int] = UNSET,
    is_high_skill_range_parties: Union[None, Unset, bool] = UNSET,
    is_low_pri_pool: Union[None, Unset, bool] = UNSET,
    is_new_player_pool: Union[None, Unset, bool] = UNSET,
    account_ids: Union[None, Unset, list[int]] = UNSET,
    order_by: Union[Unset, BulkMetadataOrderBy] = UNSET,
    order_direction: Union[Unset, BulkMetadataOrderDirection] = UNSET,
    limit: Union[Unset, int] = 1000,
) -> Optional[Union[Any, list[int]]]:
    """Bulk Metadata


    This endpoints lets you fetch multiple match metadata at once. The response is a JSON array of match
    metadata.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 4req/s |
    | Key | - |
    | Global | 10req/s |


    Args:
        include_info (Union[Unset, bool]):  Default: True.
        include_objectives (Union[Unset, bool]):
        include_mid_boss (Union[Unset, bool]):
        include_player_info (Union[Unset, bool]):
        include_player_items (Union[Unset, bool]):
        include_player_stats (Union[Unset, bool]):
        include_player_death_details (Union[Unset, bool]):
        match_ids (Union[None, Unset, list[int]]):
        min_unix_timestamp (Union[None, Unset, int]):
        max_unix_timestamp (Union[None, Unset, int]):
        min_duration_s (Union[None, Unset, int]):
        max_duration_s (Union[None, Unset, int]):
        min_average_badge (Union[None, Unset, int]):
        max_average_badge (Union[None, Unset, int]):
        min_match_id (Union[None, Unset, int]):
        max_match_id (Union[None, Unset, int]):
        is_high_skill_range_parties (Union[None, Unset, bool]):
        is_low_pri_pool (Union[None, Unset, bool]):
        is_new_player_pool (Union[None, Unset, bool]):
        account_ids (Union[None, Unset, list[int]]):
        order_by (Union[Unset, BulkMetadataOrderBy]):
        order_direction (Union[Unset, BulkMetadataOrderDirection]):
        limit (Union[Unset, int]):  Default: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list[int]]
    """

    return (
        await asyncio_detailed(
            client=client,
            include_info=include_info,
            include_objectives=include_objectives,
            include_mid_boss=include_mid_boss,
            include_player_info=include_player_info,
            include_player_items=include_player_items,
            include_player_stats=include_player_stats,
            include_player_death_details=include_player_death_details,
            match_ids=match_ids,
            min_unix_timestamp=min_unix_timestamp,
            max_unix_timestamp=max_unix_timestamp,
            min_duration_s=min_duration_s,
            max_duration_s=max_duration_s,
            min_average_badge=min_average_badge,
            max_average_badge=max_average_badge,
            min_match_id=min_match_id,
            max_match_id=max_match_id,
            is_high_skill_range_parties=is_high_skill_range_parties,
            is_low_pri_pool=is_low_pri_pool,
            is_new_player_pool=is_new_player_pool,
            account_ids=account_ids,
            order_by=order_by,
            order_direction=order_direction,
            limit=limit,
        )
    ).parsed
