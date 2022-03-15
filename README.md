# exam-guido-enrique

## Setup
### run the `.setup.sh` file with `bash setup.sh` or type the commands yourself
```bash
#!/bin/bash

docker pull postgres
sudo amazon-linux-extras enable python3.8
sudo yum install python3.8
docker run --name mutt -e POSTGRES_PASSWORD=root -d postgres
```
---

## <ins>**Download crypto data**</ins>
* go to `/home/ec2-user/exam-guido-enrique/`
* type: `python download_data.py --help`
```python
Mutt-data download crypto info tool

optional arguments:
  -h, --help            show this help message and exit
  -s STARTDATE, --startdate STARTDATE
                        startdate in format ISO8601(e.g. 2019-10-30)
  -e ENDDATE, --enddate ENDDATE
                        endate in format ISO8601(e.g. 2019-10-5)
  -c COIN, --coin COIN  the coin name(e.g. bitcoin - ethereum - cardano)
  -d DATE, --date DATE  the date for the coin data
  -persist              persist the data
```
**(e.g.)**
```python
python3 -c ethereum 
python3 -c ethereum -s 2021-02-02 -e 2021-02-04 
python3 -c bitcoin -d 2018-04-15

# and, if you want to persist the data into the postgreSQL database
# you should add the '-persist' param
python3 -c ethereum -persist
python3 -c cardano -d 2020-04-01 -persist
```

Note: if you don't put the date, the script will download the data for the today's date** \
*(All the data will be in /coins/$coinname)*

---

## <ins>**Crontab**</ins>
You can see the crontab file with `crontab -e`, it will contains the following lines:
```python
# everyday at 3 AM
0 3 * * * /usr/bin/python3 download_data.py -c bitcoin
0 3 * * * /usr/bin/python3 download_data.py -c ethereum
0 3 * * * /usr/bin/python3 download_data.py -c cardano
```