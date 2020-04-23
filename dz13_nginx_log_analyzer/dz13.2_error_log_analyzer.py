import os
import gzip

from log_filter import error_line_filter

base_dir = 'logs'

all_log_files = os.listdir(base_dir)
all_log_files.sort()

result_file = open('error_results.csv', 'w', encoding='utf-8')
result_file.write('Date\tURL\tError\n')

results = []

for filename in all_log_files:

    file_path = f'{base_dir}/{filename}'

    if 'access' in file_path:
        continue

    if file_path.endswith('.gz'):
        log_file = gzip.open(file_path)
    else:
        log_file = open(file_path)

    for line in log_file:

        data = error_line_filter(line)

        if not data:
            continue

        date, url, error = data

        results.append(
            {
                'date': date,
                'url': url,
                'error': error
            }
        )
    log_file.close()

for result in results:
    result_file.write(f"{result['date']}\t{result['url']}\t"
                      f"{result['error']}\n")
