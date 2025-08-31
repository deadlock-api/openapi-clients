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
    id: int,
    *,
    language: Union[Language, None, Unset] = UNSET,
    client_version: Union[None, Unset, ValidClientVersions] = UNSET,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/heroes/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, HeroV2]]:
    if response.status_code == 200:
        response_200 = HeroV2.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, HeroV2]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    language: Union[Language, None, Unset] = UNSET,
    client_version: Union[None, Unset, ValidClientVersions] = UNSET,
) -> Response[Union[HTTPValidationError, HeroV2]]:
    """Get Hero

    Args:
        id (int):
        language (Union[Language, None, Unset]):
        client_version (Union[None, Unset, ValidClientVersions]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, HeroV2]]
    """

    kwargs = _get_kwargs(
        id=id,
        language=language,
        client_version=client_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    language: Union[Language, None, Unset] = UNSET,
    client_version: Union[None, Unset, ValidClientVersions] = UNSET,
) -> Optional[Union[HTTPValidationError, HeroV2]]:
    """Get Hero

    Args:
        id (int):
        language (Union[Language, None, Unset]):
        client_version (Union[None, Unset, ValidClientVersions]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, HeroV2]
    """

    return sync_detailed(
        id=id,
        client=client,
        language=language,
        client_version=client_version,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    language: Union[Language, None, Unset] = UNSET,
    client_version: Union[None, Unset, ValidClientVersions] = UNSET,
) -> Response[Union[HTTPValidationError, HeroV2]]:
    """Get Hero

    Args:
        id (int):
        language (Union[Language, None, Unset]):
        client_version (Union[None, Unset, ValidClientVersions]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, HeroV2]]
    """

    kwargs = _get_kwargs(
        id=id,
        language=language,
        client_version=client_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    language: Union[Language, None, Unset] = UNSET,
    client_version: Union[None, Unset, ValidClientVersions] = UNSET,
) -> Optional[Union[HTTPValidationError, HeroV2]]:
    """Get Hero

    Args:
        id (int):
        language (Union[Language, None, Unset]):
        client_version (Union[None, Unset, ValidClientVersions]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, HeroV2]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            language=language,
            client_version=client_version,
        )
    ).parsed
