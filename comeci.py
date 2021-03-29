import base64
import requests
import json
from urllib import parse

def find_school(school_name):
    encoded_name = parse.quote_plus(school_name.encode("euckr"))
    res = requests.get("http://112.186.146.81:4082/138604?98128l{}".format(encoded_name))
    data = res.content.decode("utf-8").replace("\x00","")
    return json.loads(data)

def get_cigan_data(school_id):
    encoded_name = str(base64.b64encode("68737_{}_0_1".format("57333").encode()).decode())
    res = requests.get("http://112.186.146.81:4082/138604?{}".format(encoded_name))
    data = res.content.decode("utf8").replace("\x00","")
    return json.loads(data)

def get_simple_cigan_data_dict(school_id):
    data = get_cigan_data(school_id)
    out = {}
    
    for grade_num in range(1, len(data["자료185"])):
        out[grade_num] = {}
        for class_num in range(1, len(data["자료185"][grade_num])):
            out[grade_num][class_num] = {}
            for day_num in range(1, len(data["자료185"][grade_num][class_num])):
                out[grade_num][class_num][day_num] = []
                for i in range(1,9):
                    a = data["자료185"][grade_num][class_num][day_num][i]
                    time = data["일과시간"][i-1]
                    teacher_name = data["자료378"][int(a/100)][0:2]
                    subject_name = ""
                    if(a>100):
                        subject_name = data["자료545"][a - int(a/100) * 100]
                    out[grade_num][class_num][day_num].append({"time": time, "teacher": teacher_name, "subject": subject_name})
    return out

def get_simple_cigan_data_arr(school_id):
    data = get_cigan_data(school_id)
    out = []
    
    for grade_num in range(1, len(data["자료185"])):
        out.append([])
        for class_num in range(1, len(data["자료185"][grade_num])):
            out[grade_num - 1].append([])
            for day_num in range(1, len(data["자료185"][grade_num][class_num])):
                out[grade_num-1][class_num-1].append([])
                for i in range(1,9):
                    a = data["자료185"][grade_num][class_num][day_num][i]
                    time = data["일과시간"][i-1]
                    teacher_name = data["자료378"][int(a/100)][0:2]
                    subject_name = ""
                    if(a>100):
                        subject_name = data["자료545"][a - int(a/100) * 100]
                    out[grade_num-1][class_num-1][day_num-1].append({"time": time, "teacher": teacher_name, "subject": subject_name})
    return out
