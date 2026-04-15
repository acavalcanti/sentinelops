import random
def create_ticket(issue):
    return {"id":f"INC{random.randint(100,999)}","status":"open","issue":issue}
