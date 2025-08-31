from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.mmr_history import MMRHistory
from ...types import Response


def _get_kwargs(
    account_id: int,
    hero_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/players/{account_id}/mmr-history/{hero_id}",
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
    account_id: int,
    hero_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, list["MMRHistory"]]]:
    """Hero MMR History

     Player Hero MMR History

    Args:
        account_id (int):
        hero_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['MMRHistory']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        hero_id=hero_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: int,
    hero_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, list["MMRHistory"]]]:
    """Hero MMR History

     Player Hero MMR History

    Args:
        account_id (int):
        hero_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['MMRHistory']]
    """

    return sync_detailed(
        account_id=account_id,
        hero_id=hero_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: int,
    hero_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, list["MMRHistory"]]]:
    """Hero MMR History

     Player Hero MMR History

    Args:
        account_id (int):
        hero_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['MMRHistory']]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        hero_id=hero_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: int,
    hero_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, list["MMRHistory"]]]:
    """Hero MMR History

     Player Hero MMR History

    Args:
        account_id (int):
        hero_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['MMRHistory']]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            hero_id=hero_id,
            client=client,
        )
    ).parsed
