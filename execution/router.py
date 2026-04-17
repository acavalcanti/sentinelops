from mcp.executor import execute_mcp

def execute(action_spec, config):

    if config["main"]["execution"]["mode"] == "local":
        return execute_mcp(action_spec)

    return {"status": "cloud"}