#!/usr/bin/env python3
"""批量生成个股三维深度分析报告"""
import os, json, math

# 最新一周新闻数据（由 news_data.json 提供，key 为股票代码）
NEWS_DATA = {}
_NEWS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "news_data.json")
try:
    with open(_NEWS_PATH, encoding="utf-8") as _f:
        NEWS_DATA = json.load(_f)
except Exception:
    NEWS_DATA = {}

BASE = r"D:\20250703 数据留存\7. Workbuddy\7.0 XURAN的Skill库\个人产出"

stocks = [
  {
    "code":"000988","name":"华工科技","market":"SZ","secid":"0.000988",
    "price":148.90,"prev":153.59,"mcap":1497.19e8,"pe":58.63,"pb":13.09,
    "reportFolder":"华工科技000988_三维深度分析报告",
    "yearRev":"143.55亿","yearRevYoy":"+22.59%","yearNet":"14.71亿","yearNetYoy":"+20.48%",
    "roe":"12.50%","grossMargin":"22.50%","debtRatio":"47.52%",
    "q1Rev":"33.55亿","q1RevYoy":"+52.28%","q1Net":"4.10亿","q1NetYoy":"+40.88%",
    "opCash":"-3.42亿","opCashNote":"季度波动",
    "score":6.8,
    "scores":{"fundamental":7.5,"news":6.5,"capital":6.0,"technical":6.0},
    "rating":"推荐关注 · 中性偏多",
    "ratingNote":"AI光模块+激光双轮驱动，营收利润双增，但短线主力流出",
    "summary":"AI 光模块第一梯队 · 激光装备龙头 · 量子点激光器布局 · 2026E PE 2.35元",
    "industry":"光模块/激光设备",
    "northbound":"约0.8%",
    "newsPos":"6","newsNeu":"3","newsNeg":"1",
    "newsItems":[
      ("正面","Q2单季3.8-5.2亿预期升温","2026-07"),
      ("正面","AI光模块全球份额提升，进入第一梯队","2026-06"),
      ("中性","量子业务拆分调研公布","2026-04"),
    ],
      "flowKlines":[
    "2026-06-25,-16388304.0,-158704384.0,175092672.0,-38576880.0,22188576.0",
    "2026-06-26,-2413018992.0,1428696432.0,984322560.0,-518745792.0,-1894273200.0",
    "2026-06-29,2369900032.0,-728482912.0,-1641417328.0,-724254208.0,3094154240.0",
    "2026-06-30,-373005568.0,83908720.0,289096704.0,73755136.0,-446760704.0",
    "2026-07-01,-2322938816.0,1391416432.0,931522272.0,-573646192.0,-1749292624.0",
    "2026-07-02,-2387161456.0,1380959168.0,1006202224.0,-601098848.0,-1786062608.0",
    "2026-07-03,-308999760.0,243719856.0,65279904.0,-132835728.0,-176164032.0",
    "2026-07-06,-755171504.0,481913856.0,273257648.0,-255821216.0,-499350288.0",
    "2026-07-07,-20834032.0,4132208.0,16701808.0,36874352.0,-57708384.0",
    "2026-07-08,-538217392.0,312578720.0,225638672.0,-169472032.0,-368745360.0"
  ],
  "flow10d":[-1639,-241302,23699,-37301,-232294,-238716,-30900,-75517,-2083,-53822],
    "flowTodayMain":-538220000,"flowTodayBig":312580000,"flowTodayLarge":225640000,
    "flowTodayMid":-169470000,"flowTodaySmall":-368750000,
  },
  {
    "code":"603929","name":"亚翔集成","market":"SH","secid":"1.603929",
    "price":221.10,"prev":222.19,"mcap":471.74e8,"pe":47.56,"pb":21.70,
    "reportFolder":"亚翔集成603929_三维深度分析报告",
    "yearRev":"49.07亿","yearRevYoy":"-8.81%","yearNet":"8.92亿","yearNetYoy":"+40.30%",
    "roe":"34.77%","grossMargin":"24.57%","debtRatio":"54.20%",
    "q1Rev":"8.35亿","q1RevYoy":"-","q1Net":"0.82亿","q1NetYoy":"-",
    "opCash":"-","opCashNote":"在手订单48.3亿",
    "score":7.2,
    "scores":{"fundamental":7.5,"news":6.5,"capital":7.0,"technical":7.0},
    "rating":"推荐关注 · 偏多",
    "ratingNote":"业绩持续高增，订单充裕，但营收有所下滑",
    "summary":"洁净室工程龙头 · 新加坡市场占72% · 在手订单48.3亿 · ROE 35%",
    "industry":"洁净室工程",
    "northbound":"约0.5%",
    "newsPos":"5","newsNeu":"2","newsNeg":"1",
    "newsItems":[
      ("正面","在手订单48.3亿，海外扩张提速","2026-03"),
      ("正面","毛利率同比+11pp至24.57%，盈利能力大幅改善","2026-03"),
      ("中性","营收微降8.81%，但净利润率高增","2026-03"),
    ],
      "flowKlines":[
    "2026-06-25,123921228.0,-52003550.0,-71917670.0,-46214995.0,170136223.0",
    "2026-06-26,149783344.0,-182406816.0,32623472.0,256283280.0,-106499936.0",
    "2026-06-29,208147568.0,-251342832.0,43195264.0,91213888.0,116933680.0",
    "2026-06-30,-23212928.0,53625712.0,-30412800.0,61432752.0,-84645680.0",
    "2026-07-01,-146047120.0,219477136.0,-73430016.0,-68086416.0,-77960704.0",
    "2026-07-02,-357301751.0,386900688.0,-29598944.0,-134749408.0,-222552343.0",
    "2026-07-03,11158785.0,28904240.0,-40063024.0,10805360.0,353425.0",
    "2026-07-06,-73843781.0,116176080.0,-42332288.0,-65578055.0,-8265726.0",
    "2026-07-07,29976218.0,34287616.0,-64263840.0,-5583675.0,35559893.0",
    "2026-07-08,8095953.0,-8697792.0,579792.0,-4436521.0,12532474.0"
  ],
  "flow10d":[12392,14978,20815,-2321,-14605,-35730,1116,-7384,2998,810],
    "flowTodayMain":8100000,"flowTodayBig":-870000,"flowTodayLarge":580000,
    "flowTodayMid":-440000,"flowTodaySmall":1250000,
  },
  {
    "code":"301308","name":"江波龙","market":"SZ","secid":"0.301308",
    "price":604.00,"prev":627.90,"mcap":2555.29e8,"pe":16.54,"pb":21.46,
    "reportFolder":"江波龙301308_三维深度分析报告",
    "yearRev":"227.66亿","yearRevYoy":"+30.36%","yearNet":"14.23亿","yearNetYoy":"+185.41%",
    "roe":"8.00%","grossMargin":"19.40%","debtRatio":"55.00%",
    "q1Rev":"-","q1RevYoy":"-","q1Net":"-","q1NetYoy":"-",
    "opCash":"-","opCashNote":"2026H1 预增92-110亿",
    "score":7.5,
    "scores":{"fundamental":8.0,"news":8.0,"capital":7.0,"technical":6.0},
    "rating":"推荐关注 · 偏多",
    "ratingNote":"存储行业景气高涨，2026H1净利预增近744倍，估值处合理区间",
    "summary":"国产存储模组龙头 · 2026H1净利预增92-110亿 · 行业周期+备货红利",
    "industry":"存储芯片/模组",
    "northbound":"约1.2%",
    "newsPos":"7","newsNeu":"2","newsNeg":"1",
    "newsItems":[
      ("正面","2026H1预增净利92-110亿，最高增744倍","2026-07"),
      ("正面","国产存储替代加速，AI需求爆发","2026-05"),
      ("中性","存储周期波动风险需关注","2026-06"),
    ],
      "flowKlines":[
    "2026-06-25,223213824.0,-735059.0,-222478848.0,224076544.0,-862720.0",
    "2026-06-26,-768215552.0,-696991.0,768912384.0,212411392.0,-980626944.0",
    "2026-06-29,419073024.0,-655657.0,-418417664.0,164404480.0,254668544.0",
    "2026-06-30,-858537712.0,-412622.0,858950208.0,-231791744.0,-626745968.0",
    "2026-07-01,-893001216.0,-602000.0,893603072.0,-443485440.0,-449515776.0",
    "2026-07-02,-1824789296.0,-255638.0,1825044880.0,-608576480.0,-1216212816.0",
    "2026-07-03,-147472432.0,-688885.0,148161280.0,-255147744.0,107675312.0",
    "2026-07-06,63377408.0,-1120334.0,-62257152.0,35969792.0,27407616.0",
    "2026-07-07,-794837600.0,-370133.0,795207680.0,-192882624.0,-601954976.0",
    "2026-07-08,-868125184.0,-605535.0,868730784.0,-343050992.0,-525074192.0"
  ],
  "flow10d":[22321,-76822,41907,-85854,-89300,-182479,-14747,6338,-79484,-86813],
    "flowTodayMain":-868130000,"flowTodayBig":-610000,"flowTodayLarge":868730000,
    "flowTodayMid":-343050000,"flowTodaySmall":-525070000,
  },
  {
    "code":"603986","name":"兆易创新","market":"SH","secid":"1.603986",
    "price":612.00,"prev":620.00,"mcap":4294.71e8,"pe":73.48,"pb":17.33,
    "reportFolder":"兆易创新603986_三维深度分析报告",
    "yearRev":"92.03亿","yearRevYoy":"+25.12%","yearNet":"16.48亿","yearNetYoy":"+49.47%",
    "roe":"8.00%","grossMargin":"38.00%","debtRatio":"20.00%",
    "q1Rev":"-","q1RevYoy":"-","q1Net":"-","q1NetYoy":"-",
    "opCash":"-","opCashNote":"存储芯片龙头",
    "score":6.5,
    "scores":{"fundamental":7.0,"news":6.5,"capital":5.0,"technical":7.0},
    "rating":"观察 · 中性",
    "ratingNote":"业绩稳健增长，但估值偏高(PE 73x)，主力近期大幅流出",
    "summary":"存储芯片/Nor Flash龙头 · MCU+DRAM布局 · 2025营收92亿净利16.5亿",
    "industry":"存储芯片/半导体",
    "northbound":"约2.5%",
    "newsPos":"5","newsNeu":"4","newsNeg":"2",
    "newsItems":[
      ("正面","2025营收92亿+25%，净利16.5亿+49%","2026-03"),
      ("正面","存储芯片毛利率提升，MCU需求回暖","2026-03"),
      ("负面","近10日主力累计净流出超300亿","2026-07"),
    ],
      "flowKlines":[
    "2026-06-25,512332032.0,-1058202.0,-511273984.0,-133932544.0,646264576.0",
    "2026-06-26,-3412004096.0,-1154977.0,3413158912.0,610856704.0,-4022860800.0",
    "2026-06-29,440185856.0,-1411216.0,-438774528.0,548244480.0,-108058624.0",
    "2026-06-30,-3124227328.0,-1226619.0,3125453824.0,-331776768.0,-2792450560.0",
    "2026-07-01,-5341379328.0,-1237223.0,5342616320.0,-684178688.0,-4657200640.0",
    "2026-07-02,-6391418112.0,-978171.0,6392396288.0,-1915247616.0,-4476170496.0",
    "2026-07-03,-3061302528.0,-955560.0,3062258176.0,-1099033600.0,-1962268928.0",
    "2026-07-06,-4491170304.0,-791449.0,4491961856.0,-1754345472.0,-2736824832.0",
    "2026-07-07,-2820833024.0,-2990442.0,2823823616.0,-966642176.0,-1854190848.0",
    "2026-07-08,-1051309568.0,-804872.0,1052175360.0,-97961472.0,-953348096.0"
  ],
  "flow10d":[51233,-341200,44019,-312423,-534138,-639142,-306130,-449117,-282083,-105131],
    "flowTodayMain":-1051310000,"flowTodayBig":-800000,"flowTodayLarge":1052180000,
    "flowTodayMid":-97960000,"flowTodaySmall":-953350000,
    "flow10dDesc":"近10日主力累计净流出约 -317 亿",
  },
  {
    "code":"300476","name":"胜宏科技","market":"SZ","secid":"0.300476",
    "price":282.99,"prev":284.92,"mcap":2781.18e8,"pe":53.96,"pb":17.76,
    "reportFolder":"胜宏科技300476_三维深度分析报告",
    "yearRev":"192.92亿","yearRevYoy":"+79.77%","yearNet":"43.12亿","yearNetYoy":"+273.52%",
    "roe":"35.56%","grossMargin":"28.00%","debtRatio":"50.00%",
    "q1Rev":"-","q1RevYoy":"-","q1Net":"-","q1NetYoy":"-",
    "opCash":"-","opCashNote":"AI PCB 高景气",
    "score":7.0,
    "scores":{"fundamental":8.5,"news":7.0,"capital":5.5,"technical":6.5},
    "rating":"推荐关注 · 偏多",
    "ratingNote":"AI PCB驱动业绩爆发(净利+273%)，ROE 35.56%，但近期资金面偏弱",
    "summary":"AI PCB龙头 · 2025净利43亿+273% · ROE 35.6% · 2026E利润或达100亿",
    "industry":"PCB/电子电路",
    "northbound":"约1.8%",
    "newsPos":"6","newsNeu":"2","newsNeg":"1",
    "newsItems":[
      ("正面","2025净利43亿+273%，AI PCB需求旺盛","2026-03"),
      ("正面","2026E净利润市场预期约100亿","2026-04"),
      ("中性","Q4单季营收51.75亿+70.58%，增速略放缓","2026-03"),
    ],
      "flowKlines":[
    "2026-06-25,-140726784.0,97552272.0,43174416.0,206763520.0,-347490304.0",
    "2026-06-26,-3128106112.0,1947322928.0,1180783040.0,-735038208.0,-2393067904.0",
    "2026-06-29,-958073504.0,470934672.0,487138848.0,-101651328.0,-856422176.0",
    "2026-06-30,2023224320.0,-458784976.0,-1564439376.0,-226547456.0,2249771776.0",
    "2026-07-01,-1214523744.0,744853152.0,469670656.0,-431709728.0,-782814016.0",
    "2026-07-02,-1153349296.0,563454624.0,589894672.0,-27796496.0,-1125552800.0",
    "2026-07-03,117707632.0,-131492656.0,13785024.0,201123808.0,-83416176.0",
    "2026-07-06,-1444668048.0,820209584.0,624458480.0,-253359408.0,-1191308640.0",
    "2026-07-07,-863108080.0,678217264.0,184890800.0,-163633408.0,-699474672.0",
    "2026-07-08,41526512.0,13484160.0,-55010688.0,-83956848.0,125483360.0"
  ],
  "flow10d":[-14073,-312811,-95807,202322,-121452,-115335,11771,-144467,-86311,4153],
    "flowTodayMain":41530000,"flowTodayBig":13480000,"flowTodayLarge":-55010000,
    "flowTodayMid":-83960000,"flowTodaySmall":125480000,
  },
  {
    "code":"002916","name":"深南电路","market":"SZ","secid":"0.002916",
    "price":406.19,"prev":412.10,"mcap":2766.83e8,"pe":81.36,"pb":16.81,
    "reportFolder":"深南电路002916_三维深度分析报告",
    "yearRev":"236.47亿","yearRevYoy":"+25.00%","yearNet":"32.76亿","yearNetYoy":"+80.00%",
    "roe":"15.00%","grossMargin":"26.00%","debtRatio":"40.00%",
    "q1Rev":"-","q1RevYoy":"-","q1Net":"-","q1NetYoy":"-",
    "opCash":"-","opCashNote":"PCB/封装基板双轮驱动",
    "score":6.5,
    "scores":{"fundamental":7.5,"news":6.5,"capital":5.5,"technical":6.0},
    "rating":"观察 · 中性",
    "ratingNote":"PCB/封装基板龙头，业绩稳健增长，但PE 81x估值偏高",
    "summary":"PCB+封装基板双龙头 · 2025营收236亿净利33亿 · 5G/AI驱动",
    "industry":"PCB/封装基板",
    "northbound":"约3.0%",
    "newsPos":"5","newsNeu":"3","newsNeg":"1",
    "newsItems":[
      ("正面","封装基板产能持续扩张，AI需求拉动","2026-05"),
      ("正面","2025营收236亿，净利润同比+80%","2026-03"),
      ("中性","估值偏高(PE 81x)，需业绩消化","2026-06"),
    ],
      "flowKlines":[
    "2026-06-25,635547408.0,-499505.0,-635047904.0,237807552.0,397739856.0",
    "2026-06-26,-266661920.0,-423410.0,267085344.0,-136991648.0,-129670272.0",
    "2026-06-29,-218550448.0,-673037.0,219223488.0,-3921136.0,-214629312.0",
    "2026-06-30,762159120.0,-516984.0,-761642160.0,141920544.0,620238576.0",
    "2026-07-01,-92420384.0,-661292.0,93081664.0,-183837616.0,91417232.0",
    "2026-07-02,80608192.0,-982411.0,-79625792.0,-68849472.0,149457664.0",
    "2026-07-03,676763152.0,-736367.0,-676026784.0,-244690208.0,921453360.0",
    "2026-07-06,-32544288.0,-650364.0,33194640.0,212157648.0,-244701936.0",
    "2026-07-07,-789720128.0,194362788.0,595357344.0,-289550000.0,-500170128.0",
    "2026-07-08,-93767792.0,9115017.0,84652768.0,-101939120.0,8171328.0"
  ],
  "flow10d":[63555,-26666,-21855,76216,-9242,8061,67676,-3254,-78972,-9377],
    "flowTodayMain":-93770000,"flowTodayBig":9120000,"flowTodayLarge":84650000,
    "flowTodayMid":-101940000,"flowTodaySmall":8170000,
  },
  {
    "code":"688017","name":"绿的谐波","market":"SH","secid":"1.688017",
    "price":398.39,"prev":465.07,"mcap":730.37e8,"pe":559.51,"pb":20.69,
    "reportFolder":"绿的谐波688017_三维深度分析报告",
    "yearRev":"5.71亿","yearRevYoy":"-10.00%","yearNet":"1.24亿","yearNetYoy":"-45.00%",
    "roe":"3.52%","grossMargin":"36.91%","debtRatio":"9.82%",
    "q1Rev":"-","q1RevYoy":"-","q1Net":"-","q1NetYoy":"-",
    "opCash":"1.52亿","opCashNote":"现金充裕，无负债压力",
    "score":5.0,
    "scores":{"fundamental":4.5,"news":5.5,"capital":4.5,"technical":6.0},
    "rating":"观察 · 谨慎",
    "ratingNote":"谐波减速器核心标的，人形机器人主题热，但业绩体量小、PE极高",
    "summary":"谐波减速器龙头 · 机器人核心零部件 · 业绩体量小 · 主题炒作风险高",
    "industry":"机器人核心零部件",
    "northbound":"约0.3%",
    "newsPos":"4","newsNeu":"3","newsNeg":"2",
    "newsItems":[
      ("正面","人形机器人产业政策利好，谐波减速器核心供应商","2026-06"),
      ("正面","毛利率36.91%维持高位，技术壁垒深厚","2026-04"),
      ("负面","营收/净利双降，PE 560x严重脱离基本面","2026-07"),
    ],
      "flowKlines":[
    "2026-06-25,75967328.0,-15424418.0,-60542912.0,-165485184.0,241452512.0",
    "2026-06-26,-531750816.0,-10377316.0,542128144.0,-264187680.0,-267563136.0",
    "2026-06-29,-451934608.0,-14397754.0,466332384.0,-125601664.0,-326332944.0",
    "2026-06-30,598140160.0,-22069510.0,-576070656.0,-84377296.0,682517456.0",
    "2026-07-01,-189970704.0,-9072064.0,199042784.0,-174267328.0,-15703376.0",
    "2026-07-02,-12819008.0,-10426669.0,23245664.0,40405168.0,-53224176.0",
    "2026-07-03,855827648.0,-13054384.0,-842773248.0,-333643936.0,1189471584.0",
    "2026-07-06,-530109152.0,-9557869.0,539667024.0,192707056.0,-722816208.0",
    "2026-07-07,-431290032.0,-8275657.0,439565696.0,-33314656.0,-397975376.0",
    "2026-07-08,-848166768.0,-8431267.0,856598032.0,-166595184.0,-681571584.0"
  ],
  "flow10d":[7597,-53175,-45193,59814,-18997,-1282,85583,-53011,-43129,-84817],
    "flowTodayMain":-848170000,"flowTodayBig":-8430000,"flowTodayLarge":856600000,
    "flowTodayMid":-166600000,"flowTodaySmall":-681570000,
  },
  {
    "code":"002865","name":"钧达股份","market":"SZ","secid":"0.002865",
    "price":50.88,"prev":53.33,"mcap":158.37e8,"pe":279.54,"pb":3.93,
    "reportFolder":"钧达股份002865_三维深度分析报告",
    "yearRev":"76.27亿","yearRevYoy":"-23.36%","yearNet":"-14.16亿","yearNetYoy":"-139.51%",
    "roe":"-15.00%","grossMargin":"8.00%","debtRatio":"65.00%",
    "q1Rev":"-","q1RevYoy":"-","q1Net":"-","q1NetYoy":"-",
    "opCash":"-","opCashNote":"光伏行业深度调整",
    "score":4.0,
    "scores":{"fundamental":3.0,"news":4.0,"capital":4.5,"technical":5.0},
    "rating":"观察 · 回避",
    "ratingNote":"光伏行业产能过剩，公司亏损严重，但2026E扭亏预期(机构预测净利润5.4亿)",
    "summary":"光伏电池片龙头 · P型转N型 · 2025亏损14.16亿 · 2026E扭亏预期",
    "industry":"光伏电池片",
    "northbound":"约0.5%",
    "newsPos":"3","newsNeu":"3","newsNeg":"3",
    "newsItems":[
      ("中性","机构预测2026年净利润5.42亿，扭亏在望","2026-06"),
      ("负面","2025年亏损14.16亿，Q4减值加重","2026-04"),
      ("中性","光伏产能出清加速，行业见底预期","2026-06"),
    ],
      "flowKlines":[
    "2026-06-25,-105253969.0,120998112.0,-15744147.0,-91808797.0,-13445172.0",
    "2026-06-26,10068650.0,26260608.0,-36329254.0,-126856.0,10195506.0",
    "2026-06-29,-45782232.0,51628560.0,-5846330.0,-31828787.0,-13953445.0",
    "2026-06-30,29788149.0,-43362832.0,13574688.0,15463265.0,14324884.0",
    "2026-07-01,54659125.0,-36789792.0,-17869328.0,19872171.0,34786954.0",
    "2026-07-02,11146909.0,-9297456.0,-1849453.0,34405076.0,-23258167.0",
    "2026-07-03,19940932.0,-1714442.0,-18226489.0,9351556.0,10589376.0",
    "2026-07-06,-37762340.0,50941782.0,-13179446.0,-16306094.0,-21456246.0",
    "2026-07-07,-64889585.0,87487628.0,-22598048.0,-43361524.0,-21528061.0",
    "2026-07-08,-66192176.0,59792383.0,6399793.0,-52880896.0,-13311280.0"
  ],
  "flow10d":[-10525,1007,-4578,2979,5466,1115,1994,-3776,-6489,-6619],
    "flowTodayMain":-66190000,"flowTodayBig":59790000,"flowTodayLarge":6400000,
    "flowTodayMid":-52880000,"flowTodaySmall":-13310000,
  },
  {
    "code":"600000","name":"浦发银行","market":"SH","secid":"1.600000",
    "price":9.02,"prev":8.89,"mcap":3004.19e8,"pe":4.20,"pb":0.40,
    "reportFolder":"浦发银行600000_三维深度分析报告",
    "yearRev":"1739.64亿","yearRevYoy":"+1.88%","yearNet":"500.17亿","yearNetYoy":"+10.52%",
    "roe":"6.76%","grossMargin":"-","debtRatio":"92.00%",
    "q1Rev":"-","q1RevYoy":"-","q1Net":"-","q1NetYoy":"-",
    "opCash":"-","opCashNote":"不良率六连降，资产质量改善",
    "score":6.0,
    "scores":{"fundamental":6.5,"news":5.5,"capital":6.0,"technical":5.0},
    "rating":"持有 · 中性",
    "ratingNote":"银行低估值防御品种，ROE偏低、PB破净，但不良率持续改善",
    "summary":"全国性股份制银行 · PE 4.2x PB 0.4x · ROE 6.76% · 不良率六连降",
    "industry":"银行",
    "northbound":"约4.5%",
    "newsPos":"4","newsNeu":"3","newsNeg":"1",
    "newsItems":[
      ("正面","2025净利500亿+10.5%，不良率连续六年下降","2026-03"),
      ("正面","资产总额突破10万亿","2026-03"),
      ("中性","ROE 6.76%偏低，净息差仍有压力","2026-03"),
    ],
      "flowKlines":[
    "2026-06-25,56779526.0,-88648706.0,31869181.0,9343241.0,47436285.0",
    "2026-06-26,-1203069.0,-16254097.0,17457166.0,5413573.0,-6616642.0",
    "2026-06-29,43937490.0,-33650019.0,-10287470.0,7234640.0,36702850.0",
    "2026-06-30,21658874.0,-47470973.0,25812097.0,39547401.0,-17888527.0",
    "2026-07-01,21737180.0,914072.0,-22651253.0,23368528.0,-1631348.0",
    "2026-07-02,34811554.0,-18134004.0,-16677549.0,21185030.0,13626524.0",
    "2026-07-03,46053618.0,-11136149.0,-34917469.0,41458163.0,4595455.0",
    "2026-07-06,101327895.0,143806.0,-101471699.0,17165994.0,84161901.0",
    "2026-07-07,14128888.0,-1410448.0,-12718440.0,21230384.0,-7101496.0",
    "2026-07-08,43816003.0,-7765758.0,-36050246.0,-8728240.0,52544243.0"
  ],
  "flow10d":[5678,-120,4394,2166,2174,3481,4605,10133,1413,4382],
    "flowTodayMain":43820000,"flowTodayBig":-780000,"flowTodayLarge":-36050000,
    "flowTodayMid":-8730000,"flowTodaySmall":52540000,
  },
  {
    "code":"002475","name":"立讯精密","market":"SZ","secid":"0.002475",
    "price":63.05,"prev":63.28,"mcap":4614.69e8,"pe":31.52,"pb":5.22,
    "reportFolder":"立讯精密002475_三维深度分析报告",
    "yearRev":"3323.44亿","yearRevYoy":"+23.64%","yearNet":"166.0亿","yearNetYoy":"+24.2%",
    "roe":"22.00%","grossMargin":"12.00%","debtRatio":"55.00%",
    "q1Rev":"-","q1RevYoy":"-","q1Net":"-","q1NetYoy":"-",
    "opCash":"-","opCashNote":"消费电子+汽车电子双驱动",
    "score":7.0,
    "scores":{"fundamental":8.0,"news":6.5,"capital":6.5,"technical":6.0},
    "rating":"推荐关注 · 中性偏多",
    "ratingNote":"苹果产业链+汽车电子双轮驱动，估值合理(PE 31.5x)，资金面中性",
    "summary":"消费电子精密制造龙头 · 苹果核心供应商 · 汽车电子+通讯布局 · ROE 22%",
    "industry":"消费电子/精密制造",
    "northbound":"约8.5%",
    "newsPos":"6","newsNeu":"2","newsNeg":"2",
    "newsItems":[
      ("正面","2025营收3323亿+24%，净利166亿+24%","2026-04"),
      ("正面","汽车电子业务快速增长，第二曲线成型","2026-05"),
      ("负面","苹果供应链转移风险持续关注","2026-06"),
    ],
      "flowKlines":[
    "2026-06-25,-1301461488.0,1057728128.0,243733248.0,609805824.0,-1911267312.0",
    "2026-06-26,-2918012416.0,2148676320.0,769336320.0,-1049421056.0,-1868591360.0",
    "2026-06-29,-840900848.0,767541136.0,73359776.0,-409500784.0,-431400064.0",
    "2026-06-30,2011135072.0,-1423584400.0,-587550400.0,181368064.0,1829767008.0",
    "2026-07-01,-1519732560.0,1355377296.0,164355168.0,-531434560.0,-988298000.0",
    "2026-07-02,-2212759920.0,1228060912.0,984698992.0,-947520624.0,-1265239296.0",
    "2026-07-03,1423893552.0,-389222288.0,-1034671280.0,344888752.0,1079004800.0",
    "2026-07-06,-35224368.0,-22287696.0,57512064.0,92738496.0,-127962864.0",
    "2026-07-07,533229424.0,-342606768.0,-190622656.0,45294752.0,487934672.0",
    "2026-07-08,205701440.0,3998752.0,-209700192.0,-39675040.0,245376480.0"
  ],
  "flow10d":[-130146,-291801,-84090,201114,-151973,-221275,142389,-3522,53323,20570],
    "flowTodayMain":205700000,"flowTodayBig":4000000,"flowTodayLarge":-209700000,
    "flowTodayMid":-39680000,"flowTodaySmall":245380000,
  },
]

def gen_report(s):
  chg = s["price"] - s["prev"]
  pct = round(chg / s["prev"] * 100, 2)
  up = chg >= 0
  arrow = "▲" if up else "▼"
  sign = "+" if up else ""
  pxCls = "up" if up else "down"
  mcapStr = f"{s['mcap']/1e8:.2f}亿" if s['mcap'] >= 1e8 else f"{s['mcap']/1e8:.2f}亿"
  if s['mcap'] >= 1e11:
    mcapStr = f"{s['mcap']/1e11:.2f}万亿"

  # Cap flow summary (从 flowKlines 计算，保证与表格一致)
  klines = s.get("flowKlines", [])
  mainVals = [float(k.split(",")[1]) for k in klines]  # 元
  flow10sum = round(sum(mainVals) / 1e8, 2)
  flow5sum = round(sum(mainVals[-5:]) / 1e8, 2) if len(mainVals)>=5 else 0
  flow10cls = "up" if flow10sum>=0 else "down"
  flow5cls = "up" if flow5sum>=0 else "down"

  # Today's flow (最后一条 kline)
  if klines:
    lastP = klines[-1].split(",")
    tf = float(lastP[1]) / 1e8  # 主力
    tfBig = float(lastP[4]) / 1e8  # 超大单
    tfLarge = float(lastP[5]) / 1e8  # 大单
  else:
    tf = 0; tfBig = 0; tfLarge = 0
  tfCls = "up" if tf>=0 else "down"
  tfSign = "+" if tf>=0 else ""

  # Build flow table rows from flowKlines (倒序：最新在前)
  flowRows = ""
  for kline in reversed(s.get("flowKlines", [])):
    parts = kline.split(",")
    date = parts[0]
    # Values in 元 -> 亿: /1e8
    mainYi = float(parts[1]) / 1e8
    smallYi = float(parts[2]) / 1e8
    mediumYi = float(parts[3]) / 1e8
    superLargeYi = float(parts[4]) / 1e8
    largeYi = float(parts[5]) / 1e8
    def fmt(v): return ("+" if v>=0 else "")+f"{v:.2f}"
    def cls(v): return "up" if v>=0 else "down"
    flowRows += f'<tr><td>{date}</td><td class="{cls(mainYi)}">{fmt(mainYi)}</td><td class="{cls(superLargeYi)}">{fmt(superLargeYi)}</td><td class="{cls(largeYi)}">{fmt(largeYi)}</td><td class="{cls(mediumYi)}">{fmt(mediumYi)}</td><td class="{cls(smallYi)}">{fmt(smallYi)}</td></tr>\n'

  # News items
  newsItems = ""
  for tag, txt, date in s["newsItems"]:
    badgeCls = {"正面":"b-pos","中性":"b-neu","负面":"b-neg"}.get(tag,"b-neu")
    newsItems += f'<div class="ni"><span class="badge {badgeCls}">{tag}</span><div class="tx">{txt} <small>{date}</small></div></div>\n'

  # Sub-score bars
  subBars = ""
  for key, label, color in [("fundamental","基本面","#2b5ce6"),("news","新闻面","#f5a623"),("capital","资金面","#1faa59"),("technical","技术面","#9aa6b2")]:
    v = s["scores"][key]
    subBars += f'<div class="srow"><div class="nm">{label}</div><div class="b"><i style="width:{v*10}%;background:{color}"></i></div><div class="sc" style="color:{color}">{v}</div><div class="wt">{"35%" if key=="fundamental" or key=="capital" else "20%" if key=="news" else "10%"}</div></div>\n'

  # Estimate price range
  estPE_low = 25
  estPE_high = 40
  # Estimate EPS from PE and price
  eps_est = round(s["price"] / s["pe"], 2) if s["pe"] > 0 else 1.0
  est_low = round(eps_est * estPE_low, 2) if s["pe"] > 0 else round(s["price"]*0.8,2)
  est_high = round(eps_est * estPE_high, 2) if s["pe"] > 0 else round(s["price"]*1.2,2)
  # Position of current price on range
  rng = est_high - est_low
  pos_pct = round((s["price"]-est_low)/rng*100,1) if rng>0 else 50
  pos_label = "偏低区" if pos_pct < 33 else "中枢区" if pos_pct < 66 else "偏高区"

  # 最新一周动态与关键新闻分析（来自 news_data.json）
  news = NEWS_DATA.get(s.get("code"))
  if news:
    _items = ""
    for _it in news.get("items", []):
      _badge = {"pos":"b-pos","neu":"b-neu","neg":"b-neg"}.get(_it.get("sentiment"),"b-neu")
      _items += '<div class="ni"><span class="badge %s">%s</span><div class="tx"><b>%s</b><small> · %s</small><br>%s</div></div>\n' % (_badge, _it.get("title",""), _it.get("title",""), _it.get("date",""), _it.get("analysis",""))
    newsHtml = (
      '  <div class="sec">\n'
      '    <h2><span class="dot" style="background:var(--brand2)"></span>最新一周动态与关键新闻分析</h2>\n'
      '    <div class="lead">截至 2026-07-22 的近一周公开资讯梳理（来源：东方财富/同花顺等公开新闻检索，仅供研究参考）。</div>\n'
      '    <div style="font-size:14px;line-height:1.8;margin-bottom:6px"><b>本周综述：</b>' + news.get("summary","") + '</div>\n'
      '    <div class="news-list">\n' + _items + '    </div>\n'
      '    <div class="note">⚠️ 以上为公开新闻的归纳与客观转述，不代表本方观点，亦不构成投资建议。新闻时效性较强，请以最新公告为准。</div>\n'
      '  </div>\n'
    )
  else:
    newsHtml = ""

  html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{s['name']}({s['code']}) 个股三维深度分析报告</title>
<style>
:root{{--red:#e23b3b;--green:#1faa59;--bg:#f5f7fa;--card:#fff;--ink:#1f2733;--sub:#6b7785;--line:#e8edf2;--brand:#2b5ce6;--brand2:#15b8a6;--amber:#f5a623;--shadow:0 2px 14px rgba(20,40,80,.06)}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--ink);line-height:1.65;padding:26px 16px 60px;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:1080px;margin:0 auto}}
.up{{color:var(--red);font-weight:600}}
.down{{color:var(--green);font-weight:600}}
.muted{{color:var(--sub);font-size:13px}}
.hero{{background:linear-gradient(120deg,#1b2a4e 0%,#284b8c 55%,#2b5ce6 100%);color:#fff;border-radius:18px;padding:26px 30px;box-shadow:var(--shadow);position:relative;overflow:hidden}}
.hero:after{{content:"";position:absolute;right:-60px;top:-60px;width:220px;height:220px;background:radial-gradient(circle,rgba(255,255,255,.12),transparent 70%);border-radius:50%}}
.hero .tag{{display:inline-block;background:rgba(255,255,255,.16);padding:3px 11px;border-radius:20px;font-size:12px;letter-spacing:.5px}}
.hero h1{{font-size:27px;margin:10px 0 4px}}
.hero .code{{opacity:.85;font-size:14px}}
.hero .price{{font-size:42px;font-weight:800;margin-top:12px;letter-spacing:.5px}}
.hero .chg{{font-size:16px;margin-left:10px}}
.hero .meta{{display:flex;flex-wrap:wrap;gap:22px;margin-top:16px;font-size:13.5px;opacity:.95}}
.hero .meta b{{display:block;font-size:17px;font-weight:700;margin-top:2px}}
.hero .meta span{{opacity:.78}}
.disclaim{{margin-top:14px;font-size:12px;opacity:.8;border-top:1px solid rgba(255,255,255,.2);padding-top:10px}}
.sec{{background:var(--card);border-radius:16px;padding:22px 26px;margin-top:20px;box-shadow:var(--shadow)}}
.sec h2{{font-size:19px;display:flex;align-items:center;gap:9px;margin-bottom:6px}}
.sec h2 .dot{{width:9px;height:22px;border-radius:5px;background:var(--brand)}}
.sec .lead{{color:var(--sub);font-size:13px;margin-bottom:16px}}
.grid3{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}
.grid2{{display:grid;grid-template-columns:1.3fr 1fr;gap:18px}}
@media(max-width:820px){{.grid3,.grid2{{grid-template-columns:1fr}}}}
.kpi{{background:#fafbfd;border:1px solid var(--line);border-radius:12px;padding:13px 14px}}
.kpi .lab{{font-size:12.5px;color:var(--sub)}}
.kpi .val{{font-size:21px;font-weight:750;margin-top:3px}}
.kpi .sub{{font-size:12px;margin-top:2px}}
.bar{{height:9px;border-radius:6px;background:#eef1f5;overflow:hidden;margin-top:9px}}
.bar>i{{display:block;height:100%;border-radius:6px}}
.scorecard{{display:flex;align-items:center;gap:26px;flex-wrap:wrap}}
.gauge{{position:relative;width:170px;height:170px;flex:0 0 auto}}
.gauge svg{{transform:rotate(-90deg)}}
.gauge .num{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}}
.gauge .num b{{font-size:40px;font-weight:800;line-height:1}}
.gauge .num small{{color:var(--sub);font-size:13px;margin-top:3px}}
.scorebars{{flex:1;min-width:260px}}
.srow{{display:flex;align-items:center;gap:10px;margin:9px 0}}
.srow .nm{{width:74px;font-size:13.5px}}
.srow .b{{flex:1;height:12px;background:#eef1f5;border-radius:7px;overflow:hidden}}
.srow .b>i{{display:block;height:100%;border-radius:7px;background:linear-gradient(90deg,#2b5ce6,#15b8a6)}}
.srow .sc{{width:62px;text-align:right;font-size:13.5px;font-weight:700}}
.srow .wt{{width:46px;text-align:right;font-size:11.5px;color:var(--sub)}}
.rating{{display:inline-block;margin-top:4px;padding:5px 16px;border-radius:30px;font-weight:700;font-size:15px;background:#fff4e0;color:#c77700;border:1px solid #f3d9a8}}
.donut-row{{display:flex;align-items:center;gap:24px;flex-wrap:wrap}}
.news-list{{margin-top:14px;border-top:1px dashed var(--line);padding-top:12px}}
.news-list .ni{{display:flex;gap:10px;padding:8px 0;border-bottom:1px solid #f1f4f8;font-size:13.5px}}
.news-list .ni .badge{{flex:0 0 auto;font-size:11px;padding:2px 8px;border-radius:6px;height:fit-content;margin-top:2px}}
.b-pos{{background:#fdeaea;color:var(--red)}}
.b-neu{{background:#eef1f5;color:var(--sub)}}
.b-neg{{background:#e7f6ee;color:var(--green)}}
.news-list .ni .tx small{{color:var(--sub);margin-left:6px}}
table{{width:100%;border-collapse:collapse;font-size:13px;margin-top:6px}}
th,td{{padding:9px 10px;text-align:right;border-bottom:1px solid var(--line)}}
th:first-child,td:first-child{{text-align:left}}
thead th{{color:var(--sub);font-weight:600;background:#fafbfd}}
.range{{background:linear-gradient(120deg,#eef4ff,#f3fbff);border-radius:14px;padding:18px 20px;border:1px solid #e1ecff}}
.range .calc{{font-size:13px;color:#33415c;line-height:1.9}}
.range .calc code{{background:#fff;padding:1px 7px;border-radius:5px;border:1px solid #d8e3f5;font-size:12.5px}}
.priceline{{position:relative;height:54px;margin:18px 0 6px}}
.priceline .track{{position:absolute;top:24px;left:0;right:0;height:8px;border-radius:6px;background:linear-gradient(90deg,#cfe0ff,#2b5ce6 50%,#9ec6ff)}}
.priceline .cur{{position:absolute;top:6px;transform:translateX(-50%);text-align:center}}
.priceline .cur b{{color:var(--brand);font-size:14px}}
.priceline .cur small{{display:block;color:var(--sub);font-size:11px}}
.priceline .rng{{position:absolute;top:18px;border-top:2px dashed #fff;color:#fff;font-size:11px;padding:0 6px}}
.src-table td:first-child{{text-align:left}}
.src-table .st{{font-weight:700}}
.note{{background:#fffaf0;border:1px solid #f3e3c0;border-radius:12px;padding:14px 18px;font-size:13px;color:#7a5c12;margin-top:14px}}
.risk{{font-size:13px;color:#5a4632;line-height:1.85}}
.risk li{{margin-left:18px;margin-bottom:5px}}
footer{{text-align:center;color:var(--sub);font-size:12px;margin-top:26px;line-height:1.7}}
.pill{{display:inline-block;font-size:11.5px;padding:2px 9px;border-radius:20px;background:#eef1f5;color:var(--sub);margin:2px 3px}}
#btnRefresh{{background:var(--brand);color:#fff;border:none;padding:9px 18px;border-radius:10px;font-size:14px;font-weight:700;cursor:pointer;box-shadow:0 2px 8px rgba(43,92,230,.3);transition:.2s}}
#btnRefresh:hover{{background:#1f49c4}}
#btnRefresh:disabled{{background:#9fb2e0;cursor:wait;box-shadow:none}}
</style>
</head>
<body>
<div class="wrap">
  <div class="hero">
    <span class="tag">个股三维深度分析 · A股</span>
    <h1>{s['name']} <span style="font-weight:500">{s['industry']}</span></h1>
    <div class="code">代码 {s['code']}.{s['market']} ｜ {s['market']}交所 ｜ 数据截至 2026-07-08 盘中</div>
    <div class="price">¥{s['price']} <span class="chg {pxCls}">{arrow} {sign}{chg:.2f} ({sign}{pct}%)</span></div>
    <div class="meta">
      <div><span>总市值</span><b>{mcapStr}</b></div>
      <div><span>市盈率(动)</span><b>{s['pe']}</b></div>
      <div><span>市净率</span><b>{s['pb']}</b></div>
    </div>
    <div class="disclaim">⚠️ 本报告基于公开数据整理，仅供研究与学习参考，<b>不构成任何投资建议</b>。股市有风险，决策需谨慎。</div>
  </div>

  <div class="sec" style="margin-top:20px;padding:14px 22px;display:flex;align-items:center;gap:14px;flex-wrap:wrap">
    <button id="btnRefresh" onclick="refreshLive()">🔄 刷新实时行情</button>
    <span id="pxStatus" class="muted">点击按钮拉取东方财富盘中实时数据（仅更新行情与今日资金流，财务/北向/新闻为定期数据）</span>
    <span id="pxStamp" class="pill" style="margin-left:auto">最后刷新：页面载入时</span>
  </div>

  <div class="sec">
    <h2><span class="dot"></span>综合评分与评级</h2>
    <div class="lead">三维加权评分（基本面 35% · 新闻面 20% · 资金面 35% · 技术面 10%），满分 10 分。</div>
    <div class="scorecard">
      <div class="gauge">
        <svg width="170" height="170" viewBox="0 0 170 170">
          <circle cx="85" cy="85" r="72" fill="none" stroke="#eef1f5" stroke-width="16"/>
          <circle id="g" cx="85" cy="85" r="72" fill="none" stroke="#2b5ce6" stroke-width="16" stroke-linecap="round" stroke-dasharray="452" stroke-dashoffset="452"/>
        </svg>
        <div class="num"><b id="gnum">0</b><small>综合评分 / 10</small></div>
      </div>
      <div class="scorebars">
{subBars}
        <div style="margin-top:10px"><span class="rating">{s['rating']}（{s['score']} 分）</span></div>
      </div>
    </div>
    <div class="note">💡 {s['ratingNote']}</div>
  </div>

  <div class="sec">
    <h2><span class="dot"></span>① 基本面 · 财务质地</h2>
    <div class="lead">数据来源：2025 年年报（公开披露），部分为估算值。</div>
    <div class="grid3">
      <div class="kpi"><div class="lab">2025 营业收入</div><div class="val">{s['yearRev']}</div><div class="sub up">同比 {s['yearRevYoy']}</div></div>
      <div class="kpi"><div class="lab">2025 归母净利润</div><div class="val">{s['yearNet']}</div><div class="sub up">同比 {s['yearNetYoy']}</div></div>
      <div class="kpi"><div class="lab">加权 ROE</div><div class="val">{s['roe']}</div></div>
      <div class="kpi"><div class="lab">毛利率</div><div class="val">{s['grossMargin']}</div></div>
      <div class="kpi"><div class="lab">资产负债率</div><div class="val">{s['debtRatio']}</div></div>
      <div class="kpi"><div class="lab">经营现金流</div><div class="val">{s['opCash'] if s['opCash']!='-' else '-'}</div><div class="sub">{s['opCashNote']}</div></div>
    </div>
    <div class="note" style="background:#eef6ff;border-color:#cfe0ff;color:#1f4f9e">📌 {s['summary']}</div>
  </div>

  <div class="sec">
    <h2><span class="dot"></span>② 新闻面 · 近 30 天舆情</h2>
    <div class="lead">基于公开新闻与研报的情绪监测估算（非精确统计）。</div>
    <div class="news-list">
{newsItems}
    </div>
  </div>

  <div class="sec">
    <h2><span class="dot"></span>③ 资金面 · 主力净流入</h2>
    <div class="lead">主力净流入来自东方财富资金流 API（单位：亿元）。</div>
    <div class="grid3" style="margin-bottom:16px">
      <div class="kpi"><div class="lab">今日主力净流入</div><div class="val {tfCls}">{tfSign}{tf:.2f}</div><div class="sub {tfCls}">超大单 {tfBig:.2f} ｜ 大单 {tfLarge:.2f}</div></div>
      <div class="kpi"><div class="lab">近 5 日主力净流入</div><div class="val {flow5cls}">{flow5sum:.2f}</div></div>
      <div class="kpi"><div class="lab">近 10 日主力净流入</div><div class="val {flow10cls}">{flow10sum:.2f}</div></div>
    </div>
    <h3 style="font-size:14px;margin-bottom:6px;color:#33415c">近 10 个交易日主力净流入（亿元，万元原始值）</h3>
    <table>
      <thead><tr><th>日期</th><th>主力净流入</th><th>超大单</th><th>大单</th><th>中单</th><th>小单</th></tr></thead>
      <tbody>
{flowRows}
      </tbody>
    </table>
    <div class="note" style="background:#eef6ff;border-color:#cfe0ff;color:#1f4f9e">📌 北向（沪/深股通）持股约 {s['northbound']}，整体占比偏低。</div>
  </div>

  <div class="sec">
    <h2><span class="dot"></span>合理价格区间参考（估值测算）</h2>
    <div class="range">
      <div class="calc">
        <b>测算假设：</b><br>
        ① 当前动态 PE {s['pe']}x，EPS ≈ <code>{eps_est:.2f} 元</code>（基于现价反推）；<br>
        ② 给予 {estPE_low}–{estPE_high} 倍 PE 区间（考虑行业与成长性溢价）；<br>
        ③ 合理价 = {eps_est:.2f} × {estPE_low} ~ {eps_est:.2f} × {estPE_high} ≈ <b style="color:var(--brand)">¥{est_low:.0f} ~ ¥{est_high:.0f}</b>。<br>
        <b>结合资金面与基本面，综合合理区间：</b>
      </div>
      <div class="priceline">
        <div class="track"></div>
        <div class="rng" style="left:8%">¥{est_low:.0f}<br>保守</div>
        <div class="rng" style="left:60%">¥{est_high:.0f}<br>乐观</div>
        <div class="cur" style="left:{pos_pct}%"><b>¥{s['price']}</b><small>当前价（{pos_label}）</small></div>
      </div>
      <div style="text-align:center;font-size:12.5px;color:#33415c">估值区间（12 个月视角）：<b style="color:var(--brand)">¥{est_low:.0f} — ¥{est_high:.0f}</b></div>
    </div>
    <div class="note" style="background:#fff4f4;border-color:#f3c9c9;color:#a33636">⚠️ 上述价格区间仅为基于盈利与估值的情景测算，不构成目标价或买卖建议。实际价格可能显著偏离区间。</div>
  </div>

  <div class="sec">
    <h2><span class="dot" style="background:var(--amber)"></span>风险提示</h2>
    <ul class="risk">
      <li><b>资金面波动：</b>近 10 日主力净流入 {flow10sum:.2f} 亿，若回流不持续，短线仍有压力。</li>
      <li><b>估值与拥挤度：</b>动态 PE {s['pe']}x，需关注业绩与估值的匹配度。</li>
      <li><b>行业与政策风险：</b>行业竞争加剧、下游需求变化、政策调整可能影响公司业绩。</li>
      <li><b>非投资建议：</b>本报告由公开数据自动整理生成，仅供研究与学习，不构成任何证券买卖建议。</li>
    </ul>
  </div>

{newsHtml}
  <footer>
    {s['name']}（{s['code']}.{s['market']}）个股三维深度分析报告 ｜ 生成日期 2026-07-08<br>
    数据来源：东方财富行情/资金流API、公司定期报告及公开新闻检索 ｜ 涨跌色按 A 股习惯（涨红跌绿）<br>
    ⚠️ 本报告仅供研究参考，不构成投资建议。
  </footer>
</div>

<script>
(function(){{
  var score={s['score']}, circ=452;
  var g=document.getElementById('g'), n=0, num=document.getElementById('gnum');
  if(!g||!num) return;
  var t=setInterval(function(){{
    n+=0.1; if(n>=score){{n=score;clearInterval(t);}}
    g.setAttribute('stroke-dashoffset', circ*(1-n/10));
    num.textContent=n.toFixed(1);
  }},28);
}})();
setTimeout(refreshLive, 500);  // 页面载入后自动刷新

function jsonp(url, cbName, timeout){{
  return new Promise(function(resolve, reject){{
    var s=document.createElement('script');
    var done=false;
    var timer=setTimeout(function(){{
      if(!done){{done=true; if(s.parentNode) s.parentNode.removeChild(s); reject(new Error('timeout'));}}
    }}, timeout||9000);
    window[cbName]=function(data){{ if(done) return; done=true; clearTimeout(timer); if(s.parentNode) s.parentNode.removeChild(s); resolve(data); }};
    s.onerror=function(){{ if(done) return; done=true; clearTimeout(timer); reject(new Error('load error')); }};
    s.src=url+(url.indexOf('?')>=0?'&':'?')+'cb='+cbName;
    document.body.appendChild(s);
  }});
}}
function fmtYi(v){{ return (v/1e8).toFixed(2); }}
function fmtCap(v){{ return v>=1e12 ? (v/1e12).toFixed(2)+' 万亿' : (v/1e8).toFixed(1)+' 亿'; }}
function setVal(id, txt, cls){{
  var el=document.getElementById(id); if(!el) return;
  el.textContent=txt; if(cls!==undefined) el.className=cls;
}}

function refreshLive(){{
  var btn=document.getElementById('btnRefresh'), st=document.getElementById('pxStatus');
  if(!btn||!st) return;
  btn.disabled=true; st.textContent='正在拉取东方财富实时数据…';
  var ts=new Date();
  var p2=function(n){{return String(n).padStart(2,'0');}};
  var stamp=ts.getFullYear()+'-'+p2(ts.getMonth()+1)+'-'+p2(ts.getDate())+' '+p2(ts.getHours())+':'+p2(ts.getMinutes())+':'+p2(ts.getSeconds());

  var qp='https://push2.eastmoney.com/api/qt/stock/get?secid={s['secid']}&fields=f43,f44,f45,f46,f47,f48,f57,f58,f60,f168,f116,f117,f162,f167,f171,f173';
  var fp='https://push2his.eastmoney.com/api/qt/stock/fflow/kline/get?lmt=10&klt=101&secid={s['secid']}&fields1=f1,f2,f3&fields2=f51,f52,f53,f54,f55,f56';

  Promise.allSettled([jsonp(qp,'__emq_'+Date.now()), jsonp(fp,'__emf_'+Date.now())]).then(function(r){{
    var okQ = r[0].status==='fulfilled' && r[0].value && r[0].value.data;
    var okF = r[1].status==='fulfilled' && r[1].value && r[1].value.data && r[1].value.data.klines;

    if(okQ){{
      var d=r[0].value.data;
      var price=d.f43/100, prev=d.f60/100, chg=price-prev, pct=chg/prev*100, up=chg>=0;
      var pxEl=document.querySelector('.hero .price');
      if(pxEl) pxEl.innerHTML='<span>¥'+price.toFixed(2)+'</span> <span class="chg '+(up?'up':'down')+'">'+(up?'▲ ':'▼ ')+(up?'+':'')+chg.toFixed(2)+' ('+(up?'+':'')+pct.toFixed(2)+'%)</span>';
      var metaEl=document.querySelector('.hero .meta');
      if(metaEl){{
        var children=metaEl.children;
        if(children[0]) children[0].innerHTML='<span>总市值</span><b>'+fmtCap(d.f116)+'</b>';
        if(children[1]) children[1].innerHTML='<span>市盈率(动)</span><b>'+(d.f162/100).toFixed(1)+'</b>';
        if(children[2]) children[2].innerHTML='<span>市净率</span><b>'+(d.f167/100).toFixed(2)+'</b>';
      }}
    }}

    if(okF){{
      var kl= r[1].value.data.klines;
      // Rebuild flow table
      var tbody=document.querySelector('table tbody');
      if(tbody){{
        var klRev=kl.slice().reverse(), sum5=0, sum10=0, htmlRev='';
        // 倒序渲染 + 计算合计
        klRev.forEach(function(line,i){{
            var p=line.split(',');
            var d=p[0], main=parseFloat(p[1])/1e8, small=parseFloat(p[2])/1e8, medium=parseFloat(p[3])/1e8;
            var superLarge=parseFloat(p[4])/1e8, large=parseFloat(p[5])/1e8;
            function fmt(v){{return (v>=0?'+':'')+v.toFixed(2);}}
            function cl(v){{return v>=0?'up':'down';}}
            htmlRev+='<tr><td>'+d+'</td><td class="'+cl(main)+'">'+fmt(main)+'</td><td class="'+cl(superLarge)+'">'+fmt(superLarge)+'</td><td class="'+cl(large)+'">'+fmt(large)+'</td><td class="'+cl(medium)+'">'+fmt(medium)+'</td><td class="'+cl(small)+'">'+fmt(small)+'</td></tr>';
            // 只有在原始数组中处于后5位才计入 sum5（klRev 是倒序，i<5 对应原始后5）
            if(i<5) sum5+=main;
            sum10+=main;
            // 第一行（klRev[0] = 最新一天）→ 更新 KPI 卡片
            if(i===0){{
              var fk=document.getElementById('flowKpis'); var kpis=fk?fk.querySelectorAll('.kpi'):[];
              if(kpis.length>=3){{
                var mCls=main>=0?'up':'down';
                kpis[0].querySelector('.val').className='val '+mCls;
                kpis[0].querySelector('.val').textContent=(main>=0?'+':'')+main.toFixed(2);
                kpis[0].querySelector('.sub').className='sub '+mCls;
                kpis[0].querySelector('.sub').textContent='超大单 '+(superLarge>=0?'+':'')+superLarge.toFixed(2)+' ｜ 大单 '+(large>=0?'+':'')+large.toFixed(2);
                var c5=sum5>=0?'up':'down', c10=sum10>=0?'up':'down';
                kpis[1].querySelector('.val').className='val '+c5;
                kpis[1].querySelector('.val').textContent=(sum5>=0?'+':'')+sum5.toFixed(2);
                kpis[2].querySelector('.val').className='val '+c10;
                kpis[2].querySelector('.val').textContent=(sum10>=0?'+':'')+sum10.toFixed(2);
              }}
            }}
        }});
        tbody.innerHTML=htmlRev;
      }}
    }}
    if(okQ||okF){{
      st.textContent='✅ 行情与资金流已实时更新';
      var stampEl=document.getElementById('pxStamp');
      if(stampEl) stampEl.textContent='最后刷新：'+stamp;
    }} else {{
      st.textContent='❌ 刷新失败：接口被限制或网络不通，已保留原数据。请稍后重试。';
    }}
    btn.disabled=false;
  }});
}}
</script>
</body>
</html>"""
  return html


if __name__ == "__main__":
  for s in stocks:
    folder = os.path.join(BASE, s["reportFolder"])
    os.makedirs(folder, exist_ok=True)
    fname = f"{s['code']}_{s['name']}_三维深度分析报告_20260708.html"
    fpath = os.path.join(folder, fname)
    html = gen_report(s)
    with open(fpath, "w", encoding="utf-8") as f:
      f.write(html)
    print(f"✅ {s['name']} ({s['code']}) → {fpath}  ({len(html)} bytes)")
  print("\n== 全部 10 只报告生成完成 ==")
