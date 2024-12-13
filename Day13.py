import re


def parse_input(file_path):
    # Read the file content
    with open(file_path, 'r') as file:
        input_text = file.read()

    # Regular expression to match each block of data
    pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"

    # Find all matches in the input
    matches = re.findall(pattern, input_text)

    # Parse matches into a structured format
    results = []
    count = 1
    for match in matches:
        results.append({
            "id" : count,
            "a": {"x": int(match[0]), "y": int(match[1])},
            "b": {"x": int(match[2]), "y": int(match[3])},
            "prize": {"x": int(match[4]), "y": int(match[5])}
        })
        count += 1
    

    return results

data = parse_input("Day13_input.txt")

def token_count(xa, ya, xb, yb, px, py):

    #print((xa, ya, xb, yb, px, py))

    ca = (py*xb - px*yb)/(xb*ya - xa*yb)
    cb = -(py*xa - px*ya)/(xb*ya - xa*yb)

    ca = int(ca + .5)
    cb = int(cb + .5)

    #print(ca, cb)

    if ca < 0 or cb < 0:
        return -1

    dx = px - (ca * xa + cb * xb)
    dy = py - (ca * ya + cb * yb)

    if dx != 0 or dy != 0:
        return -1

    return ca * 3 + cb

offset = 10000000000000
total = 0
for m in data:
    count = token_count(m['a']['x'], m['a']['y'], m['b']['x'], m['b']['y'], m['prize']['x'] + offset, m['prize']['y'] + offset)


    print(m['id'], count)

    if count < 0:
        continue

    total += count

print(total)

