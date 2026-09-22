# -*- coding: utf-8 -*-
"""Buying-guide articles (EN / TH / ZH).

โครงสร้างแต่ละบทความ: slug, updated, per-language dict with
title, meta (meta description), lead, sections [(heading, [paragraphs])], faq [[q, a], ...]
กฎสำคัญ: เนื้อหากฎหมายต้องระมัดระวัง ไม่ฟันธง และไม่ทำให้เข้าใจว่าชาวต่างชาติถือครองที่ดินไทยได้โดยไม่มีข้อจำกัด
"""

ARTICLES = [
{
 "slug": "can-foreigners-buy-land-in-thailand",
 "updated": "2026-01-01",
 "en": {
  "title": "Can foreigners buy land in Thailand?",
  "meta": "A plain-English explanation of how Thai law restricts land ownership by foreign nationals, and the structures buyers discuss with their lawyers.",
  "lead": "The short answer is that Thai law restricts land ownership by foreign individuals. That restriction is the starting point for every conversation about buying land in Phuket.",
  "sections": [
   ("The general rule", [
    "Under the Land Code, foreign nationals are generally not permitted to own land in Thailand in their own name. Narrow exceptions exist in law, and they are exceptions rather than a route most buyers can use.",
    "This is why a foreign buyer looking at a plot in Phuket is usually really asking a different question: what lawful structure gives me the use of this land for the period I need, and what are its risks?"]),
   ("Structures buyers commonly ask about", [
    "Long leasehold is the structure most often discussed. A lease registered at the Land Office gives a right to use the land for a fixed term. The enforceability of renewals promised beyond the registered term is a question your lawyer must address.",
    "Ownership through a Thai company is also discussed. Companies that are genuine, properly capitalised businesses are treated differently from companies created only to hold land for a foreigner using nominee shareholders, which is unlawful.",
    "Buildings are treated separately from land in Thai law, which is why some buyers lease land and own the house on it. Condominium units are a separate regime again, with foreign freehold possible within the limits set by the Condominium Act."]),
   ("What this means in practice", [
    "There is no single structure that is right for everyone. The correct answer depends on your nationality, your timeline, whether you intend to develop, your tax position at home, and your succession plans.",
    "Anyone who tells you that a foreigner can simply buy Thai land outright, or that a particular structure is risk-free, is not describing the legal position accurately."]),
   ("Getting reliable advice", [
    "Take advice from a Thai lawyer who is licensed, independent of the seller, and instructed by you. Ask them to explain the risks of the structure in writing, not only its benefits.",
    "Benz can introduce lawyers and will provide the documents that exist for any plot, but he does not give legal opinions and you should not rely on an agent — any agent — for that."]),
  ],
  "faq": [
   ["Can I own the house but not the land?", "Thai law treats buildings and land as separate property, and this separation is the basis of several structures. Your lawyer should confirm how it applies to your plan."],
   ["Is a 30-year lease the maximum?", "Registered leases of immovable property in Thailand are subject to statutory maximum terms, and renewal clauses raise enforceability questions. Ask your lawyer to explain the term and renewal position for your specific transaction."],
   ["Are nominee shareholders acceptable?", "Using Thai nominees to hold shares on behalf of a foreigner in order to own land is not lawful. Do not accept any arrangement described this way."]]},
 "th": {
  "title": "ชาวต่างชาติซื้อที่ดินในประเทศไทยได้หรือไม่",
  "meta": "คำอธิบายเข้าใจง่ายว่ากฎหมายไทยจำกัดการถือครองที่ดินของคนต่างด้าวอย่างไร และโครงสร้างที่ผู้ซื้อมักหารือกับทนายความ",
  "lead": "คำตอบสั้น ๆ คือ กฎหมายไทยจำกัดการถือครองที่ดินของบุคคลต่างด้าว และข้อจำกัดนี้คือจุดตั้งต้นของทุกการพูดคุยเรื่องการซื้อที่ดินในภูเก็ต",
  "sections": [
   ("หลักทั่วไป", [
    "ตามประมวลกฎหมายที่ดิน โดยทั่วไปคนต่างด้าวไม่สามารถถือครองที่ดินในประเทศไทยในนามของตนเองได้ มีข้อยกเว้นอยู่บ้างตามกฎหมาย แต่เป็นข้อยกเว้นที่ผู้ซื้อส่วนใหญ่ไม่สามารถใช้ได้",
    "ด้วยเหตุนี้ คำถามที่แท้จริงของผู้ซื้อต่างชาติจึงมักเป็นอีกคำถามหนึ่ง คือ โครงสร้างใดที่ชอบด้วยกฎหมายและให้สิทธิใช้ที่ดินนี้ตามระยะเวลาที่ต้องการ และมีความเสี่ยงอะไรบ้าง"]),
   ("โครงสร้างที่ผู้ซื้อมักสอบถาม", [
    "สัญญาเช่าระยะยาวเป็นโครงสร้างที่พูดถึงมากที่สุด การจดทะเบียนเช่าที่สำนักงานที่ดินให้สิทธิใช้ที่ดินตามระยะเวลาที่กำหนด ส่วนคำมั่นเรื่องการต่ออายุเกินระยะที่จดทะเบียนไว้ มีประเด็นเรื่องการบังคับได้ซึ่งทนายความของคุณต้องอธิบาย",
    "การถือครองผ่านบริษัทไทยก็เป็นอีกเรื่องที่ถูกถามบ่อย บริษัทที่ประกอบธุรกิจจริงและมีทุนตามจริง ต่างจากบริษัทที่ตั้งขึ้นเพียงเพื่อถือที่ดินแทนคนต่างด้าวโดยใช้ผู้ถือหุ้นนอมินี ซึ่งไม่ชอบด้วยกฎหมาย",
    "กฎหมายไทยแยกสิ่งปลูกสร้างออกจากที่ดิน ผู้ซื้อบางรายจึงเช่าที่ดินและเป็นเจ้าของบ้านบนที่ดินนั้น ส่วนห้องชุดอยู่ภายใต้กฎหมายอีกฉบับ ซึ่งคนต่างด้าวถือกรรมสิทธิ์ได้ภายในสัดส่วนที่พระราชบัญญัติอาคารชุดกำหนด"]),
   ("ความหมายในทางปฏิบัติ", [
    "ไม่มีโครงสร้างใดที่เหมาะกับทุกคน คำตอบที่ถูกต้องขึ้นอยู่กับสัญชาติ ระยะเวลาที่ต้องการถือครอง แผนการพัฒนา สถานะทางภาษีในประเทศของคุณ และการวางแผนมรดก",
    "หากมีใครบอกว่าชาวต่างชาติซื้อที่ดินไทยได้เต็มรูปแบบ หรือบอกว่าโครงสร้างใดปราศจากความเสี่ยง นั่นไม่ใช่การอธิบายสถานะทางกฎหมายที่ถูกต้อง"]),
   ("การขอคำแนะนำที่เชื่อถือได้", [
    "ควรปรึกษาทนายความไทยที่มีใบอนุญาต เป็นอิสระจากผู้ขาย และได้รับการว่าจ้างจากคุณ ขอให้อธิบายความเสี่ยงของโครงสร้างเป็นลายลักษณ์อักษร ไม่ใช่เฉพาะข้อดี",
    "เบนซ์แนะนำทนายความให้ได้ และจะส่งเอกสารเท่าที่มีของแต่ละแปลงให้ แต่ไม่ให้ความเห็นทางกฎหมาย และคุณไม่ควรพึ่งพาตัวแทนรายใดในเรื่องนี้"]),
  ],
  "faq": [
   ["เป็นเจ้าของบ้านแต่ไม่ได้เป็นเจ้าของที่ดินได้ไหม", "กฎหมายไทยแยกสิ่งปลูกสร้างกับที่ดินออกจากกัน ซึ่งเป็นพื้นฐานของหลายโครงสร้าง ควรให้ทนายความยืนยันว่าใช้กับแผนของคุณอย่างไร"],
   ["สัญญาเช่า 30 ปีคือสูงสุดหรือไม่", "การจดทะเบียนเช่าอสังหาริมทรัพย์ในไทยมีกำหนดระยะเวลาสูงสุดตามกฎหมาย และข้อสัญญาต่ออายุมีประเด็นเรื่องการบังคับได้ ควรให้ทนายความอธิบายเฉพาะกรณีของคุณ"],
   ["ใช้ผู้ถือหุ้นนอมินีได้ไหม", "การใช้คนไทยถือหุ้นแทนคนต่างด้าวเพื่อให้ได้มาซึ่งที่ดินไม่ชอบด้วยกฎหมาย อย่ารับข้อเสนอที่อธิบายในลักษณะนี้"]]},
 "zh": {
  "title": "外国人可以在泰国购买土地吗？",
  "meta": "用通俗语言说明泰国法律如何限制外国人持有土地，以及买家常与律师讨论的各种结构。",
  "lead": "简短的回答是：泰国法律限制外国自然人持有土地。这一限制是所有关于在普吉购地讨论的出发点。",
  "sections": [
   ("一般规则", [
    "根据泰国《土地法》，外国人通常不得以本人名义在泰国持有土地。法律中存在少数例外，但只是例外，多数买家无法适用。",
    "因此，外国买家看中普吉某地块时，真正要问的其实是另一个问题：哪种合法结构能让我在所需期限内使用这块土地，其风险又是什么？"]),
   ("买家常问的几种结构", [
    "长期租赁是最常被讨论的结构。在土地厅登记的租约赋予在固定期限内使用土地的权利。登记期限之外所承诺的续期是否可强制执行，需由您的律师说明。",
    "通过泰国公司持有也常被提及。真实经营、资本到位的公司，与仅为替外国人持地而以代名股东设立的公司性质完全不同，后者不合法。",
    "泰国法律将建筑物与土地分开处理，因此有些买家租赁土地而拥有其上的房屋。公寓单元则适用另一套制度，外国人可在《公寓法》规定的比例内持有永久产权。"]),
   ("实务含义", [
    "没有一种结构适合所有人。正确答案取决于您的国籍、持有期限、是否计划开发、母国税务状况以及继承安排。",
    "若有人告诉您外国人可以直接买下泰国土地，或声称某种结构毫无风险，那并未如实描述法律状况。"]),
   ("如何获得可靠意见", [
    "请咨询持牌、独立于卖方、并由您本人委任的泰国律师。要求其以书面说明该结构的风险，而不仅是好处。",
    "Benz 可以介绍律师，并提供各地块现有的文件，但他不提供法律意见；在这一点上，您不应依赖任何代理人。"]),
  ],
  "faq": [
   ["我可以拥有房屋但不拥有土地吗？", "泰国法律将建筑物与土地视为独立财产，这是多种结构的基础。请由律师确认其如何适用于您的计划。"],
   ["租期 30 年是上限吗？", "泰国不动产登记租赁有法定最长期限，续期条款也涉及可执行性问题。请让律师就您的具体交易说明期限与续期状况。"],
   ["可以使用代名股东吗？", "由泰国人代外国人持股以取得土地并不合法。请勿接受任何以此方式描述的安排。"]]}},

{
 "slug": "buying-property-in-phuket-guide-for-foreign-buyers",
 "updated": "2026-01-01",
 "en": {
  "title": "Buying property in Phuket: a guide for foreign buyers",
  "meta": "How a Phuket land purchase actually runs, from first enquiry and site visit through due diligence, deposit and transfer at the Land Office.",
  "lead": "A Phuket purchase runs in a predictable order. Knowing the order makes it much easier to spot when something is being skipped.",
  "sections": [
   ("1. Decide what you are buying it for", [
    "A plot for a family home, a villa project for resale, and land held for the long term are three different briefs. They point to different areas, different sizes and different title requirements.",
    "Write down your budget for land and for the build separately. Land price alone rarely tells you whether a project works."]),
   ("2. Shortlist and visit", [
    "Photographs flatten slope, hide access problems and make boundaries look tidier than they are. Visit the plots, walk the access road, and look at what sits on the neighbouring land.",
    "Ask what the plot is next to, not only what it faces. Quarries, temples, schools and planned roads all affect day-to-day life."]),
   ("3. Verify before you commit money", [
    "Once you are serious, your lawyer checks the title document, the registered owner, the boundaries, encumbrances, access rights and zoning. This is due diligence and it comes before any significant payment.",
    "Where a plot has been subdivided or has unclear access, expect this stage to take longer. That delay is protection, not friction."]),
   ("4. Deposit and contract", [
    "A reservation or deposit agreement takes the plot off the market for an agreed period. Read what happens to the deposit if due diligence fails — that clause matters more than the amount.",
    "The sale and purchase agreement should reflect what you were actually shown, including size, boundaries and anything promised about access or utilities."]),
   ("5. Transfer", [
    "Transfer happens at the Land Office, where the registration is made and taxes and fees are paid. Agree in writing beforehand who pays what.",
    "Keep every document you receive. You will need them again when you build, connect utilities or eventually sell."]),
  ],
  "faq": [
   ["Do I need to be in Thailand for the transfer?", "Buyers sometimes attend in person and sometimes act through a properly executed power of attorney. Your lawyer will advise which applies to your situation."],
   ["How long does a land purchase take?", "It depends on the title, the seller and how quickly documents are produced. Plots with clean, straightforward title move faster."]]},
 "th": {
  "title": "ซื้ออสังหาริมทรัพย์ในภูเก็ต: คู่มือสำหรับผู้ซื้อชาวต่างชาติ",
  "meta": "ขั้นตอนการซื้อที่ดินภูเก็ตตั้งแต่การสอบถาม ลงดูพื้นที่ ตรวจสอบเอกสาร วางมัดจำ จนถึงการโอนที่สำนักงานที่ดิน",
  "lead": "การซื้อที่ดินในภูเก็ตมีลำดับขั้นตอนที่ชัดเจน เมื่อรู้ลำดับแล้ว จะสังเกตได้ง่ายขึ้นว่ามีขั้นตอนใดถูกข้าม",
  "sections": [
   ("1. กำหนดวัตถุประสงค์ให้ชัด", [
    "ที่ดินสำหรับบ้านครอบครัว โครงการวิลล่าเพื่อขาย และที่ดินเพื่อถือครองระยะยาว คือโจทย์คนละแบบ นำไปสู่ทำเล ขนาด และเงื่อนไขเอกสารสิทธิ์ที่ต่างกัน",
    "ควรแยกงบค่าที่ดินกับงบก่อสร้างออกจากกัน ราคาที่ดินอย่างเดียวมักไม่บอกว่าโครงการคุ้มหรือไม่"]),
   ("2. คัดเลือกและลงดูพื้นที่จริง", [
    "ภาพถ่ายทำให้ความลาดชันดูน้อยลง ซ่อนปัญหาทางเข้า และทำให้แนวเขตดูเรียบร้อยกว่าความจริง ควรไปดูแปลงจริง เดินดูถนนเข้า และดูว่าที่ดินข้างเคียงเป็นอะไร",
    "ถามว่าแปลงนี้อยู่ติดกับอะไร ไม่ใช่แค่หันหน้าไปทางไหน ทั้งบ่อหิน วัด โรงเรียน และแนวถนนตามผัง ล้วนมีผลต่อการอยู่อาศัย"]),
   ("3. ตรวจสอบก่อนจ่ายเงินก้อน", [
    "เมื่อสนใจจริงจัง ทนายความจะตรวจเอกสารสิทธิ์ ผู้ถือกรรมสิทธิ์ แนวเขต ภาระผูกพัน สิทธิทางเข้า-ออก และผังสี ขั้นตอนนี้คือ due diligence และต้องทำก่อนจ่ายเงินจำนวนมาก",
    "หากแปลงเคยแบ่งแยกหรือทางเข้าไม่ชัดเจน ขั้นตอนนี้จะใช้เวลานานขึ้น ความล่าช้านี้คือการป้องกันความเสี่ยง ไม่ใช่ความยุ่งยาก"]),
   ("4. มัดจำและสัญญา", [
    "สัญญาจองหรือสัญญามัดจำทำให้แปลงถูกกันไว้ตามระยะเวลาที่ตกลง ควรอ่านให้ชัดว่าหากผลตรวจสอบไม่ผ่าน เงินมัดจำจะเป็นอย่างไร ข้อนี้สำคัญกว่าจำนวนเงิน",
    "สัญญาจะซื้อจะขายควรสะท้อนสิ่งที่คุณได้เห็นจริง ทั้งขนาด แนวเขต และคำมั่นเรื่องทางเข้าและสาธารณูปโภค"]),
   ("5. โอนกรรมสิทธิ์", [
    "การโอนทำที่สำนักงานที่ดิน มีการจดทะเบียนและชำระภาษีกับค่าธรรมเนียม ควรตกลงเป็นลายลักษณ์อักษรล่วงหน้าว่าฝ่ายใดรับผิดชอบส่วนใด",
    "เก็บเอกสารทุกฉบับไว้ เพราะจะต้องใช้อีกเมื่อก่อสร้าง ขอสาธารณูปโภค หรือขายต่อในอนาคต"]),
  ],
  "faq": [
   ["ต้องอยู่ในประเทศไทยตอนโอนหรือไม่", "ผู้ซื้อบางรายไปด้วยตนเอง บางรายมอบอำนาจตามแบบที่ถูกต้อง ทนายความจะแนะนำตามกรณีของคุณ"],
   ["ใช้เวลาซื้อที่ดินนานเท่าใด", "ขึ้นอยู่กับเอกสารสิทธิ์ ตัวผู้ขาย และความเร็วในการจัดหาเอกสาร แปลงที่เอกสารชัดเจนจะดำเนินการได้เร็วกว่า"]]},
 "zh": {
  "title": "在普吉购房购地：外国买家指南",
  "meta": "从首次咨询、实地看地，到尽职调查、定金与土地厅过户，完整说明普吉购地流程。",
  "lead": "普吉的购地流程有固定顺序。了解顺序后，就更容易发现哪一步被跳过了。",
  "sections": [
   ("1. 先明确购买目的", [
    "自住家庭住宅、用于转售的别墅项目、以及长期持有的土地，是三种完全不同的需求，对应不同区域、面积与权属要求。",
    "请分别写下土地预算与建造预算。仅凭地价往往无法判断项目是否可行。"]),
   ("2. 筛选并实地查看", [
    "照片会弱化坡度、掩盖通路问题，并让地界看起来比实际整齐。请到现场查看、走一遍进场道路，并了解邻地状况。",
    "要问这块地紧邻什么，而不只是朝向哪里。采石场、寺庙、学校与规划道路都会影响日常生活。"]),
   ("3. 付款前先核实", [
    "当您认真考虑时，律师会核查权属文件、登记所有人、地界、他项权利、通行权与规划用途。这就是尽职调查，应在支付大额款项之前完成。",
    "若地块曾分割或通路不清，此阶段会更久。这种延迟是保护，而非阻碍。"]),
   ("4. 定金与合同", [
    "预订或定金协议会在约定期间内为您保留地块。请务必看清：若尽职调查未通过，定金如何处理——这一条比金额更重要。",
    "买卖合同应如实反映您所见到的内容，包括面积、地界，以及关于通路与配套的任何承诺。"]),
   ("5. 过户", [
    "过户在土地厅办理，完成登记并缴纳税费。请事先书面约定各项费用由谁承担。",
    "保存好收到的每一份文件。日后建设、接通水电或出售时还会用到。"]),
  ],
  "faq": [
   ["过户时必须本人在泰国吗？", "有的买家亲自到场，有的通过依法签署的授权书办理。律师会根据您的情况给出建议。"],
   ["购地需要多长时间？", "取决于权属状况、卖方配合度与出具文件的速度。权属清晰的地块进展更快。"]]}},

{
 "slug": "freehold-vs-leasehold-in-thailand",
 "updated": "2026-01-01",
 "en": {
  "title": "Freehold vs leasehold in Thailand",
  "meta": "What freehold and leasehold mean in a Thai context, how they differ for foreign buyers, and the questions to put to your lawyer.",
  "lead": "The words freehold and leasehold are used loosely in marketing. In a Thai transaction they describe very different legal positions, and the difference matters most to foreign buyers.",
  "sections": [
   ("Freehold", [
    "Freehold means ownership of the property registered in the owner's name, with no fixed end date. For land, Thai law restricts who can hold it, which is why freehold land ownership is generally not available to foreign individuals.",
    "Condominium units are the common exception discussed, where foreign freehold is possible within the foreign-ownership quota set by the Condominium Act for that building."]),
   ("Leasehold", [
    "A lease is a right to use property for a fixed registered term. It is a contractual right, registered at the Land Office, rather than ownership.",
    "Renewal promises made in a lease are one of the most commonly misunderstood parts of Thai property marketing. Whether a promised renewal will be enforceable against a future owner is a legal question, and the answer is not automatic."]),
   ("Practical differences", [
    "Freehold is generally easier to resell and to finance. Leasehold value declines as the remaining term shortens, which affects resale price and the pool of buyers.",
    "For a development project, the remaining term matters enormously: a build takes years, and the value of the finished asset depends on what is left after that."]),
   ("Questions worth asking", [
    "Who is the registered owner today, and are they the person signing? What exactly is registered — the lease itself, or only an agreement to lease? What happens on the owner's death or if the land is sold?",
    "Put these questions to your own lawyer in writing and keep the answer."]),
  ],
  "faq": [
   ["Is leasehold always worse than freehold?", "Not necessarily. It depends on the term, the price paid relative to that term, and what you want to do with the property. It is a trade-off, not a defect."]]},
 "th": {
  "title": "Freehold กับ Leasehold ในประเทศไทย",
  "meta": "ความหมายของกรรมสิทธิ์และสิทธิการเช่าในบริบทกฎหมายไทย ความต่างสำหรับผู้ซื้อต่างชาติ และคำถามที่ควรถามทนายความ",
  "lead": "คำว่า freehold และ leasehold ถูกใช้อย่างหลวม ๆ ในการตลาด แต่ในธุรกรรมของไทย สองคำนี้หมายถึงสถานะทางกฎหมายที่ต่างกันมาก และสำคัญที่สุดสำหรับผู้ซื้อชาวต่างชาติ",
  "sections": [
   ("Freehold (กรรมสิทธิ์)", [
    "Freehold คือการถือกรรมสิทธิ์ที่จดทะเบียนในชื่อเจ้าของ โดยไม่มีกำหนดสิ้นสุด สำหรับที่ดิน กฎหมายไทยจำกัดว่าใครถือได้ การถือกรรมสิทธิ์ที่ดินแบบ freehold จึงโดยทั่วไปไม่เปิดให้บุคคลต่างด้าว",
    "ข้อยกเว้นที่พูดถึงบ่อยคือห้องชุด ซึ่งคนต่างด้าวถือกรรมสิทธิ์ได้ภายในสัดส่วนที่พระราชบัญญัติอาคารชุดกำหนดสำหรับอาคารนั้น"]),
   ("Leasehold (สิทธิการเช่า)", [
    "การเช่าคือสิทธิใช้ทรัพย์ตามระยะเวลาที่จดทะเบียนไว้ เป็นสิทธิตามสัญญาที่จดทะเบียนที่สำนักงานที่ดิน ไม่ใช่กรรมสิทธิ์",
    "คำมั่นเรื่องการต่ออายุในสัญญาเช่าเป็นเรื่องที่เข้าใจผิดกันมากที่สุดในการตลาดอสังหาริมทรัพย์ไทย การต่ออายุจะบังคับได้กับเจ้าของรายใหม่หรือไม่ เป็นประเด็นทางกฎหมาย และไม่ได้เกิดขึ้นโดยอัตโนมัติ"]),
   ("ความต่างในทางปฏิบัติ", [
    "Freehold มักขายต่อและขอสินเชื่อได้ง่ายกว่า ส่วนมูลค่าของ leasehold จะลดลงเมื่อระยะเวลาคงเหลือสั้นลง ซึ่งกระทบทั้งราคาขายต่อและจำนวนผู้ซื้อที่สนใจ",
    "สำหรับโครงการพัฒนา ระยะเวลาคงเหลือสำคัญมาก เพราะการก่อสร้างใช้เวลาหลายปี และมูลค่าทรัพย์ที่เสร็จแล้วขึ้นกับระยะเวลาที่เหลือหลังจากนั้น"]),
   ("คำถามที่ควรถาม", [
    "ปัจจุบันใครเป็นผู้ถือกรรมสิทธิ์ และเป็นคนเดียวกับผู้ลงนามหรือไม่ สิ่งที่จดทะเบียนคืออะไร เป็นสัญญาเช่าหรือเป็นเพียงสัญญาจะให้เช่า และจะเกิดอะไรขึ้นหากเจ้าของเสียชีวิตหรือขายที่ดิน",
    "ควรถามทนายความของคุณเป็นลายลักษณ์อักษรและเก็บคำตอบไว้"]),
  ],
  "faq": [
   ["Leasehold แย่กว่า Freehold เสมอไปหรือไม่", "ไม่เสมอไป ขึ้นอยู่กับระยะเวลา ราคาที่จ่ายเทียบกับระยะเวลานั้น และสิ่งที่คุณต้องการทำกับทรัพย์สิน เป็นการแลกเปลี่ยนข้อดีข้อเสีย ไม่ใช่ข้อบกพร่อง"]]},
 "zh": {
  "title": "泰国的永久产权与租赁产权",
  "meta": "在泰国语境下永久产权与租赁产权的含义、对外国买家的差异，以及应向律师提出的问题。",
  "lead": "“永久产权”和“租赁产权”在营销中常被混用。在泰国交易中，两者代表截然不同的法律地位，对外国买家尤其重要。",
  "sections": [
   ("永久产权", [
    "永久产权指以所有人名义登记、没有固定终止日期的所有权。就土地而言，泰国法律限制持有主体，因此外国自然人通常无法取得土地的永久产权。",
    "常被讨论的例外是公寓单元：在该楼盘依《公寓法》设定的外资比例内，外国人可持有永久产权。"]),
   ("租赁产权", [
    "租赁是在登记的固定期限内使用财产的权利，属于在土地厅登记的合同权利，而非所有权。",
    "租约中的续期承诺是泰国房产营销中最常被误解的部分。所承诺的续期能否对抗未来的业主属于法律问题，并非自动生效。"]),
   ("实务差异", [
    "永久产权通常更易转售与融资。租赁产权的价值会随剩余年限缩短而下降，影响转售价格与潜在买家数量。",
    "对开发项目而言，剩余年限极为关键：建设本身需数年，建成后资产的价值取决于其后还剩多少年。"]),
   ("值得提出的问题", [
    "目前登记所有人是谁，与签约人是否同一人？登记的究竟是租赁本身，还是仅为租赁预约协议？业主去世或土地被出售时会怎样？",
    "请以书面形式向您自己的律师提出这些问题，并保存答复。"]),
  ],
  "faq": [
   ["租赁产权一定比永久产权差吗？", "不一定。取决于年限、相对于年限所支付的价格，以及您的使用目的。这是取舍，而非缺陷。"]]}},

{
 "slug": "how-to-buy-property-in-phuket",
 "updated": "2026-01-01",
 "en": {
  "title": "How to buy property in Phuket",
  "meta": "A practical checklist for buying land or property in Phuket: who to appoint, what to verify, how payments are usually staged and what to keep.",
  "lead": "This is the practical version: who you need around you, what gets checked, and in what order money changes hands.",
  "sections": [
   ("Assemble a small team", [
    "An agent to find and access the land. A licensed Thai lawyer, appointed by you, to verify and draft. A surveyor if boundaries are unclear. An architect early if you are developing, because design constraints can rule a plot out before you buy it."]),
   ("Verify the essentials", [
    "The title document and the registered owner. The exact boundaries on the ground. Legal access to a public road. Utilities availability. Zoning colour and what it permits. Any mortgage, charge or servitude registered against the land."]),
   ("Stage the money", [
    "Payments are usually staged: a reservation or deposit, then the balance on transfer. Conditions for the return of the deposit should be written, not spoken.",
    "Funds coming from abroad should be documented properly on arrival in Thailand. Your lawyer and bank will tell you what form the evidence should take and why it matters later."]),
   ("Keep the record", [
    "Keep the title document copy, the contracts, the receipts, the transfer paperwork and the correspondence. Buyers who keep a complete file have a much easier time when they build or resell."]),
  ],
  "faq": [
   ["Should I use the seller's lawyer?", "No. Appoint your own, independent of the seller and the agent."],
   ["Can I pay a deposit to hold a plot before due diligence?", "It happens often, but the agreement must say what occurs if due diligence reveals a problem. Have your lawyer review it before you pay."]]},
 "th": {
  "title": "ขั้นตอนการซื้ออสังหาริมทรัพย์ในภูเก็ต",
  "meta": "เช็กลิสต์เชิงปฏิบัติสำหรับการซื้อที่ดินในภูเก็ต ตั้งแต่ทีมที่ต้องมี สิ่งที่ต้องตรวจสอบ การแบ่งงวดชำระเงิน และเอกสารที่ต้องเก็บ",
  "lead": "นี่คือฉบับลงมือทำจริง ว่าคุณต้องมีใครอยู่ข้างตัว ต้องตรวจอะไร และเงินเปลี่ยนมือในลำดับใด",
  "sections": [
   ("ตั้งทีมเล็ก ๆ ของคุณ", [
    "ตัวแทนเพื่อหาและพาเข้าดูที่ดิน ทนายความไทยที่มีใบอนุญาตซึ่งคุณว่าจ้างเองเพื่อตรวจสอบและร่างสัญญา ช่างรังวัดหากแนวเขตไม่ชัดเจน และสถาปนิกตั้งแต่ต้นหากจะพัฒนาโครงการ เพราะข้อจำกัดด้านการออกแบบอาจทำให้แปลงนั้นไม่เหมาะตั้งแต่ก่อนซื้อ"]),
   ("ตรวจสิ่งสำคัญ", [
    "เอกสารสิทธิ์และผู้ถือกรรมสิทธิ์ แนวเขตที่แท้จริงในพื้นที่ ทางเข้า-ออกสู่ทางสาธารณะตามกฎหมาย ความพร้อมของสาธารณูปโภค ผังสีและการใช้ประโยชน์ที่อนุญาต รวมถึงภาระจำนอง ภาระติดพัน หรือภาระจำยอมที่จดทะเบียนไว้"]),
   ("แบ่งงวดการชำระเงิน", [
    "โดยทั่วไปแบ่งเป็นเงินจองหรือมัดจำ แล้วจึงชำระส่วนที่เหลือในวันโอน เงื่อนไขการคืนมัดจำต้องเขียนไว้ ไม่ใช่ตกลงด้วยวาจา",
    "เงินที่โอนมาจากต่างประเทศควรมีเอกสารรองรับเมื่อเข้าสู่ประเทศไทย ทนายความและธนาคารจะแจ้งว่าหลักฐานควรอยู่ในรูปแบบใดและเหตุใดจึงสำคัญในภายหลัง"]),
   ("เก็บเอกสารให้ครบ", [
    "เก็บสำเนาเอกสารสิทธิ์ สัญญา ใบเสร็จ เอกสารการโอน และการติดต่อสื่อสารทั้งหมด ผู้ซื้อที่มีแฟ้มเอกสารครบถ้วนจะทำงานง่ายขึ้นมากเมื่อถึงเวลาก่อสร้างหรือขายต่อ"]),
  ],
  "faq": [
   ["ใช้ทนายความของผู้ขายได้ไหม", "ไม่ควร ควรว่าจ้างทนายความของคุณเองที่เป็นอิสระจากผู้ขายและตัวแทน"],
   ["วางมัดจำจองแปลงก่อนตรวจสอบได้ไหม", "เกิดขึ้นบ่อย แต่สัญญาต้องระบุว่าจะเกิดอะไรขึ้นหากตรวจพบปัญหา ควรให้ทนายความตรวจก่อนจ่าย"]]},
 "zh": {
  "title": "如何在普吉购置房产",
  "meta": "在普吉购地的实用清单：需要委任哪些人、核实哪些事项、款项如何分期以及应保存哪些文件。",
  "lead": "这是实操版：您身边需要哪些人、要核实什么，以及资金按什么顺序支付。",
  "sections": [
   ("组建一支小团队", [
    "由代理负责寻找并带看土地；由您自行委任的持牌泰国律师负责核实与起草；地界不清时聘请测量师；若计划开发，应尽早引入建筑师，因为设计限制可能在购买前就否决某块地。"]),
   ("核实关键事项", [
    "权属文件与登记所有人；现场的准确地界；通往公共道路的合法通行权；水电配套；用地颜色及其允许用途；以及土地上登记的抵押、负担或地役权。"]),
   ("分期付款", [
    "通常分为预订金或定金，余款在过户时支付。定金退还条件必须书面写明，不能只是口头约定。",
    "自境外汇入的资金在进入泰国时应有妥当凭证。律师与银行会说明凭证形式，以及为何日后很重要。"]),
   ("保存完整档案", [
    "保存权属文件副本、合同、收据、过户文件与往来沟通记录。档案齐全的买家在建设或转售时会顺利得多。"]),
  ],
  "faq": [
   ["可以用卖方的律师吗？", "不建议。请委任独立于卖方与代理的自有律师。"],
   ["可以在尽职调查前先付定金锁定地块吗？", "这种做法常见，但协议必须写明若调查发现问题将如何处理。付款前请让律师审阅。"]]}},

{
 "slug": "property-due-diligence-in-thailand",
 "updated": "2026-01-01",
 "en": {
  "title": "Property due diligence in Thailand",
  "meta": "What a lawyer checks before you buy Thai land: title, ownership, boundaries, access, encumbrances, zoning and building constraints.",
  "lead": "Due diligence is the stage where a plot either proves itself or quietly falls apart. It is the least glamorous part of a purchase and the part most worth paying for.",
  "sections": [
   ("Title and ownership", [
    "Thai land is held under several different documents, and they do not carry equal rights. The strongest is a full title deed; weaker documents may limit transfer or use.",
    "Your lawyer confirms the document at the Land Office, checks the registered owner against identity documents, and looks at the history of the plot."]),
   ("Boundaries and size", [
    "The size on paper and the size on the ground do not always match, particularly where land has been subdivided or fenced informally. A survey resolves this.",
    "Neighbouring structures, walls and driveways that encroach are easier to deal with before purchase than after."]),
   ("Access", [
    "Legal access to a public road is not the same as a track people have used for years. Access may depend on a registered servitude or on a neighbour's goodwill, and those are very different positions.",
    "Access width also affects what can be built and whether construction vehicles can reach the site."]),
   ("Encumbrances and planning", [
    "Mortgages, court seizures, usufructs, leases and servitudes are registered against land and must be checked.",
    "Zoning colour under the town plan, plus rules on slope, elevation, setbacks from the shoreline and building height, determine what can lawfully be built. Confirm these with a licensed professional before purchase, not after."]),
  ],
  "faq": [
   ["How long does due diligence take?", "It varies with the plot and how quickly documents are produced. A clean plot is faster; a subdivided plot with unclear access takes longer."],
   ["Can I skip it if the seller seems trustworthy?", "No. Due diligence protects against problems the seller may not know about, as well as ones they do."]]},
 "th": {
  "title": "การตรวจสอบทรัพย์สิน (Due Diligence) ในประเทศไทย",
  "meta": "สิ่งที่ทนายความตรวจก่อนซื้อที่ดินไทย ทั้งเอกสารสิทธิ์ กรรมสิทธิ์ แนวเขต ทางเข้า ภาระผูกพัน ผังเมือง และข้อจำกัดการก่อสร้าง",
  "lead": "Due diligence คือขั้นตอนที่ที่ดินจะพิสูจน์ตัวเองหรือแตกหักเงียบ ๆ เป็นขั้นตอนที่ดูไม่น่าตื่นเต้นที่สุด แต่คุ้มค่าที่จะจ่ายมากที่สุด",
  "sections": [
   ("เอกสารสิทธิ์และกรรมสิทธิ์", [
    "ที่ดินในไทยถือครองด้วยเอกสารหลายประเภท ซึ่งให้สิทธิไม่เท่ากัน เอกสารที่แข็งแรงที่สุดคือโฉนดที่ดิน ส่วนเอกสารประเภทอื่นอาจจำกัดการโอนหรือการใช้ประโยชน์",
    "ทนายความจะตรวจสอบเอกสารที่สำนักงานที่ดิน ตรวจชื่อผู้ถือกรรมสิทธิ์เทียบกับเอกสารแสดงตน และดูประวัติของแปลงที่ดิน"]),
   ("แนวเขตและขนาด", [
    "ขนาดในเอกสารกับขนาดในพื้นที่จริงไม่ตรงกันเสมอไป โดยเฉพาะแปลงที่เคยแบ่งแยกหรือล้อมรั้วกันเอง การรังวัดจะช่วยคลี่คลาย",
    "สิ่งปลูกสร้าง กำแพง หรือทางรถของเพื่อนบ้านที่รุกล้ำ จัดการก่อนซื้อง่ายกว่าหลังซื้อ"]),
   ("ทางเข้า-ออก", [
    "ทางเข้าสู่ทางสาธารณะตามกฎหมาย ไม่เหมือนกับทางที่คนใช้กันมานาน ทางเข้าอาจขึ้นอยู่กับภาระจำยอมที่จดทะเบียน หรือขึ้นอยู่กับความยินยอมของเพื่อนบ้าน ซึ่งต่างกันมาก",
    "ความกว้างของทางเข้ายังมีผลต่อสิ่งที่สร้างได้ และรถก่อสร้างจะเข้าถึงได้หรือไม่"]),
   ("ภาระผูกพันและผังเมือง", [
    "จำนอง การอายัดตามคำสั่งศาล สิทธิเก็บกิน สัญญาเช่า และภาระจำยอม ล้วนจดทะเบียนไว้กับที่ดินและต้องตรวจสอบ",
    "ผังสีตามผังเมือง รวมถึงข้อกำหนดเรื่องความลาดชัน ระดับความสูง ระยะร่นจากแนวชายฝั่ง และความสูงอาคาร เป็นตัวกำหนดว่าสร้างอะไรได้ตามกฎหมาย ควรให้ผู้เชี่ยวชาญที่มีใบอนุญาตยืนยันก่อนซื้อ ไม่ใช่หลังซื้อ"]),
  ],
  "faq": [
   ["Due diligence ใช้เวลานานเท่าใด", "แตกต่างกันตามแปลงและความเร็วในการจัดหาเอกสาร แปลงที่เอกสารชัดเจนจะเร็วกว่า ส่วนแปลงที่เคยแบ่งแยกและทางเข้าไม่ชัดจะใช้เวลานานกว่า"],
   ["ถ้าผู้ขายดูน่าเชื่อถือ ข้ามขั้นตอนนี้ได้ไหม", "ไม่ได้ การตรวจสอบช่วยป้องกันทั้งปัญหาที่ผู้ขายรู้และที่ผู้ขายเองก็อาจไม่รู้"]]},
 "zh": {
  "title": "泰国房地产尽职调查",
  "meta": "购买泰国土地前律师会核查什么：权属、所有人、地界、通路、他项权利、规划与建设限制。",
  "lead": "尽职调查是地块自证或悄然出局的阶段。它是购买过程中最不光鲜、却最值得付费的一环。",
  "sections": [
   ("权属与所有人", [
    "泰国土地有多种权属文件，赋予的权利并不相同。最强的是完整地契；较弱的文件可能限制转让或使用。",
    "律师会在土地厅核实文件、将登记所有人与身份证件比对，并查阅该地块的历史。"]),
   ("地界与面积", [
    "纸面面积与现场面积未必一致，尤其是曾经分割或自行围合的地块。实地测量可以厘清。",
    "邻地建筑、围墙或车道的越界问题，在购买前处理远比购买后容易。"]),
   ("通行", [
    "法律上通往公共道路的通行权，与人们多年使用的小路并不相同。通路可能依赖登记的地役权，也可能只靠邻里默许，两者差别巨大。",
    "通路宽度还会影响可建内容以及施工车辆能否进场。"]),
   ("他项权利与规划", [
    "抵押、法院查封、用益权、租赁与地役权都会登记在土地上，必须核查。",
    "城市规划中的用地颜色，以及坡度、海拔、海岸退缩与建筑高度等规定，决定了合法可建的内容。请在购买前由持牌专业人士确认，而非购买之后。"]),
  ],
  "faq": [
   ["尽职调查需要多久？", "视地块情况与出具文件的速度而定。权属清晰的地块更快；曾分割且通路不明的地块更慢。"],
   ["如果卖方看起来可信，可以省略吗？", "不可以。尽职调查不仅防范卖方知情的问题，也防范其并不知情的问题。"]]}},

{
 "slug": "costs-of-buying-property-in-thailand",
 "updated": "2026-01-01",
 "en": {
  "title": "Costs of buying property in Thailand",
  "meta": "The cost categories to budget for beyond the purchase price: transfer taxes and fees, professional fees, survey, and ongoing holding costs.",
  "lead": "The purchase price is not the total cost. Budget for the categories below, and agree in writing who pays each one before you sign.",
  "sections": [
   ("Transfer taxes and fees", [
    "Transfers of land in Thailand attract government fees and taxes calculated at the Land Office, which can include a transfer fee, stamp duty or specific business tax, and withholding tax. Which apply, and at what rate, depends on the seller, how long the property has been held and the assessed value.",
    "Rates and rules change, and temporary measures are sometimes introduced. Ask your lawyer for a current calculation for your specific transaction rather than relying on figures found online."]),
   ("Who pays what", [
    "There is no fixed rule. Sharing of transfer costs is negotiable and should be stated in the contract. A price quoted as net to the seller means the buyer carries the costs."]),
   ("Professional costs", [
    "Legal fees for due diligence and contract work, survey fees if boundaries need confirming, translation and notarisation where required, and company formation or lease registration costs if your structure involves them."]),
   ("Holding and development costs", [
    "Land and building tax, maintenance and clearing of vacant land, and utility connection charges when you develop. Construction costs, permits and design fees sit on top of the land price for any project.",
    "For a project budget, treat land as one line among several rather than as the whole cost."]),
  ],
  "faq": [
   ["Can costs be estimated before I choose a plot?", "Broad categories, yes. Exact figures depend on the assessed value, the seller's position and the structure you use."]]},
 "th": {
  "title": "ค่าใช้จ่ายในการซื้ออสังหาริมทรัพย์ในประเทศไทย",
  "meta": "หมวดค่าใช้จ่ายที่ต้องตั้งงบนอกเหนือจากราคาซื้อ ทั้งภาษีและค่าธรรมเนียมการโอน ค่าวิชาชีพ ค่ารังวัด และค่าถือครอง",
  "lead": "ราคาซื้อไม่ใช่ต้นทุนทั้งหมด ควรตั้งงบตามหมวดด้านล่าง และตกลงเป็นลายลักษณ์อักษรว่าใครจ่ายส่วนใดก่อนลงนาม",
  "sections": [
   ("ภาษีและค่าธรรมเนียมการโอน", [
    "การโอนที่ดินในไทยมีค่าธรรมเนียมและภาษีที่คำนวณที่สำนักงานที่ดิน ซึ่งอาจรวมค่าธรรมเนียมการโอน อากรแสตมป์หรือภาษีธุรกิจเฉพาะ และภาษีหัก ณ ที่จ่าย รายการใดใช้บังคับและในอัตราเท่าใด ขึ้นอยู่กับตัวผู้ขาย ระยะเวลาถือครอง และราคาประเมิน",
    "อัตราและกฎเกณฑ์เปลี่ยนแปลงได้ และบางช่วงมีมาตรการชั่วคราว ควรให้ทนายความคำนวณตามธุรกรรมของคุณในปัจจุบัน แทนการอ้างอิงตัวเลขที่พบทางอินเทอร์เน็ต"]),
   ("ใครจ่ายอะไร", [
    "ไม่มีกฎตายตัว การแบ่งค่าใช้จ่ายในการโอนเป็นเรื่องเจรจาได้ และควรระบุไว้ในสัญญา หากเสนอราคาแบบสุทธิถึงมือผู้ขาย หมายความว่าผู้ซื้อรับภาระค่าใช้จ่ายทั้งหมด"]),
   ("ค่าวิชาชีพ", [
    "ค่าทนายความสำหรับการตรวจสอบและงานสัญญา ค่ารังวัดหากต้องยืนยันแนวเขต ค่าแปลเอกสารและรับรองเอกสารเท่าที่จำเป็น รวมถึงค่าจดทะเบียนบริษัทหรือจดทะเบียนสิทธิการเช่า หากโครงสร้างของคุณเกี่ยวข้อง"]),
   ("ค่าถือครองและค่าพัฒนา", [
    "ภาษีที่ดินและสิ่งปลูกสร้าง ค่าดูแลและถางที่ดินว่าง และค่าเชื่อมต่อสาธารณูปโภคเมื่อเริ่มพัฒนา ส่วนค่าก่อสร้าง ค่าขออนุญาต และค่าออกแบบ เป็นต้นทุนที่อยู่เหนือราคาที่ดินสำหรับทุกโครงการ",
    "ในการทำงบโครงการ ควรมองที่ดินเป็นเพียงหนึ่งบรรทัดในหลายบรรทัด ไม่ใช่ต้นทุนทั้งหมด"]),
  ],
  "faq": [
   ["ประเมินค่าใช้จ่ายก่อนเลือกแปลงได้ไหม", "ประเมินเป็นหมวดกว้าง ๆ ได้ แต่ตัวเลขที่แน่นอนขึ้นอยู่กับราคาประเมิน สถานะของผู้ขาย และโครงสร้างที่คุณใช้"]]},
 "zh": {
  "title": "在泰国购房的相关费用",
  "meta": "除成交价之外需要预留的费用：过户税费、专业服务费、测量费以及持有成本。",
  "lead": "成交价并不是全部成本。请按下列类别做预算，并在签约前书面约定各项由谁承担。",
  "sections": [
   ("过户税费", [
    "泰国土地过户需在土地厅缴纳政府规费与税款，可能包括过户费、印花税或特定营业税以及预扣税。适用哪些项目及税率，取决于卖方身份、持有年限与评估价值。",
    "税率与规则会变动，有时还有临时措施。请让律师就您的具体交易作出当期测算，而不要依赖网上查到的数字。"]),
   ("费用由谁承担", [
    "没有固定规则。过户费用的分摊可协商，并应写入合同。若报价为卖方净得价，则意味着买方承担全部费用。"]),
   ("专业服务费", [
    "尽职调查与合同工作的律师费；需要确认地界时的测量费；必要的翻译与公证费；若采用相关结构，还有公司设立或租赁登记费用。"]),
   ("持有与开发成本", [
    "土地与建筑税、空地维护清理费用，以及开发时的水电接入费。建造费、审批费与设计费则叠加在地价之上。",
    "编制项目预算时，应把土地视为若干项之一，而非全部成本。"]),
  ],
  "faq": [
   ["选地之前能估算费用吗？", "大类可以估算。确切数字取决于评估价值、卖方情况与您采用的结构。"]]}},

{
 "slug": "investing-in-phuket-property",
 "updated": "2026-01-01",
 "en": {
  "title": "Investing in Phuket property",
  "meta": "How to think about Phuket property as an investment: demand drivers, liquidity, costs, and the risks that are easy to overlook.",
  "lead": "Phuket attracts investors because demand comes from more than one direction. That does not make it a safe bet, and nothing on this site promises a return.",
  "sections": [
   ("What drives demand", [
    "Tourism, long-stay residents, remote workers, retirees and regional buyers all compete for property here, and they want different things. Tourism supports short-stay assets; residents support housing near schools and hospitals.",
    "Infrastructure changes — roads, the airport, utilities — shift where demand lands over time."]),
   ("Liquidity is the thing people underestimate", [
    "Land is not a liquid asset. Selling can take months, sometimes much longer, and the buyer pool for a specific plot may be small.",
    "This matters most if your plan depends on selling by a particular date."]),
   ("Costs eat returns", [
    "Transfer taxes, professional fees, holding costs, management and maintenance all reduce a gross number. Model the net position, not the headline."]),
   ("Risks worth naming", [
    "Regulatory change, construction delay, cost overrun, title problems discovered late, oversupply in one segment, and currency movement between your home currency and the baht.",
    "An honest agent will raise these before a sale rather than after. Benz will not publish guaranteed returns, because no one can guarantee them."]),
  ],
  "faq": [
   ["Is land or a built villa the better investment?", "They are different risk profiles. Land avoids construction risk but produces no income; a built asset can produce income and carries operating and maintenance obligations. Model both with your own adviser."]]},
 "th": {
  "title": "การลงทุนในอสังหาริมทรัพย์ภูเก็ต",
  "meta": "มุมมองการลงทุนอสังหาริมทรัพย์ภูเก็ต ทั้งปัจจัยด้านอุปสงค์ สภาพคล่อง ต้นทุน และความเสี่ยงที่มักถูกมองข้าม",
  "lead": "ภูเก็ตดึงดูดนักลงทุนเพราะอุปสงค์มาจากหลายทาง แต่นั่นไม่ได้แปลว่าปลอดภัย และเว็บไซต์นี้ไม่รับประกันผลตอบแทนใด ๆ",
  "sections": [
   ("อะไรขับเคลื่อนอุปสงค์", [
    "ทั้งการท่องเที่ยว ผู้พำนักระยะยาว คนทำงานทางไกล ผู้เกษียณ และผู้ซื้อในภูมิภาค ต่างแข่งกันหาอสังหาริมทรัพย์ที่นี่ และต้องการสิ่งที่ต่างกัน การท่องเที่ยวหนุนทรัพย์สินสำหรับพักระยะสั้น ส่วนผู้อยู่อาศัยหนุนที่อยู่อาศัยใกล้โรงเรียนและโรงพยาบาล",
    "การเปลี่ยนแปลงของโครงสร้างพื้นฐาน ทั้งถนน สนามบิน และสาธารณูปโภค ทำให้จุดที่อุปสงค์ลงไปเปลี่ยนไปตามเวลา"]),
   ("สภาพคล่องคือสิ่งที่คนประเมินต่ำเกินไป", [
    "ที่ดินไม่ใช่สินทรัพย์สภาพคล่องสูง การขายอาจใช้เวลาหลายเดือนหรือนานกว่านั้นมาก และกลุ่มผู้ซื้อสำหรับแปลงหนึ่ง ๆ อาจมีจำกัด",
    "ประเด็นนี้สำคัญที่สุดหากแผนของคุณต้องขายให้ได้ภายในเวลาที่กำหนด"]),
   ("ต้นทุนกินผลตอบแทน", [
    "ภาษีการโอน ค่าวิชาชีพ ค่าถือครอง ค่าบริหารจัดการ และค่าบำรุงรักษา ล้วนลดทอนตัวเลขรวม ควรคำนวณผลลัพธ์สุทธิ ไม่ใช่ตัวเลขพาดหัว"]),
   ("ความเสี่ยงที่ควรพูดถึงตรง ๆ", [
    "การเปลี่ยนแปลงกฎระเบียบ ความล่าช้าในการก่อสร้าง ต้นทุนบานปลาย ปัญหาเอกสารสิทธิ์ที่พบภายหลัง อุปทานล้นในบางเซกเมนต์ และความผันผวนของค่าเงินระหว่างสกุลเงินของคุณกับเงินบาท",
    "ตัวแทนที่ซื่อสัตย์จะพูดเรื่องเหล่านี้ก่อนการขาย ไม่ใช่หลังการขาย เบนซ์จะไม่ประกาศผลตอบแทนที่รับประกัน เพราะไม่มีใครรับประกันได้"]),
  ],
  "faq": [
   ["ลงทุนที่ดินเปล่าหรือวิลล่าที่สร้างแล้วดีกว่ากัน", "ความเสี่ยงคนละแบบ ที่ดินเปล่าไม่มีความเสี่ยงการก่อสร้างแต่ไม่สร้างรายได้ ส่วนทรัพย์ที่สร้างแล้วอาจมีรายได้แต่มีภาระการดำเนินงานและบำรุงรักษา ควรคำนวณทั้งสองแบบกับที่ปรึกษาของคุณ"]]},
 "zh": {
  "title": "投资普吉房地产",
  "meta": "如何看待普吉房地产投资：需求来源、流动性、成本，以及容易被忽视的风险。",
  "lead": "普吉吸引投资者，是因为需求来自多个方向。但这并不意味着稳赚，本网站也不承诺任何回报。",
  "sections": [
   ("需求从何而来", [
    "旅游客群、长居住户、远程工作者、退休人士与区域买家都在争夺这里的房产，而他们的需求各不相同。旅游支撑短租资产；常住人口支撑靠近学校与医院的住宅。",
    "道路、机场与市政配套等基础设施的变化，会随时间改变需求的落点。"]),
   ("最被低估的是流动性", [
    "土地并非流动性资产。出售可能耗时数月甚至更久，某一具体地块的潜在买家群体也可能很小。",
    "如果您的计划依赖在某个时点前卖出，这一点尤其关键。"]),
   ("成本侵蚀回报", [
    "过户税费、专业服务费、持有成本、管理与维护都会削减毛收益。请测算净额，而不是看表面数字。"]),
   ("应当明说的风险", [
    "法规变化、工期延误、成本超支、后期才发现的权属问题、某一细分市场供应过剩，以及本币与泰铢之间的汇率波动。",
    "诚实的代理会在成交前而非成交后提出这些问题。Benz 不会发布保证回报，因为没有人能够保证。"]),
  ],
  "faq": [
   ["买地还是买建好的别墅更好？", "两者风险特征不同。土地没有施工风险但也不产生收入；建成资产可能有收入，但伴随运营与维护义务。请与您的顾问分别测算。"]]}},

{
 "slug": "best-areas-to-invest-in-phuket",
 "updated": "2026-01-01",
 "en": {
  "title": "Best areas to invest in Phuket",
  "meta": "How Phuket's main areas differ for buyers: west coast beaches, Thalang, the south and Phuket Town, and what each suits.",
  "lead": "There is no single best area — only areas that suit a particular plan. Here is how buyers usually narrow it down.",
  "sections": [
   ("North-west: Cherng Talay, Bang Tao, Layan", [
    "The most developed part of the island for foreign residents, with schools, shops and beach clubs close together. Land is priced accordingly and supply near the beach is tight.",
    "Suits: villa projects, family homes, assets where rental demand and resale liquidity matter."]),
   ("Thalang and the north", [
    "Where larger parcels still exist, with the airport in the district. More agricultural and residential zoning, and a wider spread of title types.",
    "Suits: resort and estate development, buyers with a longer horizon."]),
   ("West coast: Kamala, Karon, Kata", [
    "Beach towns with hillside land and tourism-led demand. Slope and access drive build cost.",
    "Suits: sea-view homes, boutique projects, tourism-facing use where regulations allow."]),
   ("South: Rawai, Nai Harn, Chalong", [
    "Residential in character, with an established foreign community and generally more accessible pricing than the central west coast.",
    "Suits: long-term living, smaller homes, buyers who prefer a quieter setting."]),
   ("Phuket Town and the east", [
    "Everyday Phuket: schools, hospitals, offices, marinas. Less beach-driven, more service-driven.",
    "Suits: commercial use, residential rental to residents, mixed-use plots."]),
  ],
  "faq": [
   ["Which area appreciates fastest?", "No one can tell you that reliably, and anyone who does is guessing. Choose on the basis of what you want to build and how long you will hold it."]]},
 "th": {
  "title": "ทำเลลงทุนที่น่าสนใจในภูเก็ต",
  "meta": "ความต่างของทำเลหลักในภูเก็ตสำหรับผู้ซื้อ ทั้งหาดฝั่งตะวันตก ถลาง ภาคใต้ของเกาะ และเมืองภูเก็ต ว่าแต่ละแห่งเหมาะกับอะไร",
  "lead": "ไม่มีทำเลที่ดีที่สุดเพียงหนึ่งเดียว มีแต่ทำเลที่เหมาะกับแผนแบบหนึ่ง ๆ นี่คือวิธีที่ผู้ซื้อมักใช้คัดกรอง",
  "sections": [
   ("ตะวันตกเฉียงเหนือ: เชิงทะเล บางเทา ลายัน", [
    "พื้นที่ที่พัฒนามากที่สุดสำหรับผู้พำนักชาวต่างชาติ ทั้งโรงเรียน ร้านค้า และบีชคลับอยู่ใกล้กัน ราคาที่ดินจึงสูงตาม และอุปทานใกล้หาดมีจำกัด",
    "เหมาะกับ: โครงการวิลล่า บ้านครอบครัว และทรัพย์สินที่ต้องการอุปสงค์เช่าและสภาพคล่องในการขายต่อ"]),
   ("ถลางและตอนเหนือ", [
    "พื้นที่ที่ยังมีแปลงใหญ่เหลืออยู่ และมีสนามบินอยู่ในอำเภอ ผังเกษตรกรรมและที่อยู่อาศัยมีมาก ประเภทเอกสารสิทธิ์หลากหลายกว่า",
    "เหมาะกับ: การพัฒนารีสอร์ตและโครงการขนาดใหญ่ ผู้ซื้อที่มองระยะยาว"]),
   ("ฝั่งตะวันตก: กมลา กะรน กะตะ", [
    "เมืองหาดที่มีที่ดินบนเนินเขาและอุปสงค์จากการท่องเที่ยว ความลาดชันและทางเข้ามีผลต่อค่าก่อสร้าง",
    "เหมาะกับ: บ้านวิวทะเล โครงการบูทีค และการใช้ประโยชน์เพื่อการท่องเที่ยวเท่าที่กฎหมายอนุญาต"]),
   ("ตอนใต้: ราไวย์ ในหาน ฉลอง", [
    "มีลักษณะเป็นย่านที่อยู่อาศัย มีชุมชนชาวต่างชาติที่ตั้งถิ่นฐานมานาน และราคาโดยทั่วไปเข้าถึงง่ายกว่าฝั่งตะวันตกตอนกลาง",
    "เหมาะกับ: การอยู่อาศัยระยะยาว บ้านขนาดไม่ใหญ่ ผู้ที่ชอบความเงียบสงบ"]),
   ("เมืองภูเก็ตและฝั่งตะวันออก", [
    "ภูเก็ตในชีวิตประจำวัน ทั้งโรงเรียน โรงพยาบาล สำนักงาน และมารีน่า ขับเคลื่อนด้วยบริการมากกว่าชายหาด",
    "เหมาะกับ: การใช้เชิงพาณิชย์ การปล่อยเช่าให้ผู้อยู่อาศัย และแปลงแบบผสมผสาน"]),
  ],
  "faq": [
   ["ทำเลไหนราคาขึ้นเร็วที่สุด", "ไม่มีใครบอกได้อย่างน่าเชื่อถือ ใครที่ตอบได้คือการเดา ควรเลือกจากสิ่งที่คุณต้องการสร้างและระยะเวลาที่จะถือครอง"]]},
 "zh": {
  "title": "普吉值得关注的投资区域",
  "meta": "普吉主要区域的差异：西海岸海滩、他朗、南部与普吉镇，各自适合哪类买家。",
  "lead": "没有唯一“最好”的区域，只有契合特定计划的区域。以下是买家常用的筛选思路。",
  "sections": [
   ("西北部：青塔莱、邦涛、拉扬", [
    "外籍居民最集中的成熟区域，学校、商店与海滩俱乐部彼此邻近。地价相应较高，近海供应紧张。",
    "适合：别墅项目、家庭住宅，以及看重租赁需求与转售流动性的资产。"]),
   ("他朗与北部", [
    "仍有大面积地块，机场位于该区。农业与住宅规划较多，权属类型也更多样。",
    "适合：度假村与社区开发，以及时间周期较长的买家。"]),
   ("西海岸：卡马拉、卡伦、卡塔", [
    "以旅游需求为主的海滨城镇，山坡地较多。坡度与通路直接影响建造成本。",
    "适合：海景住宅、精品项目，以及法规允许范围内面向旅游的用途。"]),
   ("南部：拉威、奈汉、查龙", [
    "以住宅为主，外籍社区成熟，整体价格通常比西海岸中部更易接受。",
    "适合：长期居住、中小型住宅，以及偏好安静环境的买家。"]),
   ("普吉镇与东部", [
    "日常生活的普吉：学校、医院、写字楼与游艇码头。更依赖服务业而非海滩。",
    "适合：商业用途、面向常住人口的住宅出租，以及综合用途地块。"]),
  ],
  "faq": [
   ["哪个区域升值最快？", "没有人能可靠地回答，给出答案的多半是猜测。请依据您要建什么、打算持有多久来选择。"]]}},

{
 "slug": "land-development-opportunities-in-phuket",
 "updated": "2026-01-01",
 "en": {
  "title": "Land development opportunities in Phuket",
  "meta": "What makes a Phuket plot developable: size and shape, slope, access width, utilities, zoning and approvals.",
  "lead": "Two plots with the same price and size can have completely different development value. These are the factors that separate them.",
  "sections": [
   ("Shape, size and frontage", [
    "A long narrow plot and a square plot of the same area produce very different layouts. Road frontage affects entrances, visibility and how many units a layout can support."]),
   ("Slope", [
    "Slope adds retaining works, drainage and access engineering. It can also add view value. Thailand restricts building on land above certain gradients and elevations, so slope is a legal question as well as a cost question."]),
   ("Access", [
    "Access width determines whether construction vehicles can reach the site and what can be permitted. A shared or unregistered access route is a material risk that should be resolved before purchase."]),
   ("Utilities", [
    "Power capacity, water supply and drainage all need checking against the size of your project. Upgrading capacity takes time and money and should be priced in early."]),
   ("Zoning and approvals", [
    "Zoning colour under the town plan, environmental requirements for larger projects, and building permits all shape the programme. Talk to an architect before you commit, not after."]),
  ],
  "faq": [
   ["Can Benz tell me if a plot supports my project?", "He can gather the documents and show you the site honestly. Whether a design is permitted is confirmed by a licensed architect and lawyer."]]},
 "th": {
  "title": "โอกาสในการพัฒนาที่ดินในภูเก็ต",
  "meta": "ปัจจัยที่ทำให้ที่ดินภูเก็ตพัฒนาได้ ทั้งขนาดและรูปร่าง ความลาดชัน ความกว้างทางเข้า สาธารณูปโภค ผังสี และการขออนุญาต",
  "lead": "ที่ดินสองแปลงราคาและขนาดเท่ากัน อาจมีมูลค่าเชิงพัฒนาต่างกันโดยสิ้นเชิง นี่คือปัจจัยที่แยกทั้งสองออกจากกัน",
  "sections": [
   ("รูปร่าง ขนาด และหน้ากว้างติดถนน", [
    "แปลงยาวแคบกับแปลงสี่เหลี่ยมที่มีพื้นที่เท่ากัน ให้ผังโครงการที่ต่างกันมาก หน้ากว้างติดถนนมีผลต่อทางเข้า การมองเห็น และจำนวนยูนิตที่ผังรองรับได้"]),
   ("ความลาดชัน", [
    "ความลาดชันเพิ่มงานกำแพงกันดิน ระบบระบายน้ำ และงานวิศวกรรมทางเข้า ขณะเดียวกันก็อาจเพิ่มมูลค่าจากวิว ประเทศไทยมีข้อจำกัดการก่อสร้างบนพื้นที่ที่มีความลาดชันและระดับความสูงเกินกำหนด ความลาดชันจึงเป็นทั้งประเด็นกฎหมายและต้นทุน"]),
   ("ทางเข้า-ออก", [
    "ความกว้างของทางเข้าเป็นตัวกำหนดว่ารถก่อสร้างเข้าถึงได้หรือไม่ และขออนุญาตอะไรได้บ้าง ทางเข้าที่เป็นทางร่วมหรือไม่ได้จดทะเบียนคือความเสี่ยงสำคัญที่ควรแก้ให้จบก่อนซื้อ"]),
   ("สาธารณูปโภค", [
    "กำลังไฟฟ้า แหล่งน้ำ และการระบายน้ำ ต้องตรวจเทียบกับขนาดโครงการ การเพิ่มกำลังต้องใช้เวลาและเงิน ควรคิดต้นทุนไว้ตั้งแต่ต้น"]),
   ("ผังเมืองและการอนุญาต", [
    "ผังสีตามผังเมือง ข้อกำหนดด้านสิ่งแวดล้อมสำหรับโครงการขนาดใหญ่ และใบอนุญาตก่อสร้าง ล้วนกำหนดรูปแบบโครงการ ควรคุยกับสถาปนิกก่อนตัดสินใจ ไม่ใช่หลังจากนั้น"]),
  ],
  "faq": [
   ["เบนซ์บอกได้ไหมว่าที่ดินรองรับโครงการของผมได้", "เบนซ์รวบรวมเอกสารและพาดูพื้นที่ตามจริงได้ ส่วนแบบที่เสนอจะขออนุญาตได้หรือไม่ ต้องให้สถาปนิกและทนายความที่มีใบอนุญาตเป็นผู้ยืนยัน"]]},
 "zh": {
  "title": "普吉的土地开发机会",
  "meta": "决定普吉地块可开发性的因素：面积与形状、坡度、通路宽度、市政配套、规划与审批。",
  "lead": "价格与面积相同的两块地，开发价值可能天差地别。以下就是区分它们的因素。",
  "sections": [
   ("形状、面积与临路面", [
    "同样面积下，狭长地块与方正地块能做出的布局完全不同。临路宽度影响出入口、可见性以及布局可容纳的户数。"]),
   ("坡度", [
    "坡度带来挡土、排水与进场工程的额外成本，同时也可能带来景观溢价。泰国对超过一定坡度与海拔的土地建设设有限制，因此坡度既是成本问题，也是法律问题。"]),
   ("通行", [
    "通路宽度决定施工车辆能否进场以及可获批的内容。共用或未登记的通路是重大风险，应在购买前解决。"]),
   ("市政配套", [
    "电力容量、供水与排水都需对照项目规模核查。扩容既费时又费钱，应尽早计入成本。"]),
   ("规划与审批", [
    "城市规划的用地颜色、大型项目的环境要求以及建筑许可，都会塑造项目方案。请在决定前而非之后与建筑师沟通。"]),
  ],
  "faq": [
   ["Benz 能判断某地块是否支持我的项目吗？", "他可以收集文件并如实带您看现场。设计方案是否获准，须由持牌建筑师与律师确认。"]]}},

{
 "slug": "things-to-check-before-buying-land-in-phuket",
 "updated": "2026-01-01",
 "en": {
  "title": "Things to check before buying land in Phuket",
  "meta": "A checklist to take to every Phuket land viewing: title, boundaries, access, water, power, neighbours, flooding and zoning.",
  "lead": "Take this list with you on every viewing. If an answer is missing, that is information too.",
  "sections": [
   ("On the documents", [
    "Which title document covers this plot, and what rights does it carry? Who is the registered owner, and is that person selling? Is anything registered against the land — mortgage, lease, servitude, seizure? Does the registered area match what is being sold?"]),
   ("On the ground", [
    "Where do the boundaries actually run? Is the access road public, private or shared, and how wide is it? Is there mains power and water at the boundary, and at what capacity? Which way does the ground slope, and where does water go in heavy rain?"]),
   ("Around the plot", [
    "What is on the neighbouring land now, and what could be built there? Is there a quarry, a temple, a school, a nightclub, a planned road? Visit at different times of day if you can."]),
   ("On the plan", [
    "What is the zoning colour and what does it permit? Are there slope, elevation or height restrictions here? Does your intended use require a licence — a hotel licence, for example — and is that route realistic for this plot?"]),
   ("Before you pay", [
    "Has your own lawyer reviewed the contract? Is it clear what happens to the deposit if due diligence fails? Have transfer costs been allocated in writing?"]),
  ],
  "faq": [
   ["What if the seller cannot answer these questions?", "That is not automatically a reason to walk away, but it is a reason to slow down and let your lawyer investigate before any money moves."]]},
 "th": {
  "title": "สิ่งที่ต้องตรวจก่อนซื้อที่ดินในภูเก็ต",
  "meta": "เช็กลิสต์สำหรับพกไปดูที่ดินทุกครั้ง ทั้งเอกสารสิทธิ์ แนวเขต ทางเข้า น้ำ ไฟ เพื่อนบ้าน น้ำท่วม และผังเมือง",
  "lead": "พกรายการนี้ไปทุกครั้งที่ไปดูที่ดิน หากคำถามใดไม่มีคำตอบ นั่นก็คือข้อมูลอย่างหนึ่ง",
  "sections": [
   ("ด้านเอกสาร", [
    "แปลงนี้ใช้เอกสารสิทธิ์ประเภทใด และให้สิทธิอะไรบ้าง ผู้ถือกรรมสิทธิ์คือใคร และเป็นคนที่กำลังขายหรือไม่ มีอะไรจดทะเบียนไว้กับที่ดินหรือไม่ เช่น จำนอง สัญญาเช่า ภาระจำยอม หรือการอายัด และเนื้อที่ตามทะเบียนตรงกับที่เสนอขายหรือไม่"]),
   ("ด้านพื้นที่จริง", [
    "แนวเขตจริงอยู่ตรงไหน ถนนเข้าเป็นทางสาธารณะ ทางส่วนบุคคล หรือทางร่วม และกว้างเท่าใด มีไฟฟ้าและน้ำประปาถึงแนวเขตหรือไม่ กำลังเท่าใด พื้นที่ลาดไปทางใด และน้ำไหลไปทางไหนเมื่อฝนตกหนัก"]),
   ("รอบแปลงที่ดิน", [
    "ตอนนี้ที่ดินข้างเคียงเป็นอะไร และอนาคตสร้างอะไรได้บ้าง มีบ่อหิน วัด โรงเรียน สถานบันเทิง หรือแนวถนนตามผังหรือไม่ ถ้าทำได้ ควรไปดูหลายช่วงเวลาของวัน"]),
   ("ด้านผังเมือง", [
    "ผังสีคืออะไร และอนุญาตให้ทำอะไรได้ มีข้อจำกัดเรื่องความลาดชัน ระดับความสูง หรือความสูงอาคารหรือไม่ การใช้ประโยชน์ที่คุณต้องการจำเป็นต้องมีใบอนุญาตหรือไม่ เช่น ใบอนุญาตโรงแรม และแนวทางนั้นเป็นไปได้จริงกับแปลงนี้หรือไม่"]),
   ("ก่อนจ่ายเงิน", [
    "ทนายความของคุณตรวจสัญญาแล้วหรือยัง ระบุชัดหรือไม่ว่าหากตรวจสอบไม่ผ่าน เงินมัดจำจะเป็นอย่างไร และตกลงเรื่องค่าใช้จ่ายในการโอนเป็นลายลักษณ์อักษรแล้วหรือยัง"]),
  ],
  "faq": [
   ["ถ้าผู้ขายตอบคำถามเหล่านี้ไม่ได้ควรทำอย่างไร", "ไม่ได้แปลว่าต้องถอยทันที แต่เป็นเหตุผลให้ชะลอและให้ทนายความตรวจสอบก่อนที่เงินจะเคลื่อนไหว"]]},
 "zh": {
  "title": "在普吉买地前要核查的事项",
  "meta": "每次看地都应带上的清单：权属、地界、通路、供水、供电、邻地、排涝与规划。",
  "lead": "每次看地都带上这份清单。若某个问题没有答案，这本身也是一种信息。",
  "sections": [
   ("文件方面", [
    "这块地属于哪种权属文件，赋予哪些权利？登记所有人是谁，是否即为出售人？土地上是否登记了抵押、租赁、地役权或查封？登记面积与出售面积是否一致？"]),
   ("现场方面", [
    "实际地界在哪里？进场道路是公共、私人还是共用，宽度多少？红线处是否已有市电与自来水，容量如何？地势朝哪个方向倾斜，暴雨时水往何处排？"]),
   ("周边环境", [
    "邻地现在是什么，未来可能建什么？附近有无采石场、寺庙、学校、夜店或规划道路？条件允许的话，请在一天中的不同时段各去一次。"]),
   ("规划方面", [
    "用地颜色是什么，允许什么用途？此处是否有坡度、海拔或高度限制？您计划的用途是否需要牌照（例如酒店牌照），该路径对这块地是否现实？"]),
   ("付款之前", [
    "您自己的律师审过合同了吗？若尽职调查未通过，定金如何处理是否写明？过户费用分担是否已书面约定？"]),
  ],
  "faq": [
   ["如果卖方回答不了这些问题怎么办？", "这未必意味着立刻放弃，但确实应当放慢节奏，在任何资金往来之前让律师先行核查。"]]}},
]
