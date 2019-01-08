''' Mushroom Tracker - Make sure your shrooms make it!

# from flask import Flask
'''
import time
'''
future imports
from peewee import (
    Model,
    # SqliteDatabase,
    ForeignKeyField, DateTimeField, TextField, DecimalField, IntegerField
    )
'''
import csv
# import xlsxwriter

from datetime import datetime as dt
import json
import os
import requests


darksky_key = os.environ.get('DARKSKY_KEY')
locations = [
    {
        'airport_code': "PDX",
        'latitude': '45.5122',
        'longitude': '-122.6587',
    }, {
        'airport_code': "ORD",
        'latitude': '41.9741625',
        'longitude': '-87.9095154',
    }, {
        'airport_code': "MEM",
        'latitude': '35.0420679',
        'longitude': '-89.9813669',
    }, {
        'airport_code': "SDF",
        'latitude': '38.175662',
        'longitude': '-85.7391171',
    }, {
        'airport_code': "MSP",
        'latitude': '44.8847858',
        'longitude': '-93.2219842',
    }, {
        'airport_code': "JFK",
        'latitude': '40.6413111',
        'longitude': '-73.7781391',
    }, {
        'airport_code': "EWR",
        'latitude': '40.6895314',
        'longitude': '-74.1766564',
    }, {
        'airport_code': "SAN",
        'latitude': '32.7338006',
        'longitude': '-117.1954978',
    }, {
        'airport_code': "LAX",
        'latitude': '33.9415889',
        'longitude': '-118.4107187',
    },
]


def get_darksky(key, lat, lon):
    '''This function is the Main API call to load weather data for a location.

Arguments: (key, lat, lon)

key: API key for darksky (string),

lat: lattitude (float),

long: longitude (float)'''
    return json.loads(
        requests.get(
            '{}/{}/{},{}'.format(
                    'https://api.darksky.net/forecast',
                    key,
                    lat,
                    lon,
                )
            ).text
        )


def run_report():
    for i, location in enumerate(locations):
        # Store that data in an appropriate data type so that it can be used in
        # the next task.
        # forecast for PDX
        darksky_dict = get_darksky(
            darksky_key,
            location['latitude'],
            location['longitude'],
                )
        date_list = ['']
        hi_temps = []
        low_temps = []
        humidity = []
        separator = []
        forecast = {'date': '', 'hi': '', 'low': ''}
        ''' Still working on making a XLSX version to do cool things like colors
    # data = {"1":["xyz",""],"2":["abc","def"],"3":["zzz",""]}


    # read the data from the supplied CSV file.
    workbook = xlsxwriter.Workbook('mshrm_cast_{}.xlsx'.format(dt.now().date())
    book_format = workbook.add_format(
        properties={'bold': True, 'font_color': 'red'})

    worksheet = workbook.add_worksheet('dict_data')
    '''
        with open(
            'CSV/mshrm_cast_{}.csv'.format(dt.now().date()),
            'a',
            newline='',
                ) as spreadsheet:

            # initialize spreadsheet
            sheet_writer = csv.writer(
                spreadsheet,
                delimiter=',',
                quotechar='|',
                quoting=csv.QUOTE_MINIMAL
                )
            hi_temps = ['{} Hi'.format(location['airport_code'])]
            low_temps = ['{} low'.format(location['airport_code'])]
            humidity = ['{} humidity'.format(location['airport_code'])]
            precip = ['{} in precip'.format(location['airport_code'])]

            for day in (darksky_dict['daily']['data']):
                date_string = dt.fromtimestamp(
                    day['time']).strftime('%a %m-%d')
                forecast['date'] = date_string
                date_list.append(forecast['date'])

                if day['temperatureMax'] > 55:
                    forecast['hi'] = '!!!!-' + str(
                        day['temperatureMax']) + '-!!!!'
                else:
                    forecast['hi'] = day['temperatureMax']
                hi_temps.append(forecast['hi'])

                if day['temperatureMin'] < 32:
                    forecast['low'] = '!!!!-' + str(
                        day['temperatureMin']) + '-!!!!'
                else:
                    forecast['low'] = day['temperatureMin']
                low_temps.append(forecast['low'])

                humidity.append(str(int(day['humidity']*100)) + '%')
                try:
                    precip.append(
                        "{}% chance of {}".format(
                            int(day['precipProbability']*100),
                            day['precipType'],
                        )
                    )
                except KeyError:
                    precip.append(
                        "No Precipitation"
                    )

                separator.append('---')

            # forecast_list.append(forecast)
            if i == 0:
                sheet_writer.writerow(date_list)
            sheet_writer.writerow(separator)
            sheet_writer.writerow(hi_temps)
            sheet_writer.writerow(low_temps)
            sheet_writer.writerow(humidity)
            sheet_writer.writerow(precip)
    print('Report complete')


''' It's gotta be a flask app at some point, right?
app = Flask(__name__, static_url_path='/static')1
DEBUG = True

if __name__ == "__main__":  # pragma: no cover
    DATABASE = SqliteDatabase('mshrm.db')
else:
    DATABASE = SqliteDatabase('TESTING_mshrm.db')


class City(Model):
    airport_code = TextField()
    latitude = DecimalField()
    longitude = DecimalField()

    class Meta:
        # database = DATABASE
        order_by = ('-id', )


class Forecast(Model):
    city = ForeignKeyField(City)
    date = DateTimeField()
    hi = IntegerField()
    low = IntegerField()
    humidity = IntegerField()

    class Meta:
        # database = DATABASE
        order_by = ('-id', )

'''

'''
def initialize():
    DATABASE.connect()
    DATABASE.create_tables(
        [
            City,
            Forecast
        ],
        safe=True)
    DATABASE.close()

'''
if __name__ == '__main__':
    try:
        while True:
            try:
                with open(
                        'CSV/mshrm_cast_{}.csv'.format(dt.now().date()), 'r'):
                    print('Report already exists.')
            except:
                run_report()
            print("Pausing for 4 hours")
            time.sleep(60*50*4)
    except KeyboardInterrupt:
        print("Thanks for using Mushroom Tracker!")
'''
    initialize()
    if DEBUG:
        app.run(debug=DEBUG, host=8000)
        initialize()
    else:
        pass
        http_server=WSGIServer(('', PORT), app)
        http_server.serve_forever()
'''
