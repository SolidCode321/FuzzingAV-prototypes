# fuzzers/clamav_scanner.py
import subprocess

def scan_with_clamav(file_path):
    result = subprocess.run(
        ['clamscan', '--no-summary', '--infected', file_path],
        capture_output=True,
        text=True
    )
    return {
        'file': file_path,
        'stdout': result.stdout.strip(),
        'stderr': result.stderr.strip(),
        'returncode': result.returncode
    }

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python clamav_scanner.py <file_path>")
    else:
        result = scan_with_clamav(sys.argv[1])
        print(result)