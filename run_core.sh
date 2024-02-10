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

./xpilots -map simple.xp -noquit -switchBase 1.0 +teams -maxRoundTime 60 -roundsToPlay 0 -resetOnHuman 1 -limitedLives -maxClientsPerIP 32 &
sleep 2;
# Set the number of instances you want to run
num_instances=2;

echo "Running instances"
python3 ~/Documents/xP_Core/core_controller.py $RANDOM &
python3 ~/Documents/xP_Core/core_controller.py $RANDOM &

# Labs1-20, slrm 1,3 4-14, 17
# ssh lab02 -X &
# python3 ~/Documents/xP_Core/core_controller.py "2" &
# python3 ~/Documents/xP_Core/core_controller.py "3" &

# ssh lab03 -X &
# python3 ~/Documents/xP_Core/core_controller.py "4" &
# python3 ~/Documents/xP_Core/core_controller.py "5" &

# ssh lab04 -X &
# python3 ~/Documents/xP_Core/core_controller.py "6" &
# python3 ~/Documents/xP_Core/core_controller.py "7" &


# Wait for all instances to finish
wait;

echo "All $num_instances instances have been started.";
