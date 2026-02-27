# Wakala wa AI kwa Waanzilishi - Mwongozo wa Kusoma na Muhtasari wa Kozi

Mwongozo huu unatoa muhtasari wa kozi ya "Wakala wa AI kwa Waanzilishi" na kueleza dhana kuu, mifumo, na mifano ya kubuni kwa ajili ya kutengeneza Wakala wa AI.

## 1. Utangulizi wa Wakala wa AI

**Wakala wa AI ni Nini?**  
Wakala wa AI ni mifumo inayoongeza uwezo wa Mifano Mikubwa ya Lugha (LLMs) kwa kuwapa **vyombo**, **maarifa**, na **kumbukumbu**. Tofauti na chatbot ya kawaida ya LLM inayozalisha maandishi tu kwa msingi wa data za mafunzo, Wakala wa AI anaweza:  
- **Kugundua** mazingira yake (kupitia sensa au pembejeo).  
- **Kufikiria** jinsi ya kutatua tatizo.  
- **Kufanya** ili kubadilisha mazingira (kupitia vimozo au utekelezaji wa zana).

**Vipengele Muhimu vya Wakala:**  
- **Mazingira**: Eneo ambapo wakala hufanya kazi (mfano: mfumo wa uhifadhi wa booking).  
- **Sensa**: Vifaa vya kukusanya taarifa (mfano: kusoma API).  
- **Vimozo**: Vifaa vya kufanya vitendo (mfano: kutuma barua pepe).  
- **Ubongo (LLM)**: Injini ya kufikiri inayopanga na kuamua vitendo gani kuchukua.

## 2. Mifumo ya Wakala

Kozi inatumia **Microsoft Agent Framework (MAF)** pamoja na **Azure AI Foundry Agent Service V2** kwa ajili ya kujenga wakala:

| Kipengele | Lengo | Bora Kwa |
|-----------|-------|-----------|
| **Microsoft Agent Framework** | SDK ya Python/C# iliyounganishwa kwa wakala, vyombo, na taratibu za kazi | Kujenga wakala wenye vyombo, taratibu za wakala wengi, na mifano ya ujenzi wa mfumo. |  
| **Azure AI Foundry Agent Service** | Mzigo wa usimamizi wa wingu | Usambazaji salama, wenye ukubwa, wenye usimamizi wa hali, ufuatiliaji, na kuaminika. |

## 3. Mifano ya Ubunifu wa Wakala

Mifano ya ubunifu husaidia kupanga jinsi wakala wanavyoendesha kazi ili kutatua matatizo kwa uhakika.

### **Mfano wa Matumizi ya Zana** (Somo la 4)  
Mfano huu unamruhusu wakala kuingiliana na mazingira ya nje.  
- **Dhana**: Wakala anapewa "mchoro muundo" (orodha ya shughuli zinazopatikana na vigezo vyake). LLM huamua *zi* zana gani ya kuitisha na kwa hujia *gani* kulingana na ombi la mtumiaji.  
- **Mtiririko**: Ombi la Mtumiaji -> LLM -> **Uchague wa Zana** -> **Utekelezaji wa Zana** -> LLM (ikiwa na matokeo ya zana) -> Jibu la Mwisho.  
- **Matumizi**: Kupata data ya wakati halisi (hali ya hewa, bei za hisa), kufanya mahesabu, kuendesha msimbo.

### **Mfano wa Mipango** (Somo la 7)  
Mfano huu unaruhusu wakala kutatua kazi ngumu zenye hatua nyingi.  
- **Dhana**: Wakala hugawanya lengo kuu kuwa mfululizo wa kazi ndogo ndogo.  
- **Mbinu**:  
  - **Ugawaji wa Kazi**: Kugawanya "Panga safari" kuwa "Hifadhi ndege", "Hifadhi hoteli", "Kodi gari".  
  - **Mipango Inayorudiwa**: Kurekebisha mpango kwa mujibu wa matokeo ya hatua zilizopita (mfano, kama ndege imejaa, chagua tarehe nyingine).  
- **Utekelezaji**: Mara nyingi inahusisha wakala "Mpangaji" anayetengeneza mpango ulio na muundo (mfano, JSON) kisha utekelezwe na wakala wengine.

## 4. Kanuni za Ubunifu

Unapobuni wakala, chukua vipengele vitatu:  
- **Eneo**: Wakala wanapaswa kuunganisha watu na maarifa, waweze kupatikana lakini wasionekane sana.  
- **Wakati**: Wakala wanapaswa kujifunza kutoka *Zamani*, kutoa msukumo unaohitajika *Sasa*, na kubadilika kwa ajili ya *Baadaye*.  
- **Msingi**: Kubali kutokuwa na uhakika lakini anzisha uaminifu kupitia uwazi na udhibiti wa mtumiaji.

## 5. Muhtasari wa Masomo Muhimu

- **Somo 1**: Wakala ni mifumo, si mifano tu. Wanagundua, kufikiri, na kufanya.  
- **Somo 2**: Microsoft Agent Framework hupunguza ugumu wa kuita zana na usimamizi wa hali.  
- **Somo 3**: Buni kwa uwazi na udhibiti wa mtumiaji akilini.  
- **Somo 4**: Vyombo ni "mikono" ya wakala. Ufafanuzi wa mchoro ni muhimu kwa LLM kuelewa jinsi ya kuvitumia.  
- **Somo 7**: Upangaji ni "kazi ya utendaji" ya wakala, ikimruhusu kushughulikia taratibu ngumu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Taarifa ya Kukataa**:
Hati hii imefasiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kuwa tafsiri za moja kwa moja zinaweza kuwa na makosa au ukosefu wa usahihi. Hati ya asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa habari muhimu, tafsiri ya kitaalamu ya binadamu inashauriwa. Hatubeba dhamana kwa maelewano mabaya au tafsiri potovu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->