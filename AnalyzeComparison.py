__author__ = 'konstantindmitriev'

import csv
from os.path import expanduser
import os

dict_results = {}  # {'country1': '% - affected rate', ...}
path = os.path.join(expanduser("~"), 'RussiaCCResults')
list_of_csv_files_of_results = os.listdir(path)
list_of_csv_files_of_results.remove('.DS_Store')


# read files and keep the results in dict_temp_results_for_a_test for each file
dict_temp_results_for_a_test = {}  # {'url': {'country1': 'score1', ...}, ...}
for file in list_of_csv_files_of_results:
    csv_results_reader = csv.reader(open(os.path.join(path, file)))
    current_url = ''
    dict_for_current_url = {}
    for url, country, score in csv_results_reader:
        if url == current_url:
            dict_for_current_url[country] = score
        else:
            dict_for_current_url = {}
            current_url = url
        dict_temp_results_for_a_test[current_url] = dict_for_current_url

    # delete url from dict_temp_results_for_a_test that has the same
    # score (or very close) for all countries (by doing this,
    # we assume that such url is a outlier)
    list_or_urls_to_remove = []
    for url in dict_temp_results_for_a_test.keys():
        results_for_url = dict_temp_results_for_a_test[url]

        list_of_values = list(results_for_url.values())
        remove_flag = True
        country_count = 0
        for value in list_of_values:
            if (float(value) < 0.1) and (float(value) > 0):  # if there is any country that has a
                                                            # score that is not suspicious leave this url
                country_count = country_count + 1
        if country_count >= 2:
            remove_flag = False
        if remove_flag == True:
            list_or_urls_to_remove.append(url)


    # remove outliers
    for url in list_or_urls_to_remove:
        dict_temp_results_for_a_test.pop(url)

    for url in dict_temp_results_for_a_test.keys():
        print(url)
    print("# of urls:", len(dict_temp_results_for_a_test.keys()))

    # calculate an affected rate
    for url in dict_temp_results_for_a_test.keys():
        results_for_url = dict_temp_results_for_a_test[url]
        for country in results_for_url:
            if country in dict_results:
                previous_score = dict_results[country]
                dict_results[country] = previous_score + float(results_for_url[country])
            else:
                dict_results[country] = 0

results_for_russia = dict_results['Russia']
for country in dict_results:
    dict_results[country] = dict_results[country] * 100 / results_for_russia

print(dict_results)






# csv_results_reader = csv.reader(open(path))