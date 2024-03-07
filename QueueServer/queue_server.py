from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class Chromosome(BaseModel):
    quadrant: int = -1
    chromo: List[List[str]]


queue_1 = []
queue_2 = []
queue_3 = []
queue_4 = []

stats = {"connections": 0, "error_requests": 0}


queues = [queue_1, queue_2, queue_3, queue_4]
app = FastAPI() 


@app.get("/stats")
def get_stats():
    return stats


@app.get("/is_alive")
def is_alive():
    stats["connections"] += 1
    return {0}


@app.get("/check_queues")
def get_queues():
    return {"queues": queues}


@app.get("/req_{num}")
def read_num(num):
    num = int(num) - 1

    if num < 0 or num > 4:
        stats["error_requests"] += 1
        return {-1}

    if len(queues[num]) == 0:
        stats["error_requests"] += 1
        return {-1}

    chromosome = queues[num].pop(0)
    return {"chromosome": chromosome}


@app.post("/post")
async def post_data(chromosome: Chromosome):
    if chromosome.quadrant < 1 or chromosome.quadrant > 4:
        stats["error_requests"] += 1

    if chromosome.quadrant == 1:
        queue_1.append(chromosome.chromo)
    elif chromosome.quadrant == 2:
        queue_2.append(chromosome.chromo)
    elif chromosome.quadrant == 3:
        queue_3.append(chromosome.chromo)
    elif chromosome.quadrant == 4:
        queue_4.append(chromosome.chromo)

    return({"queue_1": queue_1, "queue_2": queue_2, "queue_3": queue_3, 
            "queue_4": queue_4})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="136.244.224.61", port=8000)