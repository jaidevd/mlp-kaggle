from yaml import safe_load

with open('cols.yaml', 'r') as fin:
    cols = safe_load(fin)
