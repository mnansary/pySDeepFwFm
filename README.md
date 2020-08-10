# pySDeepFwFm
DeepFwFM Code porting for Criteo and Avazu

        Version: 0.0.1   
        Author : Md. Nazmuddoha Ansary
                  
# Version and Requirements
* Python == 3.6.8
> Create a Virtualenv and *pip3 install -r requirements.txt*

#  DataSet

### Criteo

1. Download [Criteo CTR DataSet From Here](http://labs.criteo.com/2014/02/download-kaggle-display-advertising-challenge-dataset/)    
2. Extract the **dac.tar.gz** and keep a note of the absolute path of the **dac** folder       

#  Preprocessing
* **clear_mem.sh (Ubuntu/Linux)**:The complete preprocessing may take huge time and also cause to crash the system due to high memory useage. A way around is built for **Ubuntu** users is to run **sudo ./clear_mem.sh** in parallel with **criteo.py**
* **criteo.py**:

        usage: criteo.py [-h] dataset_path save_path

        Preprocessing Script for Criteo DataSet :Sparse Deep Field Aware
        Factorization Machine

        positional arguments:
        dataset_path  /absolute/path/to/dac/folder/
        save_path     /absolute/path/to/folder/where/.csv/and/other/files/wiil/
                        be/saved/

        optional arguments:
        -h, --help    show this help message and exit

    * the **dataset_path** is the absolute path of the **dac** folder
    * if meromy on hardisk is not a problem keep the **save_path** same as **dataset_path**

* **Routine**:
    * **Splits The Dataset (train.txt) into evaluation and training file**

    > Takes around **5 min** time

    * **Counts Feature Maps**: needed for creating **.csv** files for pipeline

    > Takes around **15 min** time


**ENVIRONMENT**  

    OS          : Ubuntu 18.04.3 LTS (64-bit) Bionic Beaver        
    Memory      : 7.7 GiB  
    Processor   : Intel® Core™ i5-8250U CPU @ 1.60GHz × 8    
    Graphics    : Intel® UHD Graphics 620 (Kabylake GT2)  
    Gnome       : 3.28.2  

# TODO

- [x] Create script for **Criteo** dataset preprocessing
- [ ] Create script for **Avazu** dataset preprocessing
- [ ] Prepare Pipeline code 
- [ ] Port **DeepFwFM** code 
- [ ] Create Training Loop
- [ ] Add CPP code for complexity calculation(optional)
