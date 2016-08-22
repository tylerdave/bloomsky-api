GOOD_API_RESPONSE = '[{"DeviceID":"93E18E","LAT":41.482582100000002,"LON":-81.805958899999993,"ALT":213.5209045410156,"UTC":-4,"DST":1,"Searchable":true,"RegisterTime":1441487381,"CityName":"Lakewood","StreetName":"Lakeland Avenue","FullAddress":"Lakeland Ave, Lakewood, OH, US","DeviceName":"Lakeland Ave","BoundedPoint":"831EBB","NumOfFollowers":53,"Data":{"Temperature":71.420000000000002,"ImageURL":"http://storage.googleapis.com/bloomsky-img/eaB1rJytnpS5mZ23qJ1krZaunZSomJY=.jpg","Humidity":90,"Night":false,"ImageTS":1471783401,"Luminance":3460,"TS":1471783401,"Rain":false,"Pressure":29.175738800000001,"Voltage":2593,"UVIndex":"1"},"Point":{"Temperature":72.104000000000013,"Humidity":37},"VideoList":["http://storage.googleapis.com/bloomsky-video/eaB1rJytnpS5mZ23_-4_2016-08-16.mp4","http://storage.googleapis.com/bloomsky-video/eaB1rJytnpS5mZ23_-4_2016-08-17.mp4","http://storage.googleapis.com/bloomsky-video/eaB1rJytnpS5mZ23_-4_2016-08-18.mp4","http://storage.googleapis.com/bloomsky-video/eaB1rJytnpS5mZ23_-4_2016-08-19.mp4","http://storage.googleapis.com/bloomsky-video/eaB1rJytnpS5mZ23_-4_2016-08-20.mp4"],"NumOfFavorites":17}]'
GOOD_DATA_RESPONSE_JSON = """[{"street_name": "Lakeland Avenue", "utc_offset": -4, "outdoor": {"uv_index": 1, "luminance": 3460, "temperature": 71.42, "is_raining": false, "humidity": 90, "pressure": 29.1757388, "is_night": false, "image_url": "http://storage.googleapis.com/bloomsky-img/eaB1rJytnpS5mZ23qJ1krZaunZSomJY=.jpg", "image_timestamp": "2016-08-21T08:43:21-04:00", "data_timestamp": "2016-08-21T08:43:21-04:00", "voltage": 2593}, "favorites_count": 17, "altitude": 213.5209045410156,
"indoor": {"temperature": 72.10400000000001, "humidity": 37}, "followers_count": 53, "full_address": "Lakeland Ave, Lakewood, OH, US", "device_name": "Lakeland Ave", "latitude": 41.4825821, "is_dst": true, "video_urls": ["http://storage.googleapis.com/bloomsky-video/eaB1rJytnpS5mZ23_-4_2016-08-16.mp4", "http://storage.googleapis.com/bloomsky-video/eaB1rJytnpS5mZ23_-4_2016-08-17.mp4", "http://storage.googleapis.com/bloomsky-video/eaB1rJytnpS5mZ23_-4_2016-08-18.mp4",
"http://storage.googleapis.com/bloomsky-video/eaB1rJytnpS5mZ23_-4_2016-08-19.mp4", "http://storage.googleapis.com/bloomsky-video/eaB1rJytnpS5mZ23_-4_2016-08-20.mp4"], "longitude": -81.8059589, "is_searchable": true, "city_name": "Lakewood", "registered_timestamp": "2015-09-05T17:09:41-04:00", "device_id": "93E18E"}]"""
GOOD_CLI_OUTPUT_JSON = """
[
 {
  "street_name": "Lakeland Avenue",
  "utc_offset": -4,
  "outdoor": {
   "uv_index": 1,
   "luminance": 3460,
   "temperature": 71.42,
   "is_raining": false,
   "humidity": 90,
   "pressure": 29.1757388,
   "is_night": false,
   "image_url": "http://storage.googleapis.com/bloomsky-img/eaB1rJytnpS5mZ23qJ1krZaunZSomJY=.jpg",
   "image_timestamp": "2016-08-21T08:43:21-04:00",
   "data_timestamp": "2016-08-21T08:43:21-04:00",
   "voltage": 2593
  },
  "favorites_count": 17,
  "altitude": 213.5209045410156,
  "indoor": {
   "temperature": 72.10400000000001,
   "humidity": 37
  },
  "followers_count": 53,
  "full_address": "Lakeland Ave, Lakewood, OH, US",
  "device_name": "Lakeland Ave",
  "latitude": 41.4825821,
  "is_dst": true,
  "video_urls": [
   "http://storage.googleapis.com/bloomsky-video/eaB1rJytnpS5mZ23_-4_2016-08-16.mp4",
   "http://storage.googleapis.com/bloomsky-video/eaB1rJytnpS5mZ23_-4_2016-08-17.mp4",
   "http://storage.googleapis.com/bloomsky-video/eaB1rJytnpS5mZ23_-4_2016-08-18.mp4",
   "http://storage.googleapis.com/bloomsky-video/eaB1rJytnpS5mZ23_-4_2016-08-19.mp4",
   "http://storage.googleapis.com/bloomsky-video/eaB1rJytnpS5mZ23_-4_2016-08-20.mp4"
  ],
  "longitude": -81.8059589,
  "is_searchable": true,
  "city_name": "Lakewood",
  "registered_timestamp": "2015-09-05T17:09:41-04:00",
  "device_id": "93E18E"
 }
]
"""

