# -*- coding: utf-8 -*-
"""Editorial copy for location pages, investment page, about page and home sections."""

# ---------------------------------------------------------------- locations
# key: slug -> per language: intro (list of paragraphs), typical (str),
# nearby (list), faq (list of [q, a])
LOCATION_COPY = {
"phuket": {
 "en": {
  "intro": [
   "Phuket is Thailand's largest island and its most established international property market, with an airport, international schools, hospitals and marinas serving residents and visitors all year round.",
   "Land here ranges from small residential plots inland to large development parcels on the west coast. What a plot can be used for depends on its title document, its zoning colour under the Phuket town plan, its slope and its road access — which is why every plot needs to be checked individually."],
  "typical": "Plots are usually measured in rai, ngan and square wah. West coast and sea-view land trades at a premium; inland plots in Thalang and around Phuket Town are generally the entry point for buyers with a development budget.",
  "nearby": ["Phuket International Airport", "Patong, Kamala and Bang Tao beaches", "Marinas on the east coast", "International schools and private hospitals"],
  "faq": [
   ["Can a foreigner own land in Phuket?", "Thai law restricts land ownership by foreign individuals. Structures such as long leases, Thai company ownership and condominium freehold are used in practice, and each has legal and tax consequences. Take advice from a licensed Thai lawyer before you commit to any structure."],
   ["What size of plot do I need for a villa?", "It depends on the design, setbacks and slope. Benz can show you plots that suit a single villa as well as parcels large enough for a small villa estate."],
   ["How do I view land?", "Send an enquiry with the property ID or your requirements, and Benz will arrange a site visit and share the available title information."]]},
 "th": {
  "intro": [
   "ภูเก็ตเป็นเกาะที่ใหญ่ที่สุดของไทยและเป็นตลาดอสังหาริมทรัพย์ระดับนานาชาติที่มีความพร้อมมากที่สุด ทั้งสนามบิน โรงเรียนนานาชาติ โรงพยาบาล และมารีน่า ที่รองรับผู้อยู่อาศัยและนักท่องเที่ยวตลอดทั้งปี",
   "ที่ดินมีตั้งแต่แปลงเล็กสำหรับที่อยู่อาศัยในฝั่งในเกาะ ไปจนถึงแปลงใหญ่เพื่อพัฒนาโครงการทางฝั่งตะวันตก การใช้ประโยชน์ขึ้นอยู่กับเอกสารสิทธิ์ ผังสีตามผังเมืองภูเก็ต ความลาดชัน และทางเข้า-ออก จึงต้องตรวจสอบเป็นรายแปลง"],
  "typical": "ที่ดินวัดเป็นไร่ งาน ตารางวา ทำเลฝั่งตะวันตกและแปลงวิวทะเลมีราคาสูงกว่า ส่วนแปลงฝั่งในเกาะแถบถลางและรอบเมืองภูเก็ตมักเป็นจุดเริ่มต้นสำหรับผู้ซื้อที่มีงบพัฒนาโครงการ",
  "nearby": ["ท่าอากาศยานนานาชาติภูเก็ต", "หาดป่าตอง กมลา และบางเทา", "มารีน่าฝั่งตะวันออก", "โรงเรียนนานาชาติและโรงพยาบาลเอกชน"],
  "faq": [
   ["ชาวต่างชาติถือครองที่ดินในภูเก็ตได้หรือไม่", "กฎหมายไทยจำกัดการถือครองที่ดินของบุคคลต่างชาติ ในทางปฏิบัติมีโครงสร้างเช่น สัญญาเช่าระยะยาว การถือผ่านบริษัทไทย หรือการซื้อคอนโดแบบ freehold ซึ่งแต่ละแบบมีผลทางกฎหมายและภาษีต่างกัน ควรปรึกษาทนายความไทยที่มีใบอนุญาตก่อนตัดสินใจ"],
   ["ต้องใช้ที่ดินขนาดเท่าไรในการสร้างวิลล่า", "ขึ้นอยู่กับแบบบ้าน ระยะร่น และความลาดชันของที่ดิน เบนซ์สามารถเสนอทั้งแปลงสำหรับวิลล่าหลังเดียวและแปลงใหญ่สำหรับโครงการวิลล่าขนาดเล็ก"],
   ["ขอเข้าดูที่ดินอย่างไร", "ส่งข้อความพร้อมรหัสทรัพย์สินหรือความต้องการของคุณ เบนซ์จะนัดหมายลงพื้นที่และส่งข้อมูลเอกสารสิทธิ์เท่าที่มีให้"]]},
 "zh": {
  "intro": [
   "普吉岛是泰国最大的岛屿，也是最成熟的国际房地产市场，拥有机场、国际学校、医院和游艇码头，全年服务居民与访客。",
   "岛上土地从内陆小型住宅地块到西海岸大型开发用地都有。可开发用途取决于权属文件、普吉城市规划中的用地颜色、坡度以及道路通行条件，因此每一块地都需要单独核实。"],
  "typical": "土地以莱、颜、平方哇计量。西海岸及海景地块价格较高；他朗与普吉镇周边的内陆地块通常是开发预算买家的入门选择。",
  "nearby": ["普吉国际机场", "芭东、卡马拉与邦涛海滩", "东海岸游艇码头", "国际学校与私立医院"],
  "faq": [
   ["外国人可以在普吉拥有土地吗？", "泰国法律限制外国自然人持有土地。实务中常见长期租赁、泰国公司持有、公寓永久产权等方式，各有不同的法律与税务后果。作出决定前请咨询持牌泰国律师。"],
   ["建一栋别墅需要多大的地？", "取决于设计、退缩距离与地形坡度。Benz 可以提供适合单栋别墅的地块，也有足够开发小型别墅社区的大地块。"],
   ["如何实地看地？", "发送咨询并附上房源编号或您的需求，Benz 会安排实地考察并提供现有的权属资料。"]]}},

"thalang": {
 "en": {
  "intro": [
   "Thalang is the largest district in the north of Phuket and covers the area around the airport, Mai Khao, Thep Krasattri and the inland roads towards Cherng Talay.",
   "It is where much of the island's remaining large land supply sits, which makes it the district buyers look at first for villa estates, resorts and mixed-use projects."],
  "typical": "Larger parcels, flatter ground than the west coast hillsides, and a mix of agricultural and residential zoning. Title documents vary widely between plots, so due diligence matters here more than anywhere.",
  "nearby": ["Phuket International Airport", "Mai Khao and Nai Yang beaches", "Thalang National Museum and Heroines Monument", "Main road links to Cherng Talay and Phuket Town"],
  "faq": [
   ["Why do developers look at Thalang?", "Because large, relatively flat parcels are still available and the airport is in the district, which suits resort and residential projects that rely on arrivals."],
   ["Is all land in Thalang buildable?", "No. Zoning colour, title type and access all restrict what can be built. Each plot must be checked before any agreement is signed."],
   ["Does Benz have land in Thalang?", "Listings are added as they are verified. Send your requirements and Benz will tell you what is currently available."]]},
 "th": {
  "intro": [
   "ถลางเป็นอำเภอที่ใหญ่ที่สุดทางตอนเหนือของภูเก็ต ครอบคลุมพื้นที่รอบสนามบิน ไม้ขาว เทพกระษัตรี และถนนฝั่งในเกาะที่เชื่อมไปเชิงทะเล",
   "เป็นพื้นที่ที่ยังมีที่ดินแปลงใหญ่เหลืออยู่มากที่สุดของเกาะ จึงเป็นทำเลแรกที่ผู้ซื้อมองหาเมื่อต้องการทำโครงการวิลล่า รีสอร์ต หรือโครงการผสม"],
  "typical": "แปลงใหญ่ พื้นที่ราบมากกว่าเนินเขาฝั่งตะวันตก และมีทั้งผังเกษตรกรรมและที่อยู่อาศัย เอกสารสิทธิ์แตกต่างกันมากในแต่ละแปลง การตรวจสอบจึงสำคัญเป็นพิเศษ",
  "nearby": ["ท่าอากาศยานนานาชาติภูเก็ต", "หาดไม้ขาวและหาดในยาง", "พิพิธภัณฑสถานแห่งชาติถลางและอนุสาวรีย์ท้าวเทพกระษัตรี", "ถนนสายหลักเชื่อมเชิงทะเลและเมืองภูเก็ต"],
  "faq": [
   ["ทำไมผู้พัฒนาโครงการจึงสนใจถลาง", "เพราะยังมีที่ดินแปลงใหญ่และค่อนข้างราบ อีกทั้งสนามบินอยู่ในอำเภอนี้ จึงเหมาะกับโครงการรีสอร์ตและที่อยู่อาศัยที่พึ่งพานักเดินทาง"],
   ["ที่ดินในถลางสร้างได้ทุกแปลงหรือไม่", "ไม่ใช่ ผังสี ประเภทเอกสารสิทธิ์ และทางเข้า-ออก ล้วนมีผลต่อสิ่งที่สร้างได้ ต้องตรวจสอบรายแปลงก่อนทำสัญญา"],
   ["เบนซ์มีที่ดินในถลางไหม", "ประกาศจะถูกเพิ่มเมื่อตรวจสอบข้อมูลแล้ว ส่งความต้องการของคุณมา เบนซ์จะแจ้งว่ามีแปลงใดพร้อมขายในขณะนี้"]]},
 "zh": {
  "intro": [
   "他朗是普吉北部面积最大的区，涵盖机场周边、迈考、塔克拉塔里以及通往青塔莱的内陆道路一带。",
   "岛上剩余的大面积土地多集中于此，因此别墅社区、度假村与综合项目的买家通常首先考察该区。"],
  "typical": "地块面积较大、地势比西海岸山坡平缓，规划用途既有农业也有住宅。各地块权属文件差异很大，尽职调查在此尤为重要。",
  "nearby": ["普吉国际机场", "迈考海滩与奈扬海滩", "他朗国家博物馆与英雄纪念碑", "通往青塔莱与普吉镇的主干道"],
  "faq": [
   ["开发商为什么关注他朗？", "因为这里仍有面积较大、地势相对平坦的地块，且机场位于该区，适合依赖客流的度假与住宅项目。"],
   ["他朗的土地都能建房吗？", "并非如此。用地颜色、权属类型与通路条件都会限制建设内容，签约前必须逐块核实。"],
   ["Benz 有他朗的土地吗？", "房源会在核实后陆续上架。请发送您的需求，Benz 会告知目前可供选择的地块。"]]}},

"cherng-talay": {
 "en": {
  "intro": [
   "Cherng Talay is the sub-district behind Bang Tao and Layan on Phuket's north-west coast, and one of the island's most active areas for new residential development.",
   "It combines beach access with established services: international schools, supermarkets, restaurants and a large expatriate community."],
  "typical": "A mix of mid-size residential plots and larger parcels set back from the beach road. Sea-view land is limited and priced accordingly; plots inland are generally where villa projects are built.",
  "nearby": ["Bang Tao and Layan beaches", "Laguna Phuket area", "International schools", "Boat Avenue and Porto de Phuket shopping"],
  "faq": [
   ["Why is Cherng Talay popular with foreign buyers?", "Because daily life works here without a long drive — schools, shops, clinics and beaches are all close, which supports both residence and rental demand."],
   ["Is beachfront land available?", "Genuine beachfront plots are rare and tightly held. Benz will tell you honestly whether anything is available rather than advertising plots that are not."],
   ["What about access roads?", "Access can be private or shared, and this affects value and buildability. It is one of the first things checked on any plot."]]},
 "th": {
  "intro": [
   "เชิงทะเลเป็นตำบลด้านหลังหาดบางเทาและลายัน ทางฝั่งตะวันตกเฉียงเหนือของภูเก็ต และเป็นหนึ่งในพื้นที่ที่มีการพัฒนาที่อยู่อาศัยใหม่มากที่สุดของเกาะ",
   "จุดเด่นคือเข้าถึงชายหาดได้ง่ายพร้อมสิ่งอำนวยความสะดวกครบ ทั้งโรงเรียนนานาชาติ ซูเปอร์มาร์เก็ต ร้านอาหาร และชุมชนชาวต่างชาติขนาดใหญ่"],
  "typical": "มีทั้งแปลงขนาดกลางสำหรับที่อยู่อาศัยและแปลงใหญ่ที่ถัดจากถนนเลียบหาดเข้ามา ที่ดินวิวทะเลมีจำกัดและราคาสูง ส่วนแปลงฝั่งในมักเป็นที่ตั้งของโครงการวิลล่า",
  "nearby": ["หาดบางเทาและหาดลายัน", "พื้นที่ลากูน่าภูเก็ต", "โรงเรียนนานาชาติ", "Boat Avenue และ Porto de Phuket"],
  "faq": [
   ["ทำไมชาวต่างชาตินิยมเชิงทะเล", "เพราะใช้ชีวิตประจำวันได้โดยไม่ต้องขับรถไกล ทั้งโรงเรียน ร้านค้า คลินิก และชายหาดอยู่ใกล้ ซึ่งส่งผลดีทั้งการอยู่อาศัยและความต้องการเช่า"],
   ["มีที่ดินติดหาดขายไหม", "แปลงติดหาดจริงมีน้อยมากและมักไม่เปลี่ยนมือ เบนซ์จะแจ้งตามความเป็นจริงว่ามีหรือไม่ ไม่โฆษณาแปลงที่ไม่มีอยู่จริง"],
   ["เรื่องทางเข้า-ออกเป็นอย่างไร", "ทางเข้าอาจเป็นทางส่วนบุคคลหรือทางร่วม ซึ่งมีผลต่อมูลค่าและการก่อสร้าง เป็นสิ่งแรก ๆ ที่ต้องตรวจสอบทุกแปลง"]]},
 "zh": {
  "intro": [
   "青塔莱位于普吉西北海岸邦涛与拉扬海滩后方，是全岛新建住宅开发最活跃的区域之一。",
   "这里既靠近海滩，配套也成熟：国际学校、超市、餐厅以及规模可观的外籍居民社区。"],
  "typical": "既有中等面积的住宅地块，也有离海滨道路稍远的大地块。海景地供应有限、价格较高；别墅项目多建在内陆一侧。",
  "nearby": ["邦涛海滩与拉扬海滩", "普吉乐古浪区域", "国际学校", "Boat Avenue 与 Porto de Phuket 商业区"],
  "faq": [
   ["为什么外国买家偏好青塔莱？", "因为日常生活无需长途驾车——学校、商店、诊所与海滩都在附近，既适合自住也支撑租赁需求。"],
   ["有海滨土地出售吗？", "真正的海滨地块极为稀少且少有转手。Benz 会如实告知是否有货，不会宣传并不存在的地块。"],
   ["通路情况如何？", "通路可能是私人道路或共用道路，这会影响价值与可建性，也是每块地最先核查的内容之一。"]]}},

"bang-tao": {
 "en": {
  "intro": [
   "Bang Tao is a long beach on the north-west coast, known for resorts, beach clubs and a steady stream of new residential projects behind the beach road.",
   "Buyer interest here is usually driven by rental demand and resale liquidity rather than by price alone."],
  "typical": "Plots close to the beach are small and expensive; the larger parcels sit further back towards the main road and the hills behind.",
  "nearby": ["Bang Tao beach and beach clubs", "Laguna Phuket", "Boat Avenue", "Road link north towards the airport"],
  "faq": [
   ["Is Bang Tao a good area for a villa project?", "It is one of the most actively developed areas on the island. Whether a specific plot works depends on its size, access and zoning."],
   ["How close to the beach can I build?", "Building near the shoreline is subject to Thai regulations on setbacks and building height. A licensed architect and lawyer should confirm this for any specific plot."],
   ["Are there off-market plots?", "Some owners prefer not to advertise. Tell Benz what you are looking for and he will check what is quietly available."]]},
 "th": {
  "intro": [
   "บางเทาเป็นหาดยาวทางฝั่งตะวันตกเฉียงเหนือ มีรีสอร์ต บีชคลับ และโครงการที่อยู่อาศัยใหม่เกิดขึ้นต่อเนื่องด้านหลังถนนเลียบหาด",
   "ความสนใจของผู้ซื้อในทำเลนี้มักมาจากความต้องการเช่าและสภาพคล่องในการขายต่อ มากกว่าเรื่องราคาเพียงอย่างเดียว"],
  "typical": "แปลงใกล้หาดมีขนาดเล็กและราคาสูง ส่วนแปลงใหญ่จะอยู่ถัดเข้าไปทางถนนสายหลักและเนินเขาด้านหลัง",
  "nearby": ["หาดบางเทาและบีชคลับ", "ลากูน่าภูเก็ต", "Boat Avenue", "เส้นทางขึ้นเหนือสู่สนามบิน"],
  "faq": [
   ["บางเทาเหมาะกับโครงการวิลล่าไหม", "เป็นหนึ่งในทำเลที่มีการพัฒนามากที่สุดของเกาะ แต่แปลงใดเหมาะหรือไม่ขึ้นอยู่กับขนาด ทางเข้า และผังสีของแปลงนั้น"],
   ["สร้างใกล้หาดได้แค่ไหน", "การก่อสร้างใกล้แนวชายฝั่งอยู่ภายใต้กฎหมายไทยเรื่องระยะร่นและความสูงอาคาร ควรให้สถาปนิกและทนายความที่มีใบอนุญาตยืนยันเป็นรายแปลง"],
   ["มีแปลงที่ไม่ประกาศขายทั่วไปไหม", "เจ้าของบางรายไม่ต้องการประกาศ แจ้งความต้องการกับเบนซ์ แล้วจะช่วยตรวจสอบให้"]]},
 "zh": {
  "intro": [
   "邦涛是西北海岸的一条长滩，以度假村、海滩俱乐部以及海滨路后方不断涌现的新住宅项目著称。",
   "买家兴趣通常来自租赁需求与转售流动性，而不仅是价格。"],
  "typical": "靠近海滩的地块面积小、价格高；面积较大的地块位于更靠近主干道与后方山坡一带。",
  "nearby": ["邦涛海滩与海滩俱乐部", "普吉乐古浪", "Boat Avenue", "北上通往机场的道路"],
  "faq": [
   ["邦涛适合做别墅项目吗？", "这里是全岛开发最活跃的区域之一。具体地块是否合适，取决于面积、通路与规划用途。"],
   ["可以离海滩多近建房？", "近岸建设受泰国关于退缩距离与建筑高度的法规约束，应由持牌建筑师与律师针对具体地块确认。"],
   ["有未公开出售的地块吗？", "部分业主不愿公开挂牌。把需求告诉 Benz，他会帮您了解。"]]}},

"kamala": {
 "en": {
  "intro": [
   "Kamala sits between Patong and Bang Tao, with a quieter beach, a local village centre and hillside land with sea views to the north and south of the bay.",
   "It attracts buyers who want west-coast access without the intensity of Patong."],
  "typical": "Hillside plots with slope and view, plus flatter land in the valley behind the village. Slope affects both build cost and what is permitted.",
  "nearby": ["Kamala beach", "Kamala village and local market", "Patong to the south", "Bang Tao to the north"],
  "faq": [
   ["Is hillside land more expensive to build on?", "Usually yes. Retaining structures, access roads and services on sloped land add cost that should be in your budget from the start."],
   ["Are there height restrictions on the hillsides?", "Thailand restricts building on land above certain gradients and elevations. Confirm the position for a specific plot with a licensed professional before purchase."],
   ["What is available in Kamala now?", "Ask Benz — availability changes, and only verified plots are listed on this site."]]},
 "th": {
  "intro": [
   "กมลาอยู่ระหว่างป่าตองและบางเทา มีหาดที่เงียบกว่า มีศูนย์กลางชุมชน และมีที่ดินบนเนินเขาที่มองเห็นวิวทะเลทั้งด้านเหนือและใต้ของอ่าว",
   "เหมาะกับผู้ซื้อที่ต้องการอยู่ฝั่งตะวันตกแต่ไม่ต้องการความพลุกพล่านแบบป่าตอง"],
  "typical": "มีทั้งแปลงบนเนินเขาที่มีความลาดชันและวิว และแปลงที่ราบในหุบด้านหลังหมู่บ้าน ความลาดชันมีผลทั้งต่อค่าก่อสร้างและสิ่งที่กฎหมายอนุญาต",
  "nearby": ["หาดกมลา", "หมู่บ้านและตลาดกมลา", "ป่าตองทางทิศใต้", "บางเทาทางทิศเหนือ"],
  "faq": [
   ["ที่ดินบนเนินเขาก่อสร้างแพงกว่าไหม", "โดยทั่วไปแพงกว่า ทั้งกำแพงกันดิน ถนนเข้า และงานระบบบนพื้นที่ลาดชัน ควรคำนวณไว้ในงบตั้งแต่แรก"],
   ["มีข้อจำกัดความสูงบนเนินเขาไหม", "ประเทศไทยมีข้อจำกัดการก่อสร้างบนพื้นที่ที่มีความลาดชันและระดับความสูงเกินกำหนด ควรให้ผู้เชี่ยวชาญที่มีใบอนุญาตตรวจสอบเป็นรายแปลงก่อนซื้อ"],
   ["ตอนนี้กมลามีอะไรขายบ้าง", "สอบถามเบนซ์ได้ เพราะรายการเปลี่ยนแปลงตลอด และเว็บไซต์นี้ลงเฉพาะแปลงที่ตรวจสอบแล้ว"]]},
 "zh": {
  "intro": [
   "卡马拉位于芭东与邦涛之间，海滩更安静，有本地村落中心，海湾南北两侧的山坡地可俯瞰海景。",
   "适合希望位于西海岸、但不想要芭东喧嚣的买家。"],
  "typical": "既有带坡度与景观的山坡地块，也有村后谷地的平地。坡度会影响建造成本与法规允许的内容。",
  "nearby": ["卡马拉海滩", "卡马拉村与本地市场", "南侧的芭东", "北侧的邦涛"],
  "faq": [
   ["山坡地建造成本更高吗？", "通常更高。挡土结构、进场道路与市政配套都会增加成本，应从一开始纳入预算。"],
   ["山坡建设有高度限制吗？", "泰国对超过一定坡度与海拔的土地建设有限制。购买前请由持牌专业人士针对具体地块确认。"],
   ["卡马拉现在有什么在售？", "请咨询 Benz。供应情况随时变化，本网站只登载已核实的地块。"]]}},

"rawai": {
 "en": {
  "intro": [
   "Rawai is on the southern tip of Phuket, a residential area with a long-established foreign community, seafood restaurants along the shore and easy access to the island's southern beaches and piers.",
   "Prices here have historically been more accessible than the central west coast."],
  "typical": "Smaller residential plots are common, with some larger parcels on the slopes towards Nai Harn and the hills inland.",
  "nearby": ["Rawai beach and pier", "Nai Harn beach", "Promthep Cape", "Chalong and the marina area"],
  "faq": [
   ["Is Rawai suitable for a family home?", "It is largely residential with schools, clinics and shops nearby, which is why many long-term residents choose it."],
   ["Can I reach the airport easily?", "The airport is at the opposite end of the island, so allow travel time. Many residents accept this in exchange for the quieter setting."],
   ["Are there development plots?", "Occasionally. Larger parcels come to market less often here than in Thalang."]]},
 "th": {
  "intro": [
   "ราไวย์อยู่ปลายสุดทางใต้ของภูเก็ต เป็นย่านที่อยู่อาศัยที่มีชุมชนชาวต่างชาติมานาน มีร้านอาหารทะเลริมหาด และเดินทางไปหาดและท่าเรือทางใต้ได้สะดวก",
   "ระดับราคาที่ผ่านมาเข้าถึงได้ง่ายกว่าฝั่งตะวันตกตอนกลาง"],
  "typical": "ส่วนใหญ่เป็นแปลงที่อยู่อาศัยขนาดไม่ใหญ่ และมีแปลงใหญ่บางส่วนบนเนินไปทางในหานและเนินเขาฝั่งใน",
  "nearby": ["หาดและท่าเรือราไวย์", "หาดในหาน", "แหลมพรหมเทพ", "ฉลองและย่านมารีน่า"],
  "faq": [
   ["ราไวย์เหมาะกับบ้านครอบครัวไหม", "เป็นย่านที่อยู่อาศัยเป็นหลัก มีโรงเรียน คลินิก และร้านค้าใกล้เคียง จึงเป็นทำเลที่ผู้อยู่อาศัยระยะยาวจำนวนมากเลือก"],
   ["เดินทางไปสนามบินสะดวกไหม", "สนามบินอยู่คนละฝั่งของเกาะ จึงต้องเผื่อเวลาเดินทาง หลายคนยอมรับได้เพื่อแลกกับความเงียบสงบ"],
   ["มีที่ดินเพื่อพัฒนาโครงการไหม", "มีบ้างเป็นครั้งคราว แปลงใหญ่ออกสู่ตลาดน้อยกว่าฝั่งถลาง"]]},
 "zh": {
  "intro": [
   "拉威位于普吉最南端，是外籍居民聚居多年的住宅区，岸边有海鲜餐厅，前往南部海滩与码头都很方便。",
   "该区价格长期以来比西海岸中部更易入手。"],
  "typical": "以中小型住宅地块为主，通往奈汉方向的坡地与内陆山区有一些较大地块。",
  "nearby": ["拉威海滩与码头", "奈汉海滩", "神仙半岛", "查龙与游艇码头区"],
  "faq": [
   ["拉威适合作为家庭住宅吗？", "该区以住宅为主，学校、诊所与商店都在附近，因此很多长期居民选择这里。"],
   ["去机场方便吗？", "机场位于岛的另一端，需预留车程。许多居民以此换取更安静的环境。"],
   ["有开发用地吗？", "偶尔会有。相比他朗，这里的大地块进入市场的频率较低。"]]}},

"nai-harn": {
 "en": {
  "intro": [
   "Nai Harn is a bay in the south-west of the island, bordered by hills and a lake, with a beach that stays comparatively low-rise.",
   "Land is limited by the surrounding terrain, which is part of why the area keeps its character."],
  "typical": "Mostly hillside and valley plots of modest size; larger flat parcels are rare.",
  "nearby": ["Nai Harn beach and lake", "Ya Nui beach", "Promthep Cape", "Rawai to the east"],
  "faq": [
   ["Why is there so little land for sale in Nai Harn?", "The bay is enclosed by hills and protected areas, so supply is naturally limited."],
   ["Is a sea view guaranteed by elevation?", "No. Views depend on the plot, the trees and what may be built in front of it. This should be checked on site, not assumed from a map."],
   ["Can Benz find land here?", "He can look and will tell you if nothing genuine is available rather than offering a substitute you did not ask for."]]},
 "th": {
  "intro": [
   "ในหานเป็นอ่าวทางตะวันตกเฉียงใต้ของเกาะ ล้อมด้วยเนินเขาและทะเลสาบ หาดยังคงลักษณะอาคารไม่สูงเมื่อเทียบกับทำเลอื่น",
   "ที่ดินมีจำกัดด้วยสภาพภูมิประเทศ ซึ่งเป็นส่วนหนึ่งที่ทำให้พื้นที่ยังคงเอกลักษณ์"],
  "typical": "ส่วนใหญ่เป็นแปลงบนเนินเขาและในหุบ ขนาดไม่ใหญ่ แปลงราบขนาดใหญ่หาได้ยาก",
  "nearby": ["หาดและทะเลสาบในหาน", "หาดยะนุ้ย", "แหลมพรหมเทพ", "ราไวย์ทางทิศตะวันออก"],
  "faq": [
   ["ทำไมที่ดินขายในหานถึงมีน้อย", "อ่าวถูกล้อมด้วยเนินเขาและพื้นที่คุ้มครอง อุปทานจึงจำกัดโดยธรรมชาติ"],
   ["อยู่สูงแล้วได้วิวทะเลแน่นอนไหม", "ไม่แน่นอน วิวขึ้นอยู่กับตำแหน่งแปลง ต้นไม้ และสิ่งที่อาจสร้างขึ้นด้านหน้า ควรตรวจสอบหน้างานจริง ไม่ใช่ดูจากแผนที่"],
   ["เบนซ์หาที่ดินแถวนี้ได้ไหม", "หาให้ได้ และจะแจ้งตามตรงหากไม่มีแปลงที่ตรงจริง ๆ แทนที่จะเสนอแปลงอื่นแทน"]]},
 "zh": {
  "intro": [
   "奈汉是岛屿西南部的一处海湾，三面环山并有湖泊，海滩周边建筑相对低矮。",
   "地形限制了土地供应，这也是该区得以保持特色的原因之一。"],
  "typical": "以面积适中的山坡与谷地地块为主，大面积平地非常少见。",
  "nearby": ["奈汉海滩与湖泊", "雅奴伊海滩", "神仙半岛", "东侧的拉威"],
  "faq": [
   ["奈汉为什么很少有土地出售？", "海湾被山体与保护区环抱，供应天然有限。"],
   ["地势高就一定有海景吗？", "不一定。视野取决于地块位置、树木以及前方可能的建设，应实地查看而非凭地图判断。"],
   ["Benz 能在这里找到土地吗？", "可以帮您寻找；若确实没有合适的地块，他会如实相告，而不会推荐您并未要求的替代地块。"]]}},

"kata": {
 "en": {
  "intro": [
   "Kata is a west-coast beach town south of Karon, with a compact centre, a surf beach and hillside roads that lead to viewpoints over the bay.",
   "Demand is driven by tourism, which supports short-stay rental use where regulations allow."],
  "typical": "Hillside plots with views and smaller plots in the built-up area behind the beach.",
  "nearby": ["Kata and Kata Noi beaches", "Karon to the north", "Karon viewpoint", "Chalong and the main road east"],
  "faq": [
   ["Can I rent out a property in Kata short term?", "Short-term rental in Thailand is regulated by hotel licensing and other rules. Confirm the position for your specific plan with a licensed Thai lawyer before you buy."],
   ["Is parking an issue on hillside plots?", "Steep access and turning space are practical constraints worth checking on site."],
   ["Are plots here suitable for boutique projects?", "Some are. Size, access and zoning determine what can realistically be built."]]},
 "th": {
  "intro": [
   "กะตะเป็นเมืองหาดฝั่งตะวันตกถัดจากกะรนลงมาทางใต้ มีศูนย์กลางเมืองกะทัดรัด หาดสำหรับเล่นเซิร์ฟ และถนนบนเนินที่นำไปสู่จุดชมวิวอ่าว",
   "ความต้องการขับเคลื่อนด้วยการท่องเที่ยว ซึ่งส่งผลต่อการใช้ประโยชน์แบบปล่อยเช่าระยะสั้นเท่าที่กฎหมายอนุญาต"],
  "typical": "มีทั้งแปลงบนเนินที่มีวิว และแปลงขนาดเล็กในย่านชุมชนด้านหลังหาด",
  "nearby": ["หาดกะตะและกะตะน้อย", "กะรนทางทิศเหนือ", "จุดชมวิวกะรน", "ฉลองและถนนสายหลักไปทางตะวันออก"],
  "faq": [
   ["ปล่อยเช่าระยะสั้นในกะตะได้ไหม", "การปล่อยเช่าระยะสั้นในประเทศไทยอยู่ภายใต้กฎหมายโรงแรมและกฎระเบียบอื่น ควรให้ทนายความไทยที่มีใบอนุญาตตรวจสอบแผนของคุณก่อนซื้อ"],
   ["ที่จอดรถบนแปลงเนินเขาเป็นปัญหาไหม", "ทางเข้าชันและพื้นที่กลับรถเป็นข้อจำกัดเชิงปฏิบัติที่ควรดูหน้างาน"],
   ["เหมาะกับโครงการบูทีคไหม", "บางแปลงเหมาะ ขึ้นอยู่กับขนาด ทางเข้า และผังสีว่าสร้างอะไรได้จริง"]]},
 "zh": {
  "intro": [
   "卡塔是卡伦以南的西海岸海滨小镇，市中心紧凑，拥有适合冲浪的海滩，山路通往可俯瞰海湾的观景点。",
   "需求主要来自旅游，在法规允许范围内支撑短租用途。"],
  "typical": "既有带景观的山坡地块，也有海滩后方成熟社区中的小地块。",
  "nearby": ["卡塔海滩与小卡塔海滩", "北侧的卡伦", "卡伦观景台", "查龙与东向主干道"],
  "faq": [
   ["卡塔的房产可以做短租吗？", "泰国短租受酒店牌照等法规约束。购买前请由持牌泰国律师就您的具体计划进行确认。"],
   ["山坡地块停车是否不便？", "陡坡进场与回车空间是实际限制，建议实地查看。"],
   ["这里的地块适合精品项目吗？", "部分适合。面积、通路与规划用途决定实际可建内容。"]]}},

"karon": {
 "en": {
  "intro": [
   "Karon lies between Patong and Kata on the west coast, with one of the longest beaches on the island and a mix of hotels, residential streets and hillside plots.",
   "It is a practical middle ground for buyers who want west-coast beach access with more space than Patong."],
  "typical": "Plots inland from the beach road, hillside land towards the Karon viewpoint, and occasional commercial plots along the main roads.",
  "nearby": ["Karon beach", "Kata to the south", "Patong to the north", "Karon viewpoint"],
  "faq": [
   ["What is the main difference between Karon and Kata?", "Karon has a longer beach and more open space; Kata has a more compact centre. Both are tourism-led."],
   ["Is commercial land available?", "Commercial plots appear on the main roads from time to time. Availability and permitted use vary by plot."],
   ["How do I know a plot's zoning?", "Zoning is set by the Phuket town plan and shown by colour. Benz can point you to the relevant information and your lawyer should verify it."]]},
 "th": {
  "intro": [
   "กะรนอยู่ระหว่างป่าตองและกะตะทางฝั่งตะวันตก มีหาดที่ยาวที่สุดแห่งหนึ่งของเกาะ ผสมกันระหว่างโรงแรม ย่านที่อยู่อาศัย และแปลงบนเนินเขา",
   "เป็นทางเลือกกลาง ๆ สำหรับผู้ซื้อที่อยากอยู่ใกล้หาดฝั่งตะวันตกแต่ต้องการพื้นที่มากกว่าป่าตอง"],
  "typical": "มีแปลงถัดจากถนนเลียบหาดเข้ามา แปลงบนเนินไปทางจุดชมวิวกะรน และบางครั้งมีแปลงพาณิชย์ริมถนนสายหลัก",
  "nearby": ["หาดกะรน", "กะตะทางทิศใต้", "ป่าตองทางทิศเหนือ", "จุดชมวิวกะรน"],
  "faq": [
   ["กะรนกับกะตะต่างกันอย่างไร", "กะรนมีหาดยาวกว่าและพื้นที่โปร่งกว่า ส่วนกะตะมีศูนย์กลางกะทัดรัดกว่า ทั้งคู่ขับเคลื่อนด้วยการท่องเที่ยว"],
   ["มีที่ดินเชิงพาณิชย์ไหม", "มีออกมาเป็นระยะริมถนนสายหลัก ความพร้อมและการใช้ประโยชน์ต่างกันไปในแต่ละแปลง"],
   ["จะรู้ผังสีของแปลงได้อย่างไร", "ผังสีกำหนดตามผังเมืองภูเก็ต เบนซ์ช่วยชี้แหล่งข้อมูลได้ และควรให้ทนายความของคุณตรวจสอบยืนยัน"]]},
 "zh": {
  "intro": [
   "卡伦位于芭东与卡塔之间的西海岸，拥有全岛最长的海滩之一，酒店、住宅街区与山坡地块并存。",
   "对于想靠近西海岸海滩、又希望空间比芭东更开阔的买家来说，是务实的折中之选。"],
  "typical": "海滨路以内的地块、通往卡伦观景台的坡地，以及主干道旁偶尔出现的商业地块。",
  "nearby": ["卡伦海滩", "南侧的卡塔", "北侧的芭东", "卡伦观景台"],
  "faq": [
   ["卡伦与卡塔的主要区别是什么？", "卡伦海滩更长、空间更开阔；卡塔的中心更紧凑。两者都以旅游为主导。"],
   ["有商业用地吗？", "主干道沿线不时会有商业地块，供应与允许用途因地块而异。"],
   ["如何确认地块的规划用途？", "用地性质由普吉城市规划以颜色标示。Benz 可以指引相关信息，并应由您的律师核实。"]]}},
}

# ---------------------------------------------------------------- home: services
SERVICES = [
 {"en": ("Land sourcing", "Tell Benz the area, budget and what you want to build. He looks for plots that match, including ones not advertised online."),
  "th": ("จัดหาที่ดิน", "บอกทำเล งบประมาณ และสิ่งที่คุณต้องการสร้าง เบนซ์จะหาแปลงที่ตรงให้ รวมถึงแปลงที่ไม่ได้ประกาศขายออนไลน์"),
  "zh": ("土地寻源", "告诉 Benz 区域、预算与开发意图，他会为您寻找匹配的地块，包括未在网上公开的地块。")},
 {"en": ("Site viewings", "Plots look different on the ground than in photos. Benz takes you to the land, walks the boundaries and shows the access road."),
  "th": ("พาดูที่ดินจริง", "ที่ดินในภาพกับของจริงต่างกัน เบนซ์พาลงพื้นที่ เดินดูแนวเขต และดูทางเข้า-ออกจริง"),
  "zh": ("实地看地", "现场与照片差别很大。Benz 会带您到现场、走一遍地界并查看进场道路。")},
 {"en": ("Land information", "Title documents, size, access, utilities and zoning colour, collected and passed to you and your lawyer in one pack."),
  "th": ("ข้อมูลที่ดิน", "เอกสารสิทธิ์ ขนาด ทางเข้า สาธารณูปโภค และผังสี รวบรวมส่งให้คุณและทนายความในชุดเดียว"),
  "zh": ("土地资料", "权属文件、面积、通路、配套与用地颜色，整理成一份资料交给您与您的律师。")},
 {"en": ("Negotiation support", "Benz speaks to the owner in Thai, relays offers and keeps both sides clear on what has been agreed."),
  "th": ("ช่วยเจรจาต่อรอง", "เบนซ์คุยกับเจ้าของที่เป็นภาษาไทย ส่งต่อข้อเสนอ และทำให้ทั้งสองฝ่ายเข้าใจตรงกันว่าตกลงอะไรไว้"),
  "zh": ("议价协助", "Benz 用泰语与业主沟通，传达报价，并确保双方对已达成的条件理解一致。")},
 {"en": ("Buyer coordination", "Introductions to independent lawyers, surveyors and architects. You appoint them; Benz keeps the process moving."),
  "th": ("ประสานงานให้ผู้ซื้อ", "แนะนำทนายความ ช่างรังวัด และสถาปนิกที่เป็นอิสระ คุณเป็นผู้ว่าจ้างเอง เบนซ์ช่วยให้ขั้นตอนเดินหน้า"),
  "zh": ("买家协调", "介绍独立律师、测量师与建筑师，由您自行委任；Benz 负责推动流程。")},
 {"en": ("After the sale", "Handover, utility connections and introductions to builders when you are ready to develop."),
  "th": ("หลังการขาย", "ส่งมอบ ต่อสาธารณูปโภค และแนะนำผู้รับเหมาเมื่อคุณพร้อมพัฒนาโครงการ"),
  "zh": ("成交之后", "交接、水电接入，并在您准备开发时介绍施工方。")},
]

# ---------------------------------------------------------------- investment page
INVEST_INTRO = {
 "en": ["Phuket land is bought for different reasons: to build a home, to develop and sell, to hold, or to operate a business on. Each of these has a different risk profile and a different exit.",
        "The categories below describe the kinds of projects buyers bring to Benz. They are opportunities to consider with your own advisers, not forecasts. No return is promised or implied on this site."],
 "th": ["ที่ดินภูเก็ตถูกซื้อด้วยเหตุผลต่างกัน ทั้งเพื่อสร้างบ้าน เพื่อพัฒนาแล้วขาย เพื่อถือครอง หรือเพื่อประกอบธุรกิจ แต่ละแบบมีความเสี่ยงและทางออกต่างกัน",
        "หมวดด้านล่างคือประเภทโครงการที่ผู้ซื้อนำมาปรึกษาเบนซ์ ถือเป็นโอกาสที่ควรพิจารณาร่วมกับที่ปรึกษาของคุณเอง ไม่ใช่การคาดการณ์ และเว็บไซต์นี้ไม่รับประกันผลตอบแทนใด ๆ"],
 "zh": ["购买普吉土地的目的各不相同：自建住宅、开发出售、长期持有，或用于经营业务。每种目的的风险与退出方式都不同。",
        "以下类别是买家常与 Benz 讨论的项目类型，属于可与您自己的顾问共同评估的机会，而非预测。本网站不承诺也不暗示任何回报。"],
}

INVEST_CATEGORIES = [
 {"slug": "villa-development",
  "en": ("Villa development", "Single villas or small estates, usually on plots from around one rai upwards. Build cost, slope, access and permitted density drive the numbers more than the land price alone.",
         ["Plot sizes suited to one house or a small cluster", "Access road width and ownership matter for construction", "Design must respect setbacks and slope rules"]),
  "th": ("พัฒนาวิลล่า", "ตั้งแต่วิลล่าหลังเดียวถึงโครงการขนาดเล็ก มักใช้ที่ดินตั้งแต่ราวหนึ่งไร่ขึ้นไป ต้นทุนก่อสร้าง ความลาดชัน ทางเข้า และความหนาแน่นที่อนุญาต มีผลต่อตัวเลขมากกว่าราคาที่ดินเพียงอย่างเดียว",
         ["ขนาดแปลงเหมาะกับบ้านหลังเดียวหรือกลุ่มเล็ก", "ความกว้างและกรรมสิทธิ์ของถนนเข้ามีผลต่อการก่อสร้าง", "แบบต้องเป็นไปตามระยะร่นและกฎเรื่องความลาดชัน"]),
  "zh": ("别墅开发", "单栋别墅或小型社区，通常用地约一莱以上。建造成本、坡度、通路与允许密度对财务模型的影响大于地价本身。",
         ["适合单栋或小组团的地块面积", "进场道路宽度与产权影响施工", "设计须符合退缩与坡度规定"])},
 {"slug": "boutique-resort",
  "en": ("Boutique resort", "Small hospitality projects need licensing as well as land. Hotel operation in Thailand is regulated, and the licence route should be confirmed before land is bought.",
         ["Land size and room count must work together", "Hotel licensing is a separate process from land purchase", "Location relative to beach and road access affects demand"]),
  "th": ("รีสอร์ตบูทีค", "โครงการโรงแรมขนาดเล็กต้องมีทั้งที่ดินและใบอนุญาต การประกอบกิจการโรงแรมในไทยอยู่ภายใต้กฎหมาย ควรตรวจสอบแนวทางขอใบอนุญาตก่อนซื้อที่ดิน",
         ["ขนาดที่ดินต้องสอดคล้องกับจำนวนห้อง", "การขอใบอนุญาตโรงแรมเป็นคนละขั้นตอนกับการซื้อที่ดิน", "ระยะถึงหาดและทางเข้ามีผลต่อความต้องการ"]),
  "zh": ("精品度假村", "小型酒店项目不仅需要土地，还需要牌照。泰国酒店经营受监管，购地前应先确认牌照路径。",
         ["土地面积须与客房数量匹配", "酒店牌照与购地是两个独立流程", "与海滩及道路的相对位置影响需求"])},
 {"slug": "hotel-development",
  "en": ("Hotel development", "Larger parcels, usually inland or on secondary roads where scale is achievable. Infrastructure capacity — water, power, drainage — is a practical limit worth checking early.",
         ["Parcel shape and frontage affect layout", "Utility capacity may need upgrading", "Environmental and building approvals take time"]),
  "th": ("พัฒนาโรงแรม", "ใช้แปลงใหญ่ ส่วนมากอยู่ฝั่งในหรือถนนรอง ซึ่งทำสเกลได้ กำลังของสาธารณูปโภคทั้งน้ำ ไฟ และระบบระบายน้ำ เป็นข้อจำกัดที่ควรตรวจตั้งแต่ต้น",
         ["รูปร่างแปลงและหน้ากว้างมีผลต่อผังโครงการ", "อาจต้องขยายกำลังสาธารณูปโภค", "การอนุมัติด้านสิ่งแวดล้อมและอาคารใช้เวลา"]),
  "zh": ("酒店开发", "多为内陆或次干道的大型地块，便于形成规模。水、电、排水等基础设施容量是应尽早核查的现实限制。",
         ["地块形状与临路面影响布局", "配套容量可能需要扩容", "环评与建筑审批需要时间"])},
 {"slug": "commercial-property",
  "en": ("Commercial property", "Roadside plots for retail, offices, clinics or service businesses. Frontage, traffic and permitted use matter more than view.",
         ["Road frontage and visibility are the main value drivers", "Permitted commercial use depends on zoning", "Parking provision is often a constraint"]),
  "th": ("อสังหาริมทรัพย์เชิงพาณิชย์", "แปลงริมถนนสำหรับร้านค้า สำนักงาน คลินิก หรือธุรกิจบริการ หน้ากว้างติดถนน ปริมาณการสัญจร และการใช้ประโยชน์ที่อนุญาต สำคัญกว่าเรื่องวิว",
         ["หน้ากว้างติดถนนและการมองเห็นคือปัจจัยหลักของมูลค่า", "การใช้เชิงพาณิชย์ขึ้นอยู่กับผังสี", "พื้นที่จอดรถมักเป็นข้อจำกัด"]),
  "zh": ("商业地产", "临街地块，可用于零售、办公、诊所或服务业。临路面、车流与允许用途比景观更关键。",
         ["临街宽度与可见性是主要价值来源", "允许的商业用途取决于规划", "停车配置常是限制因素"])},
 {"slug": "land-investment",
  "en": ("Land investment", "Holding land without developing it. Costs are low but so is liquidity; land can take time to sell and values are not guaranteed to rise.",
         ["Holding costs include tax and maintenance", "Resale can take months or longer", "Title quality strongly affects resale"]),
  "th": ("ลงทุนถือครองที่ดิน", "ถือที่ดินไว้โดยยังไม่พัฒนา ค่าใช้จ่ายต่ำแต่สภาพคล่องก็ต่ำเช่นกัน การขายต่ออาจใช้เวลา และมูลค่าไม่ได้รับประกันว่าจะเพิ่มขึ้น",
         ["ต้นทุนการถือครองรวมภาษีและการดูแลพื้นที่", "การขายต่ออาจใช้เวลาหลายเดือนหรือนานกว่านั้น", "คุณภาพเอกสารสิทธิ์มีผลอย่างมากต่อการขายต่อ"]),
  "zh": ("土地投资", "持有土地而暂不开发。持有成本低，但流动性也低；转售可能耗时，且价值上涨没有保证。",
         ["持有成本包括税费与维护", "转售可能需要数月甚至更久", "权属质量对转售影响很大"])},
 {"slug": "residential-development",
  "en": ("Residential development", "Housing projects aimed at long-term residents rather than tourists. These depend on schools, hospitals and daily amenities being within reach.",
         ["Proximity to schools and services drives demand", "Plot layout determines unit count", "Infrastructure must be planned from the start"]),
  "th": ("พัฒนาที่อยู่อาศัย", "โครงการบ้านสำหรับผู้อยู่อาศัยระยะยาวมากกว่านักท่องเที่ยว ขึ้นอยู่กับการเข้าถึงโรงเรียน โรงพยาบาล และสิ่งอำนวยความสะดวกในชีวิตประจำวัน",
         ["ความใกล้โรงเรียนและบริการมีผลต่อความต้องการ", "ผังแปลงกำหนดจำนวนยูนิต", "ต้องวางระบบสาธารณูปโภคตั้งแต่ต้น"]),
  "zh": ("住宅开发", "面向长期居民而非游客的住宅项目，取决于学校、医院与日常配套是否便利。",
         ["靠近学校与服务设施决定需求", "地块布局决定户数", "基础设施须从一开始规划"])},
]

INVEST_RISK = {
 "en": ("How we talk about returns", "This website does not publish guaranteed returns, guaranteed profit or risk-free claims, because property does not work that way. Prices can fall as well as rise, projects can be delayed, and regulations change. Any figures you receive from Benz are the seller's asking terms or your own project assumptions — they are not a forecast, and you should test them with your own financial and legal advisers."),
 "th": ("เราพูดถึงผลตอบแทนอย่างไร", "เว็บไซต์นี้ไม่ประกาศผลตอบแทนที่รับประกัน กำไรที่รับประกัน หรือการลงทุนที่ปราศจากความเสี่ยง เพราะอสังหาริมทรัพย์ไม่ได้ทำงานแบบนั้น ราคามีทั้งขึ้นและลง โครงการอาจล่าช้า และกฎระเบียบเปลี่ยนแปลงได้ ตัวเลขใด ๆ ที่ได้รับจากเบนซ์คือเงื่อนไขที่ผู้ขายเสนอ หรือสมมติฐานโครงการของคุณเอง ไม่ใช่การคาดการณ์ และควรตรวจสอบกับที่ปรึกษาทางการเงินและกฎหมายของคุณ"),
 "zh": ("关于回报的说明", "本网站不发布保证回报、保证利润或零风险的说法，因为房地产并非如此运作。价格可能上涨也可能下跌，项目可能延期，法规也会变化。您从 Benz 处获得的任何数字，均为卖方的要价条件或您自己的项目假设，不构成预测，应由您的财务与法律顾问核验。"),
}

# ---------------------------------------------------------------- about page
ABOUT = {
 "en": {
  "lead": "Andaman Land is a Phuket land agency run by Benz Supawat. The work is simple to describe: find land that matches what a buyer actually wants to build, tell them the truth about it, and help them get to a decision with their own lawyer beside them.",
  "sections": [
   ("Who Benz works with", ["Most enquiries come from buyers outside Thailand — European, American, Australian and Chinese — who are looking at Phuket for a home, a villa project, a small resort or a long-term land holding.",
     "Some know the island well. Others have visited twice. Both need the same thing: land information they can check, not a sales pitch."]),
   ("How the work is done", ["Benz is based in Phuket and speaks with landowners directly in Thai. That means offers, conditions and title questions are communicated without a layer of guesswork in between.",
     "Every plot presented to you comes with the documents that exist for it. If something is missing or unclear, you will be told that it is missing or unclear."]),
   ("What Benz does not do", ["Benz is a property agent, not a lawyer, accountant or licensed financial adviser. He does not give legal opinions on ownership structures, and he does not promise returns.",
     "Independent legal advice is not optional on a Thai land purchase. Benz will introduce lawyers, but you appoint and instruct them yourself."]),
  ],
  "facts_title": "Company details",
  "facts_note": "These fields are shown exactly as they will appear once the real details are filled in. Nothing has been invented.",
 },
 "th": {
  "lead": "Andaman Land คือเอเจนซี่ที่ดินในภูเก็ต ดำเนินงานโดย เบนซ์ ศุภวัฒน์ หลักการทำงานเรียบง่าย คือหาที่ดินที่ตรงกับสิ่งที่ผู้ซื้อต้องการสร้างจริง ๆ บอกความจริงเกี่ยวกับแปลงนั้น และช่วยให้ตัดสินใจได้โดยมีทนายความของผู้ซื้อร่วมตรวจสอบ",
  "sections": [
   ("เบนซ์ทำงานกับใคร", ["ผู้ติดต่อส่วนใหญ่เป็นผู้ซื้อจากต่างประเทศ ทั้งยุโรป อเมริกา ออสเตรเลีย และจีน ที่มองภูเก็ตเพื่อเป็นบ้าน โครงการวิลล่า รีสอร์ตขนาดเล็ก หรือการถือครองที่ดินระยะยาว",
     "บางคนรู้จักเกาะนี้ดี บางคนเพิ่งมาสองครั้ง แต่ทั้งคู่ต้องการสิ่งเดียวกัน คือข้อมูลที่ดินที่ตรวจสอบได้ ไม่ใช่คำโฆษณา"]),
   ("ทำงานอย่างไร", ["เบนซ์อยู่ในภูเก็ตและคุยกับเจ้าของที่ดินเป็นภาษาไทยโดยตรง ข้อเสนอ เงื่อนไข และคำถามเรื่องเอกสารสิทธิ์จึงสื่อสารได้โดยไม่ต้องเดา",
     "ทุกแปลงที่เสนอจะมาพร้อมเอกสารเท่าที่มีจริง หากข้อมูลส่วนใดขาดหรือยังไม่ชัดเจน จะแจ้งตามนั้น"]),
   ("สิ่งที่เบนซ์ไม่ทำ", ["เบนซ์เป็นตัวแทนอสังหาริมทรัพย์ ไม่ใช่ทนายความ นักบัญชี หรือที่ปรึกษาการเงินที่มีใบอนุญาต จึงไม่ให้ความเห็นทางกฎหมายเรื่องโครงสร้างการถือครอง และไม่รับประกันผลตอบแทน",
     "การปรึกษาทนายความอิสระไม่ใช่ทางเลือกเสริมในการซื้อที่ดินในไทย เบนซ์แนะนำทนายความให้ได้ แต่คุณเป็นผู้ว่าจ้างและสั่งงานเอง"]),
  ],
  "facts_title": "ข้อมูลบริษัท",
  "facts_note": "ช่องเหล่านี้แสดงตามรูปแบบที่จะปรากฏจริงเมื่อกรอกข้อมูลแล้ว ไม่มีการสร้างข้อมูลสมมติ",
 },
 "zh": {
  "lead": "Andaman Land 是由 Benz Supawat 经营的普吉土地代理机构。工作内容很直接：找到真正符合买家建设意图的土地，如实告知情况，并协助买家在自己律师的陪同下作出决定。",
  "sections": [
   ("Benz 的客户", ["大部分咨询来自泰国以外的买家——欧洲、美国、澳大利亚与中国——他们希望在普吉置业、开发别墅项目、建小型度假村或长期持有土地。",
     "有人对这座岛很熟悉，有人只来过两次。但两者需要的是同一件事：可核实的土地资料，而不是推销话术。"]),
   ("工作方式", ["Benz 常驻普吉，直接用泰语与地主沟通。因此报价、条件与权属问题的传达不会夹杂猜测。",
     "每一块推荐给您的地都会附上现有文件。如果某项资料缺失或不明确，也会如实说明。"]),
   ("Benz 不做的事", ["Benz 是房产代理，不是律师、会计师或持牌财务顾问。他不对持有结构提供法律意见，也不承诺回报。",
     "在泰国购地，独立法律意见并非可选项。Benz 可以介绍律师，但由您自行委任与指示。"]),
  ],
  "facts_title": "公司信息",
  "facts_note": "以下字段按填入真实资料后的呈现方式显示，未虚构任何内容。",
 },
}

# ---------------------------------------------------------------- contact page
CONTACT_COPY = {
 "en": ("Contact Benz", "Send the property ID you are interested in, or describe the land you are looking for — area, budget and what you plan to build. Replies are usually within one working day."),
 "th": ("ติดต่อเบนซ์", "ส่งรหัสทรัพย์สินที่คุณสนใจ หรืออธิบายที่ดินที่คุณกำลังมองหา ทั้งทำเล งบประมาณ และสิ่งที่ต้องการสร้าง โดยปกติตอบกลับภายใน 1 วันทำการ"),
 "zh": ("联系 Benz", "请发送您感兴趣的房源编号，或描述您想找的土地——区域、预算与建设计划。通常在一个工作日内回复。"),
}

# ---------------------------------------------------------------- legal pages
LEGAL_PAGES = {
"disclaimer": {
 "en": ("Legal disclaimer", [
  ("General information only", ["Everything published on this website — listings, guides, location pages and investment pages — is general information about the Phuket property market. It is not legal advice, tax advice, investment advice or a professional opinion on any specific plot of land."]),
  ("Foreign ownership", ["Thai law restricts the ownership of land by foreign nationals. Nothing on this site should be read as saying that a foreign buyer can freely own land in Thailand. Any ownership structure must be reviewed by a licensed Thai lawyer for your specific circumstances before you sign or pay anything."]),
  ("Accuracy of listings", ["Listing details are supplied by owners and checked as far as reasonably possible, but sizes, boundaries, title status, zoning and availability must be verified independently during due diligence. Details can change without notice and a plot may be sold or withdrawn at any time."]),
  ("No guaranteed returns", ["No return, yield, profit or capital growth is promised or implied anywhere on this website. Property values can fall as well as rise."]),
  ("Third parties", ["Any lawyer, surveyor, architect or contractor introduced to you is independent. You appoint and instruct them directly, and Andaman Land by Benz Supawat is not responsible for their work."]),
 ]),
 "th": ("ข้อจำกัดความรับผิดชอบ", [
  ("ข้อมูลทั่วไปเท่านั้น", ["ทุกอย่างที่เผยแพร่บนเว็บไซต์นี้ ทั้งประกาศทรัพย์สิน คู่มือ หน้าทำเล และหน้าการลงทุน เป็นข้อมูลทั่วไปเกี่ยวกับตลาดอสังหาริมทรัพย์ภูเก็ต ไม่ใช่คำแนะนำทางกฎหมาย ภาษี การลงทุน หรือความเห็นทางวิชาชีพต่อที่ดินแปลงใดแปลงหนึ่ง"]),
  ("การถือครองโดยชาวต่างชาติ", ["กฎหมายไทยจำกัดการถือครองที่ดินโดยคนต่างด้าว ไม่มีข้อความใดในเว็บไซต์นี้ที่ควรตีความว่าชาวต่างชาติสามารถถือครองที่ดินในไทยได้อย่างอิสระ โครงสร้างการถือครองใด ๆ ต้องให้ทนายความไทยที่มีใบอนุญาตตรวจสอบตามข้อเท็จจริงของคุณก่อนลงนามหรือชำระเงิน"]),
  ("ความถูกต้องของประกาศ", ["รายละเอียดประกาศมาจากเจ้าของทรัพย์และตรวจสอบเท่าที่ทำได้ตามสมควร แต่ขนาด แนวเขต สถานะเอกสารสิทธิ์ ผังสี และความพร้อมขาย ต้องตรวจสอบโดยอิสระในขั้นตอน due diligence ข้อมูลอาจเปลี่ยนแปลงโดยไม่แจ้งล่วงหน้า และแปลงที่ดินอาจถูกขายหรือถอนออกเมื่อใดก็ได้"]),
  ("ไม่มีการรับประกันผลตอบแทน", ["เว็บไซต์นี้ไม่ให้คำมั่นหรือสื่อถึงผลตอบแทน อัตราผลตอบแทน กำไร หรือการเติบโตของมูลค่าใด ๆ มูลค่าอสังหาริมทรัพย์ลดลงได้เช่นเดียวกับที่เพิ่มขึ้นได้"]),
  ("บุคคลภายนอก", ["ทนายความ ช่างรังวัด สถาปนิก หรือผู้รับเหมาที่แนะนำให้ เป็นผู้ประกอบวิชาชีพอิสระ คุณเป็นผู้ว่าจ้างและสั่งงานโดยตรง Andaman Land by Benz Supawat ไม่รับผิดชอบต่อผลงานของบุคคลเหล่านั้น"]),
 ]),
 "zh": ("免责声明", [
  ("仅为一般信息", ["本网站发布的全部内容——房源、指南、地区页面与投资页面——均为关于普吉房地产市场的一般信息，不构成法律、税务或投资建议，也不构成对任何具体地块的专业意见。"]),
  ("外国人持有", ["泰国法律限制外国人持有土地。本网站任何内容都不应被理解为外国买家可以自由持有泰国土地。任何持有结构都须在签署或付款前，由持牌泰国律师依据您的具体情况审核。"]),
  ("房源信息准确性", ["房源资料由业主提供并在合理范围内核实，但面积、地界、权属状态、规划用途与可售情况仍须在尽职调查中独立核验。信息可能随时变更，地块也可能随时售出或撤回。"]),
  ("不保证回报", ["本网站任何位置均不承诺或暗示回报、收益率、利润或资本增值。房地产价值可能上涨，也可能下跌。"]),
  ("第三方", ["向您介绍的律师、测量师、建筑师或承包商均为独立专业人士，由您直接委任与指示，Andaman Land by Benz Supawat 不对其工作负责。"]),
 ])},

"privacy": {
 "en": ("Privacy policy", [
  ("What is collected", ["When you send an enquiry, the form collects the details you type: name, nationality, email, phone, WhatsApp, LINE ID, preferred contact method, property ID and your message. The site also records standard web analytics if analytics is enabled."]),
  ("Why it is collected", ["Your details are used to answer your enquiry about property and to follow up about land that matches your requirements. They are not sold."]),
  ("Who sees it", ["Enquiries go to Andaman Land by Benz Supawat and, where necessary to progress your purchase, to the lawyer or professional you appoint. [ADD ANY OTHER RECIPIENTS]"]),
  ("How long it is kept", ["[ADD RETENTION PERIOD]"]),
  ("Your choices", ["Write to [ADD EMAIL] to ask what is held about you, to correct it, or to ask for it to be deleted."]),
 ]),
 "th": ("นโยบายความเป็นส่วนตัว", [
  ("ข้อมูลที่เก็บ", ["เมื่อคุณส่งข้อความ ฟอร์มจะเก็บข้อมูลที่คุณกรอก ได้แก่ ชื่อ สัญชาติ อีเมล โทรศัพท์ WhatsApp LINE ID ช่องทางติดต่อที่สะดวก รหัสทรัพย์สิน และข้อความของคุณ รวมถึงข้อมูลสถิติการใช้งานเว็บไซต์ทั่วไปหากเปิดใช้งาน analytics"]),
  ("เก็บเพื่ออะไร", ["ใช้เพื่อตอบคำถามของคุณเกี่ยวกับทรัพย์สิน และติดตามเสนอที่ดินที่ตรงกับความต้องการ ไม่มีการขายข้อมูล"]),
  ("ใครเห็นข้อมูล", ["ข้อความส่งถึง Andaman Land by Benz Supawat และส่งต่อให้ทนายความหรือผู้เชี่ยวชาญที่คุณแต่งตั้งเท่าที่จำเป็นต่อการดำเนินการซื้อ [ADD ANY OTHER RECIPIENTS]"]),
  ("เก็บไว้นานเท่าใด", ["[ADD RETENTION PERIOD]"]),
  ("สิทธิของคุณ", ["ติดต่อ [ADD EMAIL] เพื่อขอทราบข้อมูลที่จัดเก็บ ขอแก้ไข หรือขอให้ลบข้อมูลของคุณ"]),
 ]),
 "zh": ("隐私政策", [
  ("收集哪些信息", ["当您提交咨询时，表单会收集您填写的内容：姓名、国籍、电子邮箱、电话、WhatsApp、LINE ID、首选联系方式、房源编号与留言。若启用了分析工具，网站也会记录常规访问统计。"]),
  ("收集目的", ["用于回复您的房产咨询，并就符合您需求的土地进行跟进。我们不出售您的信息。"]),
  ("谁会看到", ["咨询发送至 Andaman Land by Benz Supawat；在推进交易所必需的范围内，也会提供给您委任的律师或专业人士。[ADD ANY OTHER RECIPIENTS]"]),
  ("保留多久", ["[ADD RETENTION PERIOD]"]),
  ("您的权利", ["请发送邮件至 [ADD EMAIL]，查询、更正或要求删除我们持有的您的信息。"]),
 ])},

"terms": {
 "en": ("Terms of use", [
  ("Using this site", ["By using this website you accept these terms. If you do not accept them, please do not use the site."]),
  ("Listings are invitations to enquire", ["A listing is not an offer capable of acceptance. Price, availability and terms are set by the owner and can change until a binding contract is signed."]),
  ("No professional relationship", ["Reading this site does not create an agency, legal or advisory relationship. Any professional engagement is agreed separately in writing."]),
  ("Content", ["Text, layout and images on this site belong to Andaman Land by Benz Supawat unless credited otherwise. Do not republish listings or guides without permission."]),
  ("Governing law", ["[ADD GOVERNING LAW AND JURISDICTION — confirm with your lawyer]"]),
 ]),
 "th": ("เงื่อนไขการใช้งาน", [
  ("การใช้เว็บไซต์", ["การใช้งานเว็บไซต์นี้ถือว่าคุณยอมรับเงื่อนไขเหล่านี้ หากไม่ยอมรับ กรุณาอย่าใช้งานเว็บไซต์"]),
  ("ประกาศเป็นการเชิญให้สอบถาม", ["ประกาศทรัพย์สินไม่ใช่คำเสนอที่ผูกพันทันที ราคา ความพร้อมขาย และเงื่อนไข กำหนดโดยเจ้าของ และเปลี่ยนแปลงได้จนกว่าจะลงนามในสัญญาที่มีผลผูกพัน"]),
  ("ไม่ก่อให้เกิดความสัมพันธ์ทางวิชาชีพ", ["การอ่านเว็บไซต์นี้ไม่ก่อให้เกิดความสัมพันธ์ในฐานะตัวแทน ทนายความ หรือที่ปรึกษา การว่าจ้างใด ๆ ต้องตกลงเป็นลายลักษณ์อักษรแยกต่างหาก"]),
  ("เนื้อหา", ["ข้อความ การจัดวาง และภาพบนเว็บไซต์นี้เป็นของ Andaman Land by Benz Supawat เว้นแต่ระบุแหล่งที่มาอื่น ห้ามนำประกาศหรือคู่มือไปเผยแพร่ซ้ำโดยไม่ได้รับอนุญาต"]),
  ("กฎหมายที่ใช้บังคับ", ["[ADD GOVERNING LAW AND JURISDICTION — ตรวจสอบกับทนายความของคุณ]"]),
 ]),
 "zh": ("使用条款", [
  ("使用本网站", ["使用本网站即表示您接受本条款。若不接受，请勿使用本网站。"]),
  ("房源为邀约洽谈", ["房源信息不构成可直接承诺的要约。价格、可售状态与条件由业主决定，在签署具约束力的合同前可能变更。"]),
  ("不构成专业关系", ["浏览本网站不构成代理、法律或顾问关系。任何专业委任须另行书面约定。"]),
  ("内容", ["除另有注明外，本网站的文字、版式与图片归 Andaman Land by Benz Supawat 所有。未经许可不得转载房源或指南。"]),
  ("适用法律", ["[ADD GOVERNING LAW AND JURISDICTION — 请与您的律师确认]"]),
 ])},

"cookies": {
 "en": ("Cookie policy", [
  ("What this site uses", ["The site itself works without tracking cookies. Your language choice may be stored in your browser so the site opens in the same language next time."]),
  ("Analytics", ["If Google Analytics 4 is enabled, it sets cookies to measure page views and traffic sources. [ADD CONFIRMATION ONCE GA4 IS CONNECTED]"]),
  ("Controlling cookies", ["You can clear or block cookies in your browser settings. Blocking them does not stop you browsing listings."]),
 ]),
 "th": ("นโยบายคุกกี้", [
  ("เว็บไซต์นี้ใช้อะไรบ้าง", ["ตัวเว็บไซต์ทำงานได้โดยไม่ต้องใช้คุกกี้ติดตาม การเลือกภาษาของคุณอาจถูกเก็บไว้ในเบราว์เซอร์ เพื่อให้เปิดเว็บไซต์ด้วยภาษาเดิมในครั้งถัดไป"]),
  ("Analytics", ["หากเปิดใช้งาน Google Analytics 4 จะมีการตั้งคุกกี้เพื่อวัดจำนวนการเข้าชมและแหล่งที่มาของผู้เข้าชม [ADD CONFIRMATION ONCE GA4 IS CONNECTED]"]),
  ("การจัดการคุกกี้", ["คุณสามารถล้างหรือบล็อกคุกกี้ได้ในการตั้งค่าเบราว์เซอร์ การบล็อกคุกกี้ไม่กระทบการเรียกดูประกาศทรัพย์สิน"]),
 ]),
 "zh": ("Cookie 政策", [
  ("本网站使用什么", ["网站本身无需跟踪型 Cookie 即可运行。您的语言选择可能保存在浏览器中，以便下次以相同语言打开。"]),
  ("分析工具", ["若启用 Google Analytics 4，会设置 Cookie 以统计页面浏览量与流量来源。[ADD CONFIRMATION ONCE GA4 IS CONNECTED]"]),
  ("管理 Cookie", ["您可在浏览器设置中清除或阻止 Cookie。阻止 Cookie 不影响浏览房源。"]),
 ])},
}
