import json
import pandas as pd
import datetime
from datetime import date
from datetime import timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import gspread_dataframe as gd

class save_data_into_sheet:
    def __init__(self):
        self.scope = ['https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', self.scope)
        self.client = gspread.authorize(self.creds)
        self.observation = []
        self.list_doc = []

    def fetch_json_data_file(self):
        today = date.today()
        yesterday = today - timedelta(days=1)
        yesterday = yesterday.strftime('%d-%b-%Y') + ".json"
        with open('chatHistoryLogs/'+yesterday) as f:
            json_data = json.load(f)
        return json_data;

    def extract_data_save_in_df(self, datas):
        for data in datas:
            for item in data['events']:
                if item['event'] == 'user':
                    sender_id = data['sender_id']
                    user_question = item['text']
                    timestamp = item['timestamp']
                    c_datetime, c_date, c_time = self.convert_timestamp_into_date_time(timestamp)
                    intent_name = item['parse_data']['intent']['name']
                    self.list_doc = [c_date, sender_id, user_question, intent_name, c_datetime, c_time]

                if item['event'] == 'bot':
                    bot_reply = item['text']
                    self.list_doc.append(bot_reply)

            if len(self.list_doc) != 0:
                self.observation.append(self.list_doc)
                self.list_doc = []

        Rasa_dataframe = pd.DataFrame(self.observation,
                                      columns=['Date', 'Sender_id', 'Sender_Question', 'Intent_Name', 'Datetime', 'Time', 'Bot_Reply'])
        return Rasa_dataframe

    def convert_timestamp_into_date_time(self,timestamp):
        timestamp = datetime.datetime.fromtimestamp(timestamp)
        datetime_converted = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        convert_date = timestamp.strftime('%Y-%m-%d')
        convert_time = timestamp.strftime('%H:%M:%S')
        return datetime_converted, convert_date, convert_time

    def call_sheet(self, sheet_name, worksheet_name):
        self.sheet = self.client.open(sheet_name).worksheet(worksheet_name)
        return self.sheet

    def save_output_into_sheet(self, worksheet, df_list):
        existing_df = gd.get_as_dataframe(worksheet)
        # print("Existing DF"+ existing_df)
        try:
            print("Output of rasa appending to the new sheet...!")
            for row in df_list:
                worksheet.append_row(row)
            print("Output response of Rasa has been appended to new sheet successfully..!")
            return True
        except:
            print("something went wrong while updating google sheet..!")

data_obj = save_data_into_sheet()
data = data_obj.fetch_json_data_file()
dataframe = data_obj.extract_data_save_in_df(data)
sheet = data_obj.call_sheet("Chatbot_Daily_Report","Sheet7")
df_list_value = dataframe.values.tolist()
output = data_obj.save_output_into_sheet(sheet, df_list_value)
if output == True:
    print("Added today's data successfully...!!!")