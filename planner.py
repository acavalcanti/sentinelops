def planner(log):
    if "timeout" in log:
        return ["analysis","diagnosis","fix"]
    if "memory" in log:
        return ["analysis","fix"]
    return ["analysis"]
