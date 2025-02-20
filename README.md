# MCP Toolhouse
[![smithery badge](https://smithery.ai/badge/@SecretiveShell/MCP-toolhouse)](https://smithery.ai/server/@SecretiveShell/MCP-toolhouse)

This is a model context protocol (MCP) server that provides access to tools from the [Toolhouse](https://toolhouse.ai) platform.

## Installation

### Installing via Smithery

To install Toolhouse for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@SecretiveShell/MCP-toolhouse):

```bash
npx -y @smithery/cli install @SecretiveShell/MCP-toolhouse --client claude
```

### Manual Setup
Setup your json like this:

```json
{
    "mcpServers": {
        "MCP-Toolhouse": {
            "command": "uv",
            "args": ["run", "mcp-toolhouse"],
            "env": {
                "TOOLHOUSE_API_KEY": "th-******************_*****_******************",
                "TOOLHOUSE_BUNDLE": "toolhouse-bundle-name",
                "PYTHONUTF8": "1"
            }
        }
    }
}
```

The python utf8 env is required for some tools to work on windows.
