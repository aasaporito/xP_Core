# Loop from 1 to 32
for ((i = 1; i <= 32; i++)); do
  (
    # Call the command, replacing "5" with the current iteration number
    python3 ~/Documents/xP_Core/src/core_controller.py $RANDOM </dev/null >/dev/null 2>&1 &
    sleep 0.75;
    )
done

echo "Launched 32 agents on machine, exiting.";
exit;
