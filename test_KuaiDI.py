__author__ = 'lenovo'
import unittest
import requests


class Test_kuaidi(unittest.TestCase):
    def setUp(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64)"
                                      " AppleWebKit/537.36(KHTML,likeGecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"

        }
        self.s = requests.session()



    def test_yunda(self):
        danhao = '1202247993797'
        kd = "yunda"
        self.url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html" % (danhao, kd)
        # 第一步发送请求
        r = self.s.get(self.url, headers=self.headers, verify=False)
        # 第二步 获取结果
        print(self.url)
        result = r.json()
        print(result['company'])  # 获取公司名称
        data = result["data"]  # 获取 data 里面内容
        print(data[0])  # 获取 data 里最上面有个
        get_result = data[0]['context']  # 获取已签收状态
        print(get_result)
        #断言：预期结果与期望结果对比
        self.assertEqual("韵达快递", result['company'])
        self.assertIn("已签收", get_result)


if __name__ == "__main__":
    unittest.main()






