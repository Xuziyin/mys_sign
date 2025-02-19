import requests
import json
import time

# 你的米游社 Cookie (修改此处)
MYS_COOKIE = "你的 cookie"

# 你的米游社 UID (修改此处)
MYS_UID = "你的 UID"

# 签到 API
MYS_SIGN_URL = "https://api-takumi.mihoyo.com/event/bbs_sign_reward/sign"

# 头部信息
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "https://webstatic.mihoyo.com/",
    "Origin": "https://webstatic.mihoyo.com",
    "Cookie": MYS_COOKIE
}

# 签到请求参数
DATA = {
    "act_id": "e202009291139501",  # 这个 ID 可能会变，需要更新
    "uid": MYS_UID,
    "region": "cn_gf01"  # 国服，其他服需调整
}

def sign_in():
    try:
        response = requests.post(MYS_SIGN_URL, headers=HEADERS, data=json.dumps(DATA))
        result = response.json()
        if result["retcode"] == 0:
            print(f"签到成功！奖励: {result['data']['award']['name']}")
        else:
            print(f"签到失败: {result['message']}")
    except Exception as e:
        print(f"请求错误: {e}")

if __name__ == "__main__":
    sign_in()
