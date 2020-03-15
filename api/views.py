from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

'''
<Fitbit 데이터 가져오기 API>
- GET https://api.fitbit.com/1/user/-/activities/heart/date/[date]/[end-date]/[detail-level]/time/[start-time]/[end-time].json
- GET https://api.fitbit.com/1/user/-/activities/heart/date/[date]/1d/[detail-level]/time/[start-time]/[end-time].json

<Example Request>
GET https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1sec/time/00:00/00:01.json

<Example Response>
{
    "activities-heart": [
        {
            "customHeartRateZones": [],
            "dateTime": "today",
            "heartRateZones": [
                {
                    "caloriesOut": 2.3246,
                    "max": 94,
                    "min": 30,
                    "minutes": 2,
                    "name": "Out of Range"
                },
                {
                    "caloriesOut": 0,
                    "max": 132,
                    "min": 94,
                    "minutes": 0,
                    "name": "Fat Burn"
                },
                {
                    "caloriesOut": 0,
                    "max": 160,
                    "min": 132,
                    "minutes": 0,
                    "name": "Cardio"
                },
                {
                    "caloriesOut": 0,
                    "max": 220,
                    "min": 160,
                    "minutes": 0,
                    "name": "Peak"
                }
            ],
            "value": "64.2"
        }
    ],
    "activities-heart-intraday": {
        "dataset": [
            {
                "time": "00:00:00",
                "value": 64
            },
            {
                "time": "00:00:10",
                "value": 63
            },
            {
                "time": "00:00:20",
                "value": 64
            },
            {
                "time": "00:00:30",
                "value": 65
            },
            {
                "time": "00:00:45",
                "value": 65
            }
        ],
        "datasetInterval": 1,
        "datasetType": "second"
    }
}
'''
def apiTest(request):
    test_data = {
        "activities-heart": [
            {
                "customHeartRateZones": [],
                "dateTime": "today",
                "heartRateZones": [
                    {
                        "caloriesOut": 2.3246,
                        "max": 94,
                        "min": 30,
                        "minutes": 2,
                        "name": "Out of Range"
                    },
                    {
                        "caloriesOut": 0,
                        "max": 132,
                        "min": 94,
                        "minutes": 0,
                        "name": "Fat Burn"
                    },
                    {
                        "caloriesOut": 0,
                        "max": 160,
                        "min": 132,
                        "minutes": 0,
                        "name": "Cardio"
                    },
                    {
                        "caloriesOut": 0,
                        "max": 220,
                        "min": 160,
                        "minutes": 0,
                        "name": "Peak"
                    }
                ],
                "value": "64.2"
            }
        ],
        "activities-heart-intraday": {
            "dataset": [
                {
                    "time": "00:00:00",
                    "value": 64
                },
                {
                    "time": "00:00:10",
                    "value": 63
                },
                {
                    "time": "00:00:20",
                    "value": 64
                },
                {
                    "time": "00:00:30",
                    "value": 65
                },
                {
                    "time": "00:00:45",
                    "value": 65
                }
            ],
            "datasetInterval": 1,
            "datasetType": "second"
        }
    }
    heartRateZones = test_data['activities-heart'][0]['heartRateZones']
    heartRateZones = { i : heartRateZones[i] for i in range(0, len(heartRateZones) ) }
    print(heartRateZones)
    # if (test_data['activities-heart'][0]['heartRateZones'])
    return JsonResponse(heartRateZones, json_dumps_params = {'ensure_ascii': True})
