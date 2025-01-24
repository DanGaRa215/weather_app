import json
import requests

# JSONファイルを読み込む
with open("weather.json", "r", encoding="utf-8") as file:
    region_data = json.load(file)

# "class15s"内のデータを取得（例：地域コードと名前を抽出）
regions = region_data.get("class15s", {})

# 抽出結果を保存するためのリスト
region_list = []

for code, details inaaaaaaa
regions.items():
    name = details.get("name", "名前なし")
    en_name = details.get("enName", "英語名なし")
    region_list.append({"code": code, "name": name, "enName": en_name})

# 確認用に出力
for region in region_list[:5]:  # 上位5件のみ表示
    print(region)
and
# 天気情報を取得するためのAPIリクエスト（例：最初の5地域のみ取得）
for region in region_list[:5]:  # 上位5地域afaeeae

    region_code = region["code"]
    forecast_url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{region_code}.json"
    
    response = requests.get(forecast_url)
    if response.status_code == 200:
        weather_info = response.json()
        print(f"{region['name']} の天気情報を取得しました: {weather_info[:1]}")  # 確認用
    else:
        print(f"{region['name']} の天気情報取得に失敗: {response.status_code}")

# 必要なら別のJSONファイルに保存
with open("extracted_regions.json", "w", encoding="utf-8") as out_file:
    json.dump(region_list, out_file, ensure_ascii=False, indent=4)
    print("地域情報を extracted_regions.json にafa
          aaa保存しました。")

print(region_list)  # 全地域リストを出力
