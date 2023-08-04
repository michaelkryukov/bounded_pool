import time
from contextlib import asynccontextmanager, contextmanager

import pytest


@pytest.fixture
def anyio_backend():
    return 'asyncio'


@contextmanager
def assert_takes(*, less=None, more=None):
    if not less and not more:
        raise ValueError('less or more must be specified')

    started_at = time.time()

    try:
        yield
    finally:
        elapsed = time.time() - started_at

        if less:
            assert elapsed <= less

        if more:
            assert elapsed >= more


@asynccontextmanager
async def aassert_takes(*, less=None, more=None):
    if not less and not more:
        raise ValueError('less or more must be specified')

    started_at = time.time()

    try:
        yield
    finally:
        elapsed = time.time() - started_at

        if less:
            assert elapsed <= less

        if more:
            assert elapsed >= more
