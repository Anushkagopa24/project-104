from collections import Counter
import csv

def get_mean(total_height, total_entries):
    mean = total_height / total_entries
    print ("mean (average) is -> {mean:2f}")

def get_median(total_entries, sorted_data):
    if total_entries %2 == 0:
        median1 = float(sorted_data[total_entries//2])
        median2 = float(sorted_data[total_entries//2 - 1])
        median = (median1 + median2)/2  
    else:
        median = float(sorted_data[total_entries//2])
        print ("mean (average) is -> {mean:2f}")

def get_mode(sorted_data):
    data = Counter(sorted_data)
    mode_data_for_range = {
                             "75-80":0,
                             "80-85":0,
                             "85-90":0,
                             "90-95":0,
                             "95-100":0,
                             "100-105":0,
                             "105-110":0,
                             "110-115":0,
                             "115-120":0,
                             "120-125":0,
                             "125-130":0,
                             "130-135":0,
                             "135-140":0,
                             "145-150":0,
                             "150-155":0,
                             "155-160":0,
                             "160-165":0,
                             "165-170":0,
                             "170-175":0
}
for height, occurence in data.items():
    if 75 < float(height) <80:
        mode_data_for_range["75-80"] += occurence 
    elif 80 < float(height) <85:
        mode_data_for_range["80-85"] += occurence
    elif 85 < float(height) <90:
        mode_data_for_range["85-90"] += occurence 
    elif 90 < float(height) <95:
        mode_data_for_range["90-95"] += occurence 
    elif 95 < float(height) <100:
        mode_data_for_range["95-100"] += occurence 
    elif 100 < float(height) <105:
        mode_data_for_range["100-105"] += occurence
    elif 105 < float(height) <110:
        mode_data_for_range["105-110"] += occurence 
    elif 110 < float(height) <115:
        mode_data_for_range["110-115"] += occurence 
    elif 115 < float(height) <120:
        mode_data_for_range["115-120"] += occurence 
    elif 120 < float(height) <125:
        mode_data_for_range["120-125"] += occurence
    elif 125 < float(height) <130:
        mode_data_for_range["125-130"] += occurence
    elif 130 < float(height) <135:
        mode_data_for_range["130-135"] += occurence
    elif 135 < float(height) <140:
        mode_data_for_range["135-140"] += occurence 
    elif 140 < float(height) <145:
        mode_data_for_range["140-145"] += occurence
    elif 145 < float(height) <150:
        mode_data_for_range["145-150"] += occurence
    elif 150 < float(height) <155:
        mode_data_for_range["150-155"] += occurence
    elif 155 < float(height) <160:
        mode_data_for_range["155-160"] += occurence
    elif 160 < float(height) <165:
        mode_data_for_range["160-165"] += occurence
    elif 165 < float(height) <170:
        mode_data_for_range["165-170"] += occurence
    elif 170 < float(height) <175:
        mode_data_for_range["170-175"] += occurence 
        
    mode_range, mode_occurence = 0, 0
    for range, occurence in mode_data_for_range.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float((mode_range[0] + mode_range[1]) / 2)
    print(f"Mode is -> {mode:2f}")