import json

def clean_nones(value):
    """
    Recursively remove all None values from dictionaries and lists, and returns
    the result as a new dictionary or list.
    """
    exclusion_list = [None, 0, '', [], {}]
    if isinstance(value, list):
        return [clean_nones(x) for x in value if x not in exclusion_list]
    elif isinstance(value, dict):
        return {
            key: clean_nones(val)
            for key, val in value.items()
            if val not in exclusion_list
        }
    else:
        return value


# Counts how many performances there are in the sample data
count = 0
for i in range(1,5):
    fname = "BSO_Data/sample_data/bso_out_" + str(i) + ".json"
    f = open(fname)
    bsoj = json.load(f)
    resultcount = len(bsoj["Results"])
    count += resultcount
