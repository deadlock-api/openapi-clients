from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.leaderboard_raw_region import LeaderboardRawRegion
from ...types import Response


def _get_kwargs(
    region: LeaderboardRawRegion,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/leaderboard/{region}/raw",
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

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

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
    region: LeaderboardRawRegion,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, list[int]]]:
    """Leaderboard as Protobuf


    Returns the leaderboard, serialized as protobuf message.

    You have to decode the protobuf message.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Message:
    - CMsgClientToGcGetLeaderboardResponse

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        region (LeaderboardRawRegion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list[int]]]
    """

    kwargs = _get_kwargs(
        region=region,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    region: LeaderboardRawRegion,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, list[int]]]:
    """Leaderboard as Protobuf


    Returns the leaderboard, serialized as protobuf message.

    You have to decode the protobuf message.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Message:
    - CMsgClientToGcGetLeaderboardResponse

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        region (LeaderboardRawRegion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list[int]]
    """

    return sync_detailed(
        region=region,
        client=client,
    ).parsed


async def asyncio_detailed(
    region: LeaderboardRawRegion,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, list[int]]]:
    """Leaderboard as Protobuf


    Returns the leaderboard, serialized as protobuf message.

    You have to decode the protobuf message.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Message:
    - CMsgClientToGcGetLeaderboardResponse

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        region (LeaderboardRawRegion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list[int]]]
    """

    kwargs = _get_kwargs(
        region=region,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    region: LeaderboardRawRegion,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, list[int]]]:
    """Leaderboard as Protobuf


    Returns the leaderboard, serialized as protobuf message.

    You have to decode the protobuf message.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Message:
    - CMsgClientToGcGetLeaderboardResponse

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        region (LeaderboardRawRegion):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list[int]]
    """

    return (
        await asyncio_detailed(
            region=region,
            client=client,
        )
    ).parsed
