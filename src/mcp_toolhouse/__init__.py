import platform
from typing import Any
import httpx
from mcp.server.lowlevel import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio
import mcp.types as types
import os

TOOLHOUSE_API_KEY: str | None = os.environ.get("TOOLHOUSE_API_KEY", None)
assert (
    TOOLHOUSE_API_KEY is not None
), "TOOLHOUSE_API_KEY environment variable is not set"


TOOLHOUSE_BUNDLE: str | None = os.environ.get("TOOLHOUSE_BUNDLE", None)
assert (
    TOOLHOUSE_BUNDLE is not None
), "TOOLHOUSE_BUNDLE environment variable is not set"


# Create a server instance
server = Server("MCP-Toolhouse")


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    tools = list[types.Tool]()

    headers = {}

    headers["Content-Type"] = "application/json"
    headers["User-Agent"] = f"Toolhouse/1.2.1 Python/{platform.python_version()}"
    headers["Authorization"] = f"Bearer {TOOLHOUSE_API_KEY}"

    model: dict[str, Any] = {
        "bundle": TOOLHOUSE_BUNDLE,
        "metadata": {},
        "provider": "openai",
    }

    base_url = "https://api.toolhouse.ai/v1"

    response = httpx.post(base_url + "/get_tools", headers=headers, json=model)
    response_data = response.json()

    for tool in response_data:
        function = tool["function"]
        tools.append(
            types.Tool.model_construct(
                **{
                    "name": function["name"],
                    "description": function["description"],
                    "inputSchema": function["parameters"],
                }
            )
        )

    return tools

@server.call_tool()
async def handle_call_tool(name: str, args: dict) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    headers = {}
    headers["Content-Type"] = "application/json"
    headers["User-Agent"] = f"Toolhouse/1.2.1 Python/{platform.python_version()}"
    headers["Authorization"] = f"Bearer {TOOLHOUSE_API_KEY}"

    model = {

    }

    return []



async def run():
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="MCP Toolhouse",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


def main() -> None:
    import asyncio

    asyncio.run(run())


if __name__ == "__main__":
    main()
