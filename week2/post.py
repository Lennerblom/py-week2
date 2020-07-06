#  !/usr/bin/python3
import requests

# define the URL we want to use
POSTURL = "http://validate.jsontest.com/"
DATEURL = "http://date.jsontest.com/"
IPURL = "http://ip.jsontest.com"

def main():

    #getting Date in JSON format
    dt = requests.get(DATEURL)
    date_time = dt.json()
    print(date_time)

    #getting IP address in JSON format
    ip_raw = requests.get(IPURL)
    ip = ip_raw.json()
    print('ip is: ', ip)

    with open('myservers.txt', 'r') as f:
        server_file = f.readlines()
        print('Server file: ', server_file)

    myjson = {
        "json": {
            "time": f"{date_time['date']} {date_time['time']}",
            "ip": ip['ip'],
            "mysvrs": f"{server_file},"
        }
    }

    print('myjson: ', myjson)

    # test data to validate as legal json
    # when a POST json= is replaced by the KEY "json"
    # the key "json" is mapped to a VALUE of the json to test
    # because the test item is a string, we can include whitespaces
    mydata = {"json": "{'fruit': ['apple', 'pear'], 'vegetable': ['carrot']}" }
    

    # use requests library to send an HTTP POST
    resp = requests.post(POSTURL, data=myjson)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print("YO",respjson)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()
