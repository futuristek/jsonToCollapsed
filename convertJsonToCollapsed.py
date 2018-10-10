import json, sys

def convert(file_name):
    file_name = parse_input()

    with open(file_name) as f:
        data = json.load(f)
        stack = "business"
        traces = []
        walk_tree(data, stack, traces)
    
    return traces

def save(file_name, traces):
    new_file_name = file_name + ".txt"
    with open (new_file_name, 'w') as f:
       for line in traces:
           f.write(line.encode('utf-8') + " 1" + "\n")

def walk_tree(data, stack, traces):
    if not data:
        return
    
    for k, v in data.items():
        newStack = stack + ";" + k
        traces.append(newStack)
        walk_tree(v, newStack, traces)

def parse_input():
    if len(sys.argv) != 2:
        sys.exit('Example usage: python convertJsonTOCollapsed.py facebookBizTree.json')

    return sys.argv[1]

if __name__ == "__main__":
    file_name = parse_input()
    traces = convert(file_name)
    save(file_name, traces)