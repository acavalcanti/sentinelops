from mcp.registry import TOOLS

def execute_mcp(action_spec):

    tool = TOOLS.get(action_spec["action"])

    return tool(action_spec["params"])