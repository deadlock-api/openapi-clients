from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.enemy_stats import EnemyStats
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: int,
    *,
    min_unix_timestamp: Union[None, Unset, int] = UNSET,
    max_unix_timestamp: Union[None, Unset, int] = UNSET,
    min_duration_s: Union[None, Unset, int] = UNSET,
    max_duration_s: Union[None, Unset, int] = UNSET,
    min_average_badge: Union[None, Unset, int] = UNSET,
    max_average_badge: Union[None, Unset, int] = UNSET,
    min_match_id: Union[None, Unset, int] = UNSET,
    max_match_id: Union[None, Unset, int] = UNSET,
    min_matches_played: Union[None, Unset, int] = UNSET,
    max_matches_played: Union[None, Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

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

    json_min_matches_played: Union[None, Unset, int]
    if isinstance(min_matches_played, Unset):
        json_min_matches_played = UNSET
    else:
        json_min_matches_played = min_matches_played
    params["min_matches_played"] = json_min_matches_played

    json_max_matches_played: Union[None, Unset, int]
    if isinstance(max_matches_played, Unset):
        json_max_matches_played = UNSET
    else:
        json_max_matches_played = max_matches_played
    params["max_matches_played"] = json_max_matches_played

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/players/{account_id}/enemy-stats",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["EnemyStats"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = EnemyStats.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, list["EnemyStats"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    min_unix_timestamp: Union[None, Unset, int] = UNSET,
    max_unix_timestamp: Union[None, Unset, int] = UNSET,
    min_duration_s: Union[None, Unset, int] = UNSET,
    max_duration_s: Union[None, Unset, int] = UNSET,
    min_average_badge: Union[None, Unset, int] = UNSET,
    max_average_badge: Union[None, Unset, int] = UNSET,
    min_match_id: Union[None, Unset, int] = UNSET,
    max_match_id: Union[None, Unset, int] = UNSET,
    min_matches_played: Union[None, Unset, int] = UNSET,
    max_matches_played: Union[None, Unset, int] = UNSET,
) -> Response[Union[Any, list["EnemyStats"]]]:
    """Enemy Stats


    This endpoint returns the enemy stats.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        account_id (int):
        min_unix_timestamp (Union[None, Unset, int]):
        max_unix_timestamp (Union[None, Unset, int]):
        min_duration_s (Union[None, Unset, int]):
        max_duration_s (Union[None, Unset, int]):
        min_average_badge (Union[None, Unset, int]):
        max_average_badge (Union[None, Unset, int]):
        min_match_id (Union[None, Unset, int]):
        max_match_id (Union[None, Unset, int]):
        min_matches_played (Union[None, Unset, int]):
        max_matches_played (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['EnemyStats']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        min_unix_timestamp=min_unix_timestamp,
        max_unix_timestamp=max_unix_timestamp,
        min_duration_s=min_duration_s,
        max_duration_s=max_duration_s,
        min_average_badge=min_average_badge,
        max_average_badge=max_average_badge,
        min_match_id=min_match_id,
        max_match_id=max_match_id,
        min_matches_played=min_matches_played,
        max_matches_played=max_matches_played,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    min_unix_timestamp: Union[None, Unset, int] = UNSET,
    max_unix_timestamp: Union[None, Unset, int] = UNSET,
    min_duration_s: Union[None, Unset, int] = UNSET,
    max_duration_s: Union[None, Unset, int] = UNSET,
    min_average_badge: Union[None, Unset, int] = UNSET,
    max_average_badge: Union[None, Unset, int] = UNSET,
    min_match_id: Union[None, Unset, int] = UNSET,
    max_match_id: Union[None, Unset, int] = UNSET,
    min_matches_played: Union[None, Unset, int] = UNSET,
    max_matches_played: Union[None, Unset, int] = UNSET,
) -> Optional[Union[Any, list["EnemyStats"]]]:
    """Enemy Stats


    This endpoint returns the enemy stats.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        account_id (int):
        min_unix_timestamp (Union[None, Unset, int]):
        max_unix_timestamp (Union[None, Unset, int]):
        min_duration_s (Union[None, Unset, int]):
        max_duration_s (Union[None, Unset, int]):
        min_average_badge (Union[None, Unset, int]):
        max_average_badge (Union[None, Unset, int]):
        min_match_id (Union[None, Unset, int]):
        max_match_id (Union[None, Unset, int]):
        min_matches_played (Union[None, Unset, int]):
        max_matches_played (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['EnemyStats']]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        min_unix_timestamp=min_unix_timestamp,
        max_unix_timestamp=max_unix_timestamp,
        min_duration_s=min_duration_s,
        max_duration_s=max_duration_s,
        min_average_badge=min_average_badge,
        max_average_badge=max_average_badge,
        min_match_id=min_match_id,
        max_match_id=max_match_id,
        min_matches_played=min_matches_played,
        max_matches_played=max_matches_played,
    ).parsed


async def asyncio_detailed(
    account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    min_unix_timestamp: Union[None, Unset, int] = UNSET,
    max_unix_timestamp: Union[None, Unset, int] = UNSET,
    min_duration_s: Union[None, Unset, int] = UNSET,
    max_duration_s: Union[None, Unset, int] = UNSET,
    min_average_badge: Union[None, Unset, int] = UNSET,
    max_average_badge: Union[None, Unset, int] = UNSET,
    min_match_id: Union[None, Unset, int] = UNSET,
    max_match_id: Union[None, Unset, int] = UNSET,
    min_matches_played: Union[None, Unset, int] = UNSET,
    max_matches_played: Union[None, Unset, int] = UNSET,
) -> Response[Union[Any, list["EnemyStats"]]]:
    """Enemy Stats


    This endpoint returns the enemy stats.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        account_id (int):
        min_unix_timestamp (Union[None, Unset, int]):
        max_unix_timestamp (Union[None, Unset, int]):
        min_duration_s (Union[None, Unset, int]):
        max_duration_s (Union[None, Unset, int]):
        min_average_badge (Union[None, Unset, int]):
        max_average_badge (Union[None, Unset, int]):
        min_match_id (Union[None, Unset, int]):
        max_match_id (Union[None, Unset, int]):
        min_matches_played (Union[None, Unset, int]):
        max_matches_played (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['EnemyStats']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        min_unix_timestamp=min_unix_timestamp,
        max_unix_timestamp=max_unix_timestamp,
        min_duration_s=min_duration_s,
        max_duration_s=max_duration_s,
        min_average_badge=min_average_badge,
        max_average_badge=max_average_badge,
        min_match_id=min_match_id,
        max_match_id=max_match_id,
        min_matches_played=min_matches_played,
        max_matches_played=max_matches_played,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    min_unix_timestamp: Union[None, Unset, int] = UNSET,
    max_unix_timestamp: Union[None, Unset, int] = UNSET,
    min_duration_s: Union[None, Unset, int] = UNSET,
    max_duration_s: Union[None, Unset, int] = UNSET,
    min_average_badge: Union[None, Unset, int] = UNSET,
    max_average_badge: Union[None, Unset, int] = UNSET,
    min_match_id: Union[None, Unset, int] = UNSET,
    max_match_id: Union[None, Unset, int] = UNSET,
    min_matches_played: Union[None, Unset, int] = UNSET,
    max_matches_played: Union[None, Unset, int] = UNSET,
) -> Optional[Union[Any, list["EnemyStats"]]]:
    """Enemy Stats


    This endpoint returns the enemy stats.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        account_id (int):
        min_unix_timestamp (Union[None, Unset, int]):
        max_unix_timestamp (Union[None, Unset, int]):
        min_duration_s (Union[None, Unset, int]):
        max_duration_s (Union[None, Unset, int]):
        min_average_badge (Union[None, Unset, int]):
        max_average_badge (Union[None, Unset, int]):
        min_match_id (Union[None, Unset, int]):
        max_match_id (Union[None, Unset, int]):
        min_matches_played (Union[None, Unset, int]):
        max_matches_played (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['EnemyStats']]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            min_unix_timestamp=min_unix_timestamp,
            max_unix_timestamp=max_unix_timestamp,
            min_duration_s=min_duration_s,
            max_duration_s=max_duration_s,
            min_average_badge=min_average_badge,
            max_average_badge=max_average_badge,
            min_match_id=min_match_id,
            max_match_id=max_match_id,
            min_matches_played=min_matches_played,
            max_matches_played=max_matches_played,
        )
    ).parsed
