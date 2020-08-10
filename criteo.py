#!/usr/bin/env python3
"""
@author: MD.Nazmuddoha Ansary
"""
from __future__ import print_function
from termcolor import colored
from tqdm import tqdm
import math 
import os
import random
import time
#--------------------------------------------------------------------------------------------------------------------------------------------------
random.seed(0)
#--------------------------------------------------------------------------------------------------------------------------------------------------
class CRITEO:
    LABEL_COLUMN_INDEX  =   0
    NUMERICAL_FEATS     =   13
    CATEGORICAL_FEATS   =   26
    TOTAL_COLUMNS       =   40
#--------------------------------------------------------------------------------------------------------------------------------------------------
def log_msg(msg,mcolor='blue'):
    '''
    Prints Current Sate of program execution or necessary information in terminal
    args:
        msg     =   the message to print
        mcolor  =   the color for the message (default:blue)
    '''
    print(colored('#    LOG:','green'),colored(msg,mcolor))
#--------------------------------------------------------------------------------------------------------------------------------------------------
def scale_data(x):
    '''
    Scales Numerical Feature Columns (1 to 13)
    args:
        x   = numerical feature value
    returns:
        scaled data
    '''
    # When a value is missing, the field is just empty.There is no label field in the test set.
    if x == '':
        return '0'
    # formatting values > 2    
    elif float(x) > 2:
        return str(int(math.log(float(x))**2))
    else:
        return x
#--------------------------------------------------------------------------------------------------------------------------------------------------
def random_split(train_file,temp_file,eval_file):
    '''
    randomly splits and creates new files for training and evaluation
    args:
        train_file  =   original train.txt file
        temp_file   =   new file to be created for training after split
        eval_file   =   new file to be created for evaluation after split
    '''
    start_time=time.time()

    log_msg('Spliting Files!')
    with  open(temp_file,'w') as f_temp,open(eval_file,'w') as f_eval:
        for line in tqdm(open(train_file)):
            if random.uniform(0, 1) < 0.9:
                f_temp.write(line)
            else:
                f_eval.write(line)

    log_msg(f'Spliting Done!Time Taken:{round(time.time()-start_time,2)}s')
#--------------------------------------------------------------------------------------------------------------------------------------------------

def get_feature_count(input_file):
    '''
    '''
    start_time=time.time()

    log_msg('Reading File','yellow')
    log_msg(f'File path:{input_file}','cyan')
    
    count_freq = []
    for i in range(CRITEO.TOTAL_COLUMNS):
        count_freq.append({})
    
    for line in tqdm(open(input_file,'r')):
        # strip and split values
        line = line.replace('\n', '').split('\t')
        # feature colimns
        for i in range(1, CRITEO.TOTAL_COLUMNS):
            # numerical columns
            if i < CRITEO.LABEL_COLUMN_INDEX+1:
                line[i] = scale(line[i])
            # count frequency    
            if line[i] not in count_freq[i]:
                count_freq[i][line[i]] = 0
            
            count_freq[i][line[i]] += 1

    log_msg(f'Feature Count Done!Time Taken:{round(time.time()-start_time,2)}s')
    
    return count_freq
#--------------------------------------------------------------------------------------------------------------------------------------------------
def main(args):
    '''
    routine to save the .csv
    '''
    # create save_path is path does not exist
    if not os.path.exists(args.save_path):
        os.mkdir(args.save_path)
    # file paths
    train_file  =   os.path.join(args.dataset_path,'train.txt')
    temp_file   =   os.path.join(args.save_path,'temp.txt')
    eval_file   =   os.path.join(args.save_path,'eval.txt')
    # split the files
    #random_split(train_file,temp_file,eval_file)
    # get feature count 
    freq_dict=get_feature_count(train_file)
#--------------------------------------------------------------------------------------------------------------------------------------------------    
if __name__=='__main__':
#-------------------------------------------------------------------------------------------------------------------------
    import argparse
    parser = argparse.ArgumentParser(description=colored('Preprocessing Script for Criteo DataSet :Sparse Deep Field Aware Factorization Machine','yellow'))
    # dataset name
    parser.add_argument("dataset_path", help=colored('/absolute/path/to/dac/folder/','green'))
    parser.add_argument("save_path", help=colored('/absolute/path/to/folder/where/.csv/and/other/files/wiil/be/saved/','green'))
    args = parser.parse_args()
#--------------------------------------------------------------------------------------------------------------------------
    main(args)