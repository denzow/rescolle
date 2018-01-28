# coding: utf-8

import sqlite3 as sqlite


class Restaurant:

    def __init__(self, id, name, name_kana, latitude, longitude, category, url, url_mobile,
                image_url_1, image_url_2, address, tel, tel_sub, open_time, holiday, pr_short, pr_long,
                category_code_l, category_name_l, category_code_s, category_name_s, budget, party, lunch):
        """

        :param id:
        :param name:
        :param name_kana:
        :param latitude:
        :param longitude:
        :param category:
        :param url:
        :param url_mobile:
        :param image_url_1:
        :param image_url_2:
        :param address:
        :param tel:
        :param tel_sub:
        :param open_time:
        :param holiday:
        :param pr_short:
        :param pr_long:
        :param category_code_l:
        :param category_name_l:
        :param category_code_s:
        :param category_name_s:
        :param budget:
        :param party:
        :param lunch:
        """
        self.id = id
        self.name = name
        self.name_kana = name_kana
        self.latitude = latitude
        self.longitude = longitude
        self.category = category
        self.url = url
        self.url_mobile = url_mobile
        self.image_url_1 = image_url_1
        self.image_url_2 = image_url_2
        self.address = address
        self.tel = tel
        self.tel_sub = tel_sub
        self.open_time = open_time
        self.holiday = holiday
        self.pr_short = pr_short
        self.pr_long = pr_long
        self.category_code_l = category_code_l
        self.category_name_l = category_name_l
        self.category_code_s = category_code_s
        self.category_name_s = category_name_s
        self.budget = budget
        self.party = party
        self.lunch = lunch

    @classmethod
    def create_by_dict(cls, raw_dict):
        """
        dictから生成するためのメソッド
        raw_dict = {
            "@attributes": {
                "order": "0"
            },
            "id": "gdpf900",
            "update_date": "2018-01-13 01:45:57",
            "name": "チーズタッカルビ＆しゃぶしゃぶ食べ放題 はなの邸 渋谷店",
            "name_kana": "チーズタッカルビアンドシャブシャブタベホウダイ ハナノテイシブヤテン",
            "latitude": "35.658303",
            "longitude": "139.701208",
            "category": "個室居酒屋女子会合コン",
            "url": "https://r.gnavi.co.jp/1m6z2jy70000/?ak=ZOLHnox1Lh%2Bt7ZDxYP5iDDvst4%2FaDZDoCEDjuf84QBY%3D",
            "url_mobile": "http://mobile.gnavi.co.jp/shop/gdpf900/?ak=ZOLHnox1Lh%2Bt7ZDxYP5iDDvst4%2FaDZDoCEDjuf84QBY%3D",
            "coupon_url": {
                "pc": "https://r.gnavi.co.jp/1m6z2jy70000/coupon/",
                "mobile": "http://mobile.gnavi.co.jp/shop/gdpf900/coupon"
            },
            "image_url": {
                "shop_image1": "https://uds.gnst.jp/rest/img/1m6z2jy70000/t_0009.jpg",
                "shop_image2": {},
                "qrcode": "https://c-r.gnst.jp/tool/qr/?id=gdpf900&q=6"
            },
            "address": "〒150-0042 東京都渋谷区宇田川町12-7 渋谷エメラルドビル7F",
            "tel": "050-3477-2804",
            "tel_sub": "03-6706-4383",
            "fax": {},
            "opentime": " ランチ：12:00～17:00(ランチタイムは宴会・パーティーのみ受付ます。人数・ご予算などお気軽にご相談ください。)<BR>月～木・日 17:00～24:00(L.O.23:30)<BR>金・土・祝前日 17:00～翌5:00(L.O.4:30)(※17:00までのご来店は事前予約が必要となります。  ※お電話は10:00～24:00まで繋がります。)",
            "holiday": "無",
            "access": {
                "line": "ＪＲ",
                "station": "渋谷駅",
                "station_exit": {},
                "walk": "3",
                "note": {}
            },
            "parking_lots": {},
            "pr": {
                "pr_short": "渋谷駅2分！新年会団体予約まだまだ間に合います！ ★話題のチーズタッカルビ3H食べ放題！ ★豪華新年会！極上蟹鍋食べ放題4000円～ 最大100名様までの団体貸切OK！",
                "pr_long": "駅近にありながら落ち着ける大人の隠れ家居酒屋<BR>最大貸切100名様まで可能。新年会や宴会に最適！<BR>プロジェクター、マイクも完備しています。<BR>◆3h食べ放題付き贅沢宴会プラン◆<BR>・全10品『大山地鶏ちゃんこ鍋食べ放題コース』4480円⇒3480円<BR>・全10品『鹿児島県産黒豚しゃぶしゃぶ食べ放題コース』4980円⇒3980円<BR>・全11品『松坂牛のすき焼きコース』5980円⇒4980円<BR>・全11品『蟹・牡蠣入り海鮮寄せ鍋コース』7000円⇒6000円<BR>◆3hプレミアム飲み放題付◆<BR>・全12品『桔梗-KIKYOU-』5980円⇒4480円<BR>◆飲み放題＆食べ放題プラン◆<BR>・食べ放題＆飲み放題2.5h全10品『お手軽コース』 3480円⇒2480円<BR>・食べ放題＆飲み放題3h全40品『紺 -KON-コース』3500円 他<BR>◆お得に使えるクーポン多数◆<BR>・誕生日記念日特典!デザートプレートサービス<BR>・宴会特典!幹事様1名様無料"
            },
            "code": {
                "areacode": "AREA110",
                "areaname": "関東",
                "prefcode": "PREF13",
                "prefname": "東京都",
                "areacode_s": "AREAS2125",
                "areaname_s": "センター街・公園通り",
                "category_code_l": [
                    "RSFST02000",
                    {
                        "@attributes": {
                            "order": "1"
                        }
                    }
                ],
                "category_name_l": [
                    "日本料理・郷土料理",
                    {
                        "@attributes": {
                            "order": "1"
                        }
                    }
                ],
                "category_code_s": [
                    "RSFST06008",
                    {
                        "@attributes": {
                            "order": "1"
                        }
                    }
                ],
                "category_name_s": [
                    "しゃぶしゃぶ",
                    {
                        "@attributes": {
                            "order": "1"
                        }
                    }
                ]
            },
            "budget": "2500",
            "party": "2980",
            "lunch": "1980",
            "credit_card": "VISA,MasterCard,UC,DC,UFJ,ダイナースクラブ,アメリカン・エキスプレス,JCB,NICOS,アプラス,セゾン,J-DEBIT,MUFG",
            "e_money": {},
            "flags": {
                "mobile_site": "1",
                "mobile_coupon": "1",
                "pc_coupon": "1"
            }
        },
        """
        code = raw_dict.get('code')
        parsed_data = {
            'id': raw_dict.get('id'),
            'name': raw_dict.get('name'),
            'name_kana': raw_dict.get('name_kana'),
            'latitude': raw_dict.get('latitude'),
            'longitude': raw_dict.get('longitude'),
            'category': raw_dict.get('category'),
            'url': raw_dict.get('url'),
            'url_mobile': raw_dict.get('url_mobile'),
            'image_url_1': raw_dict.get('image_url').get('shop_image1'),
            'image_url_2': raw_dict.get('image_url').get('shop_image2'),
            'address': raw_dict.get('address'),
            'tel': raw_dict.get('tel'),
            'tel_sub': raw_dict.get('tel_sub'),
            'open_time': raw_dict.get('opentime'),
            'holiday': raw_dict.get('holiday'),
            'pr_short': raw_dict.get('pr').get('pr_short'),
            'pr_long': raw_dict.get('pr').get('pr_long'),
            'category_code_l': code.get('category_code_l')[0],
            'category_name_l': code.get('category_name_l')[0],
            'category_code_s': code.get('category_code_s')[0],
            'category_name_s': code.get('category_name_s')[0],
            'budget': raw_dict.get('budget'),
            'party': raw_dict.get('party'),
            'lunch': raw_dict.get('lunch'),
        }
        return cls(**parsed_data)

    def __str__(self):
        return 'Restaurant({},{},{})'.format(self.name, self.category, self.category_name_s)



class DbHelper:

    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite.connect(self.db_path)
        self.conn.row_factory = sqlite.Row

    def execute(self, sql, params=None):
        cur = self.conn.cursor()
        if params:
            return cur.execute(sql, params)
        else:
            return cur.execute(sql)

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()


class RescollePersist(DbHelper):

    def __init__(self, db_path):
        super().__init__(db_path)

        self.execute("""
        create table if not exist restaurants(
          
        
        
        
        
        )
        """)

    def save_restaurant(self, restaurant):
        """

        :param Restaurant restaurant:
        :return:
        """
