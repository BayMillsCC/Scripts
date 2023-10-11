# CSV Combinding Script

### Setup

1. place all files into the root of a Flash Drive

### CSV Collection:

1. Delete or archive any old files from the `in` folder from the Flash Drive's last use
2. Plug the Flash Drive into a system you want to get a CSV from
3. Verify that the Flash Drive is labeled as the `D:` drive
    1. **if it is:** Run the script from the `script.txt` file in an *admin* powershell window
    2. **if it is not:** Run all but the last line of the `script.txt` file in an *admin* powershell file and manually move the CSV to the `in` folder when complete
4. Unplug the Flash Drive
5. repeat steps 2-4 on all of the systems you want to get CSVs from, then proceed to CSV Merging

### CSV Merging:

1. Make sure the system is using atleast python3
2. Add any CSV(s) to the `in` folder
3. Run the `main.py` file from the terminal
4. The combinded CSV file should now be in the `out` folder (named the current date and time), it can now be uploaded to autopilot
