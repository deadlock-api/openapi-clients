from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.mmr_history import MMRHistory
from ...types import UNSET, Response


def _get_kwargs(
    hero_id: int,
    *,
    account_ids: list[int],
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_account_ids = account_ids

    params["account_ids"] = json_account_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/players/mmr/{hero_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["MMRHistory"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MMRHistory.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["MMRHistory"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    hero_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    account_ids: list[int],
) -> Response[Union[Any, list["MMRHistory"]]]:
    """Hero MMR

     Batch Player Hero MMR

    Args:
        hero_id (int):
        account_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['MMRHistory']]]
    """

    kwargs = _get_kwargs(
        hero_id=hero_id,
        account_ids=account_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    hero_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    account_ids: list[int],
) -> Optional[Union[Any, list["MMRHistory"]]]:
    """Hero MMR

     Batch Player Hero MMR

    Args:
        hero_id (int):
        account_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['MMRHistory']]
    """

    return sync_detailed(
        hero_id=hero_id,
        client=client,
        account_ids=account_ids,
    ).parsed


async def asyncio_detailed(
    hero_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    account_ids: list[int],
) -> Response[Union[Any, list["MMRHistory"]]]:
    """Hero MMR

     Batch Player Hero MMR

    Args:
        hero_id (int):
        account_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['MMRHistory']]]
    """

    kwargs = _get_kwargs(
        hero_id=hero_id,
        account_ids=account_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    hero_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    account_ids: list[int],
) -> Optional[Union[Any, list["MMRHistory"]]]:
    """Hero MMR

     Batch Player Hero MMR

    Args:
        hero_id (int):
        account_ids (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['MMRHistory']]
    """

    return (
        await asyncio_detailed(
            hero_id=hero_id,
            client=client,
            account_ids=account_ids,
        )
    ).parsed
