#!/usr/bin/bash
# Loop from 1 to 32
for ((i = 1; i <= 100; i++)); do
  (
    # Call the command, replacing "5" with the current iteration number
    ./xpilot -name a$i -join localhost &
    sleep 0.75;
    )
done

echo "Launched 32 agents on machine, exiting.";
exit;
