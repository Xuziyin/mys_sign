#!/bin/bash
set -e

echo "==== 安装 Python3 和 必要组件 ===="
apt update && apt install -y python3 python3-pip git curl

echo "==== 克隆签到代码 ===="
git clone https://github.com/Xuziyin/mys_sign.git /opt/mys_sign
cd /opt/mys_sign

echo "==== 安装 Python 依赖 ===="
pip3 install requests

echo "==== 设置定时任务 ===="
crontab -l | grep -v 'sign_in.py' > temp_cron
echo "0 9 * * * /usr/bin/python3 /opt/mys_sign/sign_in.py >> /opt/mys_sign/sign_log.txt 2>&1" >> temp_cron
crontab temp_cron
rm temp_cron

echo "==== 部署完成！===="
echo "请修改 /opt/mys_sign/sign_in.py 里的 MYS_COOKIE 和 MYS_UID"
echo "然后可以手动运行: python3 /opt/mys_sign/sign_in.py"
