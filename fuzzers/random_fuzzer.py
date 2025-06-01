# fuzzers/random_fuzzer.py
import os
import random
import string

def generate_random_string(length=100):
    return ''.join(random.choices(string.printable, k=length))

def save_to_file(content, directory=os.path.join(os.pardir, 'samples/fuzzed'), extension='.txt'):
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, f'fuzz_{random.randint(1000,9999)}{extension}')
    with open(file_path, 'w') as f:
        f.write(content)
    return file_path

if __name__ == "__main__":
    for _ in range(10):  # Generate 10 samples
        fuzz = generate_random_string()
        path = save_to_file(fuzz)
        print(f"Generated: {path}")