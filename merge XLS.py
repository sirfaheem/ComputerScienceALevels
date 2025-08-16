# importing the required modules
import glob
import pandas as pd
 
# specifying the path to csv files
path = "C:/Users/Faheem/Desktop/temp"
 
# csv files in the path
file_list = glob.glob(path + "/*.xlsx")
 
# list of excel files we want to merge.
# pd.read_excel(file_path) reads the excel
# data into pandas dataframe.
excl_list = []
 
for file in file_list:
    excl_list.append(pd.read_excel(file))
 
# create a new dataframe to store the
# merged excel file.
excl_merged = pd.DataFrame()
 
for excl_file in excl_list:
     
    # appends the data into the excl_merged
    # dataframe.
    excl_merged = excl_merged._append(
      excl_file, ignore_index=True)
 
# exports the dataframe into excel file with
# specified name.
excl_merged.to_excel('mergedfile.xlsx', index=False)
