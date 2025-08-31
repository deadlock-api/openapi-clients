from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hero_v2 import HeroV2
from ...models.http_validation_error import HTTPValidationError
from ...models.language import Language
from ...models.valid_client_versions import ValidClientVersions
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    language: Union[Language, None, Unset] = UNSET,
    client_version: Union[None, Unset, ValidClientVersions] = UNSET,
    only_active: Union[None, Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_language: Union[None, Unset, str]
    if isinstance(language, Unset):
        json_language = UNSET
    elif isinstance(language, Language):
        json_language = language.value
    else:
        json_language = language
    params["language"] = json_language

    json_client_version: Union[None, Unset, int]
    if isinstance(client_version, Unset):
        json_client_version = UNSET
    elif isinstance(client_version, ValidClientVersions):
        json_client_version = client_version.value
    else:
        json_client_version = client_version
    params["client_version"] = json_client_version

    json_only_active: Union[None, Unset, bool]
    if isinstance(only_active, Unset):
        json_only_active = UNSET
    else:
        json_only_active = only_active
    params["only_active"] = json_only_active

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/heroes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, list["HeroV2"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = HeroV2.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, list["HeroV2"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    language: Union[Language, None, Unset] = UNSET,
    client_version: Union[None, Unset, ValidClientVersions] = UNSET,
    only_active: Union[None, Unset, bool] = UNSET,
) -> Response[Union[HTTPValidationError, list["HeroV2"]]]:
    """Get Heroes

    Args:
        language (Union[Language, None, Unset]):
        client_version (Union[None, Unset, ValidClientVersions]):
        only_active (Union[None, Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list['HeroV2']]]
    """

    kwargs = _get_kwargs(
        language=language,
        client_version=client_version,
        only_active=only_active,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    language: Union[Language, None, Unset] = UNSET,
    client_version: Union[None, Unset, ValidClientVersions] = UNSET,
    only_active: Union[None, Unset, bool] = UNSET,
) -> Optional[Union[HTTPValidationError, list["HeroV2"]]]:
    """Get Heroes

    Args:
        language (Union[Language, None, Unset]):
        client_version (Union[None, Unset, ValidClientVersions]):
        only_active (Union[None, Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list['HeroV2']]
    """

    return sync_detailed(
        client=client,
        language=language,
        client_version=client_version,
        only_active=only_active,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    language: Union[Language, None, Unset] = UNSET,
    client_version: Union[None, Unset, ValidClientVersions] = UNSET,
    only_active: Union[None, Unset, bool] = UNSET,
) -> Response[Union[HTTPValidationError, list["HeroV2"]]]:
    """Get Heroes

    Args:
        language (Union[Language, None, Unset]):
        client_version (Union[None, Unset, ValidClientVersions]):
        only_active (Union[None, Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list['HeroV2']]]
    """

    kwargs = _get_kwargs(
        language=language,
        client_version=client_version,
        only_active=only_active,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    language: Union[Language, None, Unset] = UNSET,
    client_version: Union[None, Unset, ValidClientVersions] = UNSET,
    only_active: Union[None, Unset, bool] = UNSET,
) -> Optional[Union[HTTPValidationError, list["HeroV2"]]]:
    """Get Heroes

    Args:
        language (Union[Language, None, Unset]):
        client_version (Union[None, Unset, ValidClientVersions]):
        only_active (Union[None, Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list['HeroV2']]
    """

    return (
        await asyncio_detailed(
            client=client,
            language=language,
            client_version=client_version,
            only_active=only_active,
        )
    ).parsed
