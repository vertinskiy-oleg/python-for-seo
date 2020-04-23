import re

regex = r'.*sale.*'

with open('demo_keys.txt', 'r') as f:
    keys_with_sale = set(re.findall(regex, f.read()))

with open('sale_keys.txt', 'w') as f:
    f.writelines(k + '\n' for k in keys_with_sale)
