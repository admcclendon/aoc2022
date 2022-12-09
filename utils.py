def load_data(filename: str):
    with open(filename, "r") as fp:
        data = fp.readlines()
        data = [line.strip() for line in data]
    return data
