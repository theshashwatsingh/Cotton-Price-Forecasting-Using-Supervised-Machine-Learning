import json
import os

from django.shortcuts import render

import pandas as pd

from datetime import datetime
from MetaData.Data import RequiredData as rd
import joblib as jb
from .models import Download


model = jb.load('MetaData/Model/FinalModelMinMaxWorking.sav')


# dictionaries


def home(request):


    global list
    def get_key_of_variety(variety):
        for key, value in rd.VarietyRank.items():
            if variety == value:
                return key


    if request.method == "POST":

        list = []
        label = []
        data = []

        post = request.POST


        year = post.get('year')
        State = rd.State1.get(post.get('state'))
        month_for_html = rd.Month.get(post.get('month'))
        variety = get_key_of_variety((int(post.get('variety'))))

        list.append(int(post.get('year')))
        list.append(int(post.get('month')))
        list.append(int(post.get('state')))
        list.append(int(post.get('variety')))
        #retdict = {'year' : post.get('year'), 'month' :  post.get('month'), 'state' : post.get('state'), 'variety':post.get('variety')}
        predicted_value = model.predict([list])

        df = pd.read_csv('MetaData/Data/graph variety  , state wise.csv')
        df = df[(df['States_In_Number'] == list[2]) & (df['Variety_Rank'] == list[3])]

        for (i, j) in zip(df['Production_Year'].values, df['Modal Price'].values):
            label.append(str(i))
            data.append(j)

        data.append(int(predicted_value[0]))
        label.append(int(post.get('year')))


        # state = "{}.csv".format(str(post['state']))

        # df = pd.read_csv(state)
        # print(post.get('year'))
        # labels = []
        # data = []
        # for (i,j) in zip(df['Production_Year'].values,df['Modal_Price'].values):
        #     labels.append(str(i))
        #     data.append(j)

        # labels.append(str(post.get('year')))
        # data.append(int(predicted_value[0]))
        # print(labels)
        # print(data)

        # if (post.get('chart-categories')):
        #     chartcategories = str(request.POST.get('chart-categories'))
        # else:
        # year  month   state variety
        predicted_value_without_array = str(predicted_value[0])
        predicted_value_without_array = "{} RS ".format(predicted_value_without_array[:7])
        required_data = {'year': year, 'month_for_html': month_for_html, 'State': State, 'variety': variety,
                         'predicted_value': predicted_value_without_array, 'labels': label, 'data': data}

        return render(request, "prediction.html", required_data)

    else:
        # print("Dataframe is " , dfc1['Production_Year'])

        return render(request, "index.html")


def minmax(request):
    #
    # today = datetime.today()
    # y = today.year
    # m = today.month
    # month_list = [i for i in range(m, 13)]
    #
    #
    #
    #
    # pred = {}
    #
    # for m in month_list:
    #     minp = 99999
    #     maxp = 0
    #     mins = -1
    #     minv = -1
    #     maxs = -1
    #     maxv = -1
    #     for s in rd.StateDict.values():
    #         for v in rd.varietyInState[s]:
    #             predic = model.predict([[y, m, s, v]])
    #             if predic > maxp:
    #                 maxp = predic
    #                 maxs = s
    #                 maxv = v
    #             if predic < minp:
    #                 minp = predic
    #                 mins = s
    #                 minv = v
    #
    #     pred[m] = {"min": [mins, minv, minp], "max": [maxs, maxv, maxp]}
    # rd.minmax[y] = pred
    today = datetime.today()
    y = today.year
    def save(d):
        with open('MetaData/Data/MinMax.json', 'w') as f:
            json.dump(d, f)

    def calculate_and_store():
        m = today.month
        month_list = [i for i in range(1, 13)]
        pred = {}
        for m in month_list:
            minp = 99999
            maxp = 0
            mins = -1
            minv = -1
            maxs = -1
            maxv = -1
            for s in rd.StateDict.values():
                for v in rd.varietyInState[s]:
                    predic = model.predict([[y, m, s, v]])
                    if predic > maxp:
                        maxp = predic
                        maxs = s
                        maxv = v
                    if predic < minp:
                        minp = predic
                        mins = s
                        minv = v

            pred[m] = {"min": [mins, minv, minp[0]], "max": [maxs, maxv, maxp[0]]}
        final = {}
        final[y] = pred

        save(final)
        return final
    pred= {}
    if (os.path.getsize("MetaData/Data/MinMax.json") == 0):

        pred = calculate_and_store()


    else:

        with open('MetaData/Data/MinMax.json', ) as f:
            data = json.load(f)
            if (str(y) not in data):

                pred = calculate_and_store()


            else:


                pred = data[str(y)]

    context = {'pred': pred, 'Month': rd.Month, 'State': rd.State1, 'VarietyRank': rd.VarietyRank}

    return render(request, "minmax.html", context)


def help(request):
    return render(request, "Help.html")

def download_files(request):
    download_files = Download.objects.all()
    return render(request,"download.html",{'download_files':download_files})
