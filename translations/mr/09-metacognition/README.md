<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-29T09:58:04+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "mr"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.mr.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(वरील प्रतिमेवर क्लिक करून या धड्याचा व्हिडिओ पहा)_
# AI एजंट्समधील मेटाकॉग्निशन

## परिचय

AI एजंट्समधील मेटाकॉग्निशन या धड्यात आपले स्वागत आहे! हा अध्याय नवशिक्यांसाठी तयार केला आहे, ज्यांना AI एजंट्स त्यांच्या स्वतःच्या विचार प्रक्रियेबद्दल कसे विचार करू शकतात हे जाणून घ्यायचे आहे. या धड्याच्या शेवटी, तुम्हाला महत्त्वाच्या संकल्पना समजतील आणि AI एजंट डिझाइनमध्ये मेटाकॉग्निशन लागू करण्यासाठी व्यावहारिक उदाहरणे मिळतील.

## शिकण्याची उद्दिष्टे

हा धडा पूर्ण केल्यानंतर, तुम्ही हे करू शकाल:

1. एजंटच्या व्याख्यांमधील विचारमंथन लूप्सचे परिणाम समजून घ्या.
2. स्वतःला सुधारणा करणाऱ्या एजंट्ससाठी नियोजन आणि मूल्यमापन तंत्रांचा वापर करा.
3. कोड हाताळून कार्य पूर्ण करू शकणारे स्वतःचे एजंट तयार करा.

## मेटाकॉग्निशनची ओळख

मेटाकॉग्निशन म्हणजे स्वतःच्या विचारांबद्दल विचार करण्यासंबंधित उच्च-स्तरीय संज्ञानात्मक प्रक्रिया. AI एजंट्ससाठी, याचा अर्थ स्वतःच्या कृतींचे मूल्यांकन करणे आणि आत्म-जागरूकता व भूतकाळातील अनुभवांवर आधारित त्यांना समायोजित करणे. मेटाकॉग्निशन, किंवा "विचारांबद्दल विचार करणे," हे एजंटिक AI प्रणालींच्या विकासातील एक महत्त्वाचे संकल्पन आहे. यामध्ये AI प्रणालींना त्यांच्या स्वतःच्या अंतर्गत प्रक्रियांची जाणीव असणे आणि त्यांच्या वर्तनाचे निरीक्षण, नियमन आणि अनुकूलन करण्यास सक्षम असणे समाविष्ट आहे. जसे आपण एखाद्या परिस्थितीचे निरीक्षण करतो किंवा समस्येचा विचार करतो. ही आत्म-जागरूकता AI प्रणालींना चांगले निर्णय घेण्यास, चुका ओळखण्यास आणि वेळोवेळी त्यांची कार्यक्षमता सुधारण्यास मदत करू शकते—पुन्हा ट्यूरिंग चाचणी आणि AI जगावर नियंत्रण मिळवेल का यावरील चर्चेशी जोडलेले.

एजंटिक AI प्रणालींच्या संदर्भात, मेटाकॉग्निशन अनेक आव्हानांना सामोरे जाण्यास मदत करू शकते, जसे की:
- पारदर्शकता: AI प्रणाली त्यांच्या विचारसरणी आणि निर्णय स्पष्ट करू शकतील याची खात्री करणे.
- विचारमंथन: AI प्रणालींना माहितीचे संश्लेषण करण्याची आणि योग्य निर्णय घेण्याची क्षमता वाढवणे.
- अनुकूलता: AI प्रणालींना नवीन वातावरण आणि बदलत्या परिस्थितींशी जुळवून घेण्याची परवानगी देणे.
- आकलन: AI प्रणालींना त्यांच्या वातावरणातील डेटा ओळखण्यात आणि त्याचे विश्लेषण करण्यात अचूकता सुधारणे.

### मेटाकॉग्निशन म्हणजे काय?

मेटाकॉग्निशन, किंवा "विचारांबद्दल विचार करणे," ही एक उच्च-स्तरीय संज्ञानात्मक प्रक्रिया आहे जी स्वतःच्या संज्ञानात्मक प्रक्रियांची आत्म-जाणीव आणि आत्म-नियमन समाविष्ट करते. AI च्या क्षेत्रात, मेटाकॉग्निशन एजंट्सना त्यांच्या रणनीती आणि कृतींचे मूल्यांकन आणि अनुकूलन करण्यास सक्षम करते, ज्यामुळे समस्या सोडवण्याची आणि निर्णय घेण्याची क्षमता सुधारते. मेटाकॉग्निशन समजून घेऊन, तुम्ही असे AI एजंट्स डिझाइन करू शकता जे केवळ अधिक बुद्धिमानच नाहीत तर अधिक अनुकूल आणि कार्यक्षम देखील आहेत. खऱ्या मेटाकॉग्निशनमध्ये, तुम्हाला AI स्वतःच्या विचारांबद्दल स्पष्टपणे विचार करताना दिसेल.

उदाहरण: “मी स्वस्त फ्लाइट्सला प्राधान्य दिले कारण... कदाचित मी थेट फ्लाइट्स गमावत असेन, म्हणून मला पुन्हा तपासू द्या.”
एखाद्या विशिष्ट मार्गाची निवड का केली याचा मागोवा ठेवणे.
- हे लक्षात घेणे की मागील वेळेच्या वापरकर्ता प्राधान्यांवर जास्त अवलंबून राहिल्यामुळे चुका झाल्या, त्यामुळे अंतिम शिफारसीतच नव्हे तर निर्णय घेण्याच्या पद्धतीत बदल करणे.
- नमुने निदान करणे, जसे की, “जेव्हा जेव्हा वापरकर्ता ‘खूप गर्दी’चा उल्लेख करतो, तेव्हा मला केवळ विशिष्ट आकर्षणे काढून टाकायची नाहीत तर माझी ‘शीर्ष आकर्षणे’ निवडण्याची पद्धत दोषपूर्ण आहे हे देखील प्रतिबिंबित करणे आवश्यक आहे, जर मी नेहमी लोकप्रियतेनुसार क्रमवारी लावतो.”

### AI एजंट्समध्ये मेटाकॉग्निशनचे महत्त्व

AI एजंट डिझाइनमध्ये मेटाकॉग्निशन अनेक कारणांसाठी महत्त्वाची भूमिका बजावते:

![मेटाकॉग्निशनचे महत्त्व](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.mr.png)

- आत्म-चिंतन: एजंट्स त्यांच्या स्वतःच्या कामगिरीचे मूल्यांकन करू शकतात आणि सुधारणा करण्याच्या क्षेत्रांची ओळख पटवू शकतात.
- अनुकूलता: एजंट्स भूतकाळातील अनुभव आणि बदलत्या वातावरणावर आधारित त्यांच्या रणनीतींमध्ये बदल करू शकतात.
- त्रुटी सुधारणा: एजंट्स स्वयंचलितपणे चुका शोधू आणि सुधारू शकतात, ज्यामुळे अधिक अचूक परिणाम मिळतात.
- संसाधन व्यवस्थापन: एजंट्स त्यांच्या कृतींचे नियोजन आणि मूल्यांकन करून वेळ आणि संगणकीय शक्ती यासारख्या संसाधनांचा वापर अनुकूल करू शकतात.

## AI एजंटचे घटक

मेटाकॉग्निटिव्ह प्रक्रियांमध्ये जाण्यापूर्वी, AI एजंटचा मूलभूत घटक समजून घेणे आवश्यक आहे. AI एजंट सामान्यतः यांचा समावेश असतो:

- व्यक्तिमत्त्व: एजंटची व्यक्तिमत्त्व आणि वैशिष्ट्ये, जी वापरकर्त्यांसोबत कसे संवाद साधतात हे परिभाषित करतात.
- साधने: एजंट करू शकणाऱ्या क्षमता आणि कार्ये.
- कौशल्ये: एजंटकडे असलेले ज्ञान आणि कौशल्य.

हे घटक एकत्र काम करून "तज्ज्ञता युनिट" तयार करतात जे विशिष्ट कार्ये करू शकतात.

**उदाहरण**:
एका प्रवास एजंटचा विचार करा, जो केवळ तुमच्या सुट्ट्यांचे नियोजन करत नाही तर रिअल-टाइम डेटा आणि भूतकाळातील ग्राहक प्रवास अनुभवांवर आधारित त्याचा मार्ग समायोजित करतो.

### उदाहरण: प्रवास एजंट सेवेमध्ये मेटाकॉग्निशन

कल्पना करा की तुम्ही AI समर्थित प्रवास एजंट सेवा डिझाइन करत आहात. हा एजंट, "प्रवास एजंट," वापरकर्त्यांना त्यांच्या सुट्ट्यांचे नियोजन करण्यात मदत करतो. मेटाकॉग्निशन समाविष्ट करण्यासाठी, प्रवास एजंटला आत्म-जागरूकता आणि भूतकाळातील अनुभवांवर आधारित त्याच्या कृतींचे मूल्यांकन आणि समायोजन करणे आवश्यक आहे. मेटाकॉग्निशन कसे भूमिका बजावू शकते ते येथे आहे:

#### चालू कार्य

सध्याचे कार्य म्हणजे वापरकर्त्याला पॅरिसला प्रवासाचे नियोजन करण्यात मदत करणे.

#### कार्य पूर्ण करण्यासाठी पावले

1. **वापरकर्ता प्राधान्ये गोळा करा**: वापरकर्त्याला त्यांच्या प्रवासाच्या तारखा, बजेट, आवडी (उदा. संग्रहालये, खाद्यपदार्थ, खरेदी) आणि कोणत्याही विशिष्ट आवश्यकता विचारा.
2. **माहिती पुनर्प्राप्त करा**: वापरकर्त्याच्या प्राधान्यांशी जुळणाऱ्या फ्लाइट पर्याय, निवास, आकर्षणे आणि रेस्टॉरंट्स शोधा.
3. **शिफारसी तयार करा**: फ्लाइट तपशील, हॉटेल आरक्षणे आणि सुचवलेली क्रियाकलापांसह वैयक्तिकृत प्रवास योजना प्रदान करा.
4. **प्रतिक्रियेच्या आधारे समायोजने करा**: शिफारसींवर वापरकर्त्याची प्रतिक्रिया विचारून आवश्यक समायोजने करा.

#### आवश्यक संसाधने

- फ्लाइट आणि हॉटेल बुकिंग डेटाबेसमध्ये प्रवेश.
- पॅरिसमधील आकर्षणे आणि रेस्टॉरंट्सची माहिती.
- मागील संवादांमधून वापरकर्ता अभिप्राय डेटा.

#### अनुभव आणि आत्म-चिंतन

प्रवास एजंट त्याच्या कामगिरीचे मूल्यांकन करण्यासाठी आणि भूतकाळातील अनुभवांमधून शिकण्यासाठी मेटाकॉग्निशनचा वापर करतो. उदाहरणार्थ:

1. **वापरकर्ता अभिप्रायाचे विश्लेषण**: प्रवास एजंट वापरकर्ता अभिप्रायाचे पुनरावलोकन करतो जे शिफारसी चांगल्या प्रकारे प्राप्त झाल्या आणि कोणत्या नाहीत. त्यानुसार त्याच्या भविष्यातील सूचना समायोजित करतो.
2. **अनुकूलता**: जर एखाद्या वापरकर्त्याने पूर्वी गर्दीच्या ठिकाणांचा तिरस्कार व्यक्त केला असेल, तर प्रवास एजंट भविष्यात गर्दीच्या वेळेत लोकप्रिय पर्यटन स्थळांची शिफारस टाळेल.
3. **त्रुटी सुधारणा**: जर प्रवास एजंटने पूर्वीच्या बुकिंगमध्ये चूक केली असेल, जसे की पूर्णपणे बुक केलेल्या हॉटेलची शिफारस करणे, तर तो शिफारसी करण्यापूर्वी उपलब्धता अधिक काटेकोरपणे तपासणे शिकतो.

#### व्यावहारिक विकसक उदाहरण

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Search for flights, hotels, and attractions based on preferences
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # Analyze feedback and adjust future recommendations
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### मेटाकॉग्निशन का महत्त्वाचे आहे

- **आत्म-चिंतन**: एजंट्स त्यांच्या कामगिरीचे विश्लेषण करू शकतात आणि सुधारणा करण्याच्या क्षेत्रांची ओळख पटवू शकतात.
- **अनुकूलता**: एजंट्स अभिप्राय आणि बदलत्या परिस्थितींवर आधारित रणनीतींमध्ये बदल करू शकतात.
- **त्रुटी सुधारणा**: एजंट्स स्वयंचलितपणे चुका शोधू आणि सुधारू शकतात.
- **संसाधन व्यवस्थापन**: एजंट्स वेळ आणि संगणकीय शक्ती यासारख्या संसाधनांचा वापर अनुकूल करू शकतात.

मेटाकॉग्निशन समाविष्ट करून, प्रवास एजंट अधिक वैयक्तिकृत आणि अचूक प्रवास शिफारसी प्रदान करू शकतो, ज्यामुळे एकूण वापरकर्ता अनुभव सुधारतो.

---

## 2. एजंट्समधील नियोजन

नियोजन हे AI एजंटच्या वर्तनाचा एक महत्त्वाचा घटक आहे. यामध्ये सध्याच्या स्थितीचा, संसाधनांचा आणि संभाव्य अडथळ्यांचा विचार करून उद्दिष्ट साध्य करण्यासाठी आवश्यक पावले आखणे समाविष्ट आहे.

### नियोजनाचे घटक

- **सध्याचे कार्य**: कार्य स्पष्टपणे परिभाषित करा.
- **कार्य पूर्ण करण्यासाठी पावले**: कार्य व्यवस्थापनीय टप्प्यांमध्ये विभागा.
- **आवश्यक संसाधने**: आवश्यक संसाधने ओळखा.
- **अनुभव**: नियोजनासाठी भूतकाळातील अनुभवांचा उपयोग करा.

**उदाहरण**:
प्रवास एजंटला वापरकर्त्याला त्यांच्या प्रवासाचे प्रभावीपणे नियोजन करण्यात मदत करण्यासाठी आवश्यक असलेल्या पायऱ्या येथे आहेत:

### प्रवास एजंटसाठी पावले

1. **वापरकर्ता प्राधान्ये गोळा करा**
   - वापरकर्त्याला त्यांच्या प्रवासाच्या तारखा, बजेट, आवडी आणि कोणत्याही विशिष्ट आवश्यकता याबद्दल तपशील विचारा.
   - उदाहरणे: "तुम्ही प्रवास कधी करण्याचा विचार करत आहात?" "तुमचे बजेट किती आहे?" "तुम्हाला सुट्टीत कोणत्या प्रकारच्या क्रियाकलापांचा आनंद घ्यायला आवडतो?"

2. **माहिती पुनर्प्राप्त करा**
   - वापरकर्त्याच्या प्राधान्यांवर आधारित संबंधित प्रवास पर्याय शोधा.
   - **फ्लाइट्स**: वापरकर्त्याच्या बजेट आणि प्राधान्य दिलेल्या प्रवास तारखांमध्ये उपलब्ध फ्लाइट्स शोधा.
   - **निवास**: स्थान, किंमत आणि सुविधा यासाठी वापरकर्त्याच्या प्राधान्यांशी जुळणारी हॉटेल्स किंवा भाड्याच्या मालमत्ता शोधा.
   - **आकर्षणे आणि रेस्टॉरंट्स**: वापरकर्त्याच्या आवडींशी जुळणारी लोकप्रिय आकर्षणे, क्रियाकलाप आणि जेवणाचे पर्याय ओळखा.

3. **शिफारसी तयार करा**
   - पुनर्प्राप्त केलेली माहिती वैयक्तिकृत प्रवास योजनेत संकलित करा.
   - वापरकर्त्याच्या प्राधान्यांनुसार शिफारसी तयार करताना फ्लाइट पर्याय, हॉटेल आरक्षणे आणि सुचवलेली क्रियाकलाप यासारख्या तपशील प्रदान करा.

4. **वापरकर्त्याला प्रवास योजना सादर करा**
   - वापरकर्त्याला पुनरावलोकनासाठी प्रस्तावित प्रवास योजना सामायिक करा.
   - उदाहरण: "पॅरिसला तुमच्या प्रवासासाठी येथे एक सुचवलेली योजना आहे. यामध्ये फ्लाइट तपशील, हॉटेल बुकिंग्ज आणि शिफारस केलेल्या क्रियाकलाप आणि रेस्टॉरंट्सची यादी समाविष्ट आहे. तुमचे विचार मला कळवा!"

5. **प्रतिक्रिया गोळा करा**
   - प्रस्तावित प्रवास योजनेवर वापरकर्त्याची प्रतिक्रिया विचारून घ्या.
   - उदाहरणे: "तुम्हाला फ्लाइट पर्याय आवडले का?" "हॉटेल तुमच्या गरजांसाठी योग्य आहे का?" "तुम्हाला कोणतेही क्रियाकलाप जोडायचे किंवा काढायचे आहेत का?"

6. **प्रतिक्रियेच्या आधारे समायोजने करा**
   - वापरकर्त्याच्या अभिप्रायाच्या आधारे प्रवास योजना समायोजित करा.
   - फ्लाइट, निवास आणि क्रियाकलाप शिफारसींमध्ये आवश्यक बदल करा जेणेकरून वापरकर्त्याच्या प्राधान्यांशी अधिक चांगले जुळेल.

7. **अंतिम पुष्टीकरण**
   - वापरकर्त्याला अंतिम पुष्टीकरणासाठी अद्यतनित प्रवास योजना सादर करा.
   - उदाहरण: "तुमच्या अभिप्रायाच्या आधारे मी समायोजने केली आहेत. येथे अद्यतनित प्रवास योजना आहे. तुम्हाला सर्व काही योग्य दिसत आहे का?"

8. **बुकिंग आणि पुष्टीकरण आरक्षणे**
   - एकदा वापरकर्त्याने प्रवास योजनेला मान्यता दिल्यानंतर, फ्लाइट्स, निवास आणि कोणत्याही पूर्व-नियोजित क्रियाकलापांसह बुकिंग करा.
   - वापरकर्त्याला पुष्टीकरण तपशील पाठवा.

9. **सतत समर्थन प्रदान करा**
   - प्रवासाच्या आधी आणि दरम्यान वापरकर्त्याला कोणत्याही बदलांसाठी किंवा अतिरिक्त विनंत्यांसाठी मदत करण्यासाठी उपलब्ध रहा.
   - उदाहरण: "तुमच्या प्रवासादरम्यान तुम्हाला आणखी कोणत्याही मदतीची आवश्यकता असल्यास, कृपया कधीही माझ्याशी संपर्क साधा!"

### उदाहरण संवाद

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage within a booing request
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

## 3. सुधारात्मक RAG प्रणाली

प्रथम, RAG साधन आणि पूर्व-खालील संदर्भ लोड यामधील फरक समजून घेऊया.

![RAG vs संदर्भ लोडिंग](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.mr.png)

### पुनर्प्राप्ती-वर्धित निर्मिती (RAG)

RAG प्रणाली पुनर्प्राप्ती प्रणालीला जनरेटिव्ह मॉडेलसह एकत्र करते. जेव्हा क्वेरी केली जाते, तेव्हा पुनर्प्राप्ती प्रणाली बाह्य स्त्रोताकडून संबंधित दस्तऐवज किंवा डेटा पुनर्प्राप्त करते आणि ही पुनर्प्राप्त माहिती जनरेटिव्ह मॉडेलच्या इनपुटला वाढवण्यासाठी वापरली जाते. यामुळे मॉडेलला अधिक अचूक आणि संदर्भानुसार संबंधित प्रतिसाद तयार करण्यात मदत होते.

RAG प्रणालीमध्ये, एजंट ज्ञान तळातून संबंधित माहिती पुनर्प्राप्त करतो आणि योग्य प्रतिसाद किंवा कृती तयार करण्यासाठी त्याचा वापर करतो.

### सुधारात्मक RAG दृष्टिकोन

सुधारात्मक RAG दृष्टिकोन RAG तंत्रांचा वापर करून चुका सुधारण्यावर आणि AI एजंट्सची अचूकता सुधारण्यावर लक्ष केंद्रित करतो. यामध्ये समाविष्ट आहे:

1. **प्रॉम्प्टिंग तंत्र**: एजंटला संबंधित माहिती पुनर्प्राप्त करण्यात मार्गदर्शन करण्यासाठी विशिष्ट प्रॉम्प्ट्सचा वापर.
2. **साधन**: पुनर्प्राप्त केलेल्या माहितीसंबंधीचे मूल्यांकन करण्यासाठी आणि अचूक प्रतिसाद तयार करण्यासाठी एजंटला सक्षम करणाऱ्या अल्गोरिदम आणि यंत्रणांची अंमलबजावणी.
3. **मूल्यमापन**: एजंटच्या कामगिरीचे सतत मूल्यमापन करणे आणि त्याची अचूकता आणि कार्यक्षमता सुधारण्यासाठी समायोजने करणे.

#### उदाहरण: शोध एजंटमध्ये सुधारात्मक RAG

वेबवरून माहिती पुनर्प्राप्त करून वापरकर्त्याच्या क्वेरींना उत्तर देणाऱ्या शोध एजंटचा विचार करा. सुधारात्मक RAG दृष्टिकोनामध्ये समाविष्ट असू शकते:

1. **प्रॉम्प्टिंग तंत्र**:
```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)
        new_itinerary = self.generate_recommendations()
        return new_itinerary

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
new_itinerary = travel_agent.adjust_based_on_feedback(feedback)
print("Updated Itinerary:", new_itinerary)
```

### पूर्व-प्रसंग लोड

पूर्व-प्रसंग लोड म्हणजे क्वेरी प्रक्रिया करण्यापूर्वी मॉडेलमध्ये संबंधित माहिती किंवा पार्श्वभूमी लोड करणे. यामुळे मॉडेलला सुरुवातीपासूनच ही माहिती उपलब्ध होते, ज्यामुळे अतिरिक्त डेटा मिळवण्याची गरज न पडता अधिक माहितीपूर्ण प्रतिसाद तयार करण्यात मदत होते.

Python मध्ये ट्रॅव्हल एजंट अॅप्लिकेशनसाठी पूर्व-प्रसंग लोड कसा दिसतो याचे सोपे उदाहरण येथे दिले आहे:

```python
class TravelAgent:
    def __init__(self):
        # Pre-load popular destinations and their information
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Fetch destination information from pre-loaded context
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Example usage
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### स्पष्टीकरण

1. **प्रारंभ (`__init__` method)**: `TravelAgent` क्लासमध्ये लोकप्रिय स्थळांची माहिती असलेला डिक्शनरी पूर्व-लोड केला जातो, जसे की पॅरिस, टोकियो, न्यूयॉर्क आणि सिडनी. या डिक्शनरीमध्ये देश, चलन, भाषा आणि प्रमुख आकर्षणे यासारख्या तपशीलांचा समावेश आहे.

2. **माहिती मिळवणे (`get_destination_info` method)**: जेव्हा वापरकर्ता विशिष्ट स्थळाबद्दल क्वेरी करतो, तेव्हा `get_destination_info` मेथड पूर्व-लोड केलेल्या डिक्शनरीमधून संबंधित माहिती मिळवते.

पूर्व-प्रसंग लोड करून, ट्रॅव्हल एजंट अॅप्लिकेशन वापरकर्त्याच्या क्वेरीला जलद प्रतिसाद देऊ शकते, वास्तविक वेळेत बाह्य स्रोतांकडून ही माहिती मिळवण्याची गरज न पडता. यामुळे अॅप्लिकेशन अधिक कार्यक्षम आणि प्रतिसादक्षम बनते.

### उद्दिष्टासह योजना सुरू करणे आणि पुनरावृत्ती करणे

उद्दिष्टासह योजना सुरू करणे म्हणजे स्पष्ट उद्दिष्ट किंवा लक्ष्य निश्चित करून प्रक्रिया सुरू करणे. हे उद्दिष्ट मॉडेलला मार्गदर्शक तत्त्व म्हणून वापरता येते, ज्यामुळे प्रत्येक पुनरावृत्ती इच्छित परिणाम साध्य करण्याच्या दिशेने पुढे जाते. यामुळे प्रक्रिया अधिक कार्यक्षम आणि केंद्रित होते.

Python मध्ये ट्रॅव्हल एजंटसाठी उद्दिष्टासह योजना कशी सुरू करावी याचे उदाहरण येथे दिले आहे:

### परिस्थिती

एक ट्रॅव्हल एजंट क्लायंटसाठी वैयक्तिकृत सुट्टीची योजना तयार करू इच्छित आहे. उद्दिष्ट म्हणजे क्लायंटच्या पसंती आणि बजेटवर आधारित प्रवासाचा कार्यक्रम तयार करणे.

### पायऱ्या

1. क्लायंटच्या पसंती आणि बजेट निश्चित करा.
2. या पसंतींवर आधारित प्रारंभिक योजना तयार करा.
3. योजना सुधारण्यासाठी पुनरावृत्ती करा, क्लायंटच्या समाधानासाठी अनुकूलित करा.

#### Python कोड

```python
class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def bootstrap_plan(self, preferences, budget):
        plan = []
        total_cost = 0

        for destination in self.destinations:
            if total_cost + destination['cost'] <= budget and self.match_preferences(destination, preferences):
                plan.append(destination)
                total_cost += destination['cost']

        return plan

    def match_preferences(self, destination, preferences):
        for key, value in preferences.items():
            if destination.get(key) != value:
                return False
        return True

    def iterate_plan(self, plan, preferences, budget):
        for i in range(len(plan)):
            for destination in self.destinations:
                if destination not in plan and self.match_preferences(destination, preferences) and self.calculate_cost(plan, destination) <= budget:
                    plan[i] = destination
                    break
        return plan

    def calculate_cost(self, plan, new_destination):
        return sum(destination['cost'] for destination in plan) + new_destination['cost']

# Example usage
destinations = [
    {"name": "Paris", "cost": 1000, "activity": "sightseeing"},
    {"name": "Tokyo", "cost": 1200, "activity": "shopping"},
    {"name": "New York", "cost": 900, "activity": "sightseeing"},
    {"name": "Sydney", "cost": 1100, "activity": "beach"},
]

preferences = {"activity": "sightseeing"}
budget = 2000

travel_agent = TravelAgent(destinations)
initial_plan = travel_agent.bootstrap_plan(preferences, budget)
print("Initial Plan:", initial_plan)

refined_plan = travel_agent.iterate_plan(initial_plan, preferences, budget)
print("Refined Plan:", refined_plan)
```

#### कोड स्पष्टीकरण

1. **प्रारंभ (`__init__` method)**: `TravelAgent` क्लास संभाव्य स्थळांची यादीसह प्रारंभ केला जातो, ज्यामध्ये नाव, खर्च आणि क्रियाकलाप प्रकार यासारखे गुणधर्म असतात.

2. **योजना सुरू करणे (`bootstrap_plan` method)**: ही मेथड क्लायंटच्या पसंती आणि बजेटवर आधारित प्रारंभिक प्रवास योजना तयार करते. ती स्थळांच्या यादीतून पुनरावृत्ती करते आणि जर ती क्लायंटच्या पसंतींशी जुळत असेल आणि बजेटमध्ये बसत असेल तर ती योजना तयार करते.

3. **पसंती जुळवणे (`match_preferences` method)**: ही मेथड तपासते की एखादे स्थळ क्लायंटच्या पसंतींशी जुळते का.

4. **योजना सुधारणे (`iterate_plan` method)**: ही मेथड प्रारंभिक योजना सुधारते, क्लायंटच्या पसंती आणि बजेट मर्यादांचा विचार करून प्रत्येक स्थळासाठी चांगले पर्याय शोधते.

5. **खर्च मोजणे (`calculate_cost` method)**: ही मेथड सध्याच्या योजनेचा एकूण खर्च मोजते, ज्यामध्ये संभाव्य नवीन स्थळाचा समावेश असतो.

#### उदाहरण वापर

- **प्रारंभिक योजना**: ट्रॅव्हल एजंट क्लायंटच्या पर्यटनासाठी पसंती आणि $2000 च्या बजेटवर आधारित प्रारंभिक योजना तयार करतो.
- **सुधारित योजना**: ट्रॅव्हल एजंट योजना सुधारतो, क्लायंटच्या पसंती आणि बजेटसाठी अनुकूलित करतो.

उद्दिष्टासह योजना सुरू करून (उदा. क्लायंटचे समाधान वाढवणे) आणि योजना सुधारण्यासाठी पुनरावृत्ती करून, ट्रॅव्हल एजंट क्लायंटसाठी वैयक्तिकृत आणि अनुकूलित प्रवास कार्यक्रम तयार करू शकतो. ही पद्धत सुनिश्चित करते की प्रवास योजना सुरुवातीपासूनच क्लायंटच्या पसंती आणि बजेटशी जुळते आणि प्रत्येक पुनरावृत्तीनंतर सुधारते.

### LLM चा पुनर्रँकिंग आणि स्कोअरिंगसाठी फायदा घेणे

मोठ्या भाषा मॉडेल्स (LLMs) पुनर्रँकिंग आणि स्कोअरिंगसाठी वापरता येतात, ज्यामुळे मिळवलेल्या दस्तऐवजांची किंवा तयार केलेल्या प्रतिसादांची सुसंगती आणि गुणवत्ता मूल्यांकन करता येते. हे कसे कार्य करते:

**मिळवणे:** प्रारंभिक मिळवण्याच्या टप्प्यात क्वेरीवर आधारित संभाव्य दस्तऐवज किंवा प्रतिसादांची यादी तयार केली जाते.

**पुनर्रँकिंग:** LLM या यादीतील पर्यायांचे मूल्यांकन करून त्यांना सुसंगती आणि गुणवत्तेच्या आधारे पुनर्रँक करते. यामुळे सर्वात सुसंगत आणि उच्च-गुणवत्तेची माहिती प्रथम सादर केली जाते.

**स्कोअरिंग:** LLM प्रत्येक पर्यायाला स्कोअर देतो, ज्यामुळे त्यांची सुसंगती आणि गुणवत्ता प्रतिबिंबित होते. यामुळे वापरकर्त्यासाठी सर्वोत्तम प्रतिसाद किंवा दस्तऐवज निवडणे सोपे होते.

LLMs चा पुनर्रँकिंग आणि स्कोअरिंगसाठी फायदा घेऊन, प्रणाली अधिक अचूक आणि संदर्भानुसार सुसंगत माहिती प्रदान करू शकते, ज्यामुळे एकूण वापरकर्ता अनुभव सुधारतो.

Python मध्ये वापरकर्त्याच्या पसंतींवर आधारित प्रवास स्थळांचे पुनर्रँकिंग आणि स्कोअरिंग करण्यासाठी ट्रॅव्हल एजंट LLM कसा वापरतो याचे उदाहरण येथे दिले आहे:

#### परिस्थिती - पसंतींवर आधारित प्रवास

एक ट्रॅव्हल एजंट क्लायंटसाठी सर्वोत्तम प्रवास स्थळांची शिफारस करू इच्छित आहे. LLM स्थळांचे पुनर्रँकिंग आणि स्कोअरिंग करून सर्वात सुसंगत पर्याय सादर करण्यास मदत करेल.

#### पायऱ्या:

1. वापरकर्त्याच्या पसंती गोळा करा.
2. संभाव्य प्रवास स्थळांची यादी मिळवा.
3. LLM वापरून स्थळांचे पुनर्रँकिंग आणि स्कोअरिंग करा.

Azure OpenAI Services वापरून मागील उदाहरण कसे अपडेट करावे याचे स्पष्टीकरण येथे दिले आहे:

#### आवश्यकता

1. Azure सदस्यता आवश्यक आहे.
2. Azure OpenAI संसाधन तयार करा आणि आपली API key मिळवा.

#### Python कोडचे उदाहरण

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generate a prompt for the Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Define headers and payload for the request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Call the Azure OpenAI API to get the re-ranked and scored destinations
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extract and return the recommendations
        recommendations = response_data['choices'][0]['text'].strip().split('\n')
        return recommendations

    def generate_prompt(self, preferences):
        prompt = "Here are the travel destinations ranked and scored based on the following user preferences:\n"
        for key, value in preferences.items():
            prompt += f"{key}: {value}\n"
        prompt += "\nDestinations:\n"
        for destination in self.destinations:
            prompt += f"- {destination['name']}: {destination['description']}\n"
        return prompt

# Example usage
destinations = [
    {"name": "Paris", "description": "City of lights, known for its art, fashion, and culture."},
    {"name": "Tokyo", "description": "Vibrant city, famous for its modernity and traditional temples."},
    {"name": "New York", "description": "The city that never sleeps, with iconic landmarks and diverse culture."},
    {"name": "Sydney", "description": "Beautiful harbour city, known for its opera house and stunning beaches."},
]

preferences = {"activity": "sightseeing", "culture": "diverse"}
api_key = 'your_azure_openai_api_key'
endpoint = 'https://your-endpoint.com/openai/deployments/your-deployment-name/completions?api-version=2022-12-01'

travel_agent = TravelAgent(destinations)
recommendations = travel_agent.get_recommendations(preferences, api_key, endpoint)
print("Recommended Destinations:")
for rec in recommendations:
    print(rec)
```

#### कोड स्पष्टीकरण - Preference Booker

1. **प्रारंभ**: `TravelAgent` क्लास संभाव्य प्रवास स्थळांची यादीसह प्रारंभ केला जातो, ज्यामध्ये नाव आणि वर्णन यासारखे गुणधर्म असतात.

2. **शिफारसी मिळवणे (`get_recommendations` method)**: ही मेथड वापरकर्त्याच्या पसंतींवर आधारित Azure OpenAI सेवेसाठी प्रॉम्प्ट तयार करते आणि Azure OpenAI API ला HTTP POST विनंती करते, ज्यामुळे पुनर्रँकिंग आणि स्कोअरिंग केलेल्या स्थळांची यादी मिळते.

3. **प्रॉम्प्ट तयार करणे (`generate_prompt` method)**: ही मेथड Azure OpenAI साठी प्रॉम्प्ट तयार करते, ज्यामध्ये वापरकर्त्याच्या पसंती आणि स्थळांची यादी समाविष्ट असते. प्रॉम्प्ट मॉडेलला दिलेल्या पसंतींवर आधारित स्थळांचे पुनर्रँकिंग आणि स्कोअरिंग करण्यासाठी मार्गदर्शन करते.

4. **API कॉल**: `requests` लायब्ररीचा वापर करून Azure OpenAI API endpoint ला HTTP POST विनंती केली जाते. प्रतिसादामध्ये पुनर्रँकिंग आणि स्कोअरिंग केलेली स्थळे असतात.

5. **उदाहरण वापर**: ट्रॅव्हल एजंट वापरकर्त्याच्या पसंती (उदा. पर्यटन आणि विविध संस्कृतीत रस) गोळा करतो आणि Azure OpenAI सेवा वापरून प्रवास स्थळांसाठी पुनर्रँकिंग आणि स्कोअरिंग केलेल्या शिफारसी मिळवतो.

`your_azure_openai_api_key` आपल्या वास्तविक Azure OpenAI API key ने बदला आणि `https://your-endpoint.com/...` आपल्या Azure OpenAI डिप्लॉयमेंटच्या वास्तविक endpoint URL ने बदला.

LLM चा पुनर्रँकिंग आणि स्कोअरिंगसाठी फायदा घेऊन, ट्रॅव्हल एजंट क्लायंटसाठी अधिक वैयक्तिकृत आणि सुसंगत प्रवास शिफारसी प्रदान करू शकतो, ज्यामुळे त्यांचा एकूण अनुभव सुधारतो.
#### व्यावहारिक उदाहरण: ट्रॅव्हल एजंटमध्ये हेतूसह शोध

चला ट्रॅव्हल एजंटचा एक उदाहरण म्हणून विचार करूया आणि हेतूसह शोध कसा अंमलात आणता येतो ते पाहूया.

1. **वापरकर्त्याच्या प्राधान्यांची माहिती गोळा करणे**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **वापरकर्त्याच्या हेतूचा समज**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **संदर्भ जागरूकता**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **शोध आणि वैयक्तिकृत निकाल**

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # Example search logic for informational intent
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Example search logic for navigational intent
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Example search logic for transactional intent
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Example personalization logic
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Return top 10 personalized results
   ```

5. **उदाहरण वापर**

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. साधन म्हणून कोड तयार करणे

कोड तयार करणारे एजंट AI मॉडेल्सचा वापर करून कोड लिहितात आणि अंमलात आणतात, जटिल समस्या सोडवतात आणि कार्ये स्वयंचलित करतात.

### कोड तयार करणारे एजंट

कोड तयार करणारे एजंट जनरेटिव्ह AI मॉडेल्सचा वापर करून कोड लिहितात आणि अंमलात आणतात. हे एजंट जटिल समस्या सोडवू शकतात, कार्ये स्वयंचलित करू शकतात आणि विविध प्रोग्रामिंग भाषांमध्ये कोड तयार व चालवून मौल्यवान अंतर्दृष्टी प्रदान करू शकतात.

#### व्यावहारिक उपयोग

1. **स्वयंचलित कोड निर्मिती**: डेटा विश्लेषण, वेब स्क्रॅपिंग किंवा मशीन लर्निंग यांसारख्या विशिष्ट कार्यांसाठी कोड तयार करा.
2. **SQL as a RAG**: डेटाबेसमधून डेटा पुनर्प्राप्त करण्यासाठी आणि त्यावर प्रक्रिया करण्यासाठी SQL क्वेरींचा वापर करा.
3. **समस्या सोडवणे**: विशिष्ट समस्या सोडवण्यासाठी कोड तयार करा आणि अंमलात आणा, जसे की अल्गोरिदम ऑप्टिमाइझ करणे किंवा डेटा विश्लेषण करणे.

#### उदाहरण: डेटा विश्लेषणासाठी कोड तयार करणारा एजंट

कल्पना करा की तुम्ही कोड तयार करणारा एजंट डिझाइन करत आहात. तो कसा कार्य करतो ते पाहूया:

1. **कार्य**: डेटासेटचे विश्लेषण करून ट्रेंड्स आणि पॅटर्न्स ओळखणे.
2. **पायऱ्या**:
   - डेटासेट डेटा विश्लेषण साधनात लोड करा.
   - डेटा फिल्टर आणि एकत्रित करण्यासाठी SQL क्वेरी तयार करा.
   - क्वेरी चालवा आणि निकाल मिळवा.
   - निकालांचा वापर करून व्हिज्युअलायझेशन आणि अंतर्दृष्टी तयार करा.
3. **आवश्यक संसाधने**: डेटासेट, डेटा विश्लेषण साधने, आणि SQL क्षमता.
4. **अनुभव**: भूतकाळातील विश्लेषणाच्या निकालांचा वापर करून भविष्यातील विश्लेषणांची अचूकता आणि सुसंगतता सुधारणे.

### उदाहरण: ट्रॅव्हल एजंटसाठी कोड तयार करणारा एजंट

या उदाहरणात, आपण ट्रॅव्हल एजंट नावाचा कोड तयार करणारा एजंट डिझाइन करू, जो वापरकर्त्यांना प्रवासाचे नियोजन करण्यात मदत करतो. हा एजंट प्रवासाचे पर्याय शोधणे, निकाल फिल्टर करणे, आणि जनरेटिव्ह AI चा वापर करून प्रवासाचा आराखडा तयार करणे यासारखी कार्ये हाताळू शकतो.

#### कोड तयार करणाऱ्या एजंटचा आढावा

1. **वापरकर्त्याच्या प्राधान्यांची माहिती गोळा करणे**: गंतव्यस्थान, प्रवासाच्या तारखा, बजेट, आणि आवडी यांसारखी माहिती गोळा करणे.
2. **डेटा मिळवण्यासाठी कोड तयार करणे**: फ्लाइट्स, हॉटेल्स, आणि आकर्षणांबद्दल डेटा मिळवण्यासाठी कोड तयार करणे.
3. **तयार केलेला कोड चालवणे**: रिअल-टाइम माहिती मिळवण्यासाठी तयार केलेला कोड चालवणे.
4. **प्रवासाचा आराखडा तयार करणे**: गोळा केलेल्या डेटावर आधारित वैयक्तिकृत प्रवास योजना तयार करणे.
5. **प्रतिक्रियेच्या आधारे समायोजन करणे**: वापरकर्त्याच्या अभिप्रायानुसार कोड पुन्हा तयार करणे आणि निकाल सुधारणे.

#### टप्प्याटप्प्याने अंमलबजावणी

1. **वापरकर्त्याच्या प्राधान्यांची माहिती गोळा करणे**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **डेटा मिळवण्यासाठी कोड तयार करणे**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Example: Generate code to search for flights based on user preferences
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Example: Generate code to search for hotels
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **तयार केलेला कोड चालवणे**

   ```python
   def execute_code(code):
       # Execute the generated code using exec
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. **प्रवासाचा आराखडा तयार करणे**

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. **प्रतिक्रियेच्या आधारे समायोजन करणे**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Adjust preferences based on user feedback
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerate and execute code with updated preferences
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### पर्यावरण जागरूकता आणि तर्कशक्तीचा उपयोग

टेबलच्या स्कीमाच्या आधारे क्वेरी तयार करण्याची प्रक्रिया पर्यावरण जागरूकता आणि तर्कशक्तीचा उपयोग करून सुधारली जाऊ शकते.

याचे उदाहरण येथे दिले आहे:

1. **स्कीमाचा समज**: प्रणाली टेबलच्या स्कीमाचा समज घेईल आणि क्वेरी तयार करण्यासाठी ही माहिती वापरेल.
2. **प्रतिक्रियेच्या आधारे समायोजन**: प्रणाली अभिप्रायाच्या आधारे वापरकर्त्याच्या प्राधान्यांमध्ये समायोजन करेल आणि स्कीमातील कोणती फील्ड्स अपडेट करायची आहेत याचा विचार करेल.
3. **क्वेरी तयार करणे आणि अंमलात आणणे**: प्रणाली समायोजित प्राधान्यांवर आधारित फ्लाइट आणि हॉटेल डेटा मिळवण्यासाठी क्वेरी तयार करेल आणि अंमलात आणेल.

येथे या संकल्पनांचा समावेश असलेला अद्ययावत Python कोड उदाहरण आहे:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Adjust preferences based on user feedback
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Reasoning based on schema to adjust other related preferences
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Custom logic to adjust preferences based on schema and feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generate code to fetch flight data based on updated preferences
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generate code to fetch hotel data based on updated preferences
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulate execution of code and return mock data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generate itinerary based on flights, hotels, and attractions
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Example schema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Example usage
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Regenerate and execute code with updated preferences
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### स्पष्टीकरण - अभिप्रायाच्या आधारे बुकिंग

1. **स्कीम जागरूकता**: `schema` डिक्शनरी अभिप्रायाच्या आधारे प्राधान्ये कशी समायोजित करायची याचे परिभाषित करते. यामध्ये `favorites` आणि `avoid` यांसारख्या फील्ड्सचा समावेश आहे.
2. **प्राधान्ये समायोजित करणे (`adjust_based_on_feedback` पद्धत)**: ही पद्धत अभिप्रायाच्या आधारे प्राधान्ये समायोजित करते.
3. **पर्यावरण-आधारित समायोजन (`adjust_based_on_environment` पद्धत)**: ही पद्धत स्कीमा आणि अभिप्रायाच्या आधारे समायोजन सानुकूलित करते.
4. **क्वेरी तयार करणे आणि अंमलात आणणे**: प्रणाली समायोजित प्राधान्यांवर आधारित फ्लाइट आणि हॉटेल डेटा मिळवण्यासाठी कोड तयार करते आणि क्वेरींची अंमलबजावणी करते.
5. **प्रवासाचा आराखडा तयार करणे**: प्रणाली नवीन फ्लाइट, हॉटेल, आणि आकर्षण डेटावर आधारित अद्ययावत प्रवास योजना तयार करते.

पर्यावरण-जागरूक प्रणाली तयार करून आणि स्कीमाच्या आधारे तर्कशक्तीचा उपयोग करून, अधिक अचूक आणि सुसंगत क्वेरी तयार करता येतात, ज्यामुळे प्रवासाच्या शिफारसी अधिक चांगल्या आणि वैयक्तिकृत होतात.

### Retrieval-Augmented Generation (RAG) तंत्र म्हणून SQL चा वापर

SQL (स्ट्रक्चर्ड क्वेरी लँग्वेज) ही डेटाबेससह संवाद साधण्यासाठी एक शक्तिशाली साधन आहे. Retrieval-Augmented Generation (RAG) दृष्टिकोनाचा भाग म्हणून SQL चा वापर केल्याने डेटाबेसमधून संबंधित डेटा पुनर्प्राप्त करता येतो, जो AI एजंट्सच्या प्रतिसादांना किंवा कृतींना माहिती देतो. ट्रॅव्हल एजंटच्या संदर्भात SQL RAG तंत्र म्हणून कसे वापरले जाऊ शकते ते पाहूया.

#### मुख्य संकल्पना

1. **डेटाबेस संवाद**:
   - SQL चा वापर डेटाबेस क्वेरी करण्यासाठी, संबंधित माहिती पुनर्प्राप्त करण्यासाठी, आणि डेटा प्रक्रिया करण्यासाठी केला जातो.
   - उदाहरण: प्रवास डेटाबेसमधून फ्लाइट तपशील, हॉटेल माहिती, आणि आकर्षणे मिळवणे.

2. **RAG सह एकत्रीकरण**:
   - SQL क्वेरी वापरकर्त्याच्या इनपुट आणि प्राधान्यांवर आधारित तयार केल्या जातात.
   - पुनर्प्राप्त केलेला डेटा वैयक्तिकृत शिफारसी किंवा कृती तयार करण्यासाठी वापरला जातो.

3. **डायनॅमिक क्वेरी निर्मिती**:
   - AI एजंट संदर्भ आणि वापरकर्त्याच्या गरजांवर आधारित डायनॅमिक SQL क्वेरी तयार करतो.
   - उदाहरण: बजेट, तारखा, आणि आवडींवर आधारित SQL क्वेरी सानुकूलित करणे.

#### उपयोग

- **स्वयंचलित कोड निर्मिती**: विशिष्ट कार्यांसाठी कोड तयार करा.
- **SQL as a RAG**: डेटा प्रक्रिया करण्यासाठी SQL क्वेरींचा वापर करा.
- **समस्या सोडवणे**: समस्या सोडवण्यासाठी कोड तयार करा आणि अंमलात आणा.

**उदाहरण**:
डेटा विश्लेषण एजंट:

1. **कार्य**: डेटासेटचे विश्लेषण करून ट्रेंड्स शोधणे.
2. **पायऱ्या**:
   - डेटासेट लोड करा.
   - डेटा फिल्टर करण्यासाठी SQL क्वेरी तयार करा.
   - क्वेरी चालवा आणि निकाल मिळवा.
   - व्हिज्युअलायझेशन आणि अंतर्दृष्टी तयार करा.
3. **संसाधने**: डेटासेट प्रवेश, SQL क्षमता.
4. **अनुभव**: भूतकाळातील निकालांचा वापर करून भविष्यातील विश्लेषण सुधारणे.

#### व्यावहारिक उदाहरण: ट्रॅव्हल एजंटमध्ये SQL चा वापर

1. **वापरकर्त्याच्या प्राधान्यांची माहिती गोळा करणे**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **SQL क्वेरी तयार करणे**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **SQL क्वेरी चालवणे**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. **शिफारसी तयार करणे**

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### SQL क्वेरींची उदाहरणे

1. **फ्लाइट क्वेरी**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **हॉटेल क्वेरी**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **आकर्षण क्वेरी**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

SQL चा Retrieval-Augmented Generation (RAG) तंत्राचा भाग म्हणून वापर करून, ट्रॅव्हल एजंटसारखे AI एजंट्स डायनॅमिकरीत्या संबंधित डेटा पुनर्प्राप्त करू शकतात आणि वैयक्तिकृत शिफारसी प्रदान करू शकतात.

### मेटाकॉग्निशनचे उदाहरण

मेटाकॉग्निशन अंमलात आणण्याचे उदाहरण दाखवण्यासाठी, आपण एक साधा एजंट तयार करूया जो *त्याच्या निर्णय प्रक्रियेवर विचार करतो* आणि समस्या सोडवताना त्याची रणनीती समायोजित करतो. उदाहरणार्थ, एजंट हॉटेल निवडताना त्याच्या निर्णयांवर पुनर्विचार करतो आणि चुका किंवा उप-इष्टतम निवडी केल्यास त्याची रणनीती बदलतो.

#### मेटाकॉग्निशन कसे दर्शवते:

1. **प्रारंभिक निर्णय**: एजंट सर्वात स्वस्त हॉटेल निवडतो, गुणवत्ता विचारात न घेता.
2. **पुनर्विचार आणि मूल्यांकन**: प्रारंभिक निवडीनंतर, एजंट अभिप्रायाच्या आधारे तपासतो की निवडलेले हॉटेल "वाईट" आहे का. जर गुणवत्ता खूपच कमी असेल, तर तो त्याच्या विचारांवर पुनर्विचार करतो.
3. **रणनीती समायोजित करणे**: एजंट त्याच्या पुनर्विचाराच्या आधारे "स्वस्त" वरून "सर्वोत्तम गुणवत्ता" कडे स्विच करतो, ज्यामुळे भविष्यातील निर्णय प्रक्रिया सुधारते.

येथे एक उदाहरण आहे:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Stores the hotels chosen previously
        self.corrected_choices = []  # Stores the corrected choices
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Available strategies

    def recommend_hotel(self, hotels, strategy):
        """
        Recommend a hotel based on the chosen strategy.
        The strategy can either be 'cheapest' or 'highest_quality'.
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        Reflect on the last choice made and decide if the agent should adjust its strategy.
        The agent considers if the previous choice led to a poor outcome.
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # Let's assume we have some user feedback that tells us whether the last choice was good or not
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Adjust strategy if the previous choice was unsatisfactory
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        Simulate user feedback based on hotel attributes.
        For simplicity, assume if the hotel is too cheap, the feedback is "bad".
        If the hotel has quality less than 7, feedback is "bad".
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# Simulate a list of hotels (price and quality)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Create an agent
agent = HotelRecommendationAgent()

# Step 1: The agent recommends a hotel using the "cheapest" strategy
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Step 2: The agent reflects on the choice and adjusts strategy if necessary
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Step 3: The agent recommends again, this time using the adjusted strategy
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### एजंट्सची मेटाकॉग्निशन क्षमता

येथे महत्त्वाचे म्हणजे एजंटची क्षमता:
- त्याच्या मागील निवडी आणि निर्णय प्रक्रियेचे मूल्यांकन करणे.
- त्या पुनर्विचाराच्या आधारे त्याची रणनीती समायोजित करणे, म्हणजेच मेटाकॉग्निशन अंमलात आणणे.

ही मेटाकॉग्निशनची एक साधी पद्धत आहे, जिथे प्रणाली अंतर्गत अभिप्रायाच्या आधारे तिच्या विचार प्रक्रियेचे समायोजन करू शकते.

### निष्कर्ष

मेटाकॉग्निशन ही एक शक्तिशाली पद्धत आहे जी AI एजंट्सच्या क्षमतेत लक्षणीय सुधारणा करू शकते. मेटाकॉग्निटिव्ह प्रक्रिया समाविष्ट करून, तुम्ही अधिक बुद्धिमान, अनुकूल, आणि कार्यक्षम एजंट्स डिझाइन करू शकता. मेटाकॉग्निशनच्या जगात अधिक सखोल जाण्यासाठी अतिरिक्त संसाधनांचा वापर करा.

### मेटाकॉग्निशन डिझाइन पॅटर्नबद्दल अधिक प्रश्न आहेत?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) मध्ये सामील व्हा, इतर शिकणाऱ्यांशी भेटा, ऑफिस तासांमध्ये सहभागी व्हा, आणि तुमचे AI एजंट्ससंबंधी प्रश्न विचारून उत्तरे मिळवा.

## मागील धडा

[मल्टी-एजंट डिझाइन पॅटर्न](../08-multi-agent/README.md)

## पुढील धडा

[उत्पादनात AI एजंट्स](../10-ai-agents-production/README.md)

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर केल्यामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.