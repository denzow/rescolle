#!/usr/bin/env bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

cd ${SCRIPT_DIR}/rescolle_crawler/rescolle_crawler
# "pref_code": "PREF13",
# 東京配下
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2184
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2116
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2217
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2295
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2141
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2207
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2241
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2254
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2286
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2228
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2923
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2273
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2156
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2178
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2250
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2142
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2101
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2146
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2278
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2164
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2107
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2170
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2169
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2198
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2125
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2222
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2133
scrapy crawl gnavi -a start_area_type=areacode_l -a start_area_code=AREAL2115