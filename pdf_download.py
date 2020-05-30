import requests
import csv
import time
import pprint
import os


def get_urls():
    path = 'Audi_MANUAL.csv'
    with open(file=path, encoding='utf-8', mode='r') as reader:
        records = list(csv.reader(reader))
    result = []
    for record in records:
        if record[5] != 'PDF':
            result.append(record[5])
    return result


def send_request(url):
    try:
        res = requests.request('GET', url=url)
        if res.status_code == 200:
            return res
        return send_request(url)
    except Exception:
        time.sleep(5)
        return send_request(url)


def write_content(content, file_name):
    if not os.path.isdir('PDF'):
        os.mkdir('PDF')
    file_path = os.path.join('PDF', file_name)
    file = open(file_path, 'wb')
    file.write(content)
    file.close()


def main():
    pdf_urls = get_urls()
    for pdf_url in pdf_urls:
        response = send_request(url=pdf_url)
        pprint.pprint(pdf_url)
        if '.pdf' in pdf_url.split('/')[-1]:
            file_name = pdf_url.split('/')[-1]
        else:
            file_name = pdf_url.split('/')[-1] + '.pdf'
        write_content(content=response.content, file_name=file_name)


if __name__ == '__main__':
    print('----- Start -----')
    main()
    print('---- The End ----')
