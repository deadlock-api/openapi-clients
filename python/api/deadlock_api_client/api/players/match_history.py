from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.player_match_history_entry import PlayerMatchHistoryEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: int,
    *,
    force_refetch: Union[Unset, bool] = UNSET,
    only_stored_history: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["force_refetch"] = force_refetch

    params["only_stored_history"] = only_stored_history

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/players/{account_id}/match-history",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["PlayerMatchHistoryEntry"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PlayerMatchHistoryEntry.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["PlayerMatchHistoryEntry"]]]:
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
    force_refetch: Union[Unset, bool] = UNSET,
    only_stored_history: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["PlayerMatchHistoryEntry"]]]:
    """Match History


    This endpoint returns the player match history for the given `account_id`.

    The player match history is a combination of the data from **Steam** and **ClickHouse**, so you
    always get the most up-to-date data and full history.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Messages:
    - CMsgClientToGcGetMatchHistory
    - CMsgClientToGcGetMatchHistoryResponse

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 5req/min<br>With `only_stored_history=true`: 100req/s<br>With `force_refetch=true`: 5req/h |
    | Key | 50req/min & 1000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`:
    5req/h |
    | Global | 2000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 10req/h |


    Args:
        account_id (int):
        force_refetch (Union[Unset, bool]):
        only_stored_history (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['PlayerMatchHistoryEntry']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        force_refetch=force_refetch,
        only_stored_history=only_stored_history,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    force_refetch: Union[Unset, bool] = UNSET,
    only_stored_history: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["PlayerMatchHistoryEntry"]]]:
    """Match History


    This endpoint returns the player match history for the given `account_id`.

    The player match history is a combination of the data from **Steam** and **ClickHouse**, so you
    always get the most up-to-date data and full history.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Messages:
    - CMsgClientToGcGetMatchHistory
    - CMsgClientToGcGetMatchHistoryResponse

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 5req/min<br>With `only_stored_history=true`: 100req/s<br>With `force_refetch=true`: 5req/h |
    | Key | 50req/min & 1000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`:
    5req/h |
    | Global | 2000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 10req/h |


    Args:
        account_id (int):
        force_refetch (Union[Unset, bool]):
        only_stored_history (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['PlayerMatchHistoryEntry']]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        force_refetch=force_refetch,
        only_stored_history=only_stored_history,
    ).parsed


async def asyncio_detailed(
    account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    force_refetch: Union[Unset, bool] = UNSET,
    only_stored_history: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["PlayerMatchHistoryEntry"]]]:
    """Match History


    This endpoint returns the player match history for the given `account_id`.

    The player match history is a combination of the data from **Steam** and **ClickHouse**, so you
    always get the most up-to-date data and full history.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Messages:
    - CMsgClientToGcGetMatchHistory
    - CMsgClientToGcGetMatchHistoryResponse

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 5req/min<br>With `only_stored_history=true`: 100req/s<br>With `force_refetch=true`: 5req/h |
    | Key | 50req/min & 1000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`:
    5req/h |
    | Global | 2000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 10req/h |


    Args:
        account_id (int):
        force_refetch (Union[Unset, bool]):
        only_stored_history (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['PlayerMatchHistoryEntry']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        force_refetch=force_refetch,
        only_stored_history=only_stored_history,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    force_refetch: Union[Unset, bool] = UNSET,
    only_stored_history: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["PlayerMatchHistoryEntry"]]]:
    """Match History


    This endpoint returns the player match history for the given `account_id`.

    The player match history is a combination of the data from **Steam** and **ClickHouse**, so you
    always get the most up-to-date data and full history.

    Protobuf definitions can be found here:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)

    Relevant Protobuf Messages:
    - CMsgClientToGcGetMatchHistory
    - CMsgClientToGcGetMatchHistoryResponse

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 5req/min<br>With `only_stored_history=true`: 100req/s<br>With `force_refetch=true`: 5req/h |
    | Key | 50req/min & 1000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`:
    5req/h |
    | Global | 2000req/h<br>With `only_stored_history=true`: -<br>With `force_refetch=true`: 10req/h |


    Args:
        account_id (int):
        force_refetch (Union[Unset, bool]):
        only_stored_history (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['PlayerMatchHistoryEntry']]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            force_refetch=force_refetch,
            only_stored_history=only_stored_history,
        )
    ).parsed
