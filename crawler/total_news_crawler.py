from common.google_crawler import GoogleCrawler
from common.en_HistoryNewsData import ukraineHistory_en

try:
    GoogleCrawler('교전 최신 상황').crawl_news('ukraine belligerence', 3).write_json('en_BattleNewsData')
    print('en_BattleNewsData')
except:
    print('en_BattleNewsData error')

try:
    GoogleCrawler('교전 최신 상황').crawl_news('우크라이나 교전 상황', 3).write_json('kr_BattleNewsData')
    print('kr_BattleNewsData')
except:
    print('kr_BattleNewsData error')

# TODO :이 사이트만 크롤링이 타 사이트인데 수정 여부 논의 필요
try:
    ukraineHistory_en('ukraine', 2, 'en_HistoryNewsData', '역사')
    print('en_HistoryNewsData')
except:
    print('en_HistoryNewsData error')

try:
    GoogleCrawler('역사').crawl_news('우크라이나 역사', 3).write_json('kr_HistoryNewsData')
    print('kr_HistoryNewsData')
except:
    print('kr_HistoryNewsData error')

try:
    GoogleCrawler('규제').crawl_news('ukraine regulation', 3).write_json('en_RegulationNewsData')
    print('en_RegulationNewsData')
except:
    print('en_RegulationNewsData error')

try:
    GoogleCrawler('규제').crawl_news('우크라이나 규제', 3).write_json('kr_RegulationNewsData')
    print('kr_RegulationNewsData')
except:
    print('en_RegulationNewsData error')

try:
    GoogleCrawler('후원').crawl_news('Ukraine Sponsor', 3).write_json('en_SponsorNewsData')
    print('en_SponsorNewsData')
except:
    print('en_SponsorNewsData error')

try:
    GoogleCrawler('후원').crawl_news('우크라이나 후원', 3).write_json('kr_SponsorNewsData')
    print('kr_SponsorNewsData')
except:
    print('kr_SponsorNewsData error')

try:
    GoogleCrawler('협상 진행 과정').crawl_news('ukraine negotiation progress situation', 3).write_json('en_NegoNewsData')
    print('en_NegoNewsData')
except:
    print('en_NegoNewsData error')

try:
    GoogleCrawler('협상 진행 과정').crawl_news('우크라이나 협상 진행 상황', 3).write_json('kr_NegoNewsData')
    print('kr_NegoNewsData')
except:
    print('kr_NegoNewsData error')

try:
    GoogleCrawler('지역 라이브 상황').crawl_news('ukraine local live', 3).write_json('en_LocalNewsData')
    print('en_LocalNewsData')
except:
    print('en_LocalNewsData error')

try:
    GoogleCrawler('지역 라이브 상황').crawl_news('우크라이나 실시간 상황', 3).write_json('kr_LocalNewsData')
    print('kr_LocalNewsData')
except:
    print('kr_LocalNewsData error')

try:
    GoogleCrawler('피해 상황').crawl_news('ukraine damage', 3).write_json('en_DamageNewsData')
    print('en_DamageNewsData')
except:
    print('en_DamageNewsData error')

try:
    GoogleCrawler('지역 라이브 상황').crawl_news('우크라이나 피해 상황', 3).write_json('kr_DamageNewsData')
    print('kr_DamageNewsData')
except:
    print('kr_DamageNewsData error')