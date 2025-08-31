from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.active_match import ActiveMatch
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_id: Union[None, Unset, int] = UNSET,
    account_ids: Union[None, Unset, list[int]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

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
        "url": "/v1/matches/active",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["ActiveMatch"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ActiveMatch.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["ActiveMatch"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    account_id: Union[None, Unset, int] = UNSET,
    account_ids: Union[None, Unset, list[int]] = UNSET,
) -> Response[Union[Any, list["ActiveMatch"]]]:
    """Active


    Returns active matches that are currently being played.

    Fetched from the watch tab in game, which is limited to the **top 200 matches**.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        account_id (Union[None, Unset, int]):
        account_ids (Union[None, Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ActiveMatch']]]
    """

    kwargs = _get_kwargs(
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
    account_id: Union[None, Unset, int] = UNSET,
    account_ids: Union[None, Unset, list[int]] = UNSET,
) -> Optional[Union[Any, list["ActiveMatch"]]]:
    """Active


    Returns active matches that are currently being played.

    Fetched from the watch tab in game, which is limited to the **top 200 matches**.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        account_id (Union[None, Unset, int]):
        account_ids (Union[None, Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ActiveMatch']]
    """

    return sync_detailed(
        client=client,
        account_id=account_id,
        account_ids=account_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    account_id: Union[None, Unset, int] = UNSET,
    account_ids: Union[None, Unset, list[int]] = UNSET,
) -> Response[Union[Any, list["ActiveMatch"]]]:
    """Active


    Returns active matches that are currently being played.

    Fetched from the watch tab in game, which is limited to the **top 200 matches**.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        account_id (Union[None, Unset, int]):
        account_ids (Union[None, Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['ActiveMatch']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        account_ids=account_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    account_id: Union[None, Unset, int] = UNSET,
    account_ids: Union[None, Unset, list[int]] = UNSET,
) -> Optional[Union[Any, list["ActiveMatch"]]]:
    """Active


    Returns active matches that are currently being played.

    Fetched from the watch tab in game, which is limited to the **top 200 matches**.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        account_id (Union[None, Unset, int]):
        account_ids (Union[None, Unset, list[int]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['ActiveMatch']]
    """

    return (
        await asyncio_detailed(
            client=client,
            account_id=account_id,
            account_ids=account_ids,
        )
    ).parsed
