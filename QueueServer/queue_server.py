from fastapi import FastAPI
from pydantic import BaseModel


class ChromeID(BaseModel):
    quadrant: int = -1
    file_name: str = ""


class ChromMap(BaseModel):
    chrom_file: str
    agent_name: str


chrom_map = {}
queue_1 = []
queue_2 = []
queue_3 = []
queue_4 = []

stats = {"connections": 0, "error_requests": 0}


queues = [queue_1, queue_2, queue_3, queue_4]
app = FastAPI() 


@app.post("/update_map")
async def update_map(data: ChromMap):
    print(data)
    chrom_map.update({data.agent_name: data.chrom_file})
    print(chrom_map)


@app.get("/get_map_{name}")
def get_map(name):
    return {chrom_map[name]}

    
@app.get("/stats")
def get_stats():
    return stats


@app.get("/is_alive")
def is_alive():
    print("New connection")
    stats["connections"] += 1
    return {0}


@app.get("/check_queues")
def get_queues():
    return {"queues": queues}


@app.get("/req_{num}")
def get_chrom(num):
    num = int(num) - 1
    print("|Q| :  {}, {}, {}, {}".format(len(queue_1), len(queue_2), len(queue_3), len(queue_4)))

    if num < 0 or num > 4:
        stats["error_requests"] += 1
        print("Failed to fetch chromosome from Q:{}".format(num + 1))
        return {"chromosome": -1}

    if len(queues[num]) == 0:
        print("Failed to fetch new chromosome from Q:{}".format(num + 1))
        stats["error_requests"] += 1
        return {"chromosome": -1}

    chromosome = queues[num].pop(0)
    print("Chromosome fetched from Q:{}".format(num + 1))
    return {"chromosome": chromosome}


@app.post("/post")
async def post_data(chromosome: ChromeID):
    if chromosome.quadrant < 1 or chromosome.quadrant > 4:
        stats["error_requests"] += 1

    if chromosome.quadrant == 1:
        queue_1.append(chromosome.file_name)
    elif chromosome.quadrant == 2:
        queue_2.append(chromosome.file_name)
    elif chromosome.quadrant == 3:
        queue_3.append(chromosome.file_name)
    elif chromosome.quadrant == 4:
        queue_4.append(chromosome.file_name)

    print("Chromosome added to Q:{}".format(chromosome.quadrant))

    return({"queue_1": queue_1, "queue_2": queue_2, "queue_3": queue_3, 
            "queue_4": queue_4})

#SLURM 01: 136.244.224.61
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
    #uvicorn.run(app, host="136.244.224.61", port=8000)