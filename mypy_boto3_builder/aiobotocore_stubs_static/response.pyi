import asyncio
from collections.abc import Generator
from typing import Any, Optional, Tuple

import wrapt
from aiobotocore import parsers as parsers
from botocore.exceptions import ReadTimeoutError
from botocore.model import OperationModel
from requests.models import Response

class AioReadTimeoutError(ReadTimeoutError, asyncio.TimeoutError): ...

class StreamingBody(wrapt.ObjectProxy):
    def __init__(self, raw_stream: Any, content_length: int) -> None: ...
    async def __aenter__(self) -> Any: ...
    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any: ...
    def tell(self) -> Any: ...
    async def read(self, amt: Optional[Any] = ...) -> Any: ...
    def __aiter__(self) -> Any: ...
    async def __anext__(self) -> Any: ...
    anext: Any
    async def iter_lines(
        self, chunk_size: int = ..., keepends: bool = ...
    ) -> Generator[Any, None, None]: ...
    async def iter_chunks(self, chunk_size: int = ...) -> Generator[Any, None, None]: ...

async def get_response(
    operation_model: OperationModel, http_response: Response
) -> Tuple[Response, Any]: ...
