from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.match_salts_response import MatchSaltsResponse
from ...types import Response


def _get_kwargs(
    match_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/matches/{match_id}/salts",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, MatchSaltsResponse]]:
    if response.status_code == 200:
        response_200 = MatchSaltsResponse.from_dict(response.json())

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
) -> Response[Union[Any, MatchSaltsResponse]]:
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
) -> Response[Union[Any, MatchSaltsResponse]]:
    """Salts


    This endpoints returns salts that can be used to fetch metadata and demofile for a match.

    **Note:** We currently fetch many matches without salts, so for these matches we do not have salts
    stored.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | From DB: 100req/s<br>From Steam: 10req/30mins |
    | Key | From DB: -<br>From Steam: 10req/min |
    | Global | From DB: -<br>From Steam: 10req/10s |


    Args:
        match_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MatchSaltsResponse]]
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
) -> Optional[Union[Any, MatchSaltsResponse]]:
    """Salts


    This endpoints returns salts that can be used to fetch metadata and demofile for a match.

    **Note:** We currently fetch many matches without salts, so for these matches we do not have salts
    stored.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | From DB: 100req/s<br>From Steam: 10req/30mins |
    | Key | From DB: -<br>From Steam: 10req/min |
    | Global | From DB: -<br>From Steam: 10req/10s |


    Args:
        match_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MatchSaltsResponse]
    """

    return sync_detailed(
        match_id=match_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    match_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, MatchSaltsResponse]]:
    """Salts


    This endpoints returns salts that can be used to fetch metadata and demofile for a match.

    **Note:** We currently fetch many matches without salts, so for these matches we do not have salts
    stored.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | From DB: 100req/s<br>From Steam: 10req/30mins |
    | Key | From DB: -<br>From Steam: 10req/min |
    | Global | From DB: -<br>From Steam: 10req/10s |


    Args:
        match_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MatchSaltsResponse]]
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
) -> Optional[Union[Any, MatchSaltsResponse]]:
    """Salts


    This endpoints returns salts that can be used to fetch metadata and demofile for a match.

    **Note:** We currently fetch many matches without salts, so for these matches we do not have salts
    stored.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | From DB: 100req/s<br>From Steam: 10req/30mins |
    | Key | From DB: -<br>From Steam: 10req/min |
    | Global | From DB: -<br>From Steam: 10req/10s |


    Args:
        match_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MatchSaltsResponse]
    """

    return (
        await asyncio_detailed(
            match_id=match_id,
            client=client,
        )
    ).parsed
