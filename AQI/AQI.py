#coding=utf8

def calcAQI(C,mold,standard='cn'):
    #index_i means AQI
    index_i=[0,50,100,150,200,300,400,500]
    #the index is use for 24hours average if without annotations at the end of the line
    #most of the index are getting form https://en.wikipedia.org/wiki/Air_quality_index expect index_cn
    if mold=='pm2.5':
        index_cn=[0,35,75,115,150,250,350,500]
        index_us=[0,15.4,40.4,65.4,150.4,250.4,350.4,500.4]
    elif mold=='pm10':
        index_cn=[0,50,150,250,350,420,500,600]
        index_us=[0,54,154,254,354,424,504,604]
    elif mold=='CO':
        index_cn=[0,2,4,14,24,36,48,60]
        #index_cn=[0,5,10,35,60,90,120,150] #1hour
        index_us=[0,4.4,9.4,12.4,15.4,30.4,40.4,50.4]
    elif mold=='SO2':
        index_cn=[0,50,150,475,800,1600,2100,2620]
        #index_cn=[0,150,500,650,800,1600,2100,2620] #1hour
        index_us=[0,35,75,185,304,604,804,1004]
    elif mold=='NO2':
        index_cn=[0,40,80,180,280,565,750,940]
        #index_cn=[0,100,200,700,1200,2340,3090,3840] #1hour
        index_us=[0,53,100,360,649,1249,1649,2049]
    elif mold=='O3':
        #index_cn=[0,100,160,215,265,800,1000,1000] #8hours
        index_cn=[0,160,200,300,400,800,1000,1200] #1hour
        #index_us=[0,54,70,85,105,200] #8hours
        index_us=[0,0,124,164,204,404,504,604] #1hour
    else:
        return 'Unknown'

    if standard=='us':
        index_calc=index_us
    else:
        index_calc=index_cn

    #consult the formula https://en.wikipedia.org/wiki/Air_quality_index#Computing_the_AQI
    for i in index_calc:
        if i>C:
            break;
    j=index_calc.index(i)

    Ih=float(index_i[j])
    Il=float(index_i[j-1])
    Ch=float(index_calc[j])
    Cl=float(index_calc[j-1])
    C=float(C)

    #formula
    aqi=(Ih-Il)*(C-Cl)/(Ch-Cl)+Il

    return int(round(aqi))

def AQILevel(aqi):
    #two languages
    #level={50: 'Good',100: 'Moderate',150: 'Unhealthy for Sensitive Groups',200: 'Unhealthy',300: 'Very Unhealthy',400: 'Hazardous',500: 'Hazardous',501:'Overflow'}
    level={50: '优',100: '良',150: '轻度污染',200: '中度污染',300: '重度污染',400: '严重污染',500: '有毒害',501:'爆表'}
    index_i=[0,50,100,150,200,300,400,500,501]
    for i in index_i:
        if i>=aqi:
            break
    return level[i]

def AQI(pm2dot5,pm10=0,co=0,so2=0,no2=0,o3=0,standard='cn'):
    #if value equals zero ,do not calcuate
    rst={'pm2.5':calcAQI(pm2dot5,'pm2.5',standard)}
    if pm10!=0:
        rst['pm10']=(calcAQI(pm10,'pm10',standard))
    if co!=0:
        rst['CO']=(calcAQI(co,'CO',standard))
    if so2!=0:
        rst['SO2']=(calcAQI(so2,'SO2',standard))
    if no2!=0:
        rst['NO2']=(calcAQI(no2,'NO2',standard))
    if o3!=0:
        rst['O3']=(calcAQI(o3,'O3',standard))

    #Print all of the result .Only return the AQI as the result
    print (rst)
    return max(rst.values())
