#!/bin/bash

rm -r ~/Documents/xP_Core/data;
rm -r ~/Documents/xP_Core/tracebacks;

mkdir ~/Documents/xP_Core/data;
mkdir ~/Documents/xP_Core/data/chromosome_logs;
mkdir ~/Documents/xP_Core/tracebacks;


echo "Purged data folder"
echo "Purged traceback folder"

echo "Launching Queue Server"
python3 ~/Documents/xP_Core/QueueServer/queue_server.py > queue_server.log &
sleep 5;

# Start Server
echo "Starting Xpilots Server";
# switchBase 1 = 100% probability to swap bases on death, + teams disables teams
~/Documents/xP_Core/xpilots -map ~/Documents/xP_Core/core.xp -noquit -switchBase 1.0 +teamPlay -maxRoundTime 60 -roundsToPlay 0 -limitedLives -maxClientsPerIP 32 &


# Slurms: 1,3,4,7,8,10,11,12,14,17
# server on slurm01
echo "Starting Agent 1-2"
python3 ~/Documents/xP_Core/core_controller.py $RANDOM >/dev/null 2>&1 &
python3 ~/Documents/xP_Core/core_controller.py $RANDOM >/dev/null 2>&1 &

#!/bin/bash

echo "Starting Agents on slurm servers"

#echo "Starting Agent 3-4 on slurm02"
#ssh -X slurm02 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
#ssh -X slurm02 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

echo "Starting Agent 5-6 on slurm03"
ssh -X slurm03 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm03 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm03 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm03 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm03 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm03 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm03 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm03 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm03 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm03 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm03 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm03 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm03 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm03 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm03 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm03 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &


# echo "Starting Agent 7-8 on slurm04"
ssh -X slurm04 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm04 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm04 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm04 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm04 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm04 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm04 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
ssh -X slurm04 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

tail -f queue_server.log
# echo "Starting Agent 9-10 on slurm05"
# ssh -X slurm05 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
# ssh -X slurm05 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

# #echo "Starting Agent 11-12 on slurm06"
# #ssh -X slurm06 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
# #ssh -X slurm06 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

# #echo "Starting Agent 13-14 on slurm07"
# #ssh -X slurm07 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
# #ssh -X slurm07 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

# echo "Starting Agent 15-16 on slurm08"
# ssh -X slurm08 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
# ssh -X slurm08 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

# echo "Starting Agent 17-18 on slurm09"
# ssh -X slurm09 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
# ssh -X slurm09 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

# echo "Starting Agent 19-20 on slurm10"
# ssh -X slurm10 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
# ssh -X slurm10 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

# echo "Starting Agent 21-22 on slurm11"
# ssh -X slurm11 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
# ssh -X slurm11 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

# echo "Starting Agent 23-24 on slurm12"
# ssh -X slurm12 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
# ssh -X slurm12 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

# #echo "Starting Agent 25-26 on slurm13"
# #ssh -X slurm13 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
# #ssh -X slurm13 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

# echo "Starting Agent 27-28 on slurm14"
# ssh -X slurm14 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
# ssh -X slurm14 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

# echo "Starting Agent 29-30 on slurm15"
# ssh -X slurm15 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
# ssh -X slurm15 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

# echo "Starting Agent 31-32 on slurm16"
# ssh -X slurm16 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
# ssh -X slurm16 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &

# echo "Starting Agent 33-34 on slurm17"
# ssh -X slurm17 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
# ssh -X slurm17 "python3 ~/Documents/xP_Core/core_controller.py $RANDOM" &
