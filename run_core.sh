#!/bin/bash

rm -r ~/Documents/xP_Core/data;
rm -r ~/Documents/xP_Core/tracebacks;

mkdir ~/Documents/xP_Core/data;
mkdir ~/Documents/xP_Core/data/chromosome_logs;
mkdir ~/Documents/xP_Core/tracebacks;


echo "Purged data folder"
echo "Purged traceback folder"

# Start Server
echo "Starting Xpilots Server";
# switchBase 1 = 100% probability to swap bases on death, + teams disables teams
~/Documents/xP_Core/xpilots -map ~/Documents/xP_Core/simple.xp -noquit -switchBase 1.0 +teams -maxRoundTime 60 -roundsToPlay 0 -resetOnHuman 1 -limitedLives -maxClientsPerIP 32 &


# Slurms: 1,3,4,7,8,10,11,12,14,17
# server on slurm01
echo "Starting Agent 1..."
python3 ~/Documents/xP_Core/core_controller.py $RANDOM >/dev/null 2>&1 &
echo "Starting Agent 2..."
python3 ~/Documents/xP_Core/core_controller.py $RANDOM >/dev/null 2>&1 &

echo "Starting Agent 3-4"
ssh -X slurm03 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm03 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

echo "Starting Agent 5-6"
ssh -X slurm04 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm04 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

echo "Starting Agent 7-8"
ssh -X slurm07 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm07 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

echo "Starting Agent 9-10"
ssh -X slurm08 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm08 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

echo "Starting Agent 11-12"
ssh -X slurm10 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm10 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

echo "Starting Agent 13-14"
ssh -X slurm11 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm11 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

echo "Starting Agent 15-16"
ssh -X slurm12 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm12 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

echo "Starting Agent 17-18"
ssh -X slurm14 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm14 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

echo "Starting Agent 19-20"
ssh -X slurm17 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm17 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &







# TODO :: Add rest of slurms
