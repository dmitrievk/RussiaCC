__author__ = 'konstantindmitriev'
import time

import csv
from os.path import expanduser
import os
from WebPageDistance import WebPageDistance
# from alignment import needle
from Main import countries

dict_of_results = {'TestURL1': {'Country1': 0}}  # {'url1': {'country1': result, ..}, .. } for each test


def create_dict_of_results_and_save(path):
    list_of_folders_of_tests = os.listdir(path)

    for i in range(0, len(list_of_folders_of_tests)):  #for each test
        test_i = list_of_folders_of_tests[i]
        print(test_i)
        t0 = time.clock()
        countries = os.listdir(os.path.join(expanduser("~"), 'RussiaCCData', test_i))
        for country in countries:
            html_pages = os.listdir(os.path.join(expanduser("~"), 'RussiaCCData', test_i, country))
            for html_page in html_pages:
                temp_dict = {}  #{'country1': result, ..}
                file = os.path.join(os.path.join(expanduser("~"), 'RussiaCCData', test_i, country, html_page))
                if os.path.isfile(file):
                    with open(file, "r") as f:
                        content = f.read()
                    temp_dict[country] = content

                    try:
                        temp_dict2 = dict_of_results[html_page]
                    except KeyError:
                        temp_dict2 = {}
                    temp_dict2.update(temp_dict)
                    dict_of_results[html_page] = temp_dict2

        if 'TestURL1' in dict_of_results.keys():
            dict_of_results.pop('TestURL1')
        scorer = WebPageDistance(metric='shift3b', max_offset=65)
        scores = {}  #{'url1': {'country1': result, ..}, .. } for each test
        # for country in countries:
        count = 1
        for url in dict_of_results.keys():
            print("Done: %3.2f%%..." % (count * 100 / len(dict_of_results.keys())))
            count = count + 1
            russian_page = dict_of_results[url]['Russia']
            temp_dict = {}
            for country in countries:
                current_page = dict_of_results[url][country]
                temp_dict[country] = scorer(russian_page, current_page)
            scores[url] = temp_dict

        #save results
        w = csv.writer(open(os.path.join(expanduser("~"), 'RussiaCCResults', test_i) + "--output.csv", "w"))
        for url in dict_of_results.keys():
            for country in countries:
                w.writerow([url, country, scores[url][country]])
        print(time.clock() - t0, "seconds")



def main():
    path = os.path.join(expanduser("~"), 'RussiaCCData')
    create_dict_of_results_and_save(path)


if __name__ == '__main__':
    main()
