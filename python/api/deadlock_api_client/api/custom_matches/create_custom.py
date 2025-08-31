from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_custom_request import CreateCustomRequest
from ...models.create_custom_response import CreateCustomResponse
from ...types import Response


def _get_kwargs(
    *,
    body: CreateCustomRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/matches/custom/create",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateCustomResponse]]:
    if response.status_code == 200:
        response_200 = CreateCustomResponse.from_dict(response.json())

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
) -> Response[Union[Any, CreateCustomResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateCustomRequest,
) -> Response[Union[Any, CreateCustomResponse]]:
    """Create Match


    This endpoint creates a custom match using a bot account.

    **Process:**
    1. A party is created with your provided settings.
    2. The system waits for the party code to be generated.
    3. The party code is returned in the response.
    4. The bot switches to spectator mode.
    5. The bot marks itself as ready.
    6. You and other players join, ready up, and start the match.

    **Callbacks:**
    If a callback URL is provided, POST requests will be sent to it:
    - **settings:** When lobby settings change, a POST is sent to `{callback_url}/settings` with the
    `CsoCitadelParty` protobuf message as JSON.
    - **match start:** When the match starts, a POST is sent to `{callback_url}` with the match ID.

    _Protobuf definitions:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)_

    **Note:**
    The bot will leave the match 15 minutes after creation, regardless of match state.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | API-Key ONLY |
    | Key | 100req/30min |
    | Global | 1000req/h |

    Args:
        body (CreateCustomRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateCustomResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateCustomRequest,
) -> Optional[Union[Any, CreateCustomResponse]]:
    """Create Match


    This endpoint creates a custom match using a bot account.

    **Process:**
    1. A party is created with your provided settings.
    2. The system waits for the party code to be generated.
    3. The party code is returned in the response.
    4. The bot switches to spectator mode.
    5. The bot marks itself as ready.
    6. You and other players join, ready up, and start the match.

    **Callbacks:**
    If a callback URL is provided, POST requests will be sent to it:
    - **settings:** When lobby settings change, a POST is sent to `{callback_url}/settings` with the
    `CsoCitadelParty` protobuf message as JSON.
    - **match start:** When the match starts, a POST is sent to `{callback_url}` with the match ID.

    _Protobuf definitions:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)_

    **Note:**
    The bot will leave the match 15 minutes after creation, regardless of match state.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | API-Key ONLY |
    | Key | 100req/30min |
    | Global | 1000req/h |

    Args:
        body (CreateCustomRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateCustomResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateCustomRequest,
) -> Response[Union[Any, CreateCustomResponse]]:
    """Create Match


    This endpoint creates a custom match using a bot account.

    **Process:**
    1. A party is created with your provided settings.
    2. The system waits for the party code to be generated.
    3. The party code is returned in the response.
    4. The bot switches to spectator mode.
    5. The bot marks itself as ready.
    6. You and other players join, ready up, and start the match.

    **Callbacks:**
    If a callback URL is provided, POST requests will be sent to it:
    - **settings:** When lobby settings change, a POST is sent to `{callback_url}/settings` with the
    `CsoCitadelParty` protobuf message as JSON.
    - **match start:** When the match starts, a POST is sent to `{callback_url}` with the match ID.

    _Protobuf definitions:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)_

    **Note:**
    The bot will leave the match 15 minutes after creation, regardless of match state.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | API-Key ONLY |
    | Key | 100req/30min |
    | Global | 1000req/h |

    Args:
        body (CreateCustomRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateCustomResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateCustomRequest,
) -> Optional[Union[Any, CreateCustomResponse]]:
    """Create Match


    This endpoint creates a custom match using a bot account.

    **Process:**
    1. A party is created with your provided settings.
    2. The system waits for the party code to be generated.
    3. The party code is returned in the response.
    4. The bot switches to spectator mode.
    5. The bot marks itself as ready.
    6. You and other players join, ready up, and start the match.

    **Callbacks:**
    If a callback URL is provided, POST requests will be sent to it:
    - **settings:** When lobby settings change, a POST is sent to `{callback_url}/settings` with the
    `CsoCitadelParty` protobuf message as JSON.
    - **match start:** When the match starts, a POST is sent to `{callback_url}` with the match ID.

    _Protobuf definitions:
    [https://github.com/SteamDatabase/Protobufs](https://github.com/SteamDatabase/Protobufs)_

    **Note:**
    The bot will leave the match 15 minutes after creation, regardless of match state.

    ### Rate Limits:
    | Type | Limit |
    | ---- | ----- |
    | IP | API-Key ONLY |
    | Key | 100req/30min |
    | Global | 1000req/h |

    Args:
        body (CreateCustomRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateCustomResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
