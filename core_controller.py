from Engine import libpyAI as ai
import os
import sys
import traceback
import json
import uuid
import time

import config
from NetworkInterface import NetworkInterface
from ShipData import ShipData
from chromosome import Evolver
from ActionGene import ActionGene


class CoreAgent(NetworkInterface, ShipData):
    def __init__(self, bot_name):
        NetworkInterface.__init__(self)
        ShipData.__init__(self)
        self.initialized = False

        self.MUT_RATE = 300
        self.GENES_PER_LOOP = 8
        self.chrom_name = ""
        self.SPAWN_QUAD = None

        self.bot_name = bot_name

        ai.setPower(5)

        self.bin_chromosome = None
        self.dec_chromosome = None
        self.current_loop = None
        self.current_loop_idx = 0
        self.current_gene_idx = 0

        self.spawn_score = 0
        self.score = 0
        self.SD = False
        self.movement_timer = -1.0

        self.framesPostDeath = 0
        self.feed_history = ['' * 5]
        self.last_death = ["null", "null"]
        self.last_kill = ["null", "null"]
        self.prior_death = ["null", "null"]
        self.crossover_completed = False

        self.generate_feelers(10)
        self.frames_dead = 0

        self.ping_server()
        print("server ping")

    def increment_gene_idx(self):
        self.current_gene_idx = (self.current_gene_idx + 1) \
                                % self.GENES_PER_LOOP
        return self.current_gene_idx

    def update_score(self):
        self.score = ai.selfScore()

    def initialize_cga(self, quadrant):
        new_bin_chromosome, new_name = self.req_chrom(int(quadrant))

        if new_bin_chromosome == "" and self.initialized:
            with open(os.path.expanduser('~/Documents/xP_Core/data/{}.json'
                                                 .format(self.chrom_name)), 'r') as f:
                self.bin_chromosome = json.loads(f.readlines()[-1])[1]
        else:
            self.bin_chromosome = new_bin_chromosome
        print("New Name: " + new_name)
        ftype = "a"

        if not self.initialized:
            self.chrom_name = str(uuid.uuid4())[:8]
            new_name = self.chrom_name
            self.bin_chromosome = Evolver.generate_chromosome()
            self.initialized = True
        elif new_name == "":
            try:
                # Rewrite if it is a single generation failed chromosome
                with open(os.path.expanduser('~/Documents/xP_Core/data/{}.json'
                                                     .format(self.chrom_name)), 'r') as f:
                    file_length = len(f.readlines())
                    print("Name: " + self.chrom_name)

                if file_length == 3:
                    ftype = "w"
                    print("Rewriting file for: " + self.chrom_name)

            except Exception as e:  # noqa: E722
                print(e)
                self.chrom_name = str(uuid.uuid4())[:8]
                print("Exception: " + self.chrom_name)

        if new_name != "":
            self.chrom_name = new_name
            ftype = "a"
            self.update_chrom_map()

        self.write_soul_data(self.SPAWN_QUAD, ftype, score=0.0)

        self.dec_chromosome = Evolver.read_chrome(self.bin_chromosome)

        self.last_kill = ["null", "null"]
        self.last_death = ["null", "null"]

        self.current_loop_idx = 0
        self.current_loop = self.dec_chromosome[0]
        self.current_gene_idx = 0

    def process_server_feed(self):
        self.feed_history = []
        for i in range(5):
            server_message = ai.scanGameMsg(i)
            if self.bot_name in server_message \
                    and "ratio" not in server_message \
                    and "crashed" not in server_message \
                    and "entered" not in server_message \
                    and "suicide" not in server_message:
                self.feed_history.append(server_message)

        killer = "null"
        victim = "null"
        for message in self.feed_history:
            if "killed" in message:
                victim = message.split(" was")[0]
                killer = message.split("from ")[-1][:-1]
                break
            elif "smashed" in message or "trashed" in message:
                self.last_death = [killer, victim]
                return
        output = [killer, victim]
        if killer == self.bot_name:
            self.last_kill = output
        elif victim == self.bot_name:
            self.last_death = output

    def write_soul_data(self, quadrant, ftype="a", score=0.0):
        if score == 0.0:
            write_score = str(0.0)
        else:
            write_score = str(round(score, 3))

        output = [str(quadrant), self.bin_chromosome, write_score]
        print(output)
        print(write_score)

        Evolver.write_chromosome_to_file(output, "{}.json"
                                         .format(self.chrom_name), ftype)
        self.update_chrom_map()
        self.spawn_score = self.score

    def was_killed(self):
        agent.update_score()

        print(self.last_death)
        print(f"Current Score: {self.score}")
        print(f"Spawn Score: {self.spawn_score}")

        life_score = self.score - self.spawn_score
        print(f"Score to log: {life_score}")
        if "null" in self.last_death:
            print("self death")

            self.push_chrom(int(self.SPAWN_QUAD), self.chrom_name)
            self.write_soul_data(self.SPAWN_QUAD, "a", score=life_score)
            self.bin_chromosome = None
            self.SPAWN_QUAD = None

            return

        if ai.selfAlive() == 0 and self.crossover_completed is False:
            print("killed")
            killer = self.get_mapping(self.last_death[0])

            new_chromosome_file_name = os.path.expanduser("~/Documents/xP_Core/data/{}.json"
                                                          .format(killer))

            print(new_chromosome_file_name)
            with open(new_chromosome_file_name, 'r') as f:
                chromosome_data = json.loads(f.readlines()[-1])

            new_chromosome = chromosome_data[1]
            quadrant = chromosome_data[0]

            cross_over_child = Evolver.crossover(
                self.bin_chromosome, new_chromosome)
            mutated_child = Evolver.mutate(cross_over_child, self.MUT_RATE)
            self.bin_chromosome = mutated_child  # Set for soul write

            print(killer)
            print("Killed ^")

            self.write_soul_data(self.SPAWN_QUAD, "a", score=life_score)
            # POST New chromosome
            self.push_chrom(quadrant, self.chrom_name)  # TODO switch to
            self.push_chrom(quadrant, self.chrom_name)

            # Prep for fetching new chromosome
            self.bin_chromosome = None  # Erase for new chromosome to load
            self.SPAWN_QUAD = None

            self.crossover_completed = True

    def find_min_wall_angle(self, wall_feelers):
        min_wall = min(wall_feelers)
        min_index = wall_feelers.index(min_wall)
        angle = int(10 * min_index)
        return angle if angle < 180 else angle - 360

    def find_max_wall_angle(self, wall_feelers):
        max_wall = max(wall_feelers)
        max_index = wall_feelers.index(max_wall)
        angle = int(10 * max_index)
        return angle if angle < 180 else angle - 360

    def check_conditional(self, conditional_index):
        min_wall_dist = min(self.agent_data["head_feelers"])
        conditional_list = [self.agent_data["speed"] < 6, self.agent_data["speed"] == 0,
                            self.enemy_data["distance"] < 50, self.agent_data["head_feelers"][0] < 100,
                            self.enemy_data["distance"] < 150 and self.enemy_data["direction"] == 1,
                            self.enemy_data["distance"] < 150 and self.enemy_data["direction"] == 2,
                            self.enemy_data["distance"] < 100 and self.enemy_data["direction"] == 3,
                            self.enemy_data["distance"] < 100 and self.enemy_data["direction"] == 4,
                            min_wall_dist < 200, min_wall_dist < 75, min_wall_dist > 300, min_wall_dist < 150,
                            self.bullet_data["distance"] < 100, self.bullet_data["distance"] < 200,
                            self.bullet_data["distance"] < 50, self.enemy_data["distance"] == -1]
        return conditional_list[conditional_index]

    def set_spawn_quad(self):
        print("X: {}".format(self.agent_data["X"]))
        print("Y: {}".format(self.agent_data["Y"]))

        if agent.SPAWN_QUAD is None and self.agent_data["X"] != -1:
            spawn_x = self.agent_data["X"] - 4500
            spawn_y = self.agent_data["Y"] - 4500

            if spawn_x >= 0 and spawn_y >= 0:
                agent.SPAWN_QUAD = 1
            elif spawn_x < 0 and spawn_y >= 0:
                agent.SPAWN_QUAD = 2
            elif spawn_x < 0 and spawn_y < 0:
                agent.SPAWN_QUAD = 3
            else:
                agent.SPAWN_QUAD = 4

        return agent.SPAWN_QUAD


def loop():
    global agent
    global bot_name
    if agent is None:
        agent = CoreAgent(bot_name)

    try:
        if ai.selfAlive() == 1:
            if agent.SPAWN_QUAD is None:
                print("Spawn Quadrant: {} ".format(agent.set_spawn_quad()))
                agent.spawn_score = ai.selfScore()
                agent.SD = False
                ai.setTurnSpeed(64.0)
                agent.update_chrom_map()

            if agent.SPAWN_QUAD is not None and agent.bin_chromosome is None:
                agent.initialize_cga(agent.SPAWN_QUAD)

            if agent.agent_data["X"] != ai.selfX() or agent.agent_data["Y"] != ai.selfY():
                agent.movement_timer = time.time()

            if agent.movement_timer == -1.0:
                agent.movement_timer = time.time()
                agent.SD = False
                print("Initial SD timer set")

            if time.time() - agent.movement_timer > 5.0 and not agent.SD:
                ai.selfDestruct()
                agent.SD = True
                print("SD'ing")

            if agent.bin_chromosome is not None:
                agent.frames_dead = 0

                agent.update_agent_data()
                agent.update_enemy_data()
                agent.update_bullet_data()
                agent.update_score()

                agent.crossover_completed = False
                gene = agent.current_loop[agent.current_gene_idx]

                if Evolver.is_jump_gene(gene):
                    if agent.check_conditional(gene[1]):
                        agent.current_loop_idx = gene[2]
                        agent.current_loop = \
                            agent.dec_chromosome[agent.current_loop_idx]
                        agent.current_gene_idx = 0
                        return
                    else:
                        agent.increment_gene_idx()

                gene = agent.current_loop[agent.current_gene_idx]
                ActionGene(gene, agent)
                agent.increment_gene_idx()
            else:
                agent.update_agent_data()
        else:
            agent.process_server_feed()
            agent.frames_dead += 1
            # agent.SPAWN_QUAD = None
            agent.agent_data["X"] = -1
            agent.agent_data["Y"] = -1
            if agent.frames_dead >= 5:
                agent.was_killed()
                agent.frames_dead = -2000

    except Exception as e:
        print("Exception")
        print(str(e))
        traceback.print_exc()
        traceback_str = traceback.format_exc()
        fs = os.path.expanduser(f"~/Documents/xP_Core/tracebacks/{agent.chrom_name}.txt")
        with open(fs, "w") as f:
            f.write(traceback_str)
            f.write(str(agent.bin_chromosome))
            f.write(str(agent.dec_chromosome))
            f.write(str(agent.current_loop))
        ai.quitAI()


# SLURM 01: NL210-Lin10138
def main():
    global bot_name
    bot_name = "CA_{}".format(sys.argv[1])
    global agent
    agent = None
    ai.start(loop, ["-name", bot_name, "-join", config.SERVER_IP])
    if config.HEADLESS:
        ai.headlessMode()
    # ai.start(loop, ["-name", bot_name, "-join", "NL210-Lin10138"])


if __name__ == "__main__":
    main()
