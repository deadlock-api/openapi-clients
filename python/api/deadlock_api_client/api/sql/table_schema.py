from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.table_schema_response_200 import TableSchemaResponse200
from ...types import Response


def _get_kwargs(
    table: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/sql/tables/{table}/schema",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[TableSchemaResponse200, str]]:
    if response.status_code == 200:
        response_200 = TableSchemaResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = response.text
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[TableSchemaResponse200, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    table: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[TableSchemaResponse200, str]]:
    """Table Schema


    Returns the schema of a table.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TableSchemaResponse200, str]]
    """

    kwargs = _get_kwargs(
        table=table,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    table: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[TableSchemaResponse200, str]]:
    """Table Schema


    Returns the schema of a table.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TableSchemaResponse200, str]
    """

    return sync_detailed(
        table=table,
        client=client,
    ).parsed


async def asyncio_detailed(
    table: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[TableSchemaResponse200, str]]:
    """Table Schema


    Returns the schema of a table.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[TableSchemaResponse200, str]]
    """

    kwargs = _get_kwargs(
        table=table,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    table: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[TableSchemaResponse200, str]]:
    """Table Schema


    Returns the schema of a table.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | 100req/s |
    | Key | - |
    | Global | - |


    Args:
        table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[TableSchemaResponse200, str]
    """

    return (
        await asyncio_detailed(
            table=table,
            client=client,
        )
    ).parsed
