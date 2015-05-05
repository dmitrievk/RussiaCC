__author__ = 'konstantindmitriev'

import csv
from os.path import expanduser
import os
import numpy

dict_results = {}  # {'country1': '% - affected rate', ...}
path = os.path.join(expanduser("~"), 'RussiaCCResults')
list_of_csv_files_of_results = os.listdir(path)
if '.DS_Store' in list_of_csv_files_of_results:
    list_of_csv_files_of_results.remove('.DS_Store')


# # mu and sigma calculation for the USA
mu_USA = 0.35888755344
std_USA = 0.189278916144
# listOfScoresFromTheUSA = []
# for file in list_of_csv_files_of_results:
#     csv_results_reader = csv.reader(open(os.path.join(path, file)))
#     for url, country, score in csv_results_reader:
#         if country == 'USA':
#             listOfScoresFromTheUSA.append(float(score))
# mean = numpy.mean(listOfScoresFromTheUSA)
# print("Mean: ", mean)
# std = numpy.std(listOfScoresFromTheUSA)
# print("STD: ", std)


pre_dict_of_scores_for_every_country = {}  # {country1: [score1, score2, ...], ...}
for file in list_of_csv_files_of_results:
    csv_results_reader = csv.reader(open(os.path.join(path, file)))
    for url, country, score in csv_results_reader:
        if country in pre_dict_of_scores_for_every_country.keys():
            prev_array_of_scores = pre_dict_of_scores_for_every_country[country]
            pre_dict_of_scores_for_every_country[country] = prev_array_of_scores + [float(score)]
        else:
            pre_dict_of_scores_for_every_country[country] = [float(score)]

dict_of_scores_for_every_country = {}  # {country1: mean1, ...}
list_of_affected_countries = []
for country in pre_dict_of_scores_for_every_country.keys():
    dict_of_scores_for_every_country[country] = numpy.mean(pre_dict_of_scores_for_every_country[country])
    if dict_of_scores_for_every_country[country] >= mu_USA + 0.2*std_USA:
        list_of_affected_countries.append(country)
print(dict_of_scores_for_every_country)
print(list_of_affected_countries)




#
# # read files and keep the results in dict_temp_results_for_a_test for each file
# dict_temp_results_for_a_test = {}  # {'url': {'country1': 'score1', ...}, ...}
# for file in list_of_csv_files_of_results:
#     csv_results_reader = csv.reader(open(os.path.join(path, file)))
#     current_url = ''
#     dict_for_current_url = {}
#     for url, country, score in csv_results_reader:
#         if url == current_url:
#             dict_for_current_url[country] = score
#         else:
#             dict_for_current_url = {}
#             current_url = url
#         dict_temp_results_for_a_test[current_url] = dict_for_current_url
#
#     # delete url from dict_temp_results_for_a_test that has the same
#     # score (or very close) for all countries (by doing this,
#     # we assume that such url is a outlier)
#     list_or_urls_to_remove = []
#     for url in dict_temp_results_for_a_test.keys():
#         results_for_url = dict_temp_results_for_a_test[url]
#
#         list_of_values = list(results_for_url.values())
#         remove_flag = True
#         sum_score = 0
#         for value in list_of_values:
#             # if (float(value) < 0.1) and (float(value) > 0):  # if there is any country that has a
#                                                             # score that is not suspicious leave this url
#                 # country_count = country_count + 1
#             sum_score = sum_score + float(value)
#         if sum_score <= 0.2 * 9:
#             remove_flag = False
#         if remove_flag == True:
#             list_or_urls_to_remove.append(url)
#
#
#     # remove outliers
#     for url in list_or_urls_to_remove:
#         dict_temp_results_for_a_test.pop(url)
#
#     for url in dict_temp_results_for_a_test.keys():
#         print(url)
#     print("# of urls:", len(dict_temp_results_for_a_test.keys()))
#
#     # calculate an affected rate
#     for url in dict_temp_results_for_a_test.keys():
#         results_for_url = dict_temp_results_for_a_test[url]
#         for country in results_for_url:
#             if country in dict_results:
#                 previous_score = dict_results[country]
#                 dict_results[country] = previous_score + float(results_for_url[country])
#             else:
#                 dict_results[country] = 0
# results_for_russia = dict_results['Russia']
# for country in dict_results:
#     dict_results[country] = dict_results[country] * 100 / results_for_russia
#
# print(dict_results)
#
#
#
#
#
#
