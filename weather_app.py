import requests

# 地域ごとの天気情報を取得
region_code = "474020"  # 適切な地域コードに変更
forecast_url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{region_code}.json"
response_weather = requests.get(forecast_url)

if response_weather.status_code == 200:
    weather_data = response_weather.json()
    print("天気情報の取得成功:")
    print(weather_data)  # データの確認
else:
    print(f"天気情報の取得失敗: {response_weather.status_code}")