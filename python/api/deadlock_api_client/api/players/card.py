from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.player_card import PlayerCard
from ...types import Response


def _get_kwargs(
    account_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/players/{account_id}/card",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["PlayerCard"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PlayerCard.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, list["PlayerCard"]]]:
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
) -> Response[Union[Any, list["PlayerCard"]]]:
    """Card


    This endpoint returns the player card for the given `account_id`.

    You have to be friend with one of the bots to use this endpoint.
    On first use this endpoint will return an error with a list of invite links to add the bot as
    friend.
    From then on you can use this endpoint.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Messages:
    - CMsgClientToGcGetProfileCard
    - CMsgCitadelProfileCard

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 5req/min |
    | Key | 20req/min & 800req/h |
    | Global | 200req/min |


    Args:
        account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['PlayerCard']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, list["PlayerCard"]]]:
    """Card


    This endpoint returns the player card for the given `account_id`.

    You have to be friend with one of the bots to use this endpoint.
    On first use this endpoint will return an error with a list of invite links to add the bot as
    friend.
    From then on you can use this endpoint.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Messages:
    - CMsgClientToGcGetProfileCard
    - CMsgCitadelProfileCard

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 5req/min |
    | Key | 20req/min & 800req/h |
    | Global | 200req/min |


    Args:
        account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['PlayerCard']]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, list["PlayerCard"]]]:
    """Card


    This endpoint returns the player card for the given `account_id`.

    You have to be friend with one of the bots to use this endpoint.
    On first use this endpoint will return an error with a list of invite links to add the bot as
    friend.
    From then on you can use this endpoint.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Messages:
    - CMsgClientToGcGetProfileCard
    - CMsgCitadelProfileCard

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 5req/min |
    | Key | 20req/min & 800req/h |
    | Global | 200req/min |


    Args:
        account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['PlayerCard']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, list["PlayerCard"]]]:
    """Card


    This endpoint returns the player card for the given `account_id`.

    You have to be friend with one of the bots to use this endpoint.
    On first use this endpoint will return an error with a list of invite links to add the bot as
    friend.
    From then on you can use this endpoint.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Messages:
    - CMsgClientToGcGetProfileCard
    - CMsgCitadelProfileCard

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 5req/min |
    | Key | 20req/min & 800req/h |
    | Global | 200req/min |


    Args:
        account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['PlayerCard']]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
        )
    ).parsed
