#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs08/progassignment?name=106

import sys
sys.setrecursionlimit=10000;
def rainaverage(city_rain):
    city_rain_list=dict();
    for city,rain in city_rain:
        try:
            city_rain_list[city].append(rain);
        except:
            city_rain_list[city]=[rain];
    city_rain_avg=dict();
    for city,rain in city_rain_list.items():
        city_rain_avg[city]=sum(rain)/len(rain);
    return sorted(city_rain_avg.items(),key=lambda x:x[0]);

def flatten(complex_list):
    simple_list=[];
    for i in complex_list:
        if(type(i)!=list):
            simple_list.append(i);
        else:
            simple_list = simple_list + flatten(i);
    return simple_list
