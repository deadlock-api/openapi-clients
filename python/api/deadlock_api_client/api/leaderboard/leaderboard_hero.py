from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.leaderboard import Leaderboard
from ...models.leaderboard_hero_region import LeaderboardHeroRegion
from ...types import Response


def _get_kwargs(
    region: LeaderboardHeroRegion,
    hero_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/leaderboard/{region}/{hero_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Leaderboard]]:
    if response.status_code == 200:
        response_200 = Leaderboard.from_dict(response.json())

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
) -> Response[Union[Any, Leaderboard]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    region: LeaderboardHeroRegion,
    hero_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Leaderboard]]:
    """Hero Leaderboard


    Returns the leaderboard for a specific hero.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        region (LeaderboardHeroRegion):
        hero_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Leaderboard]]
    """

    kwargs = _get_kwargs(
        region=region,
        hero_id=hero_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    region: LeaderboardHeroRegion,
    hero_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Leaderboard]]:
    """Hero Leaderboard


    Returns the leaderboard for a specific hero.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        region (LeaderboardHeroRegion):
        hero_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Leaderboard]
    """

    return sync_detailed(
        region=region,
        hero_id=hero_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    region: LeaderboardHeroRegion,
    hero_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, Leaderboard]]:
    """Hero Leaderboard


    Returns the leaderboard for a specific hero.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        region (LeaderboardHeroRegion):
        hero_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Leaderboard]]
    """

    kwargs = _get_kwargs(
        region=region,
        hero_id=hero_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    region: LeaderboardHeroRegion,
    hero_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, Leaderboard]]:
    """Hero Leaderboard


    Returns the leaderboard for a specific hero.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        region (LeaderboardHeroRegion):
        hero_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Leaderboard]
    """

    return (
        await asyncio_detailed(
            region=region,
            hero_id=hero_id,
            client=client,
        )
    ).parsed
