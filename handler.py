# -*- coding: utf-8 -*-

"""
<xml><appid><![CDATA[wx6cfba6aa09b9caf3]]></appid>
<bank_type><![CDATA[OTHERS]]></bank_type>
<cash_fee><![CDATA[1]]></cash_fee>
<fee_type><![CDATA[CNY]]></fee_type>
<is_subscribe><![CDATA[Y]]></is_subscribe>
<mch_id><![CDATA[1575279651]]></mch_id>
<nonce_str><![CDATA[jar4yk5t6wr8rfouen3zjcxhaolrois7]]></nonce_str>
<openid><![CDATA[oQ61n01gs3t34TglBy_x2U6l8VWk]]></openid>
<out_trade_no><![CDATA[d3i7sl76t3izxoyoyz0et2dvk8usxvbf]]></out_trade_no>
<result_code><![CDATA[SUCCESS]]></result_code>
<return_code><![CDATA[SUCCESS]]></return_code>
<sign><![CDATA[1A6A02E8CA43DC1AA5536EF731026442]]></sign>
<time_end><![CDATA[20200208153748]]></time_end>
<total_fee>1</total_fee>
<trade_type><![CDATA[JSAPI]]></trade_type>
<transaction_id><![CDATA[4200000508202002080724678605]]></transaction_id>
</xml>
"""


import web
import logging
import requests

class Handle(object):
    def GET(self):
        return "<xml><return_code><![CDATA[SUCCESS]]></return_code></xml>"


    def POST(self):

        data = web.data()  
        if len(data) != 0:
            res = requests.post('http://127.0.0.1:8080/xtcs/@@notify', data = {'xml':data})
        logging.warning('post request:%s' % res)

        if res.text == "ok":                   
            return "<xml><return_code><![CDATA[SUCCESS]]></return_code><return_msg><![CDATA[OK]]></return_msg></xml>"
        else:
            return "<xml><return_code><![CDATA[FAIL]]></return_code><return_msg><![CDATA[no]]></return_msg></xml>"
