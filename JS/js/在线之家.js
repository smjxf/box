// 在线之家地址发布页 https://www.zxzj.site/
muban.首图2.二级.desc = '.data:eq(3)&&Text;;;.data:eq(1)&&Text;.data:eq(2)&&Text';
var rule = {
    title: '在线之家',
    模板: '首图2',
    // host:'https://zxzj.vip',
    host: 'https://www.zxzj.org',
    url: '/vodshow/fyclassfyfilter.html',
    filterable: 1,//是否启用分类筛选,
    filter_url: '-{{fl.area}}-{{fl.by}}-{{fl.class}}-----fypage---{{fl.year}}',
    filter: {
        "1": [{ "key": "class", "name": "剧情", "value": [{ "n": "全部", "v": "" }, { "n": "喜剧", "v": "喜剧" }, { "n": "爱情", "v": "爱情" }, { "n": "恐怖", "v": "恐怖" }, { "n": "动作", "v": "动作" }, { "n": "科幻", "v": "科幻" }, { "n": "剧情", "v": "剧情" }, { "n": "战争", "v": "战争" }, { "n": "警匪", "v": "警匪" }, { "n": "犯罪", "v": "犯罪" }, { "n": "动画", "v": "动画" }, { "n": "奇幻", "v": "奇幻" }, { "n": "冒险", "v": "冒险" }] }, { "key": "area", "name": "地区", "value": [{ "n": "全部", "v": "" }, { "n": "大陆", "v": "大陆" }, { "n": "香港", "v": "香港" }, { "n": "台湾", "v": "台湾" }, { "n": "欧美", "v": "欧美" }, { "n": "韩国", "v": "韩国" }, { "n": "日本", "v": "日本" }, { "n": "泰国", "v": "泰国" }, { "n": "印度", "v": "印度" }, { "n": "俄罗斯", "v": "俄罗斯" }, { "n": "其他", "v": "其他" }] }, { "key": "year", "name": "年份", "value": [{ "n": "全部", "v": "" }, { "n": "2023", "v": "2023" }, { "n": "2022", "v": "2022" }, { "n": "2021", "v": "2021" }, { "n": "2020", "v": "2020" }, { "n": "2019", "v": "2019" }, { "n": "2018", "v": "2018" }, { "n": "2017", "v": "2017" }, { "n": "2016", "v": "2016" }, { "n": "2015", "v": "2015" }, { "n": "2014", "v": "2014" }, { "n": "2013", "v": "2013" }, { "n": "2012", "v": "2012" }, { "n": "2011", "v": "2011" }] }, { "key": "by", "name": "排序", "value": [{ "n": "时间", "v": "time" }, { "n": "人气", "v": "hits" }, { "n": "评分", "v": "score" }] }],
        "2": [{ "key": "class", "name": "剧情", "value": [{ "n": "全部", "v": "" }, { "n": "剧情", "v": "剧情" }, { "n": "喜剧", "v": "喜剧" }, { "n": "爱情", "v": "爱情" }, { "n": "动作", "v": "动作" }, { "n": "悬疑", "v": "悬疑" }, { "n": "恐怖", "v": "恐怖" }, { "n": "奇幻", "v": "奇幻" }, { "n": "惊悚", "v": "惊悚" }, { "n": "犯罪", "v": "犯罪" }, { "n": "科幻", "v": "科幻" }, { "n": "音乐", "v": "音乐" }, { "n": "其他", "v": "其他" }] }, { "key": "year", "name": "年份", "value": [{ "n": "全部", "v": "" }, { "n": "2023", "v": "2023" }, { "n": "2022", "v": "2022" }, { "n": "2021", "v": "2021" }, { "n": "2020", "v": "2020" }, { "n": "2019", "v": "2019" }, { "n": "2018", "v": "2018" }, { "n": "2017", "v": "2017" }, { "n": "2016", "v": "2016" }, { "n": "2015", "v": "2015" }, { "n": "2014", "v": "2014" }, { "n": "2013", "v": "2013" }, { "n": "2012", "v": "2012" }, { "n": "2011", "v": "2011" }] }, { "key": "by", "name": "排序", "value": [{ "n": "时间", "v": "time" }, { "n": "人气", "v": "hits" }, { "n": "评分", "v": "score" }] }],
        "3": [{ "key": "class", "name": "剧情", "value": [{ "n": "全部", "v": "" }, { "n": "剧情", "v": "剧情" }, { "n": "喜剧", "v": "喜剧" }, { "n": "爱情", "v": "爱情" }, { "n": "动作", "v": "动作" }, { "n": "悬疑", "v": "悬疑" }, { "n": "恐怖", "v": "恐怖" }, { "n": "奇幻", "v": "奇幻" }, { "n": "惊悚", "v": "惊悚" }, { "n": "犯罪", "v": "犯罪" }, { "n": "科幻", "v": "科幻" }, { "n": "音乐", "v": "音乐" }, { "n": "其他", "v": "其他" }] }, { "key": "year", "name": "年份", "value": [{ "n": "全部", "v": "" }, { "n": "2023", "v": "2023" }, { "n": "2022", "v": "2022" }, { "n": "2021", "v": "2021" }, { "n": "2020", "v": "2020" }, { "n": "2019", "v": "2019" }, { "n": "2018", "v": "2018" }, { "n": "2017", "v": "2017" }, { "n": "2016", "v": "2016" }, { "n": "2015", "v": "2015" }, { "n": "2014", "v": "2014" }, { "n": "2013", "v": "2013" }, { "n": "2012", "v": "2012" }, { "n": "2011", "v": "2011" }] }, { "key": "by", "name": "排序", "value": [{ "n": "时间", "v": "time" }, { "n": "人气", "v": "hits" }, { "n": "评分", "v": "score" }] }],
        "4": [{ "key": "class", "name": "剧情", "value": [{ "n": "全部", "v": "" }, { "n": "剧情", "v": "剧情" }, { "n": "喜剧", "v": "喜剧" }, { "n": "爱情", "v": "爱情" }, { "n": "动作", "v": "动作" }, { "n": "悬疑", "v": "悬疑" }, { "n": "恐怖", "v": "恐怖" }, { "n": "奇幻", "v": "奇幻" }, { "n": "惊悚", "v": "惊悚" }, { "n": "犯罪", "v": "犯罪" }, { "n": "科幻", "v": "科幻" }, { "n": "音乐", "v": "音乐" }, { "n": "其他", "v": "其他" }] }, { "key": "year", "name": "年份", "value": [{ "n": "全部", "v": "" }, { "n": "2023", "v": "2023" }, { "n": "2022", "v": "2022" }, { "n": "2021", "v": "2021" }, { "n": "2020", "v": "2020" }, { "n": "2019", "v": "2019" }, { "n": "2018", "v": "2018" }, { "n": "2017", "v": "2017" }, { "n": "2016", "v": "2016" }, { "n": "2015", "v": "2015" }, { "n": "2014", "v": "2014" }, { "n": "2013", "v": "2013" }, { "n": "2012", "v": "2012" }, { "n": "2011", "v": "2011" }] }, { "key": "by", "name": "排序", "value": [{ "n": "时间", "v": "time" }, { "n": "人气", "v": "hits" }, { "n": "评分", "v": "score" }] }],
        "5": [{ "key": "year", "name": "年份", "value": [{ "n": "全部", "v": "" }, { "n": "2023", "v": "2023" }, { "n": "2022", "v": "2022" }, { "n": "2021", "v": "2021" }, { "n": "2020", "v": "2020" }, { "n": "2019", "v": "2019" }, { "n": "2018", "v": "2018" }, { "n": "2017", "v": "2017" }, { "n": "2016", "v": "2016" }, { "n": "2015", "v": "2015" }, { "n": "2014", "v": "2014" }, { "n": "2013", "v": "2013" }, { "n": "2012", "v": "2012" }, { "n": "2011", "v": "2011" }] }, { "key": "by", "name": "排序", "value": [{ "n": "时间", "v": "time" }, { "n": "人气", "v": "hits" }, { "n": "评分", "v": "score" }] }],
        "6": [{ "key": "class", "name": "剧情", "value": [{ "n": "全部", "v": "" }, { "n": "情感", "v": "情感" }, { "n": "科幻", "v": "科幻" }, { "n": "热血", "v": "热血" }, { "n": "推理", "v": "推理" }, { "n": "搞笑", "v": "搞笑" }, { "n": "冒险", "v": "冒险" }, { "n": "萝莉", "v": "萝莉" }, { "n": "校园", "v": "校园" }, { "n": "动作", "v": "动作" }, { "n": "机战", "v": "机战" }, { "n": "运动", "v": "运动" }, { "n": "战争", "v": "战争" }, { "n": "少年", "v": "少年" }] }, { "key": "area", "name": "地区", "value": [{ "n": "全部", "v": "" }, { "n": "国产", "v": "国产" }, { "n": "日本", "v": "日本" }, { "n": "欧美", "v": "欧美" }, { "n": "其他", "v": "其他" }] }, { "key": "year", "name": "年份", "value": [{ "n": "全部", "v": "" }, { "n": "2023", "v": "2023" }, { "n": "2022", "v": "2022" }, { "n": "2021", "v": "2021" }, { "n": "2020", "v": "2020" }, { "n": "2019", "v": "2019" }, { "n": "2018", "v": "2018" }, { "n": "2017", "v": "2017" }, { "n": "2016", "v": "2016" }, { "n": "2015", "v": "2015" }, { "n": "2014", "v": "2014" }, { "n": "2013", "v": "2013" }, { "n": "2012", "v": "2012" }, { "n": "2011", "v": "2011" }] }, { "key": "by", "name": "排序", "value": [{ "n": "时间", "v": "time" }, { "n": "人气", "v": "hits" }, { "n": "评分", "v": "score" }] }]
    },
    tab_exclude: '夸克网盘|迅雷云盘|百度网盘',
    // 搜索:muban.首图2.搜索1,
    搜索: 'ul.stui-vodlist&&li;a&&title;.lazyload&&data-original;.pic-text&&Text;a&&href',
}