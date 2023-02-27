#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..')
from base.spider import Spider
import json

class Spider(Spider):  # 元类 默认的元类 type
    def getName(self):
        return "快看影视"
    def init(self,extend=""):
        print("============{0}============".format(extend))
        pass
    def homeContent(self,filter):
        result = {}
        cateManual = {
            "电影":"1",
            "电视剧":"2",
            "综艺":"3",
            "动漫":"4",
            "纪录片": "5"
        }
        classes = []
        for k in cateManual:
            classes.append({
                'type_name':k,
                'type_id':cateManual[k]
            })

        result['class'] = classes
        if(filter):
            result['filters'] = self.config['filter']
        return result
    def homeVideoContent(self):
        rsp = self.fetch("http://api.8a5.cn/parse/kuaikan/py.php?do=homeVideoContent")
        alists = json.loads(rsp.text)
        alist = alists['list']
        result = {
            'list':alist
        }
        return result
    def categoryContent(self,tid,pg,filter,extend):
        result = {}
        urlParams = []
        params = ''
        for key in extend:
            urlParams.append(str(key) + '=' + extend[key])
        params = '&'.join(urlParams)
        url = 'http://api.8a5.cn/parse/kuaikan/py.php?do=categoryContent&tid={0}&page={1}&{2}'.format(tid, pg,params)
        rsp = self.fetch(url)
        alists = json.loads(rsp.text)
        alist = alists['list']

        result['list'] = alist
        result['page'] = pg
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def detailContent(self,array):
        tid = array[0]
        url = 'http://api.8a5.cn/parse/kuaikan/py.php?do=detailContent&id={0}'.format(tid)
        rsp = self.fetch(url)
        alists = json.loads(rsp.text)
        vod = alists['vod']
        result = {
            'list':[
                vod
            ]
        }
        return result

    def searchContent(self,key,quick):
        url = 'http://api.8a5.cn/parse/kuaikan/py.php?do=searchContent&wd={0}'.format(key)
        rsp = self.fetch(url)
        alists = json.loads(rsp.text)
        list = alists['list']
        result = {
            'list':list
        }
        return result


    def playerContent(self,flag,id,vipFlags):
        result = {}
        if 'api.8a5.cn' in id:
            rsp = self.fetch(id)
            alists = json.loads(rsp.text)
            id = alists['url']
        result["parse"] = 0
        result["playUrl"] = ''
        result["url"] = id
        return result
        
    config = {
		"player": {},
		"filter":{"2":[{"key":"area","name":"地区","value":[{"n":"全部","v":0},{"n":"内地","v":1},{"n":"中国香港","v":2},{"n":"中国台湾","v":3},{"n":"韩国","v":4},{"n":"日本","v":5},{"n":"泰国","v":6},{"n":"美国","v":7},{"n":"英国","v":8},{"n":"新加坡","v":9},{"n":"法国","v":10},{"n":"德国","v":11},{"n":"印度","v":12},{"n":"欧美","v":13},{"n":"其他","v":14}]},{"key":"year","name":"年份","value":[{"n":"全部","v":0},{"n":"2022","v":20},{"n":"2021","v":19},{"n":"2020","v":18},{"n":"2019","v":17},{"n":"2018","v":16},{"n":"2017","v":15},{"n":"2016","v":14},{"n":"2015","v":13},{"n":"2014","v":12},{"n":"2013","v":11},{"n":"2012","v":10},{"n":"2011","v":9},{"n":"2010","v":8},{"n":"2009","v":7},{"n":"2008","v":6},{"n":"2007","v":5},{"n":"2006","v":4},{"n":"2005","v":3},{"n":"2004","v":2},{"n":"更早","v":1}]},{"key":"class","name":"剧情","value":[{"n":"全部","v":0},{"n":"剧情","v":2},{"n":"爱情","v":21},{"n":"犯罪","v":23},{"n":"搞笑","v":34},{"n":"武侠","v":19},{"n":"都市","v":6},{"n":"家庭","v":16},{"n":"职场","v":42},{"n":"国产","v":112},{"n":"国产剧","v":113},{"n":"年代","v":110},{"n":"文化","v":84},{"n":"网络剧","v":114},{"n":"芒果出品","v":115},{"n":"言情","v":1},{"n":"古装","v":8},{"n":"青春","v":15},{"n":"偶像","v":7},{"n":"伦理","v":3},{"n":"喜剧","v":4},{"n":"悬疑","v":5},{"n":"神话","v":13},{"n":"警匪","v":10},{"n":"历史","v":11},{"n":"励志","v":12},{"n":"情感","v":38},{"n":"战争","v":25},{"n":"电影版","v":74},{"n":"其他","v":79},{"n":"谍战","v":14},{"n":"校园","v":61},{"n":"农村","v":88},{"n":"动作","v":17},{"n":"传记","v":29},{"n":"科幻","v":20},{"n":"惊悚","v":31},{"n":"冒险","v":56},{"n":"同性","v":111},{"n":"恋爱","v":58},{"n":"奇幻","v":24},{"n":"生活","v":39},{"n":"歌舞","v":30},{"n":"恐怖","v":22},{"n":"原创","v":86},{"n":"魔幻","v":85},{"n":"战斗","v":80},{"n":"军旅","v":104},{"n":"文艺","v":27},{"n":"音乐","v":41},{"n":"新番动画","v":77},{"n":"刑侦","v":87},{"n":"情景","v":18},{"n":"玄幻","v":60},{"n":"军事","v":9},{"n":"经典","v":55},{"n":"推理","v":57},{"n":"革命","v":109},{"n":"纪录","v":28},{"n":"运动","v":66},{"n":"热血","v":53},{"n":"竞技","v":70},{"n":"童话","v":69},{"n":"友情","v":72},{"n":"少儿","v":46},{"n":"真人秀","v":33},{"n":"动画","v":26},{"n":"灾难","v":103},{"n":"纪实","v":48},{"n":"机战","v":63},{"n":"治愈","v":59},{"n":"时尚","v":44},{"n":"脱口秀","v":32},{"n":"美食","v":43},{"n":"戏曲","v":108},{"n":"人文","v":83},{"n":"完结动画","v":78},{"n":"社会","v":71},{"n":"益智","v":68},{"n":"亲子","v":64},{"n":"访谈","v":37},{"n":"游戏","v":45},{"n":"晚会","v":40},{"n":"美少女","v":54},{"n":"动物","v":62},{"n":"真人版","v":73},{"n":"科学","v":92},{"n":"内地","v":117}]}],"1":[{"key":"area","name":"地区","value":[{"n":"全部","v":0},{"n":"中国","v":1},{"n":"中国香港","v":2},{"n":"中国台湾","v":3},{"n":"韩国","v":4},{"n":"日本","v":5},{"n":"泰国","v":6},{"n":"美国","v":7},{"n":"英国","v":8},{"n":"新加坡","v":9},{"n":"法国","v":10},{"n":"德国","v":11},{"n":"印度","v":12},{"n":"欧美","v":13},{"n":"其他","v":14}]},{"key":"year","name":"年份","value":[{"n":"全部","v":0},{"n":"2022","v":20},{"n":"2021","v":19},{"n":"2020","v":18},{"n":"2019","v":17},{"n":"2018","v":16},{"n":"2017","v":15},{"n":"2016","v":14},{"n":"2015","v":13},{"n":"2014","v":12},{"n":"2013","v":11},{"n":"2012","v":10},{"n":"2011","v":9},{"n":"2010","v":8},{"n":"2009","v":7},{"n":"2008","v":6},{"n":"2007","v":5},{"n":"2006","v":4},{"n":"2005","v":3},{"n":"2004","v":2},{"n":"更早","v":1}]},{"key":"class","name":"剧情","value":[{"n":"全部","v":0},{"n":"言情","v":1},{"n":"动作","v":17},{"n":"惊悚","v":31},{"n":"剧情","v":2},{"n":"科幻","v":20},{"n":"喜剧","v":4},{"n":"冒险","v":56},{"n":"动画","v":26},{"n":"悬疑","v":5},{"n":"恐怖","v":22},{"n":"文艺","v":27},{"n":"纪实","v":48},{"n":"爱情","v":21},{"n":"历史","v":11},{"n":"犯罪","v":23},{"n":"战争","v":25},{"n":"青春","v":15},{"n":"家庭","v":16},{"n":"传记","v":29},{"n":"奇幻","v":24},{"n":"电影版","v":74},{"n":"古装","v":8},{"n":"纪录","v":28},{"n":"恋爱","v":58},{"n":"伦理","v":3},{"n":"歌舞","v":30},{"n":"音乐","v":41},{"n":"推理","v":57},{"n":"武侠","v":19},{"n":"警匪","v":10},{"n":"科普","v":102},{"n":"灾难","v":103},{"n":"军旅","v":104},{"n":"戏曲","v":108},{"n":"革命","v":109},{"n":"文化","v":84},{"n":"运动","v":66},{"n":"社会","v":71},{"n":"年代","v":110},{"n":"同性","v":111},{"n":"励志","v":12},{"n":"热血","v":53},{"n":"教育","v":90},{"n":"神话","v":13},{"n":"谍战","v":14},{"n":"搞笑","v":34},{"n":"情感","v":38},{"n":"治愈","v":59},{"n":"校园","v":61},{"n":"枪战","v":98},{"n":"玄幻","v":60},{"n":"魔幻","v":85},{"n":"友情","v":72},{"n":"少儿","v":46},{"n":"体育","v":47},{"n":"经典","v":55},{"n":"军事","v":9},{"n":"脱口秀","v":32},{"n":"刑侦","v":87},{"n":"农村","v":88},{"n":"美食","v":43},{"n":"竞技","v":70},{"n":"都市","v":6},{"n":"其他","v":79},{"n":"真人版","v":73},{"n":"战斗","v":80},{"n":"完结动画","v":78},{"n":"美少女","v":54},{"n":"亲子","v":64},{"n":"生活","v":39},{"n":"时尚","v":44},{"n":"美术","v":49},{"n":"动物","v":62},{"n":"自然","v":89},{"n":"旅游","v":82},{"n":"人文","v":83},{"n":"真人秀","v":33},{"n":"访谈","v":37},{"n":"晚会","v":40},{"n":"职场","v":42},{"n":"财经","v":50},{"n":"偶像","v":7},{"n":"科学","v":92},{"n":"解说","v":93},{"n":"新闻","v":96},{"n":"内地","v":117},{"n":"明星","v":116},{"n":"国产","v":112},{"n":"益智","v":68},{"n":"儿歌","v":65},{"n":"相声","v":81}]}],"3":[{"key":"area","name":"地区","value":[{"n":"全部","v":0},{"n":"内地","v":1},{"n":"中国香港","v":2},{"n":"中国台湾","v":3},{"n":"韩国","v":4},{"n":"日本","v":5},{"n":"泰国","v":6},{"n":"美国","v":7},{"n":"英国","v":8},{"n":"新加坡","v":9},{"n":"法国","v":10},{"n":"德国","v":11},{"n":"印度","v":12},{"n":"欧美","v":13},{"n":"其他","v":14}]},{"key":"year","name":"年份","value":[{"n":"全部","v":0},{"n":"2022","v":20},{"n":"2021","v":19},{"n":"2020","v":18},{"n":"2019","v":17},{"n":"2018","v":16},{"n":"2017","v":15},{"n":"2016","v":14},{"n":"2015","v":13},{"n":"2014","v":12},{"n":"2013","v":11},{"n":"2012","v":10},{"n":"2011","v":9},{"n":"2010","v":8},{"n":"2009","v":7},{"n":"2008","v":6},{"n":"2007","v":5},{"n":"2006","v":4},{"n":"2005","v":3},{"n":"2004","v":2},{"n":"更早","v":1}]},{"key":"class","name":"剧情","value":[{"n":"全部","v":0},{"n":"游戏","v":45},{"n":"推理","v":57},{"n":"真人秀","v":33},{"n":"生活","v":39},{"n":"言情","v":1},{"n":"青春","v":15},{"n":"爱情","v":21},{"n":"情感","v":38},{"n":"恋爱","v":58},{"n":"都市","v":6},{"n":"家庭","v":16},{"n":"电影版","v":74},{"n":"育儿","v":100},{"n":"脱口秀","v":32},{"n":"少儿","v":46},{"n":"动画","v":26},{"n":"教育","v":90},{"n":"亲子","v":64},{"n":"竞赛","v":101},{"n":"搞笑","v":34},{"n":"原创","v":86},{"n":"文化","v":84},{"n":"科普","v":102},{"n":"体育","v":47},{"n":"灾难","v":103},{"n":"同性","v":111},{"n":"时实","v":103},{"n":"军事","v":9},{"n":"军旅","v":104},{"n":"战争","v":25},{"n":"启蒙","v":105},{"n":"舞蹈","v":106},{"n":"竞技","v":70},{"n":"采访","v":107},{"n":"访谈","v":37},{"n":"戏曲","v":108},{"n":"革命","v":109},{"n":"历史","v":11},{"n":"纪录","v":28},{"n":"文艺","v":27},{"n":"传记","v":29},{"n":"人文","v":83},{"n":"文献","v":91},{"n":"音乐","v":41},{"n":"励志","v":12},{"n":"选秀","v":35},{"n":"动作","v":17},{"n":"冒险","v":56},{"n":"偶像","v":7},{"n":"剧情","v":2},{"n":"农村","v":88},{"n":"神话","v":13},{"n":"奇幻","v":24},{"n":"经典","v":55},{"n":"谍战","v":14},{"n":"歌舞","v":30},{"n":"美术","v":49},{"n":"校园","v":61},{"n":"社会","v":71},{"n":"旅游","v":82},{"n":"喜剧","v":4},{"n":"伦理","v":3},{"n":"悬疑","v":5},{"n":"科幻","v":20},{"n":"犯罪","v":23},{"n":"惊悚","v":31},{"n":"古装","v":8},{"n":"恐怖","v":22},{"n":"警匪","v":10},{"n":"纪实","v":48},{"n":"美食","v":43},{"n":"动物","v":62},{"n":"友情","v":72},{"n":"儿歌","v":65},{"n":"热血","v":53},{"n":"治愈","v":59},{"n":"运动","v":66},{"n":"魔幻","v":85},{"n":"晚会","v":40},{"n":"真人版","v":73},{"n":"益智","v":68},{"n":"分享","v":98},{"n":"其他","v":79},{"n":"自然","v":89},{"n":"相声","v":81},{"n":"八卦","v":36},{"n":"播报","v":52},{"n":"时尚","v":44},{"n":"汽车","v":51},{"n":"职场","v":42},{"n":"新闻","v":96},{"n":"财经","v":50},{"n":"科学","v":92},{"n":"教学","v":99},{"n":"解说","v":93},{"n":"枪战","v":98},{"n":"宣传","v":97},{"n":"战斗","v":80},{"n":"刑侦","v":87},{"n":"童话","v":69},{"n":"怪物","v":67},{"n":"武侠","v":19},{"n":"演讲","v":95},{"n":"明星","v":116},{"n":"游戏竞技","v":124}]}],"4":[{"key":"area","name":"\u5730\u533a","value":[{"n":"\u5168\u90e8","v":0},{"n":"\u5185\u5730","v":1},{"n":"\u4e2d\u56fd\u9999\u6e2f","v":2},{"n":"\u4e2d\u56fd\u53f0\u6e7e","v":3},{"n":"\u97e9\u56fd","v":4},{"n":"\u65e5\u672c","v":5},{"n":"\u6cf0\u56fd","v":6},{"n":"\u7f8e\u56fd","v":7},{"n":"\u82f1\u56fd","v":8},{"n":"\u65b0\u52a0\u5761","v":9},{"n":"\u6cd5\u56fd","v":10},{"n":"\u5fb7\u56fd","v":11},{"n":"\u5370\u5ea6","v":12},{"n":"\u6b27\u7f8e","v":13},{"n":"\u5176\u4ed6","v":14}]},{"key":"year","name":"\u5e74\u4efd","value":[{"n":"\u5168\u90e8","v":0},{"n":"2022","v":20},{"n":"2021","v":19},{"n":"2020","v":18},{"n":"2019","v":17},{"n":"2018","v":16},{"n":"2017","v":15},{"n":"2016","v":14},{"n":"2015","v":13},{"n":"2014","v":12},{"n":"2013","v":11},{"n":"2012","v":10},{"n":"2011","v":9},{"n":"2010","v":8},{"n":"2009","v":7},{"n":"2008","v":6},{"n":"2007","v":5},{"n":"2006","v":4},{"n":"2005","v":3},{"n":"2004","v":2},{"n":"\u66f4\u65e9","v":1}]},{"key":"class","name":"\u5267\u60c5","value":[{"n":"\u5168\u90e8","v":0},{"n":"\u559c\u5267","v":4},{"n":"\u53e4\u88c5","v":8},{"n":"\u6b66\u4fa0","v":19},{"n":"\u52a8\u753b","v":26},{"n":"\u8a00\u60c5","v":1},{"n":"\u5386\u53f2","v":11},{"n":"\u641e\u7b11","v":34},{"n":"\u5192\u9669","v":56},{"n":"\u9b54\u5e7b","v":85},{"n":"\u52b1\u5fd7","v":12},{"n":"\u9752\u6625","v":15},{"n":"\u7231\u60c5","v":21},{"n":"\u6821\u56ed","v":61},{"n":"\u5bb6\u5ead","v":16},{"n":"\u5947\u5e7b","v":24},{"n":"\u7ecf\u5178","v":55},{"n":"\u4eb2\u5b50","v":64},{"n":"\u5267\u60c5","v":2},{"n":"\u604b\u7231","v":58},{"n":"\u7f8e\u5c11\u5973","v":54},{"n":"\u8fd0\u52a8","v":66},{"n":"\u52a8\u4f5c","v":17},{"n":"\u4f26\u7406","v":3},{"n":"\u70ed\u8840","v":53},{"n":"\u60ac\u7591","v":5},{"n":"\u6050\u6016","v":22},{"n":"\u60ca\u609a","v":31},{"n":"\u5076\u50cf","v":7},{"n":"\u7384\u5e7b","v":60},{"n":"\u5e7b\u60f3","v":60},{"n":"\u7535\u5f71\u7248","v":74},{"n":"\u79d1\u5e7b","v":20},{"n":"\u804c\u573a","v":42},{"n":"\u5176\u4ed6","v":79},{"n":"\u6cbb\u6108","v":59},{"n":"\u90fd\u5e02","v":6},{"n":"\u65b0\u756a\u52a8\u753b","v":77},{"n":"\u751f\u6d3b","v":39},{"n":"\u6218\u6597","v":80},{"n":"\u80b2\u513f","v":100},{"n":"\u76ca\u667a","v":68},{"n":"\u6587\u5316","v":84},{"n":"\u771f\u4eba\u7248","v":73},{"n":"\u79d1\u666e","v":102},{"n":"\u52a8\u7269","v":62},{"n":"\u821e\u8e48","v":106},{"n":"\u795e\u8bdd","v":13},{"n":"\u6218\u4e89","v":25},{"n":"\u771f\u4eba\u79c0","v":33},{"n":"\u5c11\u513f","v":46},{"n":"\u7ae5\u8bdd","v":69},{"n":"\u5b8c\u7ed3\u52a8\u753b","v":78},{"n":"\u6559\u80b2","v":90},{"n":"\u7ade\u6280","v":70},{"n":"\u4f53\u80b2","v":47},{"n":"\u673a\u6218","v":63},{"n":"\u539f\u521b","v":86},{"n":"\u63a8\u7406","v":57},{"n":"\u6587\u827a","v":27},{"n":"\u60c5\u611f","v":38},{"n":"\u7f8e\u98df","v":43},{"n":"\u97f3\u4e50","v":41},{"n":"\u513f\u6b4c","v":65},{"n":"\u602a\u7269","v":67},{"n":"\u793e\u4f1a","v":71},{"n":"\u53cb\u60c5","v":72},{"n":"\u72af\u7f6a","v":23},{"n":"\u6b4c\u821e","v":30},{"n":"\u707e\u96be","v":103},{"n":"\u519b\u65c5","v":104},{"n":"\u5e74\u4ee3","v":110},{"n":"\u6e38\u620f","v":45},{"n":"\u540c\u6027","v":111},{"n":"\u5211\u4fa6","v":87},{"n":"TV\u7248","v":76},{"n":"\u8c0d\u6218","v":14},{"n":"OVA\u7248","v":75},{"n":"\u7eaa\u5f55","v":28},{"n":"\u4f20\u8bb0","v":29},{"n":"\u7f8e\u672f","v":49},{"n":"\u64ad\u62a5","v":52},{"n":"\u516b\u5366","v":36},{"n":"\u542f\u8499","v":105},{"n":"\u67aa\u6218","v":98},{"n":"\u81ea\u7136","v":89},{"n":"\u8131\u53e3\u79c0","v":32},{"n":"\u9009\u79c0","v":35},{"n":"\u65c5\u6e38","v":82},{"n":"\u7eaa\u5b9e","v":48},{"n":"\u60c5\u666f","v":18},{"n":"\u665a\u4f1a","v":40},{"n":"\u8bbf\u8c08","v":37},{"n":"\u65f6\u5c1a","v":44},{"n":"\u79d1\u5b66","v":92},{"n":"\u519b\u4e8b","v":9},{"n":"\u6587\u732e","v":91},{"n":"\u519c\u6751","v":88},{"n":"\u89e3\u8bf4","v":93},{"n":"\u65b0\u95fb","v":96},{"n":"\u8d22\u7ecf","v":50},{"n":"\u6c7d\u8f66","v":51},{"n":"\u56fd\u4ea7","v":112}]}],"5":[{"key":"area","name":"\u5730\u533a","value":[{"n":"\u5168\u90e8","v":0},{"n":"\u5185\u5730","v":1},{"n":"\u4e2d\u56fd\u9999\u6e2f","v":2},{"n":"\u4e2d\u56fd\u53f0\u6e7e","v":3},{"n":"\u97e9\u56fd","v":4},{"n":"\u65e5\u672c","v":5},{"n":"\u7f8e\u56fd","v":7},{"n":"\u82f1\u56fd","v":8},{"n":"\u6cd5\u56fd","v":10},{"n":"\u5fb7\u56fd","v":11},{"n":"\u5370\u5ea6","v":12},{"n":"\u6b27\u7f8e","v":13},{"n":"\u5176\u4ed6","v":14}]},{"key":"year","name":"\u5e74\u4efd","value":[{"n":"\u5168\u90e8","v":0},{"n":"2022","v":20},{"n":"2021","v":19},{"n":"2020","v":18},{"n":"2019","v":17},{"n":"2018","v":16},{"n":"2017","v":15},{"n":"2016","v":14},{"n":"2015","v":13},{"n":"2014","v":12},{"n":"2013","v":11},{"n":"2012","v":10},{"n":"2011","v":9},{"n":"2010","v":8},{"n":"2009","v":7},{"n":"2008","v":6},{"n":"2007","v":5},{"n":"2006","v":4},{"n":"2005","v":3},{"n":"2004","v":2},{"n":"\u66f4\u65e9","v":1}]},{"key":"class","name":"\u5267\u60c5","value":[{"n":"\u5168\u90e8","v":0},{"n":"\u5386\u53f2","v":11},{"n":"\u52b1\u5fd7","v":12},{"n":"\u72af\u7f6a","v":23},{"n":"\u793e\u4f1a","v":71},{"n":"\u6218\u4e89","v":25},{"n":"\u7eaa\u5f55","v":28},{"n":"\u7eaa\u5b9e","v":48},{"n":"\u81ea\u7136","v":89},{"n":"\u6587\u5316","v":84},{"n":"\u4f20\u8bb0","v":29},{"n":"\u97f3\u4e50","v":41},{"n":"\u89e3\u8bf4","v":93},{"n":"\u79d1\u666e","v":102},{"n":"\u795e\u8bdd","v":13},{"n":"\u9752\u6625","v":15},{"n":"\u5bb6\u5ead","v":16},{"n":"\u5267\u60c5","v":2},{"n":"\u7f8e\u98df","v":43},{"n":"\u5c11\u513f","v":46},{"n":"\u8fd0\u52a8","v":66},{"n":"\u5176\u4ed6","v":79},{"n":"\u79d1\u5e7b","v":20},{"n":"\u60ca\u609a","v":31},{"n":"\u52a8\u753b","v":26},{"n":"\u5192\u9669","v":56},{"n":"\u6587\u827a","v":27},{"n":"\u8131\u53e3\u79c0","v":32},{"n":"\u65b0\u95fb","v":96},{"n":"\u771f\u4eba\u79c0","v":33},{"n":"\u751f\u6d3b","v":39},{"n":"\u4f53\u80b2","v":47},{"n":"\u8d22\u7ecf","v":50},{"n":"\u52a8\u7269","v":62},{"n":"\u60c5\u611f","v":38},{"n":"\u7535\u5f71\u7248","v":74},{"n":"\u65c5\u6e38","v":82},{"n":"\u4eba\u6587","v":83},{"n":"\u519b\u4e8b","v":9},{"n":"\u6559\u80b2","v":90},{"n":"\u559c\u5267","v":4},{"n":"\u60ac\u7591","v":5},{"n":"\u6821\u56ed","v":61},{"n":"\u91c7\u8bbf","v":107},{"n":"\u79d1\u5b66","v":92}]}]}
	}
    def isVideoFormat(self,url):
        pass
    def manualVideoCheck(self):
        pass
    def localProxy(self,param):
        return [200, "video/MP2T", action, ""]
