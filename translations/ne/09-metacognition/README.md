<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-29T10:13:34+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "ne"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.ne.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(माथिको तस्बिरमा क्लिक गरेर यो पाठको भिडियो हेर्नुहोस्)_
# एआई एजेन्टहरूमा मेटाकग्निशन

## परिचय

एआई एजेन्टहरूमा मेटाकग्निशनको पाठमा स्वागत छ! यो अध्याय सुरुवात गर्नेहरूका लागि तयार गरिएको हो, जसलाई एआई एजेन्टहरूले आफ्नै सोच्ने प्रक्रियाबारे कसरी सोच्न सक्छन् भन्ने जिज्ञासा छ। यो पाठको अन्त्यसम्म, तपाईंले मुख्य अवधारणाहरू बुझ्नुहुनेछ र एआई एजेन्ट डिजाइनमा मेटाकग्निशन लागू गर्नका लागि व्यावहारिक उदाहरणहरू प्रयोग गर्न सक्षम हुनुहुनेछ।

## सिकाइका लक्ष्यहरू

यो पाठ पूरा गरेपछि, तपाईंले निम्न गर्न सक्षम हुनुहुनेछ:

1. एजेन्ट परिभाषामा तर्क गर्ने लूपहरूको प्रभाव बुझ्नुहोस्।
2. आत्म-सुधार गर्ने एजेन्टहरूलाई सहयोग गर्न योजना बनाउने र मूल्याङ्कन गर्ने प्रविधिहरू प्रयोग गर्नुहोस्।
3. कार्यहरू पूरा गर्न कोडलाई हेरफेर गर्न सक्षम आफ्नै एजेन्टहरू सिर्जना गर्नुहोस्।

## मेटाकग्निशनको परिचय

मेटाकग्निशन उच्च-स्तरीय संज्ञानात्मक प्रक्रियाहरूलाई जनाउँछ, जसमा आफ्नो सोच्ने प्रक्रियाबारे सोच्ने समावेश हुन्छ। एआई एजेन्टहरूको लागि, यसको अर्थ आफ्ना कार्यहरूलाई आत्म-जागरूकता र विगतका अनुभवहरूको आधारमा मूल्याङ्कन र समायोजन गर्न सक्षम हुनु हो। मेटाकग्निशन, वा "सोच्नेबारे सोच्ने" एजेण्टिक एआई प्रणालीहरूको विकासमा महत्त्वपूर्ण अवधारणा हो। यसले एआई प्रणालीहरूलाई आफ्नै आन्तरिक प्रक्रियाहरूको बारेमा सचेत हुन र आफ्नो व्यवहारलाई अनुगमन, नियमन, र अनुकूलन गर्न सक्षम बनाउँछ। ठीक त्यस्तै हामीले कुनै कोठाको वातावरण बुझ्दा वा समस्याको समाधान खोज्दा गर्छौं। यो आत्म-जागरूकताले एआई प्रणालीहरूलाई राम्रो निर्णय लिन, त्रुटिहरू पहिचान गर्न, र समयसँगै आफ्नो प्रदर्शन सुधार गर्न मद्दत गर्न सक्छ - फेरि ट्यूरिङ परीक्षण र एआईले नियन्त्रण लिने बहससँग जोडिन्छ।

एजेण्टिक एआई प्रणालीहरूको सन्दर्भमा, मेटाकग्निशनले निम्न चुनौतीहरूको समाधान गर्न मद्दत गर्न सक्छ:
- पारदर्शिता: एआई प्रणालीहरूले आफ्नो तर्क र निर्णयहरू व्याख्या गर्न सक्षम बनाउने।
- तर्क: एआई प्रणालीहरूको जानकारी संश्लेषण गर्ने र ठोस निर्णय लिन सक्ने क्षमता बढाउने।
- अनुकूलन: एआई प्रणालीहरूलाई नयाँ वातावरण र परिवर्तनशील अवस्थाहरूमा समायोजन गर्न सक्षम बनाउने।
- धारणा: एआई प्रणालीहरूको आफ्नो वातावरणबाट डेटा पहिचान र व्याख्या गर्ने सटीकता सुधार गर्ने।

### मेटाकग्निशन के हो?

मेटाकग्निशन, वा "सोच्नेबारे सोच्ने," उच्च-स्तरीय संज्ञानात्मक प्रक्रिया हो जसमा आत्म-जागरूकता र आफ्ना संज्ञानात्मक प्रक्रियाहरूको आत्म-नियमन समावेश हुन्छ। एआईको क्षेत्रमा, मेटाकग्निशनले एजेन्टहरूलाई आफ्ना रणनीतिहरू र कार्यहरू मूल्याङ्कन र अनुकूलन गर्न सशक्त बनाउँछ, जसले समस्या समाधान र निर्णय-लिने क्षमताहरू सुधार गर्दछ। मेटाकग्निशनलाई बुझेर, तपाईं एआई एजेन्टहरूलाई अझ बौद्धिक, अनुकूलनशील, र कुशल बनाउन डिजाइन गर्न सक्नुहुन्छ। साँचो मेटाकग्निशनमा, तपाईंले एआईलाई आफ्नै तर्कबारे स्पष्ट रूपमा तर्क गर्दै देख्नुहुनेछ।

उदाहरण: “मैले सस्तो उडानलाई प्राथमिकता दिएँ किनभने... म सिधा उडान छुटाउन सक्छु, त्यसैले फेरि जाँच गरौं।”
कसरी वा किन यसले निश्चित मार्ग रोज्यो भन्ने ट्र्याक राख्दै।
- नोट गर्दै कि यसले गल्ती गर्‍यो किनभने यसले अघिल्लो प्रयोगकर्ता प्राथमिकताहरूमा धेरै निर्भर गर्‍यो, त्यसैले यसले आफ्नो निर्णय-लिने रणनीति मात्र होइन, अन्तिम सिफारिसलाई पनि परिमार्जन गर्दछ।
- ढाँचाहरू निदान गर्दै, “जब म प्रयोगकर्ताले ‘धेरै भीडभाड’ उल्लेख गरेको देख्छु, म निश्चित आकर्षणहरू मात्र हटाउनु हुँदैन, तर मेरो ‘शीर्ष आकर्षण’ छनोट गर्ने विधि त्रुटिपूर्ण छ यदि म सधैं लोकप्रियताका आधारमा रैंक गर्छु भने।”

### एआई एजेन्टहरूमा मेटाकग्निशनको महत्त्व

मेटाकग्निशनले एआई एजेन्ट डिजाइनमा निम्न कारणहरूले महत्त्वपूर्ण भूमिका खेल्छ:

![मेटाकग्निशनको महत्त्व](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.ne.png)

- आत्म-प्रतिबिम्ब: एजेन्टहरूले आफ्नो प्रदर्शनको मूल्याङ्कन गर्न र सुधारका क्षेत्रहरू पहिचान गर्न सक्छन्।
- अनुकूलनशीलता: एजेन्टहरूले विगतका अनुभव र परिवर्तनशील वातावरणका आधारमा आफ्ना रणनीतिहरू परिमार्जन गर्न सक्छन्।
- त्रुटि सुधार: एजेन्टहरूले स्वतन्त्र रूपमा त्रुटिहरू पत्ता लगाउन र सुधार गर्न सक्छन्, जसले थप सटीक परिणामहरू ल्याउँछ।
- स्रोत व्यवस्थापन: एजेन्टहरूले योजना बनाउने र आफ्ना कार्यहरूको मूल्याङ्कन गरेर समय र कम्प्युटेशनल पावर जस्ता स्रोतहरूको उपयोगलाई अनुकूलित गर्न सक्छन्।

## एआई एजेन्टको घटकहरू

मेटाकग्निटिभ प्रक्रियाहरूमा डुबुल्की मार्नुअघि, एआई एजेन्टको आधारभूत घटकहरू बुझ्न आवश्यक छ। एआई एजेन्ट सामान्यतया निम्नबाट बनेको हुन्छ:

- व्यक्तित्व: एजेन्टको व्यक्तित्व र विशेषताहरू, जसले प्रयोगकर्ताहरूसँग कसरी अन्तरक्रिया गर्ने परिभाषित गर्दछ।
- उपकरणहरू: एजेन्टले गर्न सक्ने क्षमताहरू र कार्यहरू।
- सीपहरू: एजेन्टसँग भएको ज्ञान र विशेषज्ञता।

यी घटकहरूले मिलेर "विशेषज्ञता इकाई" बनाउँछन्, जसले विशिष्ट कार्यहरू प्रदर्शन गर्न सक्छ।

**उदाहरण**:
यात्रा एजेन्टलाई विचार गर्नुहोस्, जसले तपाईंको छुट्टी योजना मात्र गर्दैन, तर वास्तविक-समय डेटा र अघिल्लो ग्राहक अनुभवहरूको आधारमा आफ्नो मार्ग समायोजन गर्दछ।

### उदाहरण: यात्रा एजेन्ट सेवामा मेटाकग्निशन

कल्पना गर्नुहोस् कि तपाईं एआईद्वारा सञ्चालित यात्रा एजेन्ट सेवा डिजाइन गर्दै हुनुहुन्छ। यो एजेन्ट, "यात्रा एजेन्ट," प्रयोगकर्ताहरूलाई उनीहरूको छुट्टी योजना बनाउन मद्दत गर्दछ। मेटाकग्निशन समावेश गर्न, यात्रा एजेन्टले आत्म-जागरूकता र विगतका अनुभवहरूको आधारमा आफ्ना कार्यहरू मूल्याङ्कन र समायोजन गर्न आवश्यक छ। यहाँ मेटाकग्निशनले कसरी भूमिका खेल्न सक्छ:

#### वर्तमान कार्य

वर्तमान कार्य भनेको प्रयोगकर्तालाई पेरिसको यात्रा योजना बनाउन मद्दत गर्नु हो।

#### कार्य पूरा गर्नका चरणहरू

1. **प्रयोगकर्ता प्राथमिकताहरू सङ्कलन गर्नुहोस्**: प्रयोगकर्तासँग उनीहरूको यात्रा मिति, बजेट, रुचि (जस्तै, संग्रहालय, खाना, किनमेल), र कुनै विशिष्ट आवश्यकताहरूको बारेमा सोध्नुहोस्।
2. **जानकारी पुनःप्राप्त गर्नुहोस्**: प्रयोगकर्ताको प्राथमिकतासँग मेल खाने उडान विकल्पहरू, आवास, आकर्षणहरू, र रेस्टुरेन्टहरूको खोजी गर्नुहोस्।
3. **सिफारिसहरू उत्पन्न गर्नुहोस्**: उडान विवरण, होटल आरक्षण, र सुझाइएको गतिविधिहरूको साथ व्यक्तिगत यात्रा कार्यक्रम प्रदान गर्नुहोस्।
4. **प्रतिक्रियाको आधारमा समायोजन गर्नुहोस्**: सिफारिसहरूको बारेमा प्रयोगकर्तासँग प्रतिक्रिया माग्नुहोस् र आवश्यक समायोजनहरू गर्नुहोस्।

#### आवश्यक स्रोतहरू

- उडान र होटल बुकिङ डेटाबेसमा पहुँच।
- पेरिसका आकर्षण र रेस्टुरेन्टहरूको जानकारी।
- अघिल्लो अन्तरक्रियाबाट प्रयोगकर्ता प्रतिक्रिया डेटा।

#### अनुभव र आत्म-प्रतिबिम्ब

यात्रा एजेन्टले आफ्नो प्रदर्शन मूल्याङ्कन गर्न र विगतका अनुभवहरूबाट सिक्न मेटाकग्निशन प्रयोग गर्दछ। उदाहरणका लागि:

1. **प्रयोगकर्ता प्रतिक्रियाको विश्लेषण**: यात्रा एजेन्टले प्रयोगकर्ता प्रतिक्रियाको समीक्षा गरेर कुन सिफारिसहरू राम्रोसँग स्वीकार गरियो र कुन गरिएन भनेर निर्धारण गर्दछ। यसले आफ्नो भविष्यका सुझावहरू तदनुसार समायोजन गर्दछ।
2. **अनुकूलनशीलता**: यदि प्रयोगकर्ताले पहिले भीडभाड भएका ठाउँहरू मन नपर्ने उल्लेख गरेका छन् भने, यात्रा एजेन्टले भविष्यमा व्यस्त घण्टामा लोकप्रिय पर्यटक स्थलहरू सिफारिस गर्नबाट बच्नेछ।
3. **त्रुटि सुधार**: यदि यात्रा एजेन्टले अघिल्लो बुकिङमा त्रुटि गर्‍यो, जस्तै पूर्ण रूपमा बुक गरिएको होटल सिफारिस गर्दै, यसले सिफारिसहरू गर्ने अघि उपलब्धता थप कडाइका साथ जाँच्न सिक्छ।

#### व्यावहारिक विकासकर्ता उदाहरण

यहाँ यात्रा एजेन्टको कोड कस्तो देखिन सक्छ भन्ने सरल उदाहरण छ, जसमा मेटाकग्निशन समावेश गरिएको छ:

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

#### मेटाकग्निशन किन महत्त्वपूर्ण छ

- **आत्म-प्रतिबिम्ब**: एजेन्टहरूले आफ्नो प्रदर्शन विश्लेषण गर्न र सुधारका क्षेत्रहरू पहिचान गर्न सक्छन्।
- **अनुकूलनशीलता**: एजेन्टहरूले प्रतिक्रिया र परिवर्तनशील अवस्थाहरूको आधारमा रणनीतिहरू परिमार्जन गर्न सक्छन्।
- **त्रुटि सुधार**: एजेन्टहरूले स्वतन्त्र रूपमा त्रुटिहरू पत्ता लगाउन र सुधार गर्न सक्छन्।
- **स्रोत व्यवस्थापन**: एजेन्टहरूले समय र कम्प्युटेशनल पावर जस्ता स्रोतहरूको उपयोगलाई अनुकूलित गर्न सक्छन्।

मेटाकग्निशन समावेश गरेर, यात्रा एजेन्टले थप व्यक्तिगत र सटीक यात्रा सिफारिसहरू प्रदान गर्न सक्छ, जसले समग्र प्रयोगकर्ता अनुभवलाई सुधार गर्दछ।

---

## २. एजेन्टहरूमा योजना बनाउने

एजेन्ट व्यवहारको महत्त्वपूर्ण घटक योजना हो। यसमा लक्ष्य प्राप्त गर्न आवश्यक चरणहरूको रूपरेखा बनाउने, वर्तमान अवस्था, स्रोतहरू, र सम्भावित बाधाहरू विचार गर्ने समावेश छ।

### योजनाका तत्वहरू

- **वर्तमान कार्य**: कार्यलाई स्पष्ट रूपमा परिभाषित गर्नुहोस्।
- **कार्य पूरा गर्नका चरणहरू**: कार्यलाई व्यवस्थापन गर्न मिल्ने चरणहरूमा विभाजन गर्नुहोस्।
- **आवश्यक स्रोतहरू**: आवश्यक स्रोतहरू पहिचान गर्नुहोस्।
- **अनुभव**: योजनालाई जानकारी दिन विगतका अनुभवहरूको उपयोग गर्नुहोस्।

**उदाहरण**:
यहाँ यात्रा एजेन्टले प्रयोगकर्तालाई प्रभावकारी रूपमा यात्रा योजना बनाउन मद्दत गर्नका लागि लिनुपर्ने चरणहरू छन्:

### यात्रा एजेन्टका चरणहरू

1. **प्रयोगकर्ता प्राथमिकताहरू सङ्कलन गर्नुहोस्**
   - प्रयोगकर्तासँग उनीहरूको यात्रा मिति, बजेट, रुचि, र कुनै विशिष्ट आवश्यकताहरूको बारेमा सोध्नुहोस्।
   - उदाहरण: "तपाईं कहिले यात्रा गर्न योजना गर्दै हुनुहुन्छ?" "तपाईंको बजेट दायरा कति हो?" "तपाईंलाई छुट्टीमा कुन गतिविधिहरू मनपर्छ?"

2. **जानकारी पुनःप्राप्त गर्नुहोस्**
   - प्रयोगकर्ताको प्राथमिकताका आधारमा सम्बन्धित यात्रा विकल्पहरूको खोजी गर्नुहोस्।
   - **उडानहरू**: प्रयोगकर्ताको बजेट र रुचाइएको यात्रा मितिहरूभित्र उपलब्ध उडानहरूको खोजी गर्नुहोस्।
   - **आवास**: प्रयोगकर्ताको स्थान, मूल्य, र सुविधाहरूका प्राथमिकताहरू मिल्ने होटल वा भाडाका सम्पत्तिहरू फेला पार्नुहोस्।
   - **आकर्षण र रेस्टुरेन्टहरू**: प्रयोगकर्ताको रुचिसँग मेल खाने लोकप्रिय आकर्षण, गतिविधि, र भोजन विकल्पहरू पहिचान गर्नुहोस्।

3. **सिफारिसहरू उत्पन्न गर्नुहोस्**
   - पुनःप्राप्त गरिएको जानकारीलाई व्यक्तिगत यात्रा कार्यक्रममा सङ्कलन गर्नुहोस्।
   - प्रयोगकर्ताको प्राथमिकताहरूमा सिफारिसहरू अनुकूल बनाउँदै उडान विकल्पहरू, होटल आरक्षण, र सुझाइएको गतिविधिहरूको विवरण प्रदान गर्नुहोस्।

4. **प्रयोगकर्तालाई यात्रा कार्यक्रम प्रस्तुत गर्नुहोस्**
   - प्रस्तावित यात्रा कार्यक्रम प्रयोगकर्तासँग समीक्षा गर्न साझा गर्नुहोस्।
   - उदाहरण: "यहाँ तपाईंको पेरिस यात्राको लागि सुझाइएको यात्रा कार्यक्रम छ। यसमा उडान विवरण, होटल बुकिङ, र सिफारिस गरिएका गतिविधिहरू र रेस्टुरेन्टहरूको सूची समावेश छ। कृपया आफ्नो विचार दिनुहोस्!"

5. **प्रतिक्रिया सङ्कलन गर्नुहोस्**
   - प्रस्तावित यात्रा कार्यक्रमको बारेमा प्रयोगकर्तासँग प्रतिक्रिया माग्नुहोस्।
   - उदाहरण: "तपाईंलाई उडान विकल्पहरू मनपर्छ?" "होटल तपाईंको आवश्यकताहरूका लागि उपयुक्त छ?" "के त्यहाँ कुनै गतिविधिहरू छन् जुन तपाईं थप्न वा हटाउन चाहनुहुन्छ?"

6. **प्रतिक्रियाको आधारमा समायोजन गर्नुहोस्**
   - प्रयोगकर्ताको प्रतिक्रियाको आधारमा यात्रा कार्यक्रम परिमार्जन गर्नुहोस्।
   - प्रयोगकर्ताको प्राथमिकताहरूलाई अझ राम्रोसँग मेल खाने उडान, आवास, र गतिविधि सिफारिसहरूमा आवश्यक परिवर्तनहरू गर्नुहोस्।

7. **अन्तिम पुष्टि**
   - प्रयोगकर्तालाई अन्तिम पुष्टि गर्न अद्यावधिक यात्रा कार्यक्रम प्रस्तुत गर्नुहोस्।
   - उदाहरण: "मैले तपाईंको प्रतिक्रियाको आधारमा समायोजनहरू गरेको छु। यहाँ अद्यावधिक यात्रा कार्यक्रम छ। के सबै कुरा तपाईंलाई ठीक लाग्छ?"

8. **बुक र आरक्षणहरू पुष्टि गर्नुहोस्**
   - प्रयोगकर्ताले यात्रा कार्यक्रम स्वीकृत गरेपछि, उडान, आवास, र कुनै पनि पूर्व-योजना गरिएका गतिविधिहरू बुक गर्न अगाडि बढ्नुहोस्।
   - प्रयोगकर्तालाई पुष्टि विवरणहरू पठाउनुहोस्।

9. **लगातार समर्थन प्रदान गर्नुहोस्**
   - प्रयोगकर्तालाई यात्रा अघि र यात्रा क्रममा कुनै पनि परिवर्तन वा थप अनुरोधहरूमा सहयोग गर्न उपलब्ध रहनुहोस्।
   - उदाहरण: "यदि तपाईंलाई आफ्नो यात्राको क्रममा थप सहयोग चाहिन्छ भने, कुनै पनि समयमा मलाई सम्पर्क गर्न नहिचकिचाउनुहोस्!"

### उदाहरण अन्तरक्रिया

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

## ३. सुधारात्मक RAG प्रणाली

सबैभन्दा पहिले, RAG उपकरण र पूर्व-प्रत्याशित सन्दर्भ लोडको बीचको फरक बुझौं।

![RAG बनाम सन्दर्भ लोड](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.ne.png)

### पुनःप्राप्ति-अग्मेन्टेड जेनेरेसन (RAG)

RAG ले पुनःप्राप्ति प्रणालीलाई जेनेरेटिभ मोडेलसँग संयोजन गर्दछ। जब कुनै प्रश्न सोधिन्छ, पुनःप्राप्ति प्रणालीले बाह्य स्रोतबाट सम्बन्धित कागजातहरू वा डेटा पुनःप्राप्त गर्दछ, र यो पुनःप्राप्त जानकारी जेनेरेटिभ मोडेलको इनपुटलाई अग्मेन्ट गर्न प्रयोग गरिन्छ। यसले मोडेललाई थप सटीक र सन्दर्भगत रूपमा प्रासंगिक प्रतिक्रियाहरू उत्पन्न गर्न मद्दत गर्दछ।

RAG प्रणालीमा, एजेन्टले ज्ञान आधारबाट सम्बन्धित जानकारी पुनःप्राप्त गर्दछ र उपयुक्त प्रतिक्रियाहरू वा कार्यहरू उत्पन्न गर्न प्रयोग गर्दछ।

### सुधारात्मक RAG दृष्टिकोण

सुधारात्मक RAG दृष्टिकोणले त्रुटिहरू सुधार गर्न र एआई एजेन्टहरूको सटीकता सुधार गर्न RAG प्रविधिहरू प्रयोग गर्न केन्द्रित गर्दछ। यसमा समावेश छ:

1. **प्रम्टिङ प्रविधि**: एजेन्टलाई सम्बन्धित जानकारी पुनःप्राप्त गर्न मार्गदर्शन गर्न विशिष्ट प्रम्प्टहरू प्रयोग गर्दै।
2. **उपकरण**: पुनःप्राप्त जानकारीको प्रासंगिकतालाई मूल्याङ्कन गर्न र सटीक प्रतिक्रियाहरू उत्पन्न गर्न एजेन्टलाई सक्षम बनाउने एल्गोरिदम र संयन्त्रहरू कार्यान्वयन गर्दै।
3. **मूल्याङ्कन**: एजेन्टको प्रदर्शनलाई निरन्तर मूल्याङ्कन गर्दै र यसको सटीकता र दक्षता सुधार गर्न समायोजन गर्दै।

#### उदाहरण: खोज एजेन्टमा सुधारात्मक RAG

वेबबाट जानकारी पुनःप्राप्त गरेर प्रयोगकर्ता प्रश्नहरूको उत्तर दिने खोज एजेन्टलाई विचार गर्नुहोस्। सुधारात्मक RAG दृष्टिकोणले समावेश गर्न सक्छ:

1. **प्रम्टिङ प्रविधि**: प्रयोगकर्ताको इनपुटको आधारमा खोज प्रश्नहरू तयार गर्दै।
2. **उपकरण**: प्राकृतिक भाषा प्रशोधन र मेसिन लर्निङ एल्गोरिदमहरू प्रयोग गरेर खोज परिणामहरू क्रमबद्ध र फिल्टर गर्दै।
3. **मूल्याङ्कन**: प्रयोगकर्ता प्रतिक्रियाको विश्लेषण गरेर पुनःप्राप्त जानकारीमा अशुद्धताहरू पहिचान गर्दै र सुधार गर्दै।

### यात्रा एजेन्टमा सुधारात्मक RAG

सुधारात्मक RAG (पुनःप्राप्ति-अग्मेन्टेड जेनेरेसन) ले एआईलाई जानकारी पुनःप्राप्त र उत्पन्न गर्न सक्षम बनाउँछ, जबकि कुनै पनि अशुद्धताहरू सुधार गर्दछ। यात्रा एजेन्टले सुधारात्मक RAG दृष्टिकोण प्रयोग गरेर थप सटीक र प्रासंगिक यात्रा सिफारिसहरू कसरी प्रदान गर्न सक्छ, हेरौं।

यसमा समावेश छ:

- **प्रम्टिङ प्रविधि:** एजेन्टलाई सम्बन्धित जानकारी पुनःप्राप्त गर्न मार्गदर्शन गर्न विशिष्ट प्रम्प्टहरू प्रयोग गर्दै।
- **उपकरण:** पुनःप्राप्त जानकारीको प्रासंगिकतालाई मूल्याङ्कन गर्न र सटीक प्रतिक्रियाहरू उत्पन्न गर्न एजेन्टलाई सक्षम बनाउने एल्गोरिदम र संयन्त्रहरू कार्यान्वयन गर्दै।
- **मूल्याङ्कन:** एजेन्टको प्रदर्शनलाई निरन्तर मूल्याङ
### पूर्व-प्रसंग लोड

पूर्व-प्रसंग लोडले मोडेललाई प्रश्नको प्रक्रिया अघि नै सम्बन्धित जानकारी वा पृष्ठभूमि लोड गर्न समावेश गर्दछ। यसको मतलब मोडेलसँग सुरुबाटै यो जानकारी उपलब्ध हुन्छ, जसले यसलाई थप जानकारी पुनःप्राप्त नगरी अधिक सूचित उत्तरहरू उत्पन्न गर्न मद्दत गर्न सक्छ।

यहाँ एक ट्राभल एजेन्ट एप्लिकेसनको लागि पूर्व-प्रसंग लोडको सरल उदाहरण छ:

#### व्याख्या

1. **इनिसियलाइजेसन (`__init__` मेथड)**: `TravelAgent` क्लासले लोकप्रिय गन्तव्यहरूको बारेमा जानकारी समावेश गर्ने डिक्सनरी लोड गर्दछ, जस्तै पेरिस, टोकियो, न्यूयोर्क, र सिड्नी। यस डिक्सनरीमा देश, मुद्रा, भाषा, र प्रमुख आकर्षणहरूको विवरण समावेश छ।

2. **जानकारी पुनःप्राप्ति (`get_destination_info` मेथड)**: जब प्रयोगकर्ताले विशेष गन्तव्यको बारेमा सोध्छ, `get_destination_info` मेथडले पूर्व-लोड गरिएको प्रसंग डिक्सनरीबाट सम्बन्धित जानकारी पुनःप्राप्त गर्दछ।

पूर्व-प्रसंग लोड गरेर, ट्राभल एजेन्ट एप्लिकेसनले प्रयोगकर्ताको प्रश्नहरूको उत्तर छिटो दिन सक्छ, वास्तविक समयमा बाह्य स्रोतबाट जानकारी पुनःप्राप्त नगरी। यसले एप्लिकेसनलाई अधिक प्रभावकारी र प्रतिक्रियाशील बनाउँछ।

### लक्ष्यसँग योजना सुरु गर्नु अघि बुटस्ट्र्यापिङ

लक्ष्यसँग योजना सुरु गर्नु भनेको स्पष्ट उद्देश्य वा लक्ष्य परिणामको साथ सुरु गर्नु हो। यस लक्ष्यलाई अगाडि परिभाषित गरेर, मोडेलले यसलाई पुनरावृत्त प्रक्रियाको मार्गदर्शक सिद्धान्तको रूपमा प्रयोग गर्न सक्छ। यसले सुनिश्चित गर्दछ कि प्रत्येक पुनरावृत्ति इच्छित परिणाम प्राप्त गर्न नजिक जान्छ, प्रक्रिया अधिक प्रभावकारी र केन्द्रित बनाउँदै।

#### परिदृश्य

एक ट्राभल एजेन्टले ग्राहकको लागि अनुकूलित छुट्टी योजना बनाउन चाहन्छ। लक्ष्य भनेको ग्राहकको प्राथमिकता र बजेटको आधारमा यात्रा तालिका बनाउनु हो।

#### चरणहरू

1. ग्राहकको प्राथमिकता र बजेट परिभाषित गर्नुहोस्।
2. यी प्राथमिकताहरूको आधारमा प्रारम्भिक योजना बुटस्ट्र्याप गर्नुहोस्।
3. योजना सुधार गर्न पुनरावृत्ति गर्नुहोस्, ग्राहकको सन्तुष्टिको लागि अनुकूलन गर्दै।

#### कोड व्याख्या

1. **इनिसियलाइजेसन (`__init__` मेथड)**: `TravelAgent` क्लासलाई सम्भावित गन्तव्यहरूको सूचीको साथ इनिसियलाइज गरिन्छ, जसमा नाम, लागत, र गतिविधि प्रकार जस्ता विशेषताहरू छन्।

2. **योजना बुटस्ट्र्यापिङ (`bootstrap_plan` मेथड)**: यो मेथडले ग्राहकको प्राथमिकता र बजेटको आधारमा प्रारम्भिक यात्रा योजना बनाउँछ। यो गन्तव्यहरूको सूचीमा पुनरावृत्ति गर्दछ र यदि तिनीहरू ग्राहकको प्राथमिकतासँग मेल खान्छन् र बजेटभित्र फिट हुन्छन् भने तिनीहरूलाई योजनामा ​​थप्छ।

3. **प्राथमिकता मिलान (`match_preferences` मेथड)**: यो मेथडले गन्तव्य ग्राहकको प्राथमिकतासँग मेल खान्छ कि भनेर जाँच गर्दछ।

4. **योजना पुनरावृत्ति (`iterate_plan` मेथड)**: यो मेथडले प्रारम्भिक योजनालाई सुधार गर्दछ, ग्राहकको प्राथमिकता र बजेट सीमाहरू विचार गर्दै प्रत्येक गन्तव्यलाई राम्रो मेलसँग बदल्ने प्रयास गर्दै।

5. **लागत गणना (`calculate_cost` मेथड)**: यो मेथडले हालको योजनाको कुल लागत गणना गर्दछ, सम्भावित नयाँ गन्तव्य समावेश गर्दै।

#### उदाहरण प्रयोग

- **प्रारम्भिक योजना**: ट्राभल एजेन्टले ग्राहकको प्राथमिकता (जस्तै, साइटसिइङ) र $2000 बजेटको आधारमा प्रारम्भिक योजना बनाउँछ।
- **सुधारिएको योजना**: ट्राभल एजेन्टले योजना पुनरावृत्ति गर्दछ, ग्राहकको प्राथमिकता र बजेटको लागि अनुकूलन गर्दै।

लक्ष्यको साथ योजना बुटस्ट्र्याप गरेर (जस्तै, ग्राहक सन्तुष्टि अधिकतम बनाउने) र योजना सुधार गर्न पुनरावृत्ति गरेर, ट्राभल एजेन्टले ग्राहकको लागि अनुकूलित र अनुकूलित यात्रा तालिका बनाउन सक्छ। यो दृष्टिकोणले सुनिश्चित गर्दछ कि यात्रा योजना सुरुबाट ग्राहकको प्राथमिकता र बजेटसँग मेल खान्छ र प्रत्येक पुनरावृत्तिसँग सुधार हुन्छ।

### LLM प्रयोग गरेर पुनःर्‍याङ्किङ र स्कोरिङको फाइदा उठाउने

ठूला भाषा मोडेलहरू (LLMs) पुनःर्‍याङ्किङ र स्कोरिङको लागि प्रयोग गर्न सकिन्छ, पुनःप्राप्त गरिएका दस्तावेजहरू वा उत्पन्न उत्तरहरूको सान्दर्भिकता र गुणस्तर मूल्याङ्कन गरेर। यसले कसरी काम गर्छ:

**पुनःप्राप्ति:** प्रारम्भिक पुनःप्राप्ति चरणले प्रश्नको आधारमा उम्मेदवार दस्तावेजहरू वा उत्तरहरूको सेट फेच गर्दछ।

**पुनःर्‍याङ्किङ:** LLMले यी उम्मेदवारहरूको मूल्याङ्कन गर्दछ र तिनीहरूलाई सान्दर्भिकता र गुणस्तरको आधारमा पुनःर्‍याङ्क गर्दछ। यस चरणले सुनिश्चित गर्दछ कि सबैभन्दा सान्दर्भिक र उच्च गुणस्तरको जानकारी पहिले प्रस्तुत गरिएको छ।

**स्कोरिङ:** LLMले प्रत्येक उम्मेदवारलाई स्कोर प्रदान गर्दछ, जसले तिनीहरूको सान्दर्भिकता र गुणस्तरलाई प्रतिबिम्बित गर्दछ। यसले प्रयोगकर्ताको लागि उत्तम उत्तर वा दस्तावेज चयन गर्न मद्दत गर्दछ।

LLMs प्रयोग गरेर पुनःर्‍याङ्किङ र स्कोरिङको फाइदा उठाएर, प्रणालीले अधिक सटीक र सान्दर्भिक जानकारी प्रदान गर्न सक्छ, समग्र प्रयोगकर्ता अनुभव सुधार गर्दै।
#### व्यावहारिक उदाहरण: यात्रा एजेन्टमा उद्देश्यसहित खोजी

यात्रा एजेन्टलाई उदाहरणको रूपमा लिऔं र उद्देश्यसहित खोजी कसरी कार्यान्वयन गर्न सकिन्छ हेर्नुहोस्।

1. **प्रयोगकर्ताको प्राथमिकता संकलन गर्नुहोस्**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **प्रयोगकर्ताको उद्देश्य बुझ्नुहोस्**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **सन्दर्भको जानकारी राख्नुहोस्**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **खोजी गर्नुहोस् र नतिजा व्यक्तिगत बनाउनुहोस्**

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

5. **उदाहरण प्रयोग**

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

## 4. उपकरणको रूपमा कोड उत्पन्न गर्नु

कोड उत्पन्न गर्ने एजेन्टहरूले AI मोडेल प्रयोग गरेर कोड लेख्छन् र कार्यान्वयन गर्छन्, जटिल समस्याहरू समाधान गर्न र कार्यहरू स्वचालित गर्न।

### कोड उत्पन्न गर्ने एजेन्टहरू

कोड उत्पन्न गर्ने एजेन्टहरूले जेनेरेटिभ AI मोडेल प्रयोग गरेर कोड लेख्छन् र कार्यान्वयन गर्छन्। यी एजेन्टहरूले जटिल समस्याहरू समाधान गर्न, कार्यहरू स्वचालित गर्न, र विभिन्न प्रोग्रामिङ भाषाहरूमा कोड उत्पन्न र चलाएर मूल्यवान जानकारी प्रदान गर्न सक्छन्।

#### व्यावहारिक प्रयोगहरू

1. **स्वचालित कोड उत्पन्न**: डेटा विश्लेषण, वेब स्क्र्यापिङ, वा मेसिन लर्निङ जस्ता विशिष्ट कार्यहरूको लागि कोड स्निपेट उत्पन्न गर्नुहोस्।
2. **SQL लाई RAG को रूपमा प्रयोग गर्नुहोस्**: डेटाबेसबाट डेटा प्राप्त गर्न र हेरफेर गर्न SQL क्वेरीहरू प्रयोग गर्नुहोस्।
3. **समस्या समाधान**: विशिष्ट समस्याहरू समाधान गर्न कोड सिर्जना गर्नुहोस् र कार्यान्वयन गर्नुहोस्, जस्तै एल्गोरिदमलाई अनुकूलित गर्नु वा डेटा विश्लेषण गर्नु।

#### उदाहरण: डेटा विश्लेषणका लागि कोड उत्पन्न गर्ने एजेन्ट

कल्पना गर्नुहोस् कि तपाईं कोड उत्पन्न गर्ने एजेन्ट डिजाइन गर्दै हुनुहुन्छ। यसले कसरी काम गर्न सक्छ:

1. **कार्य**: ट्रेन्ड र ढाँचाहरू पहिचान गर्न डेटा सेट विश्लेषण गर्नुहोस्।
2. **चरणहरू**:
   - डेटा सेटलाई डेटा विश्लेषण उपकरणमा लोड गर्नुहोस्।
   - डेटा फिल्टर गर्न र समग्र बनाउन SQL क्वेरीहरू उत्पन्न गर्नुहोस्।
   - क्वेरीहरू कार्यान्वयन गर्नुहोस् र नतिजा प्राप्त गर्नुहोस्।
   - नतिजाको आधारमा भिजुअलाइजेसन र जानकारी उत्पन्न गर्नुहोस्।
3. **आवश्यक स्रोतहरू**: डेटा सेट पहुँच, डेटा विश्लेषण उपकरणहरू, र SQL क्षमता।
4. **अनुभव**: विगतको विश्लेषण नतिजाहरू प्रयोग गरेर भविष्यको विश्लेषणको सटीकता र सान्दर्भिकता सुधार गर्नुहोस्।

### उदाहरण: यात्रा एजेन्टका लागि कोड उत्पन्न गर्ने एजेन्ट

यस उदाहरणमा, हामी कोड उत्पन्न गर्ने एजेन्ट, यात्रा एजेन्ट, डिजाइन गर्नेछौं जसले प्रयोगकर्ताहरूलाई यात्रा योजना बनाउन सहयोग पुर्‍याउँछ। यस एजेन्टले यात्रा विकल्पहरू प्राप्त गर्ने, नतिजा फिल्टर गर्ने, र जेनेरेटिभ AI प्रयोग गरेर यात्रा योजना तयार गर्ने कार्यहरू सम्हाल्न सक्छ।

#### कोड उत्पन्न गर्ने एजेन्टको अवलोकन

1. **प्रयोगकर्ताको प्राथमिकता संकलन गर्नुहोस्**: गन्तव्य, यात्रा मिति, बजेट, र रुचि जस्ता प्रयोगकर्ताको इनपुट संकलन गर्नुहोस्।
2. **डेटा प्राप्त गर्न कोड उत्पन्न गर्नुहोस्**: उडान, होटल, र आकर्षणहरूको बारेमा डेटा प्राप्त गर्न कोड स्निपेट उत्पन्न गर्नुहोस्।
3. **उत्पन्न कोड कार्यान्वयन गर्नुहोस्**: वास्तविक-समय जानकारी प्राप्त गर्न उत्पन्न कोड चलाउनुहोस्।
4. **यात्रा योजना तयार गर्नुहोस्**: प्राप्त डेटा व्यक्तिगत यात्रा योजनामा संकलन गर्नुहोस्।
5. **प्रतिक्रिया अनुसार समायोजन गर्नुहोस्**: प्रयोगकर्ताको प्रतिक्रिया प्राप्त गर्नुहोस् र नतिजा सुधार गर्न आवश्यक भएमा कोड पुनः उत्पन्न गर्नुहोस्।

#### चरण-दर-चरण कार्यान्वयन

1. **प्रयोगकर्ताको प्राथमिकता संकलन गर्नुहोस्**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **डेटा प्राप्त गर्न कोड उत्पन्न गर्नुहोस्**

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

3. **उत्पन्न कोड कार्यान्वयन गर्नुहोस्**

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

4. **यात्रा योजना तयार गर्नुहोस्**

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

5. **प्रतिक्रिया अनुसार समायोजन गर्नुहोस्**

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

### वातावरणीय जानकारी र तर्कशक्ति प्रयोग गर्नुहोस्

तालिकाको स्किमाको आधारमा क्वेरी उत्पन्न प्रक्रिया सुधार गर्न वातावरणीय जानकारी र तर्कशक्ति प्रयोग गर्न सकिन्छ।

यसलाई कसरी गर्न सकिन्छ भन्ने उदाहरण यहाँ छ:

1. **स्किमाको समझ**: प्रणालीले तालिकाको स्किमा बुझ्नेछ र क्वेरी उत्पन्न गर्न यस जानकारीलाई प्रयोग गर्नेछ।
2. **प्रतिक्रिया अनुसार समायोजन**: प्रणालीले प्रयोगकर्ताको प्रतिक्रिया अनुसार प्राथमिकता समायोजन गर्नेछ र स्किमाका कुन क्षेत्रहरू अपडेट गर्न आवश्यक छ भनेर तर्क गर्नेछ।
3. **क्वेरी उत्पन्न र कार्यान्वयन गर्नुहोस्**: प्रणालीले नयाँ प्राथमिकताको आधारमा अपडेट गरिएको उडान र होटल डेटा प्राप्त गर्न क्वेरी उत्पन्न र कार्यान्वयन गर्नेछ।

यहाँ यी अवधारणाहरू समावेश गर्ने अद्यावधिक गरिएको Python कोड उदाहरण छ:

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

#### व्याख्या - प्रतिक्रिया अनुसार बुकिङ

1. **स्किमा जानकारी**: `schema` शब्दकोशले प्रतिक्रिया अनुसार प्राथमिकता कसरी समायोजन गर्नुपर्छ भन्ने परिभाषित गर्दछ। यसमा `favorites` र `avoid` जस्ता क्षेत्रहरू समावेश छन्, जससँग सम्बन्धित समायोजनहरू छन्।
2. **प्राथमिकता समायोजन (`adjust_based_on_feedback` विधि)**: यो विधिले प्रयोगकर्ताको प्रतिक्रिया र स्किमाको आधारमा प्राथमिकता समायोजन गर्दछ।
3. **वातावरण-आधारित समायोजन (`adjust_based_on_environment` विधि)**: यो विधिले स्किमा र प्रतिक्रियाको आधारमा समायोजनहरू अनुकूलित गर्दछ।
4. **क्वेरी उत्पन्न र कार्यान्वयन गर्नुहोस्**: प्रणालीले समायोजित प्राथमिकताको आधारमा अपडेट गरिएको उडान र होटल डेटा प्राप्त गर्न कोड उत्पन्न गर्दछ र यी क्वेरीहरूको कार्यान्वयनको अनुकरण गर्दछ।
5. **यात्रा योजना तयार गर्नुहोस्**: प्रणालीले नयाँ उडान, होटल, र आकर्षण डेटा आधारमा अद्यावधिक यात्रा योजना बनाउँछ।

प्रणालीलाई वातावरण-सचेत बनाउँदै र स्किमाको आधारमा तर्क गर्दै, यसले अधिक सटीक र सान्दर्भिक क्वेरीहरू उत्पन्न गर्न सक्छ, जसले राम्रो यात्रा सिफारिसहरू र व्यक्तिगत प्रयोगकर्ता अनुभव प्रदान गर्दछ।

### SQL लाई Retrieval-Augmented Generation (RAG) प्रविधिको रूपमा प्रयोग गर्नुहोस्

SQL (Structured Query Language) डेटाबेसहरूसँग अन्तरक्रिया गर्नको लागि शक्तिशाली उपकरण हो। Retrieval-Augmented Generation (RAG) दृष्टिकोणको भागको रूपमा प्रयोग गर्दा, SQL डेटाबेसबाट सान्दर्भिक डेटा प्राप्त गर्न प्रयोग गर्न सकिन्छ जसले AI एजेन्टहरूमा प्रतिक्रियाहरू वा कार्यहरू उत्पन्न गर्न जानकारी प्रदान गर्दछ। यात्रा एजेन्टको सन्दर्भमा SQL कसरी RAG प्रविधिको रूपमा प्रयोग गर्न सकिन्छ हेर्नुहोस्।

#### मुख्य अवधारणाहरू

1. **डेटाबेस अन्तरक्रिया**:
   - SQL डेटाबेस क्वेरी गर्न, सान्दर्भिक जानकारी प्राप्त गर्न, र डेटा हेरफेर गर्न प्रयोग गरिन्छ।
   - उदाहरण: यात्रा डेटाबेसबाट उडान विवरण, होटल जानकारी, र आकर्षणहरू प्राप्त गर्नु।

2. **RAG सँग एकीकरण**:
   - SQL क्वेरीहरू प्रयोगकर्ताको इनपुट र प्राथमिकताको आधारमा उत्पन्न गरिन्छ।
   - प्राप्त डेटा व्यक्तिगत सिफारिसहरू वा कार्यहरू उत्पन्न गर्न प्रयोग गरिन्छ।

3. **डायनामिक क्वेरी उत्पन्न**:
   - AI एजेन्टले सन्दर्भ र प्रयोगकर्ताको आवश्यकताको आधारमा डायनामिक SQL क्वेरीहरू उत्पन्न गर्दछ।
   - उदाहरण: बजेट, मिति, र रुचिको आधारमा नतिजा फिल्टर गर्न SQL क्वेरीहरू अनुकूलित गर्नुहोस्।

#### प्रयोगहरू

- **स्वचालित कोड उत्पन्न**: विशिष्ट कार्यहरूको लागि कोड स्निपेट उत्पन्न गर्नुहोस्।
- **SQL लाई RAG को रूपमा प्रयोग गर्नुहोस्**: डेटा हेरफेर गर्न SQL क्वेरीहरू प्रयोग गर्नुहोस्।
- **समस्या समाधान**: समस्याहरू समाधान गर्न कोड सिर्जना गर्नुहोस् र कार्यान्वयन गर्नुहोस्।

**उदाहरण**:
डेटा विश्लेषण एजेन्ट:

1. **कार्य**: ट्रेन्डहरू पत्ता लगाउन डेटा सेट विश्लेषण गर्नुहोस्।
2. **चरणहरू**:
   - डेटा सेट लोड गर्नुहोस्।
   - डेटा फिल्टर गर्न SQL क्वेरीहरू उत्पन्न गर्नुहोस्।
   - क्वेरीहरू कार्यान्वयन गर्नुहोस् र नतिजा प्राप्त गर्नुहोस्।
   - भिजुअलाइजेसन र जानकारी उत्पन्न गर्नुहोस्।
3. **स्रोतहरू**: डेटा सेट पहुँच, SQL क्षमता।
4. **अनुभव**: विगतको नतिजाहरू प्रयोग गरेर भविष्यको विश्लेषण सुधार गर्नुहोस्।

#### व्यावहारिक उदाहरण: यात्रा एजेन्टमा SQL प्रयोग गर्नुहोस्

1. **प्रयोगकर्ताको प्राथमिकता संकलन गर्नुहोस्**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **SQL क्वेरी उत्पन्न गर्नुहोस्**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **SQL क्वेरी कार्यान्वयन गर्नुहोस्**

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

4. **सिफारिसहरू उत्पन्न गर्नुहोस्**

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

#### SQL क्वेरीहरूको उदाहरण

1. **उडान क्वेरी**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **होटल क्वेरी**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **आकर्षण क्वेरी**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

SQL लाई Retrieval-Augmented Generation (RAG) प्रविधिको भागको रूपमा प्रयोग गरेर, यात्रा एजेन्ट जस्ता AI एजेन्टहरूले सान्दर्भिक डेटा गतिशील रूपमा प्राप्त गर्न र प्रयोग गर्न सक्छन्, जसले सटीक र व्यक्तिगत सिफारिसहरू प्रदान गर्दछ।

### मेटाकग्निशनको उदाहरण

मेटाकग्निशनको कार्यान्वयन देखाउन, एउटा सरल एजेन्ट बनाऔं जसले *आफ्नो निर्णय प्रक्रियामा प्रतिबिम्बित गर्छ* र समस्या समाधान गर्दा आफ्नो रणनीति समायोजन गर्छ। यस उदाहरणमा, हामी एउटा प्रणाली बनाउनेछौं जहाँ एजेन्टले होटलको छनोटलाई अनुकूलित गर्न प्रयास गर्छ, तर आफ्नो तर्कको मूल्यांकन गर्छ र त्रुटि वा उपयुक्तभन्दा कम छनोट गर्दा आफ्नो रणनीति समायोजन गर्छ।

#### मेटाकग्निशनलाई कसरी चित्रण गर्छ:

1. **प्रारम्भिक निर्णय**: एजेन्टले गुणस्तरको प्रभाव नबुझी सबैभन्दा सस्तो होटल चयन गर्नेछ।
2. **प्रतिबिम्ब र मूल्यांकन**: प्रारम्भिक छनोटपछि, एजेन्टले प्रयोगकर्ताको प्रतिक्रियाको आधारमा होटल "खराब" छनोट हो कि भनेर जाँच गर्नेछ। यदि होटलको गुणस्तर धेरै कम छ भने, यसले आफ्नो तर्कमा प्रतिबिम्बित गर्नेछ।
3. **रणनीति समायोजन**: एजेन्टले आफ्नो रणनीति समायोजन गर्नेछ र "सबैभन्दा सस्तो" बाट "सबैभन्दा उच्च गुणस्तर" मा स्विच गर्नेछ, जसले भविष्यको पुनरावृत्तिहरूमा निर्णय प्रक्रिया सुधार गर्नेछ।

यहाँ एक उदाहरण छ:

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

#### एजेन्टको मेटाकग्निशन क्षमता

मुख्य कुरा यहाँ एजेन्टको क्षमता हो:
- आफ्नो अघिल्लो छनोट र निर्णय प्रक्रियाको मूल्यांकन गर्नु।
- प्रतिबिम्बको आधारमा आफ्नो रणनीति समायोजन गर्नु अर्थात्, मेटाकग्निशनको कार्यान्वयन।

यो मेटाकग्निशनको सरल रूप हो जहाँ प्रणालीले आन्तरिक प्रतिक्रियाको आधारमा आफ्नो तर्क प्रक्रिया समायोजन गर्न सक्षम छ।

### निष्कर्ष

मेटाकग्निशन एक शक्तिशाली उपकरण हो जसले AI एजेन्टहरूको क्षमता उल्लेखनीय रूपमा सुधार गर्न सक्छ। मेटाकग्निशन प्रक्रियाहरू समावेश गरेर, तपाईं अधिक बुद्धिमान, अनुकूलनशील, र कुशल एजेन्टहरू डिजाइन गर्न सक्नुहुन्छ। थप स्रोतहरू प्रयोग गरेर AI एजेन्टहरूमा मेटाकग्निशनको रोचक संसार अन्वेषण गर्नुहोस्।

### मेटाकग्निशन डिजाइन ढाँचाबारे थप प्रश्नहरू छन्?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) मा सामेल हुनुहोस् अन्य सिक्नेहरूसँग भेट्न, कार्यालय समयमा भाग लिन, र आफ्नो AI एजेन्टहरूको प्रश्नहरूको उत्तर प्राप्त गर्न।

## अघिल्लो पाठ

[मल्टि-एजेन्ट डिजाइन ढाँचा](../08-multi-agent/README.md)

## अर्को पाठ

[उत्पादनमा AI एजेन्टहरू](../10-ai-agents-production/README.md)

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी यथासम्भव सटीकता सुनिश्चित गर्न प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटि वा अशुद्धता हुन सक्छ। यसको मूल भाषामा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्त्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुने छैनौं।