# pySDeepFwFm
DeepFwFM Code porting for Criteo and Avazu

        Version: 0.0.1   
        Author : Md. Nazmuddoha Ansary

![](src_img/python.ico?raw=true)

# Version and Requirements
* Python == 3.6.9
* pip    == 20.2.1

### Qucik Setup 
* install virtualenv if not present
* Create a Virtual environment: ```$virtualenv ctrenv``` 

> *(the name ctrenv is completely random, I am using this name and its already added in **.gitignore** for converience)* 

* install the requirements:```pip3 install -r requirements.txt```

#  DataSet

## Criteo

1. Download [Criteo CTR DataSet From Here](http://labs.criteo.com/2014/02/download-kaggle-display-advertising-challenge-dataset/)    
2. Extract the **dac.tar.gz** and keep a note of the absolute path of the **dac** folder       

### **Issues**:
1. Huge Data Volume ( **~11.1 GiB**): not really recommended to open with pandas 
2. Missing Feature attributes: The semantic of the features is undisclosed.Meaning we dont have the column names to find similiar features.


![](src_img/ci1.png?raw=true)


N:B:[Image Source](https://www.kaggle.com/c/criteo-display-ad-challenge/data)

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

**A Sample Execution log would look like this:**

![](src_img/log.png?raw=true)

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
