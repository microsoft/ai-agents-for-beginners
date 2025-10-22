<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-29T12:07:45+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "bn"
}
-->
[![মাল্টি-এজেন্ট ডিজাইন](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.bn.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(উপরের ছবিতে ক্লিক করে এই পাঠের ভিডিও দেখুন)_
# এআই এজেন্টে মেটাকগনিশন

## ভূমিকা

এআই এজেন্টে মেটাকগনিশন নিয়ে পাঠে আপনাকে স্বাগতম! এই অধ্যায়টি নবীনদের জন্য তৈরি করা হয়েছে যারা জানতে চান কীভাবে এআই এজেন্ট তাদের নিজস্ব চিন্তাভাবনা প্রক্রিয়া নিয়ে চিন্তা করতে পারে। এই পাঠ শেষে, আপনি গুরুত্বপূর্ণ ধারণাগুলি বুঝতে পারবেন এবং এআই এজেন্ট ডিজাইনে মেটাকগনিশন প্রয়োগের জন্য ব্যবহারিক উদাহরণে দক্ষ হবেন।

## শেখার লক্ষ্য

এই পাঠ সম্পন্ন করার পর, আপনি সক্ষম হবেন:

1. এজেন্ট সংজ্ঞায় যুক্তি চক্রের প্রভাব বুঝতে।
2. পরিকল্পনা এবং মূল্যায়ন কৌশল ব্যবহার করে স্ব-সংশোধনকারী এজেন্ট তৈরি করতে।
3. কোড পরিচালনা করতে সক্ষম এজেন্ট তৈরি করতে যা নির্দিষ্ট কাজ সম্পন্ন করতে পারে।

## মেটাকগনিশনের পরিচিতি

মেটাকগনিশন বলতে বোঝায় উচ্চ-স্তরের জ্ঞানীয় প্রক্রিয়া যা নিজের চিন্তাভাবনা নিয়ে চিন্তা করার সাথে সম্পর্কিত। এআই এজেন্টের ক্ষেত্রে, এর অর্থ হলো তাদের নিজস্ব কাজ মূল্যায়ন এবং অতীত অভিজ্ঞতার ভিত্তিতে তা সংশোধন করার ক্ষমতা থাকা। মেটাকগনিশন, বা "চিন্তাভাবনা নিয়ে চিন্তা করা," এজেন্টিক এআই সিস্টেমের উন্নয়নে একটি গুরুত্বপূর্ণ ধারণা। এটি এআই সিস্টেমকে তাদের নিজস্ব অভ্যন্তরীণ প্রক্রিয়া সম্পর্কে সচেতন হতে এবং তাদের আচরণ পর্যবেক্ষণ, নিয়ন্ত্রণ এবং মানিয়ে নিতে সক্ষম করে। যেমন আমরা কোনো পরিস্থিতি বিশ্লেষণ করি বা কোনো সমস্যার সমাধান খুঁজি। এই আত্মসচেতনতা এআই সিস্টেমকে আরও ভালো সিদ্ধান্ত নিতে, ভুল সনাক্ত করতে এবং সময়ের সাথে তাদের কর্মক্ষমতা উন্নত করতে সাহায্য করতে পারে—আবার টুরিং টেস্ট এবং এআই-এর ভবিষ্যৎ নিয়ে বিতর্কের সাথে সংযোগ স্থাপন করে।

এজেন্টিক এআই সিস্টেমের প্রেক্ষাপটে, মেটাকগনিশন নিম্নলিখিত চ্যালেঞ্জগুলির সমাধানে সাহায্য করতে পারে:
- স্বচ্ছতা: এআই সিস্টেম তাদের যুক্তি এবং সিদ্ধান্ত ব্যাখ্যা করতে পারে।
- যুক্তি: এআই সিস্টেমের তথ্য সংশ্লেষণ এবং সঠিক সিদ্ধান্ত নেওয়ার ক্ষমতা বৃদ্ধি।
- অভিযোজন: এআই সিস্টেমকে নতুন পরিবেশ এবং পরিবর্তিত পরিস্থিতির সাথে মানিয়ে নিতে সক্ষম করা।
- উপলব্ধি: এআই সিস্টেমের পরিবেশ থেকে ডেটা সনাক্ত এবং ব্যাখ্যা করার সঠিকতা উন্নত করা।

### মেটাকগনিশন কী?

মেটাকগনিশন, বা "চিন্তাভাবনা নিয়ে চিন্তা করা," একটি উচ্চ-স্তরের জ্ঞানীয় প্রক্রিয়া যা আত্মসচেতনতা এবং নিজের জ্ঞানীয় প্রক্রিয়ার নিয়ন্ত্রণের সাথে সম্পর্কিত। এআই-এর ক্ষেত্রে, মেটাকগনিশন এজেন্টকে তাদের কৌশল এবং কর্ম মূল্যায়ন ও মানিয়ে নিতে সক্ষম করে, যা সমস্যার সমাধান এবং সিদ্ধান্ত গ্রহণের ক্ষমতা উন্নত করে। মেটাকগনিশন বুঝে, আপনি এমন এআই এজেন্ট ডিজাইন করতে পারেন যা শুধু বুদ্ধিমান নয়, বরং আরও অভিযোজিত এবং দক্ষ। প্রকৃত মেটাকগনিশনে, আপনি এআই-কে তার নিজস্ব যুক্তি নিয়ে স্পষ্টভাবে চিন্তা করতে দেখবেন।

উদাহরণ: “আমি সস্তা ফ্লাইটগুলোকে অগ্রাধিকার দিয়েছি কারণ... আমি হয়তো সরাসরি ফ্লাইটগুলো মিস করছি, তাই আমাকে আবার চেক করতে হবে।”
কীভাবে বা কেন এটি একটি নির্দিষ্ট পথ বেছে নিয়েছে তা ট্র্যাক রাখা।
- লক্ষ্য করা যে এটি ভুল করেছে কারণ এটি আগের ব্যবহারকারীর পছন্দগুলোর উপর অতিরিক্ত নির্ভর করেছে, তাই এটি তার সিদ্ধান্ত গ্রহণের কৌশল পরিবর্তন করে, শুধু চূড়ান্ত সুপারিশ নয়।
- প্যাটার্ন নির্ণয় করা, যেমন “যখনই আমি ব্যবহারকারীকে ‘খুব ভিড়’ উল্লেখ করতে দেখি, তখন আমি শুধু নির্দিষ্ট আকর্ষণগুলো সরিয়ে ফেলি না, বরং আমার ‘শীর্ষ আকর্ষণ’ বাছাই করার পদ্ধতিটি ভুল যদি আমি সবসময় জনপ্রিয়তার ভিত্তিতে র‌্যাঙ্ক করি।”

### এআই এজেন্টে মেটাকগনিশনের গুরুত্ব

মেটাকগনিশন এআই এজেন্ট ডিজাইনে কয়েকটি কারণে গুরুত্বপূর্ণ ভূমিকা পালন করে:

![মেটাকগনিশনের গুরুত্ব](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.bn.png)

- আত্ম-প্রতিফলন: এজেন্ট তাদের নিজস্ব কর্মক্ষমতা মূল্যায়ন করতে পারে এবং উন্নতির ক্ষেত্র চিহ্নিত করতে পারে।
- অভিযোজনযোগ্যতা: এজেন্ট অতীত অভিজ্ঞতা এবং পরিবর্তিত পরিবেশের ভিত্তিতে তাদের কৌশল পরিবর্তন করতে পারে।
- ভুল সংশোধন: এজেন্ট স্বয়ংক্রিয়ভাবে ভুল সনাক্ত এবং সংশোধন করতে পারে, যা আরও সঠিক ফলাফল প্রদান করে।
- সম্পদ ব্যবস্থাপনা: এজেন্ট তাদের কর্ম পরিকল্পনা এবং মূল্যায়নের মাধ্যমে সময় এবং গণনাশক্তি অপ্টিমাইজ করতে পারে।

## এআই এজেন্টের উপাদান

মেটাকগনিশন প্রক্রিয়ায় যাওয়ার আগে, একটি এআই এজেন্টের মৌলিক উপাদানগুলো বোঝা গুরুত্বপূর্ণ। একটি এআই এজেন্ট সাধারণত নিম্নলিখিত উপাদানগুলো নিয়ে গঠিত:

- ব্যক্তিত্ব: এজেন্টের ব্যক্তিত্ব এবং বৈশিষ্ট্য, যা ব্যবহারকারীদের সাথে তার যোগাযোগের ধরন নির্ধারণ করে।
- সরঞ্জাম: এজেন্টের সক্ষমতা এবং কার্যকারিতা।
- দক্ষতা: এজেন্টের জ্ঞান এবং দক্ষতা।

এই উপাদানগুলো একসাথে কাজ করে একটি "বিশেষজ্ঞ ইউনিট" তৈরি করে যা নির্দিষ্ট কাজ সম্পাদন করতে পারে।

**উদাহরণ**:
একটি ভ্রমণ এজেন্টের কথা ভাবুন, যা শুধু আপনার ছুটি পরিকল্পনা করে না বরং বাস্তব-সময়ের ডেটা এবং পূর্ববর্তী গ্রাহকের অভিজ্ঞতার ভিত্তিতে তার পথ সামঞ্জস্য করে।

### উদাহরণ: ভ্রমণ এজেন্ট পরিষেবায় মেটাকগনিশন

ধরুন আপনি একটি এআই-চালিত ভ্রমণ এজেন্ট পরিষেবা ডিজাইন করছেন। এই এজেন্ট, "ট্রাভেল এজেন্ট," ব্যবহারকারীদের তাদের ছুটি পরিকল্পনা করতে সাহায্য করে। মেটাকগনিশন অন্তর্ভুক্ত করতে, ট্রাভেল এজেন্টকে আত্মসচেতনতা এবং পূর্ববর্তী অভিজ্ঞতার ভিত্তিতে তার কর্ম মূল্যায়ন এবং সামঞ্জস্য করতে হবে। এখানে মেটাকগনিশন কীভাবে ভূমিকা রাখতে পারে:

#### বর্তমান কাজ

বর্তমান কাজ হলো একজন ব্যবহারকারীকে প্যারিসে একটি ট্রিপ পরিকল্পনা করতে সাহায্য করা।

#### কাজ সম্পন্ন করার ধাপ

1. **ব্যবহারকারীর পছন্দ সংগ্রহ**: ব্যবহারকারীর ভ্রমণের তারিখ, বাজেট, আগ্রহ (যেমন জাদুঘর, খাবার, কেনাকাটা), এবং কোনো নির্দিষ্ট প্রয়োজন সম্পর্কে জিজ্ঞাসা করুন।
2. **তথ্য সংগ্রহ**: ব্যবহারকারীর পছন্দের সাথে মিলে এমন ফ্লাইট অপশন, থাকার জায়গা, আকর্ষণ এবং রেস্তোরাঁর তথ্য অনুসন্ধান করুন।
3. **সুপারিশ তৈরি**: ফ্লাইটের বিবরণ, হোটেল বুকিং এবং প্রস্তাবিত কার্যক্রম সহ একটি ব্যক্তিগতকৃত পরিকল্পনা প্রদান করুন।
4. **প্রতিক্রিয়ার ভিত্তিতে সামঞ্জস্য করুন**: সুপারিশগুলোর উপর ব্যবহারকারীর প্রতিক্রিয়া জিজ্ঞাসা করুন এবং প্রয়োজনীয় পরিবর্তন করুন।

#### প্রয়োজনীয় সম্পদ

- ফ্লাইট এবং হোটেল বুকিং ডাটাবেসে অ্যাক্সেস।
- প্যারিসের আকর্ষণ এবং রেস্তোরাঁর তথ্য।
- পূর্ববর্তী ইন্টারঅ্যাকশন থেকে ব্যবহারকারীর প্রতিক্রিয়া ডেটা।

#### অভিজ্ঞতা এবং আত্ম-প্রতিফলন

ট্রাভেল এজেন্ট তার কর্মক্ষমতা মূল্যায়ন এবং পূর্ববর্তী অভিজ্ঞতা থেকে শেখার জন্য মেটাকগনিশন ব্যবহার করে। উদাহরণস্বরূপ:

1. **ব্যবহারকারীর প্রতিক্রিয়া বিশ্লেষণ**: ট্রাভেল এজেন্ট ব্যবহারকারীর প্রতিক্রিয়া পর্যালোচনা করে নির্ধারণ করে কোন সুপারিশগুলো ভালোভাবে গ্রহণ করা হয়েছে এবং কোনগুলো হয়নি। এটি তার ভবিষ্যৎ সুপারিশগুলো সংশোধন করে।
2. **অভিযোজনযোগ্যতা**: যদি কোনো ব্যবহারকারী পূর্বে ভিড়পূর্ণ জায়গা অপছন্দ করার কথা উল্লেখ করে, ট্রাভেল এজেন্ট ভবিষ্যতে জনপ্রিয় পর্যটন স্থানের সুপারিশ এড়িয়ে চলবে।
3. **ভুল সংশোধন**: যদি ট্রাভেল এজেন্ট পূর্বে কোনো বুকিংয়ে ভুল করে, যেমন সম্পূর্ণ বুক করা হোটেল সুপারিশ করা, এটি ভবিষ্যতে সুপারিশ করার আগে আরও কঠোরভাবে প্রাপ্যতা পরীক্ষা করতে শেখে।

#### ব্যবহারিক ডেভেলপার উদাহরণ

এখানে ট্রাভেল এজেন্টের কোডের একটি সরলীকৃত উদাহরণ দেওয়া হলো যেখানে মেটাকগনিশন অন্তর্ভুক্ত করা হয়েছে:

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

#### কেন মেটাকগনিশন গুরুত্বপূর্ণ

- **আত্ম-প্রতিফলন**: এজেন্ট তাদের কর্ম বিশ্লেষণ করে এবং উন্নতির ক্ষেত্র চিহ্নিত করে।
- **অভিযোজনযোগ্যতা**: এজেন্ট প্রতিক্রিয়া এবং পরিবর্তিত পরিস্থিতির ভিত্তিতে কৌশল পরিবর্তন করতে পারে।
- **ভুল সংশোধন**: এজেন্ট স্বয়ংক্রিয়ভাবে ভুল সনাক্ত এবং সংশোধন করতে পারে।
- **সম্পদ ব্যবস্থাপনা**: এজেন্ট সম্পদ ব্যবহারের অপ্টিমাইজ করতে পারে, যেমন সময় এবং গণনাশক্তি।

মেটাকগনিশন অন্তর্ভুক্ত করে, ট্রাভেল এজেন্ট আরও ব্যক্তিগতকৃত এবং সঠিক ভ্রমণ সুপারিশ প্রদান করতে পারে, যা সামগ্রিক ব্যবহারকারীর অভিজ্ঞতা উন্নত করে।

---

## ২. এজেন্টে পরিকল্পনা

পরিকল্পনা এআই এজেন্টের আচরণের একটি গুরুত্বপূর্ণ উপাদান। এটি একটি লক্ষ্য অর্জনের জন্য প্রয়োজনীয় ধাপগুলো নির্ধারণ, বর্তমান অবস্থা, সম্পদ এবং সম্ভাব্য বাধাগুলো বিবেচনা করে।

### পরিকল্পনার উপাদান

- **বর্তমান কাজ**: কাজটি স্পষ্টভাবে সংজ্ঞায়িত করুন।
- **কাজ সম্পন্ন করার ধাপ**: কাজটিকে পরিচালনাযোগ্য ধাপে বিভক্ত করুন।
- **প্রয়োজনীয় সম্পদ**: প্রয়োজনীয় সম্পদ চিহ্নিত করুন।
- **অভিজ্ঞতা**: পরিকল্পনায় পূর্ববর্তী অভিজ্ঞতা ব্যবহার করুন।

**উদাহরণ**:
এখানে ট্রাভেল এজেন্ট ব্যবহারকারীর ট্রিপ পরিকল্পনায় কার্যকরভাবে সাহায্য করার জন্য প্রয়োজনীয় ধাপগুলো দেওয়া হলো:

### ট্রাভেল এজেন্টের ধাপ

1. **ব্যবহারকারীর পছন্দ সংগ্রহ**
   - ব্যবহারকারীর ভ্রমণের তারিখ, বাজেট, আগ্রহ এবং কোনো নির্দিষ্ট প্রয়োজন সম্পর্কে জিজ্ঞাসা করুন।
   - উদাহরণ: "আপনি কখন ভ্রমণ করতে চান?" "আপনার বাজেট কত?" "আপনি ছুটিতে কী ধরনের কার্যক্রম উপভোগ করেন?"

2. **তথ্য সংগ্রহ**
   - ব্যবহারকারীর পছন্দের ভিত্তিতে প্রাসঙ্গিক ভ্রমণ অপশন অনুসন্ধান করুন।
   - **ফ্লাইট**: ব্যবহারকারীর বাজেট এবং পছন্দের ভ্রমণের তারিখের মধ্যে উপলব্ধ ফ্লাইট খুঁজুন।
   - **থাকার জায়গা**: ব্যবহারকারীর অবস্থান, মূল্য এবং সুবিধার পছন্দের সাথে মিলে এমন হোটেল বা ভাড়া সম্পত্তি খুঁজুন।
   - **আকর্ষণ এবং রেস্তোরাঁ**: ব্যবহারকারীর আগ্রহের সাথে মিলে জনপ্রিয় আকর্ষণ, কার্যক্রম এবং খাবারের অপশন চিহ্নিত করুন।

3. **সুপারিশ তৈরি**
   - সংগৃহীত তথ্যগুলোকে একটি ব্যক্তিগতকৃত পরিকল্পনায় সংকলন করুন।
   - ব্যবহারকারীর পছন্দের সাথে সুপারিশগুলোকে মানিয়ে নিয়ে ফ্লাইট অপশন, হোটেল বুকিং এবং প্রস্তাবিত কার্যক্রমের বিবরণ প্রদান করুন।

4. **ব্যবহারকারীর কাছে পরিকল্পনা উপস্থাপন**
   - প্রস্তাবিত পরিকল্পনাটি ব্যবহারকারীর পর্যালোচনার জন্য শেয়ার করুন।
   - উদাহরণ: "প্যারিসে আপনার ট্রিপের জন্য একটি প্রস্তাবিত পরিকল্পনা এখানে দেওয়া হলো। এতে ফ্লাইটের বিবরণ, হোটেল বুকিং এবং প্রস্তাবিত কার্যক্রম ও রেস্তোরাঁর তালিকা অন্তর্ভুক্ত রয়েছে। আপনার মতামত জানান!"

5. **প্রতিক্রিয়া সংগ্রহ**
   - প্রস্তাবিত পরিকল্পনার উপর ব্যবহারকারীর প্রতিক্রিয়া জিজ্ঞাসা করুন।
   - উদাহরণ: "আপনার ফ্লাইট অপশনগুলো পছন্দ হয়েছে?" "হোটেলটি আপনার প্রয়োজনের জন্য উপযুক্ত?" "আপনি কোনো কার্যক্রম যোগ বা সরাতে চান?"

6. **প্রতিক্রিয়ার ভিত্তিতে সামঞ্জস্য করুন**
   - ব্যবহারকারীর প্রতিক্রিয়ার ভিত্তিতে পরিকল্পনাটি সংশোধন করুন।
   - ফ্লাইট, থাকার জায়গা এবং কার্যক্রমের সুপারিশগুলো ব্যবহারকারীর পছন্দের সাথে আরও ভালোভাবে মানিয়ে নিতে প্রয়োজনীয় পরিবর্তন করুন।

7. **চূড়ান্ত নিশ্চিতকরণ**
   - ব্যবহারকারীর চূড়ান্ত নিশ্চিতকরণের জন্য আপডেট করা পরিকল্পনাটি উপস্থাপন করুন।
   - উদাহরণ: "আপনার প্রতিক্রিয়ার ভিত্তিতে আমি পরিবর্তনগুলো করেছি। আপডেট করা পরিকল্পনাটি এখানে দেওয়া হলো। সবকিছু ঠিক আছে কি?"

8. **বুকিং এবং নিশ্চিতকরণ**
   - ব্যবহারকারী পরিকল্পনাটি অনুমোদন করার পর, ফ্লাইট, থাকার জায়গা এবং কোনো পূর্ব-পরিকল্পিত কার্যক্রম বুকিং করুন।
   - ব্যবহারকারীর কাছে নিশ্চিতকরণের বিবরণ পাঠান।

9. **অবিরত সহায়তা প্রদান**
   - ব্যবহারকারীর ট্রিপের আগে এবং চলাকালীন কোনো পরিবর্তন বা অতিরিক্ত অনুরোধে সাহায্য করতে উপলব্ধ থাকুন।
   - উদাহরণ: "আপনার ট্রিপ চলাকালীন যদি কোনো অতিরিক্ত সহায়তার প্রয়োজন হয়, আমাকে যেকোনো সময় জানান!"

### উদাহরণ ইন্টারঅ্যাকশন

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

## ৩. সংশোধনমূলক RAG সিস্টেম

প্রথমে আসুন RAG টুল এবং প্রি-এম্পটিভ কনটেক্সট লোডের পার্থক্য বুঝি।

![RAG বনাম কনটেক্সট লোডিং](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.bn.png)

### রিট্রিভাল-অগমেন্টেড জেনারেশন (RAG)

RAG একটি রিট্রিভাল সিস্টেমকে একটি জেনারেটিভ মডেলের সাথে সংযুক্ত করে। যখন একটি প্রশ্ন করা হয়, রিট্রিভাল সিস্টেম বাহ্যিক উৎস থেকে প্রাসঙ্গিক ডকুমেন্ট বা ডেটা সংগ্রহ করে, এবং এই সংগৃহীত তথ্য জেনারেটিভ মডেলের ইনপুটকে সমৃদ্ধ করতে ব্যবহৃত হয়। এটি মডেলকে আরও সঠিক এবং প্রাসঙ্গিক প্রতিক্রিয়া তৈরি করতে সাহায্য করে।

একটি RAG সিস্টেমে, এজেন্ট একটি জ্ঞানভাণ্ডার থেকে প্রাসঙ্গিক তথ্য সংগ্রহ করে এবং এটি ব্যবহার করে উপযুক্ত প্রতিক্রিয়া বা কর্ম তৈরি করে।

### সংশোধনমূলক RAG পদ্ধতি

সংশোধনমূলক RAG পদ্ধতি RAG কৌশল ব্যবহার করে ভুল সংশোধন এবং এআই এজেন্টের সঠিকতা উন্নত করার উপর জোর দেয়। এটি অন্তর্ভুক্ত করে:

1. **প্রম্পটিং কৌশল**: এজেন্টকে প্রাসঙ্গিক তথ্য সংগ্রহে গাইড করার জন্য নির্দিষ্ট প্রম্পট ব্যবহার।
2. **সরঞ্জাম**: সংগৃহীত তথ্যের প্রাসঙ্গিকতা মূল্যায়ন এবং সঠিক প্রতিক্রিয়া তৈরি করতে এজেন্টকে সক্ষম করার জন্য অ্যালগরিদম এবং প্রক্রিয়া প্রয়োগ।
3. **মূল্যায়ন**: এজেন্টের কর্মক্ষমতা ক্রমাগত মূল্যায়ন এবং তার সঠিকতা ও দক্ষতা উন্নত করতে সমন্বয়।

#### উদাহরণ: একটি সার্চ এজেন্টে সংশোধনমূলক RAG

ধরুন একটি সার্চ এজেন্ট ব্যবহারকারীর প্রশ্নের উত্তর দিতে ওয়েব থেকে তথ্য সংগ্রহ করে। সংশোধনমূলক RAG পদ্ধতি অন্তর্ভুক্ত করতে পারে:

1. **প্রম্পটিং কৌশল**: ব্যবহারকারীর ইনপুটের ভিত্তিতে সার্চ প্রশ্ন তৈরি।
2. **সরঞ্জাম**: প্রাকৃতিক ভাষা প্রক্রিয়া এবং মেশিন লার্নিং অ্যালগরিদম ব্যবহার করে সার্চ ফলাফল র‌্যাঙ্ক এবং ফিল্টার করা।
3. **মূল্যায়ন**: সংগৃহীত তথ্যের ভুল সনাক্ত এবং সংশোধন করতে ব্যবহারকারীর প্রতিক্রিয়া বিশ্লেষণ।

### ট্রাভেল এজেন্টে সংশোধনমূলক RAG

সংশোধনমূলক RAG (রিট্রিভাল-অগমেন্টেড জেনারেশন) একটি এআই-এর তথ্য সংগ্রহ এবং তৈরি করার ক্ষমতা উন্নত করে, পাশাপাশি কোনো ভুল সংশোধন করে। আসুন দেখি ট্রাভেল এজেন্ট কীভাবে সংশোধনমূলক RAG পদ্ধতি ব্যবহার করে আরও সঠিক এবং প্রাসঙ্গিক ভ্রমণ সুপারিশ প্রদান করতে পারে।

এটি অন্তর্ভুক্ত করে:

- **প্রম্পটিং কৌশল:** এজেন্টকে প্রাসঙ্গিক তথ্য সংগ্রহে গাইড করার জন্য নির্দিষ্ট প্রম্পট ব্যবহার।
- **সর
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

### প্রি-এম্পটিভ কন্টেক্সট লোড

প্রি-এম্পটিভ কন্টেক্সট লোড বলতে বোঝায় মডেলের কাছে কোনো প্রশ্ন প্রক্রিয়াকরণের আগে প্রাসঙ্গিক তথ্য বা পটভূমি লোড করা। এর মানে হলো, মডেল শুরু থেকেই এই তথ্য অ্যাক্সেস করতে পারে, যা তাকে আরও তথ্যপূর্ণ উত্তর তৈরি করতে সাহায্য করে, প্রক্রিয়ার সময় অতিরিক্ত তথ্য পুনরুদ্ধারের প্রয়োজন ছাড়াই।

এখানে একটি সরল উদাহরণ দেওয়া হলো, যেখানে একটি ট্রাভেল এজেন্ট অ্যাপ্লিকেশনের জন্য প্রি-এম্পটিভ কন্টেক্সট লোড কেমন হতে পারে তা দেখানো হয়েছে:

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

#### ব্যাখ্যা

1. **ইনিশিয়ালাইজেশন (`__init__` মেথড)**: `TravelAgent` ক্লাস একটি ডিকশনারি প্রি-লোড করে, যেখানে প্যারিস, টোকিও, নিউ ইয়র্ক এবং সিডনির মতো জনপ্রিয় গন্তব্যস্থানের তথ্য থাকে। এই ডিকশনারিতে প্রতিটি গন্তব্যের দেশ, মুদ্রা, ভাষা এবং প্রধান আকর্ষণগুলির মতো বিবরণ অন্তর্ভুক্ত থাকে।

2. **তথ্য পুনরুদ্ধার (`get_destination_info` মেথড)**: যখন কোনো ব্যবহারকারী নির্দিষ্ট গন্তব্য সম্পর্কে জানতে চান, তখন `get_destination_info` মেথড প্রি-লোড করা কন্টেক্সট ডিকশনারি থেকে প্রাসঙ্গিক তথ্য পুনরুদ্ধার করে।

কন্টেক্সট প্রি-লোড করার মাধ্যমে, ট্রাভেল এজেন্ট অ্যাপ্লিকেশনটি ব্যবহারকারীর প্রশ্নের দ্রুত উত্তর দিতে পারে, রিয়েল-টাইমে বাহ্যিক উৎস থেকে এই তথ্য পুনরুদ্ধার করার প্রয়োজন ছাড়াই। এটি অ্যাপ্লিকেশনটিকে আরও দক্ষ এবং প্রতিক্রিয়াশীল করে তোলে।

### লক্ষ্য নির্ধারণ করে পরিকল্পনা শুরু করা এবং পুনরাবৃত্তি করা

লক্ষ্য নির্ধারণ করে পরিকল্পনা শুরু করা মানে হলো একটি স্পষ্ট উদ্দেশ্য বা কাঙ্ক্ষিত ফলাফল নিয়ে কাজ শুরু করা। এই লক্ষ্যটি শুরুতেই সংজ্ঞায়িত করা হলে, মডেল এটি একটি গাইডলাইন হিসেবে ব্যবহার করতে পারে পুরো প্রক্রিয়ার সময়। এটি নিশ্চিত করে যে প্রতিটি ধাপ কাঙ্ক্ষিত ফলাফলের দিকে এগিয়ে যায়, যা প্রক্রিয়াটিকে আরও কার্যকর এবং লক্ষ্যভিত্তিক করে তোলে।

এখানে একটি উদাহরণ দেওয়া হলো, যেখানে একটি ট্রাভেল এজেন্ট ক্লায়েন্টের জন্য একটি ভ্রমণ পরিকল্পনা তৈরি করতে লক্ষ্য নির্ধারণ করে কাজ শুরু করছে:

### পরিস্থিতি

একজন ট্রাভেল এজেন্ট ক্লায়েন্টের জন্য একটি কাস্টমাইজড ভ্যাকেশন পরিকল্পনা করতে চান। লক্ষ্য হলো ক্লায়েন্টের পছন্দ এবং বাজেটের উপর ভিত্তি করে একটি ভ্রমণসূচি তৈরি করা, যা তাদের সন্তুষ্টি সর্বাধিক করবে।

### ধাপসমূহ

1. ক্লায়েন্টের পছন্দ এবং বাজেট নির্ধারণ করুন।
2. এই পছন্দগুলির উপর ভিত্তি করে প্রাথমিক পরিকল্পনা তৈরি করুন।
3. পরিকল্পনাটি পরিমার্জন করতে পুনরাবৃত্তি করুন, ক্লায়েন্টের সন্তুষ্টি সর্বাধিক করার জন্য অপ্টিমাইজ করুন।

#### পাইথন কোড

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

#### কোড ব্যাখ্যা

1. **ইনিশিয়ালাইজেশন (`__init__` মেথড)**: `TravelAgent` ক্লাসটি সম্ভাব্য গন্তব্যগুলির একটি তালিকা দিয়ে ইনিশিয়ালাইজ করা হয়, যেখানে প্রতিটি গন্তব্যের নাম, খরচ এবং কার্যকলাপের ধরন অন্তর্ভুক্ত থাকে।

2. **পরিকল্পনা শুরু করা (`bootstrap_plan` মেথড)**: এই মেথডটি ক্লায়েন্টের পছন্দ এবং বাজেটের উপর ভিত্তি করে একটি প্রাথমিক ভ্রমণ পরিকল্পনা তৈরি করে। এটি গন্তব্যগুলির তালিকা পর্যালোচনা করে এবং যদি সেগুলি ক্লায়েন্টের পছন্দের সাথে মেলে এবং বাজেটের মধ্যে থাকে, তবে সেগুলি পরিকল্পনায় যোগ করে।

3. **পছন্দ মেলানো (`match_preferences` মেথড)**: এই মেথডটি পরীক্ষা করে যে কোনো গন্তব্য ক্লায়েন্টের পছন্দের সাথে মেলে কিনা।

4. **পরিকল্পনা পুনরাবৃত্তি করা (`iterate_plan` মেথড)**: এই মেথডটি প্রাথমিক পরিকল্পনাটি পরিমার্জন করে, প্রতিটি গন্তব্যের পরিবর্তে আরও ভালো একটি গন্তব্য যোগ করার চেষ্টা করে, ক্লায়েন্টের পছন্দ এবং বাজেট বিবেচনা করে।

5. **খরচ গণনা করা (`calculate_cost` মেথড)**: এই মেথডটি বর্তমান পরিকল্পনার মোট খরচ গণনা করে, সম্ভাব্য নতুন গন্তব্য সহ।

#### উদাহরণ ব্যবহার

- **প্রাথমিক পরিকল্পনা**: ট্রাভেল এজেন্ট ক্লায়েন্টের দর্শনীয় স্থান দেখার পছন্দ এবং $2000 বাজেটের উপর ভিত্তি করে একটি প্রাথমিক পরিকল্পনা তৈরি করেন।
- **পরিমার্জিত পরিকল্পনা**: ট্রাভেল এজেন্ট পরিকল্পনাটি পুনরাবৃত্তি করে, ক্লায়েন্টের পছন্দ এবং বাজেটের জন্য অপ্টিমাইজ করেন।

পরিকল্পনাটি একটি স্পষ্ট লক্ষ্য (যেমন, ক্লায়েন্টের সন্তুষ্টি সর্বাধিক করা) দিয়ে শুরু করে এবং এটি পরিমার্জন করতে পুনরাবৃত্তি করে, ট্রাভেল এজেন্ট ক্লায়েন্টের জন্য একটি কাস্টমাইজড এবং অপ্টিমাইজড ভ্রমণসূচি তৈরি করতে পারেন। এই পদ্ধতিটি নিশ্চিত করে যে ভ্রমণ পরিকল্পনাটি শুরু থেকেই ক্লায়েন্টের পছন্দ এবং বাজেটের সাথে সামঞ্জস্যপূর্ণ এবং প্রতিটি পুনরাবৃত্তির সাথে উন্নত হয়।

### LLM ব্যবহার করে পুনরায় র‌্যাঙ্কিং এবং স্কোরিং

বড় ভাষা মডেল (LLM) পুনরায় র‌্যাঙ্কিং এবং স্কোরিংয়ের জন্য ব্যবহার করা যেতে পারে, যা পুনরুদ্ধার করা ডকুমেন্ট বা তৈরি করা উত্তরের প্রাসঙ্গিকতা এবং গুণমান মূল্যায়ন করে। এটি কীভাবে কাজ করে:

**পুনরুদ্ধার:** প্রাথমিক পুনরুদ্ধার ধাপে একটি প্রশ্নের ভিত্তিতে প্রার্থী ডকুমেন্ট বা উত্তরের একটি সেট সংগ্রহ করা হয়।

**পুনরায় র‌্যাঙ্কিং:** LLM এই প্রার্থীদের মূল্যায়ন করে এবং তাদের প্রাসঙ্গিকতা এবং গুণমানের ভিত্তিতে পুনরায় র‌্যাঙ্ক করে। এই ধাপটি নিশ্চিত করে যে সবচেয়ে প্রাসঙ্গিক এবং উচ্চ-গুণমানের তথ্য প্রথমে উপস্থাপন করা হয়।

**স্কোরিং:** LLM প্রতিটি প্রার্থীকে স্কোর প্রদান করে, যা তাদের প্রাসঙ্গিকতা এবং গুণমান প্রতিফলিত করে। এটি ব্যবহারকারীর জন্য সেরা উত্তর বা ডকুমেন্ট নির্বাচন করতে সাহায্য করে।

LLM ব্যবহার করে পুনরায় র‌্যাঙ্কিং এবং স্কোরিংয়ের মাধ্যমে, সিস্টেমটি আরও সঠিক এবং প্রাসঙ্গিক তথ্য প্রদান করতে পারে, যা সামগ্রিক ব্যবহারকারীর অভিজ্ঞতা উন্নত করে।
#### ভ্রমণ এজেন্টে উদ্দেশ্যভিত্তিক অনুসন্ধানের একটি বাস্তব উদাহরণ

চলুন ভ্রমণ এজেন্টকে একটি উদাহরণ হিসেবে নিই এবং দেখি কীভাবে উদ্দেশ্যভিত্তিক অনুসন্ধান বাস্তবায়ন করা যায়।

1. **ব্যবহারকারীর পছন্দ সংগ্রহ করা**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **ব্যবহারকারীর উদ্দেশ্য বোঝা**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **প্রসঙ্গ সচেতনতা**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **অনুসন্ধান এবং ব্যক্তিগতকৃত ফলাফল প্রদান**

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

5. **ব্যবহারের উদাহরণ**

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

## 4. একটি সরঞ্জাম হিসেবে কোড তৈরি করা

কোড তৈরি করার এজেন্টরা AI মডেল ব্যবহার করে কোড লিখে এবং কার্যকর করে, জটিল সমস্যার সমাধান করে এবং কাজগুলো স্বয়ংক্রিয় করে।

### কোড তৈরি করার এজেন্ট

কোড তৈরি করার এজেন্টরা জেনারেটিভ AI মডেল ব্যবহার করে কোড লিখে এবং কার্যকর করে। এই এজেন্টরা জটিল সমস্যার সমাধান করতে পারে, কাজগুলো স্বয়ংক্রিয় করতে পারে এবং বিভিন্ন প্রোগ্রামিং ভাষায় কোড তৈরি ও চালনার মাধ্যমে মূল্যবান অন্তর্দৃষ্টি প্রদান করতে পারে।

#### বাস্তব প্রয়োগ

1. **স্বয়ংক্রিয় কোড তৈরি**: নির্দিষ্ট কাজের জন্য কোড স্নিপেট তৈরি করা, যেমন ডেটা বিশ্লেষণ, ওয়েব স্ক্র্যাপিং, বা মেশিন লার্নিং।
2. **SQL একটি RAG হিসেবে**: ডেটাবেস থেকে ডেটা পুনরুদ্ধার এবং পরিচালনার জন্য SQL কোয়েরি ব্যবহার করা।
3. **সমস্যার সমাধান**: নির্দিষ্ট সমস্যার সমাধানের জন্য কোড তৈরি এবং কার্যকর করা, যেমন অ্যালগরিদম অপ্টিমাইজ করা বা ডেটা বিশ্লেষণ করা।

#### উদাহরণ: ডেটা বিশ্লেষণের জন্য কোড তৈরি করার এজেন্ট

ধরুন আপনি একটি কোড তৈরি করার এজেন্ট ডিজাইন করছেন। এটি কীভাবে কাজ করতে পারে:

1. **কাজ**: একটি ডেটাসেট বিশ্লেষণ করে প্রবণতা এবং প্যাটার্ন চিহ্নিত করা।
2. **ধাপসমূহ**:
   - ডেটাসেটটি একটি ডেটা বিশ্লেষণ সরঞ্জামে লোড করা।
   - ডেটা ফিল্টার এবং একত্রিত করার জন্য SQL কোয়েরি তৈরি করা।
   - কোয়েরিগুলি কার্যকর করে ফলাফল পুনরুদ্ধার করা।
   - ফলাফল ব্যবহার করে ভিজ্যুয়ালাইজেশন এবং অন্তর্দৃষ্টি তৈরি করা।
3. **প্রয়োজনীয় সম্পদ**: ডেটাসেট অ্যাক্সেস, ডেটা বিশ্লেষণ সরঞ্জাম এবং SQL ক্ষমতা।
4. **অভিজ্ঞতা**: পূর্ববর্তী বিশ্লেষণের ফলাফল ব্যবহার করে ভবিষ্যতের বিশ্লেষণগুলোর নির্ভুলতা এবং প্রাসঙ্গিকতা উন্নত করা।

### উদাহরণ: ভ্রমণ এজেন্টের জন্য কোড তৈরি করার এজেন্ট

এই উদাহরণে, আমরা একটি কোড তৈরি করার এজেন্ট ডিজাইন করব, ভ্রমণ এজেন্ট, যা ব্যবহারকারীদের ভ্রমণ পরিকল্পনা করতে সহায়তা করবে কোড তৈরি এবং কার্যকর করার মাধ্যমে। এই এজেন্ট ভ্রমণ বিকল্পগুলি সংগ্রহ, ফলাফল ফিল্টার এবং জেনারেটিভ AI ব্যবহার করে একটি ভ্রমণ পরিকল্পনা তৈরি করার মতো কাজ পরিচালনা করতে পারে।

#### কোড তৈরি করার এজেন্টের ওভারভিউ

1. **ব্যবহারকারীর পছন্দ সংগ্রহ করা**: গন্তব্য, ভ্রমণের তারিখ, বাজেট এবং আগ্রহের মতো ব্যবহারকারীর ইনপুট সংগ্রহ করা।
2. **ডেটা সংগ্রহের জন্য কোড তৈরি করা**: ফ্লাইট, হোটেল এবং আকর্ষণ সম্পর্কে ডেটা পুনরুদ্ধারের জন্য কোড স্নিপেট তৈরি করা।
3. **তৈরি করা কোড কার্যকর করা**: রিয়েল-টাইম তথ্য পুনরুদ্ধারের জন্য তৈরি করা কোড চালানো।
4. **ভ্রমণ পরিকল্পনা তৈরি করা**: সংগৃহীত ডেটা ব্যবহার করে একটি ব্যক্তিগতকৃত ভ্রমণ পরিকল্পনা তৈরি করা।
5. **প্রতিক্রিয়ার ভিত্তিতে সামঞ্জস্য করা**: ব্যবহারকারীর প্রতিক্রিয়া গ্রহণ করা এবং ফলাফল উন্নত করতে প্রয়োজনে কোড পুনরায় তৈরি করা।

#### ধাপে ধাপে বাস্তবায়ন

1. **ব্যবহারকারীর পছন্দ সংগ্রহ করা**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **ডেটা সংগ্রহের জন্য কোড তৈরি করা**

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

3. **তৈরি করা কোড কার্যকর করা**

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

4. **ভ্রমণ পরিকল্পনা তৈরি করা**

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

5. **প্রতিক্রিয়ার ভিত্তিতে সামঞ্জস্য করা**

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

### পরিবেশ সচেতনতা এবং যুক্তি ব্যবহার করা

টেবিলের স্কিমা বোঝার মাধ্যমে কোয়েরি তৈরির প্রক্রিয়াটি পরিবেশ সচেতনতা এবং যুক্তি ব্যবহার করে উন্নত করা যেতে পারে।

এটি কীভাবে করা যায় তার একটি উদাহরণ এখানে দেওয়া হলো:

1. **স্কিমা বোঝা**: সিস্টেমটি টেবিলের স্কিমা বুঝবে এবং এই তথ্য ব্যবহার করে কোয়েরি তৈরির ভিত্তি স্থাপন করবে।
2. **প্রতিক্রিয়ার ভিত্তিতে সামঞ্জস্য করা**: সিস্টেমটি প্রতিক্রিয়ার ভিত্তিতে ব্যবহারকারীর পছন্দ সামঞ্জস্য করবে এবং স্কিমার কোন ক্ষেত্রগুলো আপডেট করা প্রয়োজন তা নিয়ে যুক্তি করবে।
3. **কোয়েরি তৈরি এবং কার্যকর করা**: সিস্টেমটি নতুন পছন্দের ভিত্তিতে আপডেট করা ফ্লাইট এবং হোটেল ডেটা পুনরুদ্ধার করতে কোয়েরি তৈরি এবং কার্যকর করবে।

এখানে একটি আপডেটেড পাইথন কোড উদাহরণ রয়েছে যা এই ধারণাগুলো অন্তর্ভুক্ত করে:

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

#### ব্যাখ্যা - প্রতিক্রিয়ার ভিত্তিতে বুকিং

1. **স্কিমা সচেতনতা**: `schema` ডিকশনারি নির্ধারণ করে যে প্রতিক্রিয়ার ভিত্তিতে পছন্দগুলো কীভাবে সামঞ্জস্য করা উচিত। এটি `favorites` এবং `avoid` এর মতো ক্ষেত্র অন্তর্ভুক্ত করে, যার সাথে সংশ্লিষ্ট সামঞ্জস্য রয়েছে।
2. **পছন্দ সামঞ্জস্য করা (`adjust_based_on_feedback` পদ্ধতি)**: এই পদ্ধতি ব্যবহারকারীর প্রতিক্রিয়া এবং স্কিমার ভিত্তিতে পছন্দগুলো সামঞ্জস্য করে।
3. **পরিবেশ-ভিত্তিক সামঞ্জস্য (`adjust_based_on_environment` পদ্ধতি)**: এই পদ্ধতি স্কিমা এবং প্রতিক্রিয়ার ভিত্তিতে সামঞ্জস্যগুলো কাস্টমাইজ করে।
4. **কোয়েরি তৈরি এবং কার্যকর করা**: সিস্টেমটি সামঞ্জস্য করা পছন্দের ভিত্তিতে আপডেট করা ফ্লাইট এবং হোটেল ডেটা পুনরুদ্ধার করতে কোড তৈরি করে এবং কার্যকর করে।
5. **ভ্রমণ পরিকল্পনা তৈরি করা**: সিস্টেমটি নতুন ফ্লাইট, হোটেল এবং আকর্ষণের ডেটার ভিত্তিতে একটি আপডেটেড ভ্রমণ পরিকল্পনা তৈরি করে।

পরিবেশ সচেতন এবং স্কিমার ভিত্তিতে যুক্তি ব্যবহার করে, সিস্টেমটি আরও নির্ভুল এবং প্রাসঙ্গিক কোয়েরি তৈরি করতে পারে, যা আরও ভালো ভ্রমণ সুপারিশ এবং ব্যক্তিগতকৃত ব্যবহারকারীর অভিজ্ঞতা প্রদান করে।

### SQL একটি Retrieval-Augmented Generation (RAG) কৌশল হিসেবে ব্যবহার করা

SQL (স্ট্রাকচার্ড কোয়েরি ল্যাঙ্গুয়েজ) ডেটাবেসের সাথে ইন্টারঅ্যাক্ট করার জন্য একটি শক্তিশালী সরঞ্জাম। Retrieval-Augmented Generation (RAG) পদ্ধতির অংশ হিসেবে SQL ব্যবহার করে ডেটাবেস থেকে প্রাসঙ্গিক ডেটা পুনরুদ্ধার করা যায়, যা AI এজেন্টদের প্রতিক্রিয়া বা পদক্ষেপ তৈরি করতে সহায়তা করে। চলুন দেখি কীভাবে SQL একটি RAG কৌশল হিসেবে ভ্রমণ এজেন্টের ক্ষেত্রে ব্যবহার করা যায়।

#### মূল ধারণা

1. **ডেটাবেস ইন্টারঅ্যাকশন**:
   - SQL ব্যবহার করে ডেটাবেসে কোয়েরি চালানো, প্রাসঙ্গিক তথ্য পুনরুদ্ধার করা এবং ডেটা পরিচালনা করা।
   - উদাহরণ: ভ্রমণ ডেটাবেস থেকে ফ্লাইটের বিবরণ, হোটেলের তথ্য এবং আকর্ষণ পুনরুদ্ধার করা।

2. **RAG এর সাথে ইন্টিগ্রেশন**:
   - ব্যবহারকারীর ইনপুট এবং পছন্দের ভিত্তিতে SQL কোয়েরি তৈরি করা।
   - পুনরুদ্ধার করা ডেটা ব্যবহার করে ব্যক্তিগতকৃত সুপারিশ বা পদক্ষেপ তৈরি করা।

3. **ডাইনামিক কোয়েরি তৈরি**:
   - AI এজেন্ট প্রাসঙ্গিকতা এবং ব্যবহারকারীর প্রয়োজন অনুযায়ী ডাইনামিক SQL কোয়েরি তৈরি করে।
   - উদাহরণ: বাজেট, তারিখ এবং আগ্রহের ভিত্তিতে ফলাফল ফিল্টার করার জন্য SQL কোয়েরি কাস্টমাইজ করা।

#### প্রয়োগ

- **স্বয়ংক্রিয় কোড তৈরি**: নির্দিষ্ট কাজের জন্য কোড স্নিপেট তৈরি করা।
- **SQL একটি RAG হিসেবে**: SQL কোয়েরি ব্যবহার করে ডেটা পরিচালনা করা।
- **সমস্যার সমাধান**: সমস্যার সমাধানের জন্য কোড তৈরি এবং কার্যকর করা।

**উদাহরণ**:
একটি ডেটা বিশ্লেষণ এজেন্ট:

1. **কাজ**: একটি ডেটাসেট বিশ্লেষণ করে প্রবণতা খুঁজে বের করা।
2. **ধাপসমূহ**:
   - ডেটাসেট লোড করা।
   - ডেটা ফিল্টার করার জন্য SQL কোয়েরি তৈরি করা।
   - কোয়েরি কার্যকর করে ফলাফল পুনরুদ্ধার করা।
   - ভিজ্যুয়ালাইজেশন এবং অন্তর্দৃষ্টি তৈরি করা।
3. **সম্পদ**: ডেটাসেট অ্যাক্সেস, SQL ক্ষমতা।
4. **অভিজ্ঞতা**: পূর্ববর্তী ফলাফল ব্যবহার করে ভবিষ্যতের বিশ্লেষণ উন্নত করা।

#### ভ্রমণ এজেন্টে SQL ব্যবহার করার বাস্তব উদাহরণ

1. **ব্যবহারকারীর পছন্দ সংগ্রহ করা**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **SQL কোয়েরি তৈরি করা**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **SQL কোয়েরি কার্যকর করা**

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

4. **সুপারিশ তৈরি করা**

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

#### SQL কোয়েরির উদাহরণ

1. **ফ্লাইট কোয়েরি**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **হোটেল কোয়েরি**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **আকর্ষণ কোয়েরি**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

SQL-কে Retrieval-Augmented Generation (RAG) কৌশলের অংশ হিসেবে ব্যবহার করে, AI এজেন্ট যেমন ভ্রমণ এজেন্ট প্রাসঙ্গিক ডেটা পুনরুদ্ধার এবং ব্যবহার করতে পারে, যা সঠিক এবং ব্যক্তিগতকৃত সুপারিশ প্রদান করে।

### মেটাকগনিশনের একটি উদাহরণ

মেটাকগনিশনের বাস্তবায়ন দেখানোর জন্য, চলুন একটি সহজ এজেন্ট তৈরি করি যা *তার সিদ্ধান্ত গ্রহণ প্রক্রিয়া নিয়ে চিন্তা করে* এবং সমস্যার সমাধানের সময় তার কৌশল সামঞ্জস্য করে। উদাহরণস্বরূপ, আমরা একটি সিস্টেম তৈরি করব যেখানে একটি এজেন্ট হোটেল নির্বাচন অপ্টিমাইজ করার চেষ্টা করে, কিন্তু ভুল বা অপ্টিমাল নয় এমন পছন্দ করলে তার নিজের যুক্তি মূল্যায়ন করে এবং কৌশল পরিবর্তন করে।

আমরা এটি একটি মৌলিক উদাহরণ দিয়ে দেখাব যেখানে এজেন্ট দাম এবং গুণমানের সংমিশ্রণের ভিত্তিতে হোটেল নির্বাচন করে, কিন্তু "চিন্তা" করে এবং প্রয়োজন অনুযায়ী তার সিদ্ধান্ত পরিবর্তন করে।

#### এটি কীভাবে মেটাকগনিশনকে চিত্রিত করে:

1. **প্রাথমিক সিদ্ধান্ত**: এজেন্ট সবচেয়ে সস্তা হোটেল বেছে নেবে, গুণমানের প্রভাব না বুঝে।
2. **প্রতিফলন এবং মূল্যায়ন**: প্রাথমিক পছন্দের পরে, এজেন্ট ব্যবহারকারীর প্রতিক্রিয়া ব্যবহার করে চেক করবে হোটেলটি "খারাপ" পছন্দ কিনা। যদি এটি খুঁজে পায় যে হোটেলের গুণমান খুব কম, এটি তার যুক্তি নিয়ে চিন্তা করবে।
3. **কৌশল সামঞ্জস্য করা**: এজেন্ট তার প্রতিফলনের ভিত্তিতে কৌশল সামঞ্জস্য করবে এবং "সস্তা" থেকে "সর্বোচ্চ গুণমান" এ স্যুইচ করবে, ফলে ভবিষ্যতের পুনরাবৃত্তিতে তার সিদ্ধান্ত গ্রহণ প্রক্রিয়া উন্নত করবে।

এখানে একটি উদাহরণ:

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

#### এজেন্টের মেটাকগনিশন ক্ষমতা

এখানে মূল বিষয় হলো এজেন্টের ক্ষমতা:
- তার পূর্ববর্তী পছন্দ এবং সিদ্ধান্ত গ্রহণ প্রক্রিয়া মূল্যায়ন করা।
- সেই প্রতিফলনের ভিত্তিতে তার কৌশল সামঞ্জস্য করা, অর্থাৎ, মেটাকগনিশন প্রয়োগ করা।

এটি মেটাকগনিশনের একটি সহজ রূপ যেখানে সিস্টেম অভ্যন্তরীণ প্রতিক্রিয়ার ভিত্তিতে তার যুক্তি প্রক্রিয়া সামঞ্জস্য করতে সক্ষম।

### উপসংহার

মেটাকগনিশন একটি শক্তিশালী সরঞ্জাম যা AI এজেন্টদের ক্ষমতা উল্লেখযোগ্যভাবে বাড়িয়ে তুলতে পারে। মেটাকগনিটিভ প্রক্রিয়া অন্তর্ভুক্ত করে, আপনি এমন এজেন্ট ডিজাইন করতে পারেন যা আরও বুদ্ধিমান, অভিযোজনযোগ্য এবং দক্ষ। অতিরিক্ত সম্পদ ব্যবহার করে AI এজেন্টে মেটাকগনিশনের চমকপ্রদ জগৎ আরও অন্বেষণ করুন।

### মেটাকগনিশন ডিজাইন প্যাটার্ন সম্পর্কে আরও প্রশ্ন আছে?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)-এ যোগ দিন, অন্যান্য শিক্ষার্থীদের সাথে দেখা করুন, অফিস আওয়ার্সে অংশ নিন এবং আপনার AI এজেন্ট সম্পর্কিত প্রশ্নের উত্তর পান।

## পূর্ববর্তী পাঠ

[মাল্টি-এজেন্ট ডিজাইন প্যাটার্ন](../08-multi-agent/README.md)

## পরবর্তী পাঠ

[উৎপাদনে AI এজেন্ট](../10-ai-agents-production/README.md)

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিক অনুবাদের চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। নথিটির মূল ভাষায় লেখা সংস্করণটিকেই প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ ব্যবহার করার পরামর্শ দেওয়া হচ্ছে। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।