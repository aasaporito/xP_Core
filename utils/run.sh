#!/bin/bash

rm -r ~/Documents/xP_Core/data;
rm -r ~/Documents/xP_Core/tracebacks;

mkdir ~/Documents/xP_Core/data;
mkdir ~/Documents/xP_Core/tracebacks;

echo "Wiped data & traceback folder";

echo "Launching Queue Server";
python3 ~/Documents/xP_Core/src/QueueServer/queue_server.py > queue_server.log &
sleep 3;

# Start Server
echo "Starting Xpilots Server";
# switchBase 1 = 100% probability to swap bases on death, + teams disables teams
~/Documents/xP_Core/src/Engine/xpilots -map ~/Documents/xP_Core/src/Engine/maps/core.xp -noquit -switchBase 1.0 +teamPlay -maxRoundTime 60 -roundsToPlay 0 +limitedLives -maxClientsPerIP 32  > xpilots.log &


# Slurms: 1,3,4,7,8,10,11,12,14,17
# server on slurm01
echo "Starting local agents";
python3 ~/Documents/xP_Core/src/core_controller.py $RANDOM > /dev/null 2>&1  &
python3 ~/Documents/xP_Core/src/core_controller.py $RANDOM > /dev/null 2>&1 &



echo "Starting Agents on slurm servers";
ssh -X slurm03 "~/Documents/xP_Core/utils/launcher.sh" &
ssh -X slurm04 "~/Documents/xP_Core/utils/launcher.sh" &
ssh -X slurm08 "~/Documents/xP_Core/utils/launcher.sh" &
ssh -X slurm10 "~/Documents/xP_Core/utils/launcher.sh" &
ssh -X slurm11 "~/Documents/xP_Core/utils/launcher.sh" &
ssh -X slurm12 "~/Documents/xP_Core/utils/launcher.sh" &
ssh -X slurm13 "~/Documents/xP_Core/utils/launcher.sh" &
ssh -X slurm14 "~/Documents/xP_Core/utils/launcher.sh" &
ssh -X slurm17 "~/Documents/xP_Core/utils/launcher.sh" &

echo "Finished launching agents. Exiting.";
exit;