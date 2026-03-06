# Test Marketplace.

A **private** test marketplace repo for development and testing of the Claude Code plugin marketplace system.

> This repo mirrors the structure of [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) for testing purposes.

## Structure

- **`/plugins`** - Internal plugins developed and maintained in-house
- **`/external_plugins`** - Third-party plugin integrations

## Installation

Plugins can be installed directly from this marketplace via Claude Code's plugin system.

To install, run `/plugin install {plugin-name}@test-marketplace`

## Plugin Structure

Each plugin follows a standard structure:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json      # Plugin metadata (required)
├── .mcp.json            # MCP server configuration (optional)
├── commands/            # Slash commands (optional)
├── agents/              # Agent definitions (optional)
├── skills/              # Skill definitions (optional)
└── README.md            # Documentation
```
# test-public-marketplace
