from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.command_resolve_region import CommandResolveRegion
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    region: Union[Unset, CommandResolveRegion] = UNSET,
    account_id: int,
    template: Union[Unset, str] = UNSET,
    hero_name: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_region: Union[Unset, str] = UNSET
    if not isinstance(region, Unset):
        json_region = region.value

    params["region"] = json_region

    params["account_id"] = account_id

    params["template"] = template

    json_hero_name: Union[None, Unset, str]
    if isinstance(hero_name, Unset):
        json_hero_name = UNSET
    else:
        json_hero_name = hero_name
    params["hero_name"] = json_hero_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/commands/resolve",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, str]]:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    region: Union[Unset, CommandResolveRegion] = UNSET,
    account_id: int,
    template: Union[Unset, str] = UNSET,
    hero_name: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, str]]:
    """Resolve Command


        Resolves a command and returns the resolved command.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 60req/60s |
    | Key | - |
    | Global | 300req/60s |


    Args:
        region (Union[Unset, CommandResolveRegion]):
        account_id (int):
        template (Union[Unset, str]):
        hero_name (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, str]]
    """

    kwargs = _get_kwargs(
        region=region,
        account_id=account_id,
        template=template,
        hero_name=hero_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    region: Union[Unset, CommandResolveRegion] = UNSET,
    account_id: int,
    template: Union[Unset, str] = UNSET,
    hero_name: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, str]]:
    """Resolve Command


        Resolves a command and returns the resolved command.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 60req/60s |
    | Key | - |
    | Global | 300req/60s |


    Args:
        region (Union[Unset, CommandResolveRegion]):
        account_id (int):
        template (Union[Unset, str]):
        hero_name (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, str]
    """

    return sync_detailed(
        client=client,
        region=region,
        account_id=account_id,
        template=template,
        hero_name=hero_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    region: Union[Unset, CommandResolveRegion] = UNSET,
    account_id: int,
    template: Union[Unset, str] = UNSET,
    hero_name: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, str]]:
    """Resolve Command


        Resolves a command and returns the resolved command.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 60req/60s |
    | Key | - |
    | Global | 300req/60s |


    Args:
        region (Union[Unset, CommandResolveRegion]):
        account_id (int):
        template (Union[Unset, str]):
        hero_name (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, str]]
    """

    kwargs = _get_kwargs(
        region=region,
        account_id=account_id,
        template=template,
        hero_name=hero_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    region: Union[Unset, CommandResolveRegion] = UNSET,
    account_id: int,
    template: Union[Unset, str] = UNSET,
    hero_name: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, str]]:
    """Resolve Command


        Resolves a command and returns the resolved command.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 60req/60s |
    | Key | - |
    | Global | 300req/60s |


    Args:
        region (Union[Unset, CommandResolveRegion]):
        account_id (int):
        template (Union[Unset, str]):
        hero_name (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            region=region,
            account_id=account_id,
            template=template,
            hero_name=hero_name,
        )
    ).parsed
