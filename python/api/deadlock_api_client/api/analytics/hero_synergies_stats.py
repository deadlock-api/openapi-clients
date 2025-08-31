from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hero_synergy_stats import HeroSynergyStats
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    min_unix_timestamp: Union[None, Unset, int] = 1754006400,
    max_unix_timestamp: Union[None, Unset, int] = UNSET,
    min_duration_s: Union[None, Unset, int] = UNSET,
    max_duration_s: Union[None, Unset, int] = UNSET,
    min_networth: Union[None, Unset, int] = UNSET,
    max_networth: Union[None, Unset, int] = UNSET,
    min_average_badge: Union[None, Unset, int] = UNSET,
    max_average_badge: Union[None, Unset, int] = UNSET,
    min_match_id: Union[None, Unset, int] = UNSET,
    max_match_id: Union[None, Unset, int] = UNSET,
    same_lane_filter: Union[None, Unset, bool] = True,
    same_party_filter: Union[None, Unset, bool] = True,
    min_matches: Union[None, Unset, int] = 20,
    max_matches: Union[None, Unset, int] = UNSET,
    account_id: Union[None, Unset, int] = UNSET,
    account_ids: Union[None, Unset, list[int]] = UNSET,
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

    json_min_networth: Union[None, Unset, int]
    if isinstance(min_networth, Unset):
        json_min_networth = UNSET
    else:
        json_min_networth = min_networth
    params["min_networth"] = json_min_networth

    json_max_networth: Union[None, Unset, int]
    if isinstance(max_networth, Unset):
        json_max_networth = UNSET
    else:
        json_max_networth = max_networth
    params["max_networth"] = json_max_networth

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

    json_same_lane_filter: Union[None, Unset, bool]
    if isinstance(same_lane_filter, Unset):
        json_same_lane_filter = UNSET
    else:
        json_same_lane_filter = same_lane_filter
    params["same_lane_filter"] = json_same_lane_filter

    json_same_party_filter: Union[None, Unset, bool]
    if isinstance(same_party_filter, Unset):
        json_same_party_filter = UNSET
    else:
        json_same_party_filter = same_party_filter
    params["same_party_filter"] = json_same_party_filter

    json_min_matches: Union[None, Unset, int]
    if isinstance(min_matches, Unset):
        json_min_matches = UNSET
    else:
        json_min_matches = min_matches
    params["min_matches"] = json_min_matches

    json_max_matches: Union[None, Unset, int]
    if isinstance(max_matches, Unset):
        json_max_matches = UNSET
    else:
        json_max_matches = max_matches
    params["max_matches"] = json_max_matches

    json_account_id: Union[None, Unset, int]
    if isinstance(account_id, Unset):
        json_account_id = UNSET
    else:
        json_account_id = account_id
    params["account_id"] = json_account_id

    json_account_ids: Union[None, Unset, list[int]]
    if isinstance(account_ids, Unset):
        json_account_ids = UNSET
    elif isinstance(account_ids, list):
        json_account_ids = account_ids

    else:
        json_account_ids = account_ids
    params["account_ids"] = json_account_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/analytics/hero-synergy-stats",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["HeroSynergyStats"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = HeroSynergyStats.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["HeroSynergyStats"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    min_unix_timestamp: Union[None, Unset, int] = 1754006400,
    max_unix_timestamp: Union[None, Unset, int] = UNSET,
    min_duration_s: Union[None, Unset, int] = UNSET,
    max_duration_s: Union[None, Unset, int] = UNSET,
    min_networth: Union[None, Unset, int] = UNSET,
    max_networth: Union[None, Unset, int] = UNSET,
    min_average_badge: Union[None, Unset, int] = UNSET,
    max_average_badge: Union[None, Unset, int] = UNSET,
    min_match_id: Union[None, Unset, int] = UNSET,
    max_match_id: Union[None, Unset, int] = UNSET,
    same_lane_filter: Union[None, Unset, bool] = True,
    same_party_filter: Union[None, Unset, bool] = True,
    min_matches: Union[None, Unset, int] = 20,
    max_matches: Union[None, Unset, int] = UNSET,
    account_id: Union[None, Unset, int] = UNSET,
    account_ids: Union[None, Unset, list[int]] = UNSET,
) -> Response[Union[Any, list["HeroSynergyStats"]]]:
    """Hero Synergy Stats


    Retrieves hero pair synergy statistics based on historical match data.

    This endpoint analyzes completed matches to calculate how often a specific pair of heroes
    (`hero_id1` and `hero_id2`) won when playing *together on the same team*, and the total number of
    times they have played together under the specified filter conditions.

    Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent
    identical requests within this timeframe will receive the cached response.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        min_unix_timestamp (Union[None, Unset, int]):  Default: 1754006400.
        max_unix_timestamp (Union[None, Unset, int]):
        min_duration_s (Union[None, Unset, int]):
        max_duration_s (Union[None, Unset, int]):
        min_networth (Union[None, Unset, int]):
        max_networth (Union[None, Unset, int]):
        min_average_badge (Union[None, Unset, int]):
        max_average_badge (Union[None, Unset, int]):
        min_match_id (Union[None, Unset, int]):
        max_match_id (Union[None, Unset, int]):
        same_lane_filter (Union[None, Unset, bool]):  Default: True.
        same_party_filter (Union[None, Unset, bool]):  Default: True.
        min_matches (Union[None, Unset, int]):  Default: 20.
        max_matches (Union[None, Unset, int]):
        account_id (Union[None, Unset, int]):
        account_ids (Union[None, Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['HeroSynergyStats']]]
    """

    kwargs = _get_kwargs(
        min_unix_timestamp=min_unix_timestamp,
        max_unix_timestamp=max_unix_timestamp,
        min_duration_s=min_duration_s,
        max_duration_s=max_duration_s,
        min_networth=min_networth,
        max_networth=max_networth,
        min_average_badge=min_average_badge,
        max_average_badge=max_average_badge,
        min_match_id=min_match_id,
        max_match_id=max_match_id,
        same_lane_filter=same_lane_filter,
        same_party_filter=same_party_filter,
        min_matches=min_matches,
        max_matches=max_matches,
        account_id=account_id,
        account_ids=account_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    min_unix_timestamp: Union[None, Unset, int] = 1754006400,
    max_unix_timestamp: Union[None, Unset, int] = UNSET,
    min_duration_s: Union[None, Unset, int] = UNSET,
    max_duration_s: Union[None, Unset, int] = UNSET,
    min_networth: Union[None, Unset, int] = UNSET,
    max_networth: Union[None, Unset, int] = UNSET,
    min_average_badge: Union[None, Unset, int] = UNSET,
    max_average_badge: Union[None, Unset, int] = UNSET,
    min_match_id: Union[None, Unset, int] = UNSET,
    max_match_id: Union[None, Unset, int] = UNSET,
    same_lane_filter: Union[None, Unset, bool] = True,
    same_party_filter: Union[None, Unset, bool] = True,
    min_matches: Union[None, Unset, int] = 20,
    max_matches: Union[None, Unset, int] = UNSET,
    account_id: Union[None, Unset, int] = UNSET,
    account_ids: Union[None, Unset, list[int]] = UNSET,
) -> Optional[Union[Any, list["HeroSynergyStats"]]]:
    """Hero Synergy Stats


    Retrieves hero pair synergy statistics based on historical match data.

    This endpoint analyzes completed matches to calculate how often a specific pair of heroes
    (`hero_id1` and `hero_id2`) won when playing *together on the same team*, and the total number of
    times they have played together under the specified filter conditions.

    Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent
    identical requests within this timeframe will receive the cached response.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        min_unix_timestamp (Union[None, Unset, int]):  Default: 1754006400.
        max_unix_timestamp (Union[None, Unset, int]):
        min_duration_s (Union[None, Unset, int]):
        max_duration_s (Union[None, Unset, int]):
        min_networth (Union[None, Unset, int]):
        max_networth (Union[None, Unset, int]):
        min_average_badge (Union[None, Unset, int]):
        max_average_badge (Union[None, Unset, int]):
        min_match_id (Union[None, Unset, int]):
        max_match_id (Union[None, Unset, int]):
        same_lane_filter (Union[None, Unset, bool]):  Default: True.
        same_party_filter (Union[None, Unset, bool]):  Default: True.
        min_matches (Union[None, Unset, int]):  Default: 20.
        max_matches (Union[None, Unset, int]):
        account_id (Union[None, Unset, int]):
        account_ids (Union[None, Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['HeroSynergyStats']]
    """

    return sync_detailed(
        client=client,
        min_unix_timestamp=min_unix_timestamp,
        max_unix_timestamp=max_unix_timestamp,
        min_duration_s=min_duration_s,
        max_duration_s=max_duration_s,
        min_networth=min_networth,
        max_networth=max_networth,
        min_average_badge=min_average_badge,
        max_average_badge=max_average_badge,
        min_match_id=min_match_id,
        max_match_id=max_match_id,
        same_lane_filter=same_lane_filter,
        same_party_filter=same_party_filter,
        min_matches=min_matches,
        max_matches=max_matches,
        account_id=account_id,
        account_ids=account_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    min_unix_timestamp: Union[None, Unset, int] = 1754006400,
    max_unix_timestamp: Union[None, Unset, int] = UNSET,
    min_duration_s: Union[None, Unset, int] = UNSET,
    max_duration_s: Union[None, Unset, int] = UNSET,
    min_networth: Union[None, Unset, int] = UNSET,
    max_networth: Union[None, Unset, int] = UNSET,
    min_average_badge: Union[None, Unset, int] = UNSET,
    max_average_badge: Union[None, Unset, int] = UNSET,
    min_match_id: Union[None, Unset, int] = UNSET,
    max_match_id: Union[None, Unset, int] = UNSET,
    same_lane_filter: Union[None, Unset, bool] = True,
    same_party_filter: Union[None, Unset, bool] = True,
    min_matches: Union[None, Unset, int] = 20,
    max_matches: Union[None, Unset, int] = UNSET,
    account_id: Union[None, Unset, int] = UNSET,
    account_ids: Union[None, Unset, list[int]] = UNSET,
) -> Response[Union[Any, list["HeroSynergyStats"]]]:
    """Hero Synergy Stats


    Retrieves hero pair synergy statistics based on historical match data.

    This endpoint analyzes completed matches to calculate how often a specific pair of heroes
    (`hero_id1` and `hero_id2`) won when playing *together on the same team*, and the total number of
    times they have played together under the specified filter conditions.

    Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent
    identical requests within this timeframe will receive the cached response.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        min_unix_timestamp (Union[None, Unset, int]):  Default: 1754006400.
        max_unix_timestamp (Union[None, Unset, int]):
        min_duration_s (Union[None, Unset, int]):
        max_duration_s (Union[None, Unset, int]):
        min_networth (Union[None, Unset, int]):
        max_networth (Union[None, Unset, int]):
        min_average_badge (Union[None, Unset, int]):
        max_average_badge (Union[None, Unset, int]):
        min_match_id (Union[None, Unset, int]):
        max_match_id (Union[None, Unset, int]):
        same_lane_filter (Union[None, Unset, bool]):  Default: True.
        same_party_filter (Union[None, Unset, bool]):  Default: True.
        min_matches (Union[None, Unset, int]):  Default: 20.
        max_matches (Union[None, Unset, int]):
        account_id (Union[None, Unset, int]):
        account_ids (Union[None, Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['HeroSynergyStats']]]
    """

    kwargs = _get_kwargs(
        min_unix_timestamp=min_unix_timestamp,
        max_unix_timestamp=max_unix_timestamp,
        min_duration_s=min_duration_s,
        max_duration_s=max_duration_s,
        min_networth=min_networth,
        max_networth=max_networth,
        min_average_badge=min_average_badge,
        max_average_badge=max_average_badge,
        min_match_id=min_match_id,
        max_match_id=max_match_id,
        same_lane_filter=same_lane_filter,
        same_party_filter=same_party_filter,
        min_matches=min_matches,
        max_matches=max_matches,
        account_id=account_id,
        account_ids=account_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    min_unix_timestamp: Union[None, Unset, int] = 1754006400,
    max_unix_timestamp: Union[None, Unset, int] = UNSET,
    min_duration_s: Union[None, Unset, int] = UNSET,
    max_duration_s: Union[None, Unset, int] = UNSET,
    min_networth: Union[None, Unset, int] = UNSET,
    max_networth: Union[None, Unset, int] = UNSET,
    min_average_badge: Union[None, Unset, int] = UNSET,
    max_average_badge: Union[None, Unset, int] = UNSET,
    min_match_id: Union[None, Unset, int] = UNSET,
    max_match_id: Union[None, Unset, int] = UNSET,
    same_lane_filter: Union[None, Unset, bool] = True,
    same_party_filter: Union[None, Unset, bool] = True,
    min_matches: Union[None, Unset, int] = 20,
    max_matches: Union[None, Unset, int] = UNSET,
    account_id: Union[None, Unset, int] = UNSET,
    account_ids: Union[None, Unset, list[int]] = UNSET,
) -> Optional[Union[Any, list["HeroSynergyStats"]]]:
    """Hero Synergy Stats


    Retrieves hero pair synergy statistics based on historical match data.

    This endpoint analyzes completed matches to calculate how often a specific pair of heroes
    (`hero_id1` and `hero_id2`) won when playing *together on the same team*, and the total number of
    times they have played together under the specified filter conditions.

    Results are cached for **1 hour** based on the combination of query parameters provided. Subsequent
    identical requests within this timeframe will receive the cached response.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        min_unix_timestamp (Union[None, Unset, int]):  Default: 1754006400.
        max_unix_timestamp (Union[None, Unset, int]):
        min_duration_s (Union[None, Unset, int]):
        max_duration_s (Union[None, Unset, int]):
        min_networth (Union[None, Unset, int]):
        max_networth (Union[None, Unset, int]):
        min_average_badge (Union[None, Unset, int]):
        max_average_badge (Union[None, Unset, int]):
        min_match_id (Union[None, Unset, int]):
        max_match_id (Union[None, Unset, int]):
        same_lane_filter (Union[None, Unset, bool]):  Default: True.
        same_party_filter (Union[None, Unset, bool]):  Default: True.
        min_matches (Union[None, Unset, int]):  Default: 20.
        max_matches (Union[None, Unset, int]):
        account_id (Union[None, Unset, int]):
        account_ids (Union[None, Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['HeroSynergyStats']]
    """

    return (
        await asyncio_detailed(
            client=client,
            min_unix_timestamp=min_unix_timestamp,
            max_unix_timestamp=max_unix_timestamp,
            min_duration_s=min_duration_s,
            max_duration_s=max_duration_s,
            min_networth=min_networth,
            max_networth=max_networth,
            min_average_badge=min_average_badge,
            max_average_badge=max_average_badge,
            min_match_id=min_match_id,
            max_match_id=max_match_id,
            same_lane_filter=same_lane_filter,
            same_party_filter=same_party_filter,
            min_matches=min_matches,
            max_matches=max_matches,
            account_id=account_id,
            account_ids=account_ids,
        )
    ).parsed
