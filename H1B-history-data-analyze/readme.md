### Environment
Python 2.7

### data download from
[download address](https://drive.google.com/open?id=0BxGfxvHiFHqmRzdDbGZxWF9mems
)
### Dependence,Lib
numpy
scipy
matplotlib
sklearn
pandas


###Running method
python h1bSystem.py (ensure h1b_history.csv in the same level folder )


### Function description

#### 1.showCASE_STATUS
    >Analyze the H1Bs by the status of their visa applications and show the plot
    
![Image from H1B+Prediction+Research+Report, page 4](https://lh3.googleusercontent.com/-RWPj10k_oQM/Wi4VcJ6VC0I/AAAAAAAAOzs/FtpBhtCXLhgC8anSnbGaF1gi9TGzrjxZACHMYCw/I/Image%2Bfrom%2BH1B%252BPrediction%252BResearch%252BReport%252C%2Bpage%2B4.png)


#### 2.showWORKSITE
    > K-Means Clustering to separate the h1b location
    > show the plot of the h1b WORKSITE after k-mean
    > dense is the parameter to control distance between point, when gaining the info from the H1LatLong
    
![Image from H1B+Prediction+Research+Report, page 5](https://lh3.googleusercontent.com/-GrGjrojUpjA/Wi4VcbhQ8NI/AAAAAAAAOzw/HShFong4bRYi_XOdOxMWGkYGT0_-BUVLACHMYCw/I/Image%2Bfrom%2BH1B%252BPrediction%252BResearch%252BReport%252C%2Bpage%2B5.png)


#### 3.showSALARY_table
    > show the salary detail after k-mean process
    
![Image from H1B+Prediction+Research+Report, page 6](https://lh3.googleusercontent.com/-wFUd3g-4RmM/Wi4UWGg9ydI/AAAAAAAAOzY/jZcvpdTJY4Q2MzwqGJLgXkA0b8-ElNS7wCHMYCw/I/Image%2Bfrom%2BH1B%252BPrediction%252BResearch%252BReport%252C%2Bpage%2B6.png)

#### 4.showSALARY_plot
    > Plotting and comparison to the median US salary (2015)
    
![Image from H1B+Prediction+Research+Report, page 7](https://lh3.googleusercontent.com/-hu1UWwfMtxc/Wi4Vcp-rb1I/AAAAAAAAOz0/57SnlgdveGsrKAHZ3WMAaKmPcW0wkz5_ACHMYCw/I/Image%2Bfrom%2BH1B%252BPrediction%252BResearch%252BReport%252C%2Bpage%2B7.png)


#### 5.showTOP10com_table
    > show top 6 company who has apply to the h1b for employee
    
![Image from H1B+Prediction+Research+Report, page 8](https://lh3.googleusercontent.com/-xwCz1BBdwIs/Wi4Vc00pbcI/AAAAAAAAOz4/D7WZjhwkENQdETOM9n6A_3Qc7BoozLA8QCHMYCw/I/Image%2Bfrom%2BH1B%252BPrediction%252BResearch%252BReport%252C%2Bpage%2B8.png)


#### 6.showYearTrend_plot
    > show the h1b number in every year's change
    
![Image from H1B+Prediction+Research+Report, page 12](https://lh3.googleusercontent.com/-sKlXW71HBEo/Wi4UWfEgFYI/AAAAAAAAOzc/fvj9JAN-4PAyoUg0DSPMOseuFqS_nLGCwCHMYCw/I/Image%2Bfrom%2BH1B%252BPrediction%252BResearch%252BReport%252C%2Bpage%2B12.png)

#### 7.showJOBTITLE_plot
    > show top20 popular Job title and top10 Worksites for H1-B Visa holders
    
![Image from H1B+Prediction+Research+Report, page 9](https://lh3.googleusercontent.com/-JzexjBKo9Co/Wi4Vde-dlKI/AAAAAAAAOz8/_7oLb3x1-qo6egNOS6hf_wAV0tqtnr_LACHMYCw/I/Image%2Bfrom%2BH1B%252BPrediction%252BResearch%252BReport%252C%2Bpage%2B9.png)


#### 8.showAVGSalary_plot
    > show top20 salary mean Job title
    
![Image from H1B+Prediction+Research+Report, page 10](https://lh3.googleusercontent.com/-ZQHXlZQEHos/Wi4UWvBZeII/AAAAAAAAOzg/eTDqGtZ4jYkhwzU2nzqH--gQw1Zk4CVowCHMYCw/I/Image%2Bfrom%2BH1B%252BPrediction%252BResearch%252BReport%252C%2Bpage%2B10.png)

#### 9.showFullvsPart_plot
    > show the difference between fulltime job and part time job.
    
![Image from H1B+Prediction+Research+Report, page 11](https://lh3.googleusercontent.com/-g5LnvIzeso0/Wi4VdtasB8I/AAAAAAAAO0A/te3KqNs8-ykx2YmppgCvl1fgE0OQ8oveACHMYCw/I/Image%2Bfrom%2BH1B%252BPrediction%252BResearch%252BReport%252C%2Bpage%2B11.png)e


#### 10.predic_showCASE_STATUS

    > CASE_STATUS situation predict. using decision Tree algorithm from sklearn

#### 11.DecisionTreeAcuracy top10Accuracy
    > test one specify job's accuracy in 2016 base on 2011-2015 data

#### 12.top10Accuracy
    > get top10 popular job's accuracy in 2016 base on 2011-2015
    
![Screen Shot 2017-12-10 at 11.12.18 P](https://lh3.googleusercontent.com/-UM5xuWIdRn4/Wi4VeGaFdpI/AAAAAAAAO0E/qLJ-k6lol60ulypsWtqN9zHbzQzNUu0oACHMYCw/I/Screen%2BShot%2B2017-12-10%2Bat%2B11.12.18%2BPM.png)



