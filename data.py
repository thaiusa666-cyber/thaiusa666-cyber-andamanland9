# -*- coding: utf-8 -*-
"""Site configuration, UI strings (EN/TH/ZH) and location data.

ทุกค่าที่เป็น [ADD ...] คือข้อมูลที่ยังไม่มีจริง ต้องกรอกก่อนเปิดใช้งานจริง
"""

# ---------------------------------------------------------------- site config
# แก้ BASE_URL เป็นโดเมนจริงก่อน deploy (ใช้ทำ canonical / hreflang / sitemap)
BASE_URL = "https://www.andamanland.site"  # [ADD DOMAIN]

SITE = {
    "brand": "ANDAMAN LAND",
    "brand_small": "by Benz Supawat",
    "legal_name": "Andaman Land by Benz Supawat",
    "agent": "Benz Supawat",
    "phone": "[065-426-2302]",
    "phone_href": "[065-426-2302]",          # e.g. +66654262302
    "whatsapp": "[66654262302]",         # e.g. 66654262302 (digits only)
    "line": "[@exodia789]",
    "line_url": "[@exodia789]",
    "email": "[benyakuza666@gmail.com]",
    "address": "[43/6 Moo3,soi thajeen,phuket,thailand]",
    "city": "Phuket",
    "region": "Phuket",
    "postal": "[83000]",
    "country": "TH",
    "hours": "[24hrs]",
    "gbp_url": "[https://share.google/DHtrGnOVtFRSS3CtX]",
    "facebook": "[ADD FACEBOOK URL]",
    "instagram": "[ADD INSTAGRAM URL]",
    "youtube": "[ADD YOUTUBE URL]",
    "tiktok": "[ADD TIKTOK URL]",
    "founded": "[ADD YEAR]",
    "form_endpoint": "",  # ว่าง = ใช้ Netlify Forms; หรือใส่ URL endpoint ของคุณ
    "ga4_id": "",         # e.g. G-XXXXXXXXXX
    "gsc_token": "",      # Google Search Console meta verification token
}

LANGS = ["en", "th", "zh"]
LANG_LABEL = {"en": "EN", "th": "TH", "zh": "中文"}
LANG_HTML = {"en": "en", "th": "th", "zh": "zh-Hans"}
HREFLANG = {"en": "en", "th": "th", "zh": "zh-Hans"}

TAGLINE = {
    "en": "Premium Land & Property Opportunities in Phuket, Thailand",
    "th": "ที่ดินและโอกาสการลงทุนอสังหาริมทรัพย์คุณภาพในภูเก็ต ประเทศไทย",
    "zh": "泰国普吉岛优质土地与房地产投资机会",
}

# ---------------------------------------------------------------- UI strings
T = {
    # navigation
    "nav_home": {"en": "Home", "th": "หน้าแรก", "zh": "首页"},
    "nav_properties": {"en": "Properties", "th": "ทรัพย์สิน", "zh": "房产"},
    "nav_land": {"en": "Land for Sale", "th": "ที่ดินขาย", "zh": "出售土地"},
    "nav_locations": {"en": "Locations", "th": "ทำเล", "zh": "地区"},
    "nav_investment": {"en": "Investment", "th": "การลงทุน", "zh": "投资"},
    "nav_guide": {"en": "Buying Guide", "th": "คู่มือผู้ซื้อ", "zh": "购买指南"},
    "nav_about": {"en": "About", "th": "เกี่ยวกับเรา", "zh": "关于我们"},
    "nav_contact": {"en": "Contact", "th": "ติดต่อ", "zh": "联系"},
    "nav_language": {"en": "Language", "th": "ภาษา", "zh": "语言"},
    "cta_contact": {"en": "Contact Benz", "th": "ติดต่อเบนซ์", "zh": "联系 Benz"},
    "menu": {"en": "Menu", "th": "เมนู", "zh": "菜单"},
    "close": {"en": "Close", "th": "ปิด", "zh": "关闭"},

    # hero
    "home_h1": {
        "en": "Land for Sale in Phuket, Thailand",
        "th": "ที่ดินขายในภูเก็ต ประเทศไทย",
        "zh": "泰国普吉岛土地出售",
    },
    "home_sub": {
        "en": "Discover land, development opportunities and property investment opportunities in Phuket.",
        "th": "ค้นหาที่ดิน โอกาสในการพัฒนาโครงการ และโอกาสลงทุนอสังหาริมทรัพย์ในภูเก็ต",
        "zh": "探索普吉岛的土地、开发项目与房地产投资机会。",
    },
    "btn_view_land": {"en": "View land for sale", "th": "ดูที่ดินขาย", "zh": "查看出售土地"},

    # search
    "search_title": {"en": "Find land", "th": "ค้นหาที่ดิน", "zh": "查找土地"},
    "f_location": {"en": "Location", "th": "ทำเล", "zh": "地区"},
    "f_type": {"en": "Property type", "th": "ประเภททรัพย์สิน", "zh": "房产类型"},
    "f_price": {"en": "Price", "th": "ราคา", "zh": "价格"},
    "f_size": {"en": "Land size", "th": "ขนาดที่ดิน", "zh": "土地面积"},
    "f_any": {"en": "Any", "th": "ทั้งหมด", "zh": "不限"},
    "btn_search": {"en": "Search properties", "th": "ค้นหาทรัพย์สิน", "zh": "搜索房产"},
    "btn_reset": {"en": "Clear filters", "th": "ล้างตัวกรอง", "zh": "清除筛选"},
    "sort_by": {"en": "Sort by", "th": "เรียงตาม", "zh": "排序"},
    "sort_newest": {"en": "Newest", "th": "ใหม่ล่าสุด", "zh": "最新"},
    "sort_price_asc": {"en": "Price: low to high", "th": "ราคา: ต่ำไปสูง", "zh": "价格：由低到高"},
    "sort_price_desc": {"en": "Price: high to low", "th": "ราคา: สูงไปต่ำ", "zh": "价格：由高到低"},
    "sort_size": {"en": "Land size", "th": "ขนาดที่ดิน", "zh": "土地面积"},
    "results": {"en": "listings shown", "th": "รายการที่แสดง", "zh": "个房源"},
    "no_results": {
        "en": "No listings match these filters. Clear the filters, or send Benz your requirements and he will source matching land.",
        "th": "ไม่พบรายการที่ตรงกับตัวกรองนี้ ลองล้างตัวกรอง หรือส่งความต้องการของคุณมา แล้วเบนซ์จะหาที่ดินที่ตรงให้",
        "zh": "没有符合条件的房源。请清除筛选条件，或把您的需求发给 Benz，由他为您寻找合适的土地。",
    },

    # status
    "st_for-sale": {"en": "For sale", "th": "ขาย", "zh": "出售中"},
    "st_reserved": {"en": "Reserved", "th": "จองแล้ว", "zh": "已预订"},
    "st_sold": {"en": "Sold", "th": "ขายแล้ว", "zh": "已售出"},
    "st_off-market": {"en": "Off market", "th": "ไม่อยู่ในตลาด", "zh": "已下架"},
    "sold_notice": {
        "en": "This land has been sold. The page is kept for reference. Ask Benz about similar land in the same area.",
        "th": "ที่ดินแปลงนี้ขายแล้ว หน้านี้เก็บไว้เพื่อการอ้างอิง สอบถามเบนซ์เกี่ยวกับที่ดินลักษณะเดียวกันในทำเลใกล้เคียงได้",
        "zh": "该地块已售出。此页面保留供参考。可向 Benz 咨询同区域的类似地块。",
    },

    # property fields
    "p_id": {"en": "Property ID", "th": "รหัสทรัพย์สิน", "zh": "房源编号"},
    "p_price": {"en": "Price", "th": "ราคา", "zh": "价格"},
    "p_size": {"en": "Land size", "th": "ขนาดที่ดิน", "zh": "土地面积"},
    "p_rai": {"en": "Rai", "th": "ไร่", "zh": "莱"},
    "p_ngan": {"en": "Ngan", "th": "งาน", "zh": "颜"},
    "p_wah": {"en": "Square wah", "th": "ตารางวา", "zh": "平方哇"},
    "p_sqm": {"en": "Square metres", "th": "ตารางเมตร", "zh": "平方米"},
    "p_location": {"en": "Location", "th": "ทำเล", "zh": "位置"},
    "p_district": {"en": "District", "th": "อำเภอ", "zh": "区"},
    "p_province": {"en": "Province", "th": "จังหวัด", "zh": "府"},
    "p_type": {"en": "Property type", "th": "ประเภททรัพย์สิน", "zh": "房产类型"},
    "p_title_deed": {"en": "Land title document", "th": "เอกสารสิทธิ์ที่ดิน", "zh": "土地权属文件"},
    "p_gps": {"en": "GPS coordinates", "th": "พิกัด GPS", "zh": "GPS 坐标"},
    "p_road": {"en": "Road access", "th": "ทางเข้า-ออก", "zh": "道路通行"},
    "p_electricity": {"en": "Electricity", "th": "ไฟฟ้า", "zh": "电力"},
    "p_water": {"en": "Water", "th": "น้ำ", "zh": "供水"},
    "p_zoning": {"en": "Zoning / colour", "th": "ผังสี / การใช้ประโยชน์", "zh": "用地规划"},
    "p_overview": {"en": "Overview", "th": "ภาพรวม", "zh": "概览"},
    "p_key_facts": {"en": "Key facts", "th": "ข้อมูลสำคัญ", "zh": "关键信息"},
    "p_utilities": {"en": "Access & utilities", "th": "การเข้าถึงและสาธารณูปโภค", "zh": "通路与配套"},
    "p_nearby": {"en": "Nearby", "th": "สถานที่ใกล้เคียง", "zh": "周边"},
    "p_dist_airport": {"en": "Distance to airport", "th": "ระยะถึงสนามบิน", "zh": "距机场"},
    "p_dist_beach": {"en": "Distance to beach", "th": "ระยะถึงชายหาด", "zh": "距海滩"},
    "p_dist_attr": {"en": "Distance to main attractions", "th": "ระยะถึงสถานที่สำคัญ", "zh": "距主要景点"},
    "p_potential": {"en": "Development potential", "th": "ศักยภาพในการพัฒนา", "zh": "开发潜力"},
    "p_gallery": {"en": "Photo gallery", "th": "แกลเลอรีภาพ", "zh": "图片"},
    "p_video": {"en": "Video", "th": "วิดีโอ", "zh": "视频"},
    "p_map": {"en": "Map", "th": "แผนที่", "zh": "地图"},
    "p_open_maps": {"en": "Open in Google Maps", "th": "เปิดใน Google Maps", "zh": "在 Google 地图中打开"},
    "p_agent": {"en": "Your agent", "th": "ผู้ดูแลทรัพย์สิน", "zh": "您的经纪人"},
    "p_similar": {"en": "Similar land", "th": "ที่ดินใกล้เคียง", "zh": "类似地块"},
    "p_ref": {"en": "Ref", "th": "รหัส", "zh": "编号"},

    # buttons
    "btn_details": {"en": "Request property details", "th": "ขอรายละเอียดทรัพย์สิน", "zh": "索取房源资料"},
    "btn_info": {"en": "Request property information", "th": "ขอข้อมูลทรัพย์สิน", "zh": "索取房源信息"},
    "btn_viewing": {"en": "Book a viewing", "th": "นัดดูที่ดิน", "zh": "预约看地"},
    "btn_call": {"en": "Call now", "th": "โทรเลย", "zh": "立即致电"},
    "btn_whatsapp": {"en": "WhatsApp", "th": "WhatsApp", "zh": "WhatsApp"},
    "btn_line": {"en": "LINE", "th": "LINE", "zh": "LINE"},
    "btn_email": {"en": "Email", "th": "อีเมล", "zh": "电邮"},
    "btn_send": {"en": "Send inquiry", "th": "ส่งข้อความ", "zh": "发送咨询"},
    "btn_view": {"en": "View details", "th": "ดูรายละเอียด", "zh": "查看详情"},
    "btn_all_land": {"en": "See all land for sale", "th": "ดูที่ดินขายทั้งหมด", "zh": "查看全部土地"},
    "btn_read": {"en": "Read guide", "th": "อ่านคู่มือ", "zh": "阅读指南"},

    # lead form
    "lead_title": {"en": "Interested in this property?", "th": "สนใจทรัพย์สินนี้ใช่ไหม", "zh": "对这块地感兴趣？"},
    "lead_sub": {
        "en": "Send your details and Benz will reply with the full information pack, including title documents available for this plot.",
        "th": "กรอกข้อมูลของคุณ แล้วเบนซ์จะส่งชุดข้อมูลฉบับเต็มกลับไป รวมถึงเอกสารสิทธิ์ที่มีของแปลงนี้",
        "zh": "留下您的联系方式，Benz 将把完整资料发送给您，包括该地块可提供的权属文件。",
    },
    "fm_name": {"en": "Name", "th": "ชื่อ", "zh": "姓名"},
    "fm_nationality": {"en": "Nationality", "th": "สัญชาติ", "zh": "国籍"},
    "fm_email": {"en": "Email", "th": "อีเมล", "zh": "电子邮箱"},
    "fm_phone": {"en": "Phone", "th": "โทรศัพท์", "zh": "电话"},
    "fm_whatsapp": {"en": "WhatsApp", "th": "WhatsApp", "zh": "WhatsApp"},
    "fm_line": {"en": "LINE ID", "th": "LINE ID", "zh": "LINE ID"},
    "fm_pref": {"en": "Preferred contact method", "th": "ช่องทางที่สะดวกให้ติดต่อ", "zh": "首选联系方式"},
    "fm_property": {"en": "Property ID", "th": "รหัสทรัพย์สิน", "zh": "房源编号"},
    "fm_message": {"en": "Message", "th": "ข้อความ", "zh": "留言"},
    "fm_optional": {"en": "optional", "th": "ไม่บังคับ", "zh": "选填"},
    "fm_sending": {"en": "Sending…", "th": "กำลังส่ง…", "zh": "发送中…"},
    "fm_ok": {
        "en": "Thank you. Your enquiry has been sent. Benz will reply within one working day.",
        "th": "ขอบคุณครับ ส่งข้อความเรียบร้อย เบนซ์จะติดต่อกลับภายใน 1 วันทำการ",
        "zh": "谢谢。您的咨询已发送，Benz 将在一个工作日内回复。",
    },
    "fm_fail": {
        "en": "The form could not be sent. Message Benz directly on WhatsApp or by email instead.",
        "th": "ส่งฟอร์มไม่สำเร็จ กรุณาติดต่อเบนซ์ทาง WhatsApp หรืออีเมลโดยตรง",
        "zh": "表单发送失败。请直接通过 WhatsApp 或电邮联系 Benz。",
    },
    "fm_err_name": {"en": "Enter your name.", "th": "กรุณากรอกชื่อ", "zh": "请填写姓名。"},
    "fm_err_email": {"en": "Enter a valid email address.", "th": "กรุณากรอกอีเมลให้ถูกต้อง", "zh": "请输入有效的电子邮箱。"},
    "fm_err_contact": {
        "en": "Add a phone, WhatsApp or LINE so Benz can reach you.",
        "th": "กรุณาระบุเบอร์โทร WhatsApp หรือ LINE เพื่อให้ติดต่อกลับได้",
        "zh": "请留下电话、WhatsApp 或 LINE，以便与您联系。",
    },
    "fm_err_message": {"en": "Tell Benz what you are looking for.", "th": "กรุณาระบุสิ่งที่คุณกำลังมองหา", "zh": "请说明您的需求。"},
    "fm_wait": {
        "en": "One enquiry per minute. Please wait a moment before sending again.",
        "th": "ส่งได้ 1 ครั้งต่อนาที กรุณารอสักครู่ก่อนส่งใหม่",
        "zh": "每分钟限发送一次，请稍候再试。",
    },

    # sections
    "sec_featured": {"en": "Featured land", "th": "ที่ดินแนะนำ", "zh": "精选地块"},
    "sec_locations": {"en": "Phuket by area", "th": "ทำเลในภูเก็ต", "zh": "普吉分区"},
    "sec_services": {"en": "How Benz works with buyers", "th": "เบนซ์ทำงานกับผู้ซื้ออย่างไร", "zh": "Benz 如何协助买家"},
    "sec_invest": {"en": "Investment opportunities", "th": "โอกาสการลงทุน", "zh": "投资机会"},
    "sec_guide": {"en": "Before you buy", "th": "ก่อนตัดสินใจซื้อ", "zh": "购买前须知"},
    "sec_faq": {"en": "Frequently asked questions", "th": "คำถามที่พบบ่อย", "zh": "常见问题"},
    "sec_available": {"en": "Available land in this area", "th": "ที่ดินที่มีในทำเลนี้", "zh": "本区域在售地块"},
    "sec_related": {"en": "Related guides", "th": "คู่มือที่เกี่ยวข้อง", "zh": "相关指南"},
    "sec_nearby_attr": {"en": "Nearby attractions", "th": "สถานที่ใกล้เคียง", "zh": "周边景点"},
    "sec_typical": {"en": "What land here typically looks like", "th": "ลักษณะที่ดินโดยทั่วไปในทำเลนี้", "zh": "该区域土地的一般特征"},

    # footer / legal
    "quick_links": {"en": "Quick links", "th": "ลิงก์ด่วน", "zh": "快速链接"},
    "contact_us": {"en": "Contact", "th": "ติดต่อ", "zh": "联系"},
    "follow": {"en": "Social media", "th": "โซเชียลมีเดีย", "zh": "社交媒体"},
    "legal": {"en": "Legal", "th": "ข้อกฎหมาย", "zh": "法律"},
    "legal_disclaimer": {"en": "Legal disclaimer", "th": "ข้อจำกัดความรับผิดชอบ", "zh": "免责声明"},
    "privacy": {"en": "Privacy policy", "th": "นโยบายความเป็นส่วนตัว", "zh": "隐私政策"},
    "terms": {"en": "Terms of use", "th": "เงื่อนไขการใช้งาน", "zh": "使用条款"},
    "cookies": {"en": "Cookie policy", "th": "นโยบายคุกกี้", "zh": "Cookie 政策"},
    "rights": {"en": "All rights reserved.", "th": "สงวนลิขสิทธิ์", "zh": "版权所有。"},
    "breadcrumb": {"en": "Breadcrumb", "th": "เส้นทางหน้า", "zh": "面包屑导航"},
    "disclaimer_short": {
        "en": "Information on this website is provided for general guidance only and is not legal, tax or investment advice. Foreign ownership of land in Thailand is restricted by law. Always take independent advice from a licensed Thai lawyer before signing or paying anything.",
        "th": "ข้อมูลบนเว็บไซต์นี้เป็นข้อมูลทั่วไปเพื่อประกอบการพิจารณาเท่านั้น ไม่ถือเป็นคำแนะนำทางกฎหมาย ภาษี หรือการลงทุน การถือครองที่ดินของชาวต่างชาติในประเทศไทยมีข้อจำกัดตามกฎหมาย กรุณาปรึกษาทนายความไทยที่ได้รับใบอนุญาตก่อนลงนามหรือชำระเงินใด ๆ",
        "zh": "本网站信息仅供一般参考，不构成法律、税务或投资建议。外国人在泰国持有土地受法律限制。在签署任何文件或付款前，请务必咨询持牌泰国律师。",
    },
    "placeholder_note": {
        "en": "Sample entry. Replace with a real listing before publishing — no price, size or coordinates have been invented.",
        "th": "รายการตัวอย่าง กรุณาแทนที่ด้วยประกาศจริงก่อนเผยแพร่ — ไม่มีการสร้างราคา ขนาด หรือพิกัดปลอม",
        "zh": "示例条目。发布前请替换为真实房源——价格、面积与坐标均未虚构。",
    },
    "todo_banner": {
        "en": "Setup checklist: contact details, listings and analytics IDs still contain placeholders.",
        "th": "เช็กลิสต์ตั้งค่า: ข้อมูลติดต่อ ประกาศ และรหัส analytics ยังเป็น placeholder",
        "zh": "设置清单：联系方式、房源与分析 ID 仍为占位内容。",
    },
    "all_locations": {"en": "All areas", "th": "ทุกทำเล", "zh": "全部地区"},
    "read_more": {"en": "Read", "th": "อ่านต่อ", "zh": "阅读"},
    "updated": {"en": "Updated", "th": "อัปเดต", "zh": "更新"},
    "back_to_guides": {"en": "All buying guides", "th": "คู่มือผู้ซื้อทั้งหมด", "zh": "全部购买指南"},
}


def t(key, lang):
    return T[key][lang]


# ---------------------------------------------------------------- taxonomies
LOCATION_ORDER = ["phuket", "thalang", "cherng-talay", "bang-tao", "kamala",
                  "rawai", "nai-harn", "kata", "karon", "phuket-town", "other"]

LOCATION_NAMES = {
    "phuket": {"en": "Phuket", "th": "ภูเก็ต", "zh": "普吉岛"},
    "thalang": {"en": "Thalang", "th": "ถลาง", "zh": "他朗"},
    "cherng-talay": {"en": "Cherng Talay", "th": "เชิงทะเล", "zh": "青塔莱"},
    "bang-tao": {"en": "Bang Tao", "th": "บางเทา", "zh": "邦涛"},
    "kamala": {"en": "Kamala", "th": "กมลา", "zh": "卡马拉"},
    "rawai": {"en": "Rawai", "th": "ราไวย์", "zh": "拉威"},
    "nai-harn": {"en": "Nai Harn", "th": "ในหาน", "zh": "奈汉"},
    "kata": {"en": "Kata", "th": "กะตะ", "zh": "卡塔"},
    "karon": {"en": "Karon", "th": "กะรน", "zh": "卡伦"},
    "phuket-town": {"en": "Phuket Town", "th": "เมืองภูเก็ต", "zh": "普吉镇"},
    "other": {"en": "Other areas", "th": "ทำเลอื่น ๆ", "zh": "其他地区"},
}

# ทำเลที่มีหน้า SEO ของตัวเอง
LOCATION_PAGES = ["phuket", "thalang", "cherng-talay", "bang-tao", "kamala",
                  "rawai", "nai-harn", "kata", "karon"]

TYPE_ORDER = ["land", "development-land", "beachfront-land", "investment-land", "commercial-land"]

TYPE_NAMES = {
    "land": {"en": "Land", "th": "ที่ดิน", "zh": "土地"},
    "development-land": {"en": "Development land", "th": "ที่ดินเพื่อพัฒนาโครงการ", "zh": "开发用地"},
    "beachfront-land": {"en": "Beachfront land", "th": "ที่ดินติดหาด", "zh": "海滨土地"},
    "investment-land": {"en": "Investment land", "th": "ที่ดินเพื่อการลงทุน", "zh": "投资用地"},
    "commercial-land": {"en": "Commercial land", "th": "ที่ดินเชิงพาณิชย์", "zh": "商业用地"},
}

PRICE_BANDS = [
    ("0-10", {"en": "Under ฿10M", "th": "ต่ำกว่า 10 ล้านบาท", "zh": "1,000 万泰铢以下"}, 0, 10_000_000),
    ("10-30", {"en": "฿10M – ฿30M", "th": "10–30 ล้านบาท", "zh": "1,000 万 – 3,000 万泰铢"}, 10_000_000, 30_000_000),
    ("30-60", {"en": "฿30M – ฿60M", "th": "30–60 ล้านบาท", "zh": "3,000 万 – 6,000 万泰铢"}, 30_000_000, 60_000_000),
    ("60-100", {"en": "฿60M – ฿100M", "th": "60–100 ล้านบาท", "zh": "6,000 万 – 1 亿泰铢"}, 60_000_000, 100_000_000),
    ("100+", {"en": "฿100M and above", "th": "100 ล้านบาทขึ้นไป", "zh": "1 亿泰铢以上"}, 100_000_000, 10**12),
]

SIZE_BANDS = [
    ("0-1", {"en": "Under 1 rai", "th": "ต่ำกว่า 1 ไร่", "zh": "1 莱以下"}, 0, 1),
    ("1-3", {"en": "1 – 3 rai", "th": "1–3 ไร่", "zh": "1 – 3 莱"}, 1, 3),
    ("3-10", {"en": "3 – 10 rai", "th": "3–10 ไร่", "zh": "3 – 10 莱"}, 3, 10),
    ("10-50", {"en": "10 – 50 rai", "th": "10–50 ไร่", "zh": "10 – 50 莱"}, 10, 50),
    ("50+", {"en": "50 rai and above", "th": "50 ไร่ขึ้นไป", "zh": "50 莱以上"}, 50, 10**6),
]
