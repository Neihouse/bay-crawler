def get_seed_urls(seed_file):
    with open(seed_file, 'r') as file:
        return [line.strip() for line in file.readlines()]