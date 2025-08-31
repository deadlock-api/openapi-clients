from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/matches/active/raw",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list[int]]]:
    if response.status_code == 200:
        response_200 = cast(list[int], response.content)

        return response_200

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
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, list[int]]]:
    """Active as Protobuf


    Returns active matches that are currently being played, serialized as protobuf message.

    Fetched from the watch tab in game, which is limited to the **top 200 matches**.

    You have to decode the protobuf message.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Message:
    - CMsgClientToGcGetActiveMatchesResponse

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list[int]]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, list[int]]]:
    """Active as Protobuf


    Returns active matches that are currently being played, serialized as protobuf message.

    Fetched from the watch tab in game, which is limited to the **top 200 matches**.

    You have to decode the protobuf message.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Message:
    - CMsgClientToGcGetActiveMatchesResponse

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list[int]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, list[int]]]:
    """Active as Protobuf


    Returns active matches that are currently being played, serialized as protobuf message.

    Fetched from the watch tab in game, which is limited to the **top 200 matches**.

    You have to decode the protobuf message.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Message:
    - CMsgClientToGcGetActiveMatchesResponse

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list[int]]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, list[int]]]:
    """Active as Protobuf


    Returns active matches that are currently being played, serialized as protobuf message.

    Fetched from the watch tab in game, which is limited to the **top 200 matches**.

    You have to decode the protobuf message.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Message:
    - CMsgClientToGcGetActiveMatchesResponse

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list[int]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
