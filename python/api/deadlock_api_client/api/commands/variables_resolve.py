from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.variables_resolve_region import VariablesResolveRegion
from ...models.variables_resolve_response_200 import VariablesResolveResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    region: Union[Unset, VariablesResolveRegion] = UNSET,
    account_id: int,
    variables: Union[Unset, str] = UNSET,
    hero_name: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_region: Union[Unset, str] = UNSET
    if not isinstance(region, Unset):
        json_region = region.value

    params["region"] = json_region

    params["account_id"] = account_id

    params["variables"] = variables

    json_hero_name: Union[None, Unset, str]
    if isinstance(hero_name, Unset):
        json_hero_name = UNSET
    else:
        json_hero_name = hero_name
    params["hero_name"] = json_hero_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/commands/variables/resolve",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, VariablesResolveResponse200]]:
    if response.status_code == 200:
        response_200 = VariablesResolveResponse200.from_dict(response.json())

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
) -> Response[Union[Any, VariablesResolveResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    region: Union[Unset, VariablesResolveRegion] = UNSET,
    account_id: int,
    variables: Union[Unset, str] = UNSET,
    hero_name: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, VariablesResolveResponse200]]:
    """Resolve Variables


    Resolves variables and returns a map of variable name to resolved value.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 60req/min |
    | Key | - |
    | Global | 300req/min |


    Args:
        region (Union[Unset, VariablesResolveRegion]):
        account_id (int):
        variables (Union[Unset, str]):
        hero_name (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, VariablesResolveResponse200]]
    """

    kwargs = _get_kwargs(
        region=region,
        account_id=account_id,
        variables=variables,
        hero_name=hero_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    region: Union[Unset, VariablesResolveRegion] = UNSET,
    account_id: int,
    variables: Union[Unset, str] = UNSET,
    hero_name: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, VariablesResolveResponse200]]:
    """Resolve Variables


    Resolves variables and returns a map of variable name to resolved value.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 60req/min |
    | Key | - |
    | Global | 300req/min |


    Args:
        region (Union[Unset, VariablesResolveRegion]):
        account_id (int):
        variables (Union[Unset, str]):
        hero_name (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, VariablesResolveResponse200]
    """

    return sync_detailed(
        client=client,
        region=region,
        account_id=account_id,
        variables=variables,
        hero_name=hero_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    region: Union[Unset, VariablesResolveRegion] = UNSET,
    account_id: int,
    variables: Union[Unset, str] = UNSET,
    hero_name: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, VariablesResolveResponse200]]:
    """Resolve Variables


    Resolves variables and returns a map of variable name to resolved value.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 60req/min |
    | Key | - |
    | Global | 300req/min |


    Args:
        region (Union[Unset, VariablesResolveRegion]):
        account_id (int):
        variables (Union[Unset, str]):
        hero_name (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, VariablesResolveResponse200]]
    """

    kwargs = _get_kwargs(
        region=region,
        account_id=account_id,
        variables=variables,
        hero_name=hero_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    region: Union[Unset, VariablesResolveRegion] = UNSET,
    account_id: int,
    variables: Union[Unset, str] = UNSET,
    hero_name: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, VariablesResolveResponse200]]:
    """Resolve Variables


    Resolves variables and returns a map of variable name to resolved value.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 60req/min |
    | Key | - |
    | Global | 300req/min |


    Args:
        region (Union[Unset, VariablesResolveRegion]):
        account_id (int):
        variables (Union[Unset, str]):
        hero_name (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, VariablesResolveResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            region=region,
            account_id=account_id,
            variables=variables,
            hero_name=hero_name,
        )
    ).parsed
