# Physical Activity Monitoring
### Alexander Chow for CS 886 project at University of Waterloo.
### For Human Activity Recognition of the PAMAP2 Dataset
#### [1] A. Reiss and D. Stricker. Introducing a New Benchmarked Dataset for Activity Monitoring. The 16th IEEE International Symposium on Wearable Computers (ISWC), 2012. 

#### Setup

Install all the necessary programs and tools (these instructions are for homebrew. If you use apt-get, that also works).

    brew install pip
    pip install flask

Clone the git repository:

    git clone https://github.com/alexchow/PAMAP.git
    cd PAMAP

Download the data set:

    wget http://archive.ics.uci.edu/ml/machine-learning-databases/00231/PAMAP2_Dataset.zip
    unzip PAMAP2_Dataset.zip

Populate the sqlite database with the dataset

    python start.py populatedb

Note: if the python process is getting killed, it's probably linux's Out-of-memory killer. Set up a swap file

Run the server:

    python start.py

You can see data and features visualized in your web browser at 

    http://localhost:5000/view

In the source code, you can see that it uses the URL for deciding the page view. Queries accepted are as follows:

| Query         | Value         | 
| ------------- |:-------------:| 
| windowInterval| The number of samples in each time window. Default = 200               | 
| activities    | Comma separated list of activity IDs to use. Default = 'handAccX', handAccY,chestAccX,chestAccY,ankleGyrX,heartrate               | 
| data\_keys              | Comma-separated list of raw data columns to use. Example: handAccX,chestGyrY,heartrate. Default uses all sensor data               | 
| numWindows | The number of time windows to use. Default = 3| 

An example query is:

    http://localhost:5000/view?windowInterval=250&numWindows=4&data_keys=handAccX,chestAccX,ankleGyrX
