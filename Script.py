from googleapiclient.discovery import build
from google.oauth2 import service_account
import requests
import time
import datetime
from datetime import datetime
from pytz import timezone    

def Runner():
    def DataReturned():
      def Requests_from_api():
        res = requests.get("https://www.blockchain.com/ticker");
        Data =  res.json()
        return (Data)

      x = Requests_from_api()
      values=[]
      for i in x:
        values.append(i)
      ist = timezone('Asia/Kolkata')
      ist_time = datetime.now(ist)
      time_ist= (ist_time.strftime('%m/%d  -  %H:%M:%S'))
      main_ans = [[" Recorded at "+str(time_ist) + " IST "],[]]
      for i in range(len(values)):
        y=[]
        y.append(values[i])
        y.append(x[values[i]]['15m'])
        y.append(x[values[i]]['last'])
        y.append(x[values[i]]['buy'])
        y.append(x[values[i]]['sell'])
        y.append(x[values[i]]['symbol'])
        main_ans.append(y)


      return (main_ans)

    Responses =DataReturned()

    SERVICE_ACCOUNT_FILE ='keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes=SCOPES)

    SAMPLE_SPREADSHEET_ID="1k4IbmnQ3W8ySoKr1R6T5IZc15IEj0-Q3bA_Wz3tSXfE"

    service =build('sheets','v4',credentials=creds)


    sheet = service.spreadsheets()

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="BlockChain").execute()

    values = result.get('values',[])
    value = len(result.get('values',[]))+2

    rangeeval = "BlockChain!A"+str(value)+":Z"
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=rangeeval,valueInputOption="USER_ENTERED",body={"values": Responses }).execute()

    print(values)

    time.sleep(2)

while(True):
  Runner()

