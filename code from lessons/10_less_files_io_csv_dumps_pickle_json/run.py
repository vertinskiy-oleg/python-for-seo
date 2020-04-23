import csv


keywords_filter = set()
results = []


with open('keyword_stats.csv', 'r', encoding='utf-8', newline='') as file1:
    head = file1.__next__()

    fieldnames = ['keyword', 'keyword_symbols_count', 'keyword_words_count']

    file1_reader = csv.DictReader(file1, fieldnames=fieldnames, delimiter='\t')

    # file1_reader = csv.reader(file1, delimiter='\t')

    for raw in file1_reader:
        data = dict(raw)

        if data['keyword'] not in keywords_filter:
            results.append(raw)
            keywords_filter.add(raw['keyword'])


# keywords_uniq = set(keywords_all)
# keywords_result = list(keywords_uniq)
# keywords_result.sort()


# file2.writelines(keywords_result)
# result_as_text = '\n'.join(keywords_result)
# file2.write(result_as_text)

# keyword;keyword_symbols_count;keyword_words_count

results.sort(key=lambda x: x[0])


with open('result.csv', 'w', encoding='utf-8', newline='') as f2:
    f2.write(head)

    f2_writer = csv.writer(
        f2, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for line_data in results:
        f2_writer.writerow(line_data)


# head = 'Keyword\tKeyword Symbols\tKeyword Words\n'
# file2.write(head)
#
#
# for key in keywords_all:
#     key_s_count = len(key)
#     key_w_count = len(key.split())
#
#     row = f'{key}\t{key_s_count}\t{key_w_count}\n'
#
#     file2.write(row)


# lines = file1.readlines()
#
# print(lines)


# text1 = file1.read()
# text2 = file1.read()
# text3 = file1.read()
#
# print('======')
# print(text1)
# print('======')
# print(text2)
# print('======')
# print(text3)
# print('======')

# breakpoint()
