import os
import requests
import csv
from bs4 import BeautifulSoup
import time
import pprint as pp


def file_soup(path):
    file = open(path, 'r', encoding='utf-8')
    read = file.read()
    file.close()
    return BeautifulSoup(read, 'html5lib')


def write_csv(lines, file_name):
    file = open(file_name, 'a', encoding='utf-8', newline='')
    writer = csv.writer(file, delimiter=',')
    writer.writerows(lines)
    file.close()


def main():
    directory = 'html'
    for file in os.listdir(directory):
        path = os.path.join(directory, file)
        soup = file_soup(path)
        g_list = soup.select('.g .r > a')
        for g in g_list:
            link = g['href']
            year = ''
            for y in years:
                if y in link:
                    year = y
                    break
            line = [year, 'Audi', '', 'PDF', '', link]
            print(line)
            write_csv(lines=[line], file_name=file_name)


if __name__ == '__main__':
    print('------ Start ------')
    years = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
    header = [['YEAR', 'MAKE', 'MODEL', 'SECTION', 'TITLE', 'PDF']]
    file_name = 'Audi_MANUAL.csv'
    write_csv(lines=header, file_name=file_name)
    main()
    print('----- The End -----')