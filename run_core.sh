#!/bin/bash

# Start Server
echo "Starting Xpilots Server";
# switchBase 1 = 100% probability to swap bases on death, + teams disables teams
python3 reset_cga_storage.py;
echo "Reset data and tracebacks folder";
./xpilots -map simple.xp -noquit -switchBase 1.0 +teams -maxRoundTime 60 -roundsToPlay 0 -resetOnHuman 1 -limitedLives -maxClientsPerIP 32 &
sleep 2;
# Set the number of instances you want to run
num_instances=2;

echo "Running instances"
python3 ~/Documents/xP_Core/core_controller.py "$($RANDOM)" &
python3 ~/Documents/xP_Core/core_controller.py "$($RANDOM)" &

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
