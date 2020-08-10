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
def generate_feature_map_and_train_csv(temp_file, 
                                       train_csv, 
                                       file_feature_map, 
                                       freq_dict, 
                                       threshold):
    '''
    create the train_csv and returns the feature map for validation csv
    args:
        temp_file           =   the train file split that we will use for training
        tarin_csv           =   the file path for saving training data
        file_feature_map    =   the feature map file that will help us evaluate
        freq_dict           =   feature count dictionary
        threshold           =   categorical feature handling with data count
    returns:
        feature_map         =   dictionary for feature map
    '''                                   
    feature_map = []
    
    for i in range(40):
        feature_map.append({})
    
    start_time=time.time()
    log_msg('Creating train.csv File','yellow')
    
    with  open(train_csv, 'w') as fout:
        for line in tqdm(open(temp_file)):
            # read line
            line = line.replace('\n', '').split('\t')
            # label
            output_line = [line[0]]
            for i in range(1, CRITEO.TOTAL_COLUMNS):
                # map numerical features
                if i < CRITEO.NUMERICAL_FEATS+1:
                    # scale the data 
                    line[i] = scale(line[i])
                    output_line.append(line[i])
                # handle categorical features
                elif freq_dict[i][line[i]] < threshold:
                    output_line.append('0')
                elif line[i] in feature_map[i]:
                    output_line.append(feature_map[i][line[i]])
                else:
                    output_line.append(str(len(feature_map[i]) + 1))
                    feature_map[i][line[i]] = str(len(feature_map[i]) + 1)
            # write line
            output_line = ','.join(output_line)
            fout.write(output_line + '\n')
    log_msg(f'train.csv !Time Taken:{round(time.time()-start_time,2)}s')
    

    start_time=time.time()
    log_msg('Creating feature_map.csv File','yellow')
    # write feature_map file
    with  open(file_feature_map, 'w') as f_map: 
        for i in range(1, CRITEO.TOTAL_COLUMNS):
            for feature in feature_map[i]:
                f_map.write(str(i) + ',' + feature + ',' + feature_map[i][feature] + '\n')
    
    log_msg(f'feature_map.csv done!Time Taken:{round(time.time()-start_time,2)}s')
    
    return feature_map    
#--------------------------------------------------------------------------------------------------------------------------------------------------
def generate_valid_csv(eval_file,
                        eval_csv, 
                        feature_map):
    '''
    creates evaluation csv filr
    args:
        eval_file   =   splitted eval.txt file
        eval_csv    =   csv file to save eval data
        feature_map =   the feature map to generate valid evaluation data
    '''
    start_time=time.time()
    log_msg('Creating eval.csv File','yellow')
    
    with  open(eval_csv, 'w') as fout:
        for line in tqdm(open(eval_file)):
            # read line
            line = line.replace('\n', '').split('\t')
            # label
            output_line = [line[0]]
            for i in range(1, CRITEO.TOTAL_COLUMNS):
                if i < CRITEO.NUMERICAL_FEATS+1:
                    # scale the data
                    line[i] = scale(line[i])
                    output_line.append(line[i])
                elif line[i] in feature_map[i]:
                    output_line.append(feature_map[i][line[i]])
                else:
                    output_line.append('0')
            # write line
            output_line = ','.join(output_line)
            fout.write(output_line + '\n')

    log_msg(f'eval.csv done!Time Taken:{round(time.time()-start_time,2)}s')
#--------------------------------------------------------------------------------------------------------------------------------------------------
def main(args):
    '''
    routine to save the .csv
    '''
    # create save_path is path does not exist
    if not os.path.exists(args.save_path):
        os.mkdir(args.save_path)
    # file paths
    train_file      =   os.path.join(args.dataset_path,'train.txt')
    temp_file       =   os.path.join(args.save_path,'temp.txt')
    eval_file       =   os.path.join(args.save_path,'eval.txt')
    train_csv       =   os.path.join(args.save_path,'train.csv')
    eval_csv        =   os.path.join(args.save_path,'eval.csv')
    file_feature_map=   os.path.join(args.save_path,'criteo_feature_map.csv')
    # split the files
    #random_split(train_file,temp_file,eval_file)
    # get feature count 
    freq_dict=get_feature_count(train_file)
    # feature map and train.csv
    feature_map = generate_feature_map_and_train_csv(temp_file,train_csv,file_feature_map,freq_dict,8)
    # eval.csv
    generate_valid_csv(eval_file,eval_csv, feature_map)

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