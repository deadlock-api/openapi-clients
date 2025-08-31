from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_custom_match_id_response import GetCustomMatchIdResponse
from ...types import Response


def _get_kwargs(
    party_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/matches/custom/{party_id}/match-id",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetCustomMatchIdResponse]]:
    if response.status_code == 200:
        response_200 = GetCustomMatchIdResponse.from_dict(response.json())

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
) -> Response[Union[Any, GetCustomMatchIdResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    party_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetCustomMatchIdResponse]]:
    """Get Match ID


    This endpoint allows you to get the match id of a custom match.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |

    Args:
        party_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetCustomMatchIdResponse]]
    """

    kwargs = _get_kwargs(
        party_id=party_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    party_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetCustomMatchIdResponse]]:
    """Get Match ID


    This endpoint allows you to get the match id of a custom match.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |

    Args:
        party_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetCustomMatchIdResponse]
    """

    return sync_detailed(
        party_id=party_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    party_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetCustomMatchIdResponse]]:
    """Get Match ID


    This endpoint allows you to get the match id of a custom match.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |

    Args:
        party_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetCustomMatchIdResponse]]
    """

    kwargs = _get_kwargs(
        party_id=party_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    party_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetCustomMatchIdResponse]]:
    """Get Match ID


    This endpoint allows you to get the match id of a custom match.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |

    Args:
        party_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetCustomMatchIdResponse]
    """

    return (
        await asyncio_detailed(
            party_id=party_id,
            client=client,
        )
    ).parsed
