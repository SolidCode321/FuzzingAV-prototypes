# faster_fuzzer_pipeline.py

import os
import csv
import time
import clamd
from fuzzers.random_fuzzer import generate_random_string, save_to_file

# Connect to clamd daemon
cd = clamd.ClamdNetworkSocket(host='localhost', port=3310)

# Ensure logs directory exists
log_dir = 'FuzzingAV-prototypes/logs'
os.makedirs(log_dir, exist_ok=True)
logfile = os.path.join(log_dir, 'scan_results_fast.csv')

# Prepare CSV file
with open(logfile, 'w', newline='') as csvfile:
    fieldnames = ['file', 'infected', 'result']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    start_time = time.time()  # Start timing

    for _ in range(100000):  # Adjust number of iterations
        fuzz = generate_random_string(200)
        file_path = save_to_file(fuzz)  # saves to ../samples/fuzzed_xx

        try:
            result = cd.scan(file_path)
            if result and file_path in result:
                scan_result = result[file_path]
                infected = scan_result[0] == 'FOUND'
                output = scan_result[1]
            else:
                infected = False
                output = 'Clean or Unreadable'
        except Exception as e:
            infected = False
            output = f"Error: {str(e)}"

        writer.writerow({
            'file': file_path,
            'infected': infected,
            'result': output
        })

        print(f"Scanned: {file_path}, Infected: {infected}, Result: {output}")

    end_time = time.time()  # End timing
    elapsed = end_time - start_time
    print(f"\n⏱️ Total scan time for 100 files: {elapsed:.2f} seconds")
    print(f"📄 Results saved to: {logfile}")