import csv
import json
import pickle


# results = []
#
#
# with open('keyword_stats.csv', 'r', encoding='utf-8', newline='') as file1:
#     head = file1.__next__()
#     fieldnames = ['keyword', 'keyword_symbols_count', 'keyword_words_count']
#     file1_reader = csv.DictReader(file1, fieldnames=fieldnames, delimiter='\t')
#     for raw in file1_reader:
#         results.append(dict(raw))
#
#
# with open('key_dump.pickle', 'wb') as f2:
#     pickle.dump(results, f2)

#
# with open('key_dump.pickle', 'rb') as f1:
#     results = pickle.load(f1)


with open('key_dump.json', 'r') as f1:
    results = json.load(f1)


print(results)

# with open('key_dump.json', 'w') as f1:
#     json.dump(results, f1, ensure_ascii=False, indent=4)

