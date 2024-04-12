#!/bin/bash

rm -r ~/Documents/xP_Core/data;
rm -r ~/Documents/xP_Core/tracebacks;

mkdir ~/Documents/xP_Core/data;
mkdir ~/Documents/xP_Core/tracebacks;


echo "Purged data folder"
echo "Purged traceback folder"

echo "Launching Queue Server"
python3 ~/Documents/xP_Core/src/QueueServer/queue_server.py > queue_server.log &
sleep 3;

# Start Server
echo "Starting Xpilots Server";
# switchBase 1 = 100% probability to swap bases on death, + teams disables teams
~/Documents/xP_Core/src/Engine/xpilots -map ~/Documents/xP_Core/src/Engine/maps/core.xp -noquit -switchBase 1.0 +teamPlay -maxRoundTime 60 -roundsToPlay 0 -limitedLives -maxClientsPerIP 32  > /dev/null 2>&1 &


# Slurms: 1,3,4,7,8,10,11,12,14,17
# server on slurm01
echo "Starting Agent 1-2"
python3 ~/Documents/xP_Core/src/core_controller.py $RANDOM &
python3 ~/Documents/xP_Core/src/core_controller.py $RANDOM &
python3 ~/Documents/xP_Core/src/core_controller.py $RANDOM &
python3 ~/Documents/xP_Core/src/core_controller.py $RANDOM &

