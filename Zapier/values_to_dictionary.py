keys_name = list(input_data.keys())
output_dict = {}

keys = input_data[keys_name[0]].split(',')
values = input_data[keys_name[1]].split(',')

for (k, v) in zip(keys, values):
    output_dict[k] = v

return output_dict
