# Example Plugin

A comprehensive example plugin demonstrating Claude Code extension options.

## Structure

```
example-plugin/
├── .claude-plugin/
│   └── plugin.json        # Plugin metadata
├── .mcp.json              # MCP server configuration
├── commands/
│   └── example-command.md # Slash command definition
└── skills/
    └── example-skill/
        └── SKILL.md       # Skill definition
```

## Extension Options

### Commands (`commands/`)

Slash commands are user-invoked via `/command-name`. Define them as markdown files with frontmatter.

### Skills (`skills/`)

Skills are model-invoked capabilities. Create a `SKILL.md` in a subdirectory.

### MCP Servers (`.mcp.json`)

Configure external tool integration via Model Context Protocol.

## Usage

- `/example-command [args]` - Run the example slash command
- The example skill activates based on task context
- The example MCP server provides tools automatically
