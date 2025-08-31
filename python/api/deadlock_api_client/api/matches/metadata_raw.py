from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    match_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/matches/{match_id}/metadata/raw",
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

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

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
) -> Response[Union[Any, list[int]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    match_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, list[int]]]:
    """Metadata as Protobuf


    This endpoints returns the raw .meta.bz2 file for the given `match_id`.

    You have to decompress it and decode the protobuf message.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Messages:
    - CMsgMatchMetaData
    - CMsgMatchMetaDataContents

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins |
    | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min |
    | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |


    Args:
        match_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list[int]]]
    """

    kwargs = _get_kwargs(
        match_id=match_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    match_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, list[int]]]:
    """Metadata as Protobuf


    This endpoints returns the raw .meta.bz2 file for the given `match_id`.

    You have to decompress it and decode the protobuf message.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Messages:
    - CMsgMatchMetaData
    - CMsgMatchMetaDataContents

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins |
    | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min |
    | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |


    Args:
        match_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list[int]]
    """

    return sync_detailed(
        match_id=match_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    match_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, list[int]]]:
    """Metadata as Protobuf


    This endpoints returns the raw .meta.bz2 file for the given `match_id`.

    You have to decompress it and decode the protobuf message.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Messages:
    - CMsgMatchMetaData
    - CMsgMatchMetaDataContents

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins |
    | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min |
    | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |


    Args:
        match_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list[int]]]
    """

    kwargs = _get_kwargs(
        match_id=match_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    match_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, list[int]]]:
    """Metadata as Protobuf


    This endpoints returns the raw .meta.bz2 file for the given `match_id`.

    You have to decompress it and decode the protobuf message.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Messages:
    - CMsgMatchMetaData
    - CMsgMatchMetaDataContents

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | From Cache: 100req/s<br>From S3: 100req/10s<br>From Steam: 10req/30mins |
    | Key | From Cache: 100req/s<br>From S3: 100req/s<br>From Steam: 10req/min |
    | Global | From Cache: 100req/s<br>From S3: 700req/s<br>From Steam: 10req/10s |


    Args:
        match_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list[int]]
    """

    return (
        await asyncio_detailed(
            match_id=match_id,
            client=client,
        )
    ).parsed
