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
machines=(
    lab02
    lab03
    lab04
    lab05
    lab07
    lab08
    lab09
    lab10
    lab11
    lab12
    lab13
    lab14
    lab15
    lab16
    lab17
    )

echo "Running instances"
python3 ~/Documents/xP_Core/core_controller.py $RANDOM &
python3 ~/Documents/xP_Core/core_controller.py $RANDOM &


for server in "${servers[@]}"
do
    echo "Connecting to: "$server 
    ssh -X asaporito@$server
    for i in {0..2..1}
    do
        python3 ~/Documents/xP_Core/core_controller.py $RANDOM &
    done
done

# Labs1-20, slrm 1,3 4-14, 17
# ssh lab02 -X &

# Wait for all instances to finish
wait;

echo "All $num_instances instances have been started.";
