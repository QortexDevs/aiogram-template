from typing import Any

import httpx

HEADER_NAME = 'Authorization'


class AsyncClientConnector:
    """
    Example for auth: httpx.AsyncClient(auth=HeaderApiKey(api_key=self.api_key, header_name=HEADER_NAME))
    Additional info about package: https://pypi.org/project/httpx-auth/
    """

    def __init__(self, base_url: str, auth: httpx.Auth) -> None:
        self.base_url = base_url
        self.auth = auth

    async def make_request(self, method: str, url: str, **kwargs: Any) -> httpx.Response:
        async with httpx.AsyncClient(auth=self.auth) as client:
            request_method = getattr(client, method)
            response = await request_method(url, **kwargs)
            return response

    def build_url(self, id: int | None = None, query_params: dict[str, Any] | None = None) -> str:
        url = f'{self.base_url}/{id}' if id is not None else self.base_url
        if query_params:
            query_string = '&'.join(f'{key}={value}' for key, value in query_params.items())
            url += '?' + query_string
        return url

    async def get(self, query_params: dict[str, Any] | None = None, **kwargs: Any) -> httpx.Response:
        url = self.build_url(query_params=query_params)
        return await self.make_request('get', url, **kwargs)

    async def post(self, data: dict[str, Any] | None = None, **kwargs: Any) -> httpx.Response:
        data = data or {}
        return await self.make_request('post', self.base_url, json=data, **kwargs)

    async def put(self, data: dict[str, Any], id: int | None = None, **kwargs: Any) -> httpx.Response:
        url = self.build_url(id)
        return await self.make_request('put', url, json=data, **kwargs)

    async def delete(self, id: int | None = None, **kwargs: Any) -> httpx.Response:
        url = self.build_url(id)
        return await self.make_request('delete', url, **kwargs)

    async def patch(self, data: dict[str, Any], id: int | None = None, **kwargs: Any) -> httpx.Response:
        url = self.build_url(id)
        return await self.make_request('patch', url, json=data, **kwargs)
