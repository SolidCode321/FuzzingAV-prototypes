# run_fuzzer_pipeline.py

from fuzzers.random_fuzzer import generate_random_string, save_to_file
from fuzzers.clamav_scanner import scan_with_clamav
import csv
import os

# Prepare logs directory
logfile = 'FuzzingAV-prototypes/logs/scan_results.csv'
os.makedirs('logs', exist_ok=True)

# Set up CSV for logging results
with open(logfile, 'w', newline='') as csvfile:
    fieldnames = ['file', 'infected', 'crashed', 'returncode', 'stdout', 'stderr']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Fuzz and scan loop
    for i in range(10):  # Adjust number of iterations as needed
        fuzz = generate_random_string(200)
        file_path = save_to_file(fuzz)  # Saves to ../samples/fuzzed_*.txt

        result = scan_with_clamav(file_path)

        infected = 'FOUND' in result.get('stdout', '')
        crashed = result.get('returncode', 0) != 0

        writer.writerow({
            'file': file_path,
            'infected': infected,
            'crashed': crashed,
            'returncode': result.get('returncode'),
            'stdout': result.get('stdout'),
            'stderr': result.get('stderr')
        })

        print(f"[{i+1}] Scanned: {file_path} | Infected: {infected} | Crashed: {crashed}")