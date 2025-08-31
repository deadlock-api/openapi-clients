from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.build_item_stats import BuildItemStats
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    hero_id: Union[None, Unset, int] = UNSET,
    min_last_updated_unix_timestamp: Union[None, Unset, int] = 1754006400,
    max_last_updated_unix_timestamp: Union[None, Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_hero_id: Union[None, Unset, int]
    if isinstance(hero_id, Unset):
        json_hero_id = UNSET
    else:
        json_hero_id = hero_id
    params["hero_id"] = json_hero_id

    json_min_last_updated_unix_timestamp: Union[None, Unset, int]
    if isinstance(min_last_updated_unix_timestamp, Unset):
        json_min_last_updated_unix_timestamp = UNSET
    else:
        json_min_last_updated_unix_timestamp = min_last_updated_unix_timestamp
    params["min_last_updated_unix_timestamp"] = json_min_last_updated_unix_timestamp

    json_max_last_updated_unix_timestamp: Union[None, Unset, int]
    if isinstance(max_last_updated_unix_timestamp, Unset):
        json_max_last_updated_unix_timestamp = UNSET
    else:
        json_max_last_updated_unix_timestamp = max_last_updated_unix_timestamp
    params["max_last_updated_unix_timestamp"] = json_max_last_updated_unix_timestamp

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/build-item-stats",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["BuildItemStats"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BuildItemStats.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["BuildItemStats"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    hero_id: Union[None, Unset, int] = UNSET,
    min_last_updated_unix_timestamp: Union[None, Unset, int] = 1754006400,
    max_last_updated_unix_timestamp: Union[None, Unset, int] = UNSET,
) -> Response[Union[Any, list["BuildItemStats"]]]:
    """Build Item Stats


    Retrieves item statistics from hero builds.

    Results are cached for **1 hour** based on the unique combination of query parameters provided.
    Subsequent identical requests within this timeframe will receive the cached response.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        hero_id (Union[None, Unset, int]):
        min_last_updated_unix_timestamp (Union[None, Unset, int]):  Default: 1754006400.
        max_last_updated_unix_timestamp (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['BuildItemStats']]]
    """

    kwargs = _get_kwargs(
        hero_id=hero_id,
        min_last_updated_unix_timestamp=min_last_updated_unix_timestamp,
        max_last_updated_unix_timestamp=max_last_updated_unix_timestamp,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    hero_id: Union[None, Unset, int] = UNSET,
    min_last_updated_unix_timestamp: Union[None, Unset, int] = 1754006400,
    max_last_updated_unix_timestamp: Union[None, Unset, int] = UNSET,
) -> Optional[Union[Any, list["BuildItemStats"]]]:
    """Build Item Stats


    Retrieves item statistics from hero builds.

    Results are cached for **1 hour** based on the unique combination of query parameters provided.
    Subsequent identical requests within this timeframe will receive the cached response.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        hero_id (Union[None, Unset, int]):
        min_last_updated_unix_timestamp (Union[None, Unset, int]):  Default: 1754006400.
        max_last_updated_unix_timestamp (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['BuildItemStats']]
    """

    return sync_detailed(
        client=client,
        hero_id=hero_id,
        min_last_updated_unix_timestamp=min_last_updated_unix_timestamp,
        max_last_updated_unix_timestamp=max_last_updated_unix_timestamp,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    hero_id: Union[None, Unset, int] = UNSET,
    min_last_updated_unix_timestamp: Union[None, Unset, int] = 1754006400,
    max_last_updated_unix_timestamp: Union[None, Unset, int] = UNSET,
) -> Response[Union[Any, list["BuildItemStats"]]]:
    """Build Item Stats


    Retrieves item statistics from hero builds.

    Results are cached for **1 hour** based on the unique combination of query parameters provided.
    Subsequent identical requests within this timeframe will receive the cached response.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        hero_id (Union[None, Unset, int]):
        min_last_updated_unix_timestamp (Union[None, Unset, int]):  Default: 1754006400.
        max_last_updated_unix_timestamp (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['BuildItemStats']]]
    """

    kwargs = _get_kwargs(
        hero_id=hero_id,
        min_last_updated_unix_timestamp=min_last_updated_unix_timestamp,
        max_last_updated_unix_timestamp=max_last_updated_unix_timestamp,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    hero_id: Union[None, Unset, int] = UNSET,
    min_last_updated_unix_timestamp: Union[None, Unset, int] = 1754006400,
    max_last_updated_unix_timestamp: Union[None, Unset, int] = UNSET,
) -> Optional[Union[Any, list["BuildItemStats"]]]:
    """Build Item Stats


    Retrieves item statistics from hero builds.

    Results are cached for **1 hour** based on the unique combination of query parameters provided.
    Subsequent identical requests within this timeframe will receive the cached response.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        hero_id (Union[None, Unset, int]):
        min_last_updated_unix_timestamp (Union[None, Unset, int]):  Default: 1754006400.
        max_last_updated_unix_timestamp (Union[None, Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['BuildItemStats']]
    """

    return (
        await asyncio_detailed(
            client=client,
            hero_id=hero_id,
            min_last_updated_unix_timestamp=min_last_updated_unix_timestamp,
            max_last_updated_unix_timestamp=max_last_updated_unix_timestamp,
        )
    ).parsed
