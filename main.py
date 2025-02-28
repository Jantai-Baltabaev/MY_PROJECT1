from first_project.function import process
from first_project.statistic import get_stat_dict
import json

with open('parallelepipeds.json', 'r') as f:
  parallelepipeds = json.load(f)
  
charecteristics_ = dict()
for fig, atr_dict in parallelepipeds.items():
    a = float(atr_dict['a'])
    b = float(atr_dict['b'])
    c = float(atr_dict['c'])
    charecteristics_[fig] = process(a, b, c)
    
statistics = get_stat_dict(charecteristics_)
# --- get load
    
with open('outputs/charecteristics_.json', 'w') as f:
  json.dump(charecteristics_, f, indent=4)
  
with open('outputs/statistics.json', 'w') as f:
    json.dump(statistics, f, indent=4)
  

