# run_fuzzer_pipeline.py
from fuzzers.random_fuzzer import generate_random_string, save_to_file
from fuzzers.clamav_scanner import scan_with_clamav
import csv
import os

# Save logs in the current directory
logfile = 'logs/scan_results.csv'
os.makedirs('logs', exist_ok=True)

with open(logfile, 'w', newline='') as csvfile:
    fieldnames = ['file', 'infected', 'output']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for _ in range(10):  # Adjust number of iterations
        fuzz = generate_random_string(200)
        file_path = save_to_file(fuzz)  # This now saves to ../samples/fuzzed
        result = scan_with_clamav(file_path)

        infected = 'FOUND' in result['stdout']
        writer.writerow({
            'file': file_path,
            'infected': infected,
            'output': result['stdout']
        })

        print(f"Scanned: {file_path}, Infected: {infected}")