<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-29T17:59:35+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "id"
}
-->
[![Desain Multi-Agen](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.id.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_
# Metakognisi pada Agen AI

## Pendahuluan

Selamat datang di pelajaran tentang metakognisi pada agen AI! Bab ini dirancang untuk pemula yang penasaran tentang bagaimana agen AI dapat berpikir tentang proses berpikir mereka sendiri. Pada akhir pelajaran ini, Anda akan memahami konsep-konsep utama dan dilengkapi dengan contoh praktis untuk menerapkan metakognisi dalam desain agen AI.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan dapat:

1. Memahami implikasi dari loop penalaran dalam definisi agen.
2. Menggunakan teknik perencanaan dan evaluasi untuk membantu agen yang dapat memperbaiki diri sendiri.
3. Membuat agen Anda sendiri yang mampu memanipulasi kode untuk menyelesaikan tugas.

## Pengantar Metakognisi

Metakognisi mengacu pada proses kognitif tingkat tinggi yang melibatkan pemikiran tentang pemikiran seseorang sendiri. Untuk agen AI, ini berarti mampu mengevaluasi dan menyesuaikan tindakan mereka berdasarkan kesadaran diri dan pengalaman masa lalu. Metakognisi, atau "berpikir tentang berpikir," adalah konsep penting dalam pengembangan sistem AI yang bersifat agen. Ini melibatkan sistem AI yang sadar akan proses internal mereka sendiri dan mampu memantau, mengatur, dan menyesuaikan perilaku mereka sesuai kebutuhan. Sama seperti yang kita lakukan saat membaca situasi atau menghadapi masalah. Kesadaran diri ini dapat membantu sistem AI membuat keputusan yang lebih baik, mengidentifikasi kesalahan, dan meningkatkan kinerja mereka dari waktu ke waktu—kembali lagi ke tes Turing dan perdebatan tentang apakah AI akan mengambil alih.

Dalam konteks sistem AI yang bersifat agen, metakognisi dapat membantu mengatasi beberapa tantangan, seperti:
- Transparansi: Memastikan bahwa sistem AI dapat menjelaskan penalaran dan keputusan mereka.
- Penalaran: Meningkatkan kemampuan sistem AI untuk mensintesis informasi dan membuat keputusan yang tepat.
- Adaptasi: Memungkinkan sistem AI untuk menyesuaikan diri dengan lingkungan baru dan kondisi yang berubah.
- Persepsi: Meningkatkan akurasi sistem AI dalam mengenali dan menafsirkan data dari lingkungan mereka.

### Apa itu Metakognisi?

Metakognisi, atau "berpikir tentang berpikir," adalah proses kognitif tingkat tinggi yang melibatkan kesadaran diri dan pengaturan diri terhadap proses kognitif seseorang. Dalam dunia AI, metakognisi memberdayakan agen untuk mengevaluasi dan menyesuaikan strategi serta tindakan mereka, yang mengarah pada kemampuan pemecahan masalah dan pengambilan keputusan yang lebih baik. Dengan memahami metakognisi, Anda dapat merancang agen AI yang tidak hanya lebih cerdas tetapi juga lebih adaptif dan efisien. Dalam metakognisi sejati, Anda akan melihat AI secara eksplisit bernalar tentang penalarannya sendiri.

Contoh: “Saya memprioritaskan penerbangan yang lebih murah karena... Saya mungkin melewatkan penerbangan langsung, jadi biarkan saya memeriksa ulang.”
Melacak bagaimana atau mengapa ia memilih rute tertentu.
- Menyadari bahwa ia membuat kesalahan karena terlalu mengandalkan preferensi pengguna dari sebelumnya, sehingga ia memodifikasi strategi pengambilan keputusannya, bukan hanya rekomendasi akhirnya.
- Mendiagnosis pola seperti, “Setiap kali saya melihat pengguna menyebutkan ‘terlalu ramai,’ saya tidak hanya harus menghapus atraksi tertentu tetapi juga mencerminkan bahwa metode saya memilih ‘atraksi utama’ cacat jika saya selalu memberi peringkat berdasarkan popularitas.”

### Pentingnya Metakognisi pada Agen AI

Metakognisi memainkan peran penting dalam desain agen AI karena beberapa alasan:

![Pentingnya Metakognisi](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.id.png)

- Refleksi Diri: Agen dapat menilai kinerja mereka sendiri dan mengidentifikasi area yang perlu diperbaiki.
- Adaptabilitas: Agen dapat memodifikasi strategi mereka berdasarkan pengalaman masa lalu dan lingkungan yang berubah.
- Koreksi Kesalahan: Agen dapat mendeteksi dan memperbaiki kesalahan secara mandiri, yang mengarah pada hasil yang lebih akurat.
- Pengelolaan Sumber Daya: Agen dapat mengoptimalkan penggunaan sumber daya, seperti waktu dan daya komputasi, dengan merencanakan dan mengevaluasi tindakan mereka.

## Komponen Agen AI

Sebelum mendalami proses metakognitif, penting untuk memahami komponen dasar dari agen AI. Agen AI biasanya terdiri dari:

- Persona: Kepribadian dan karakteristik agen, yang menentukan bagaimana ia berinteraksi dengan pengguna.
- Alat: Kemampuan dan fungsi yang dapat dilakukan oleh agen.
- Keterampilan: Pengetahuan dan keahlian yang dimiliki oleh agen.

Komponen-komponen ini bekerja sama untuk menciptakan "unit keahlian" yang dapat melakukan tugas tertentu.

**Contoh**:
Pertimbangkan agen perjalanan, layanan agen yang tidak hanya merencanakan liburan Anda tetapi juga menyesuaikan jalurnya berdasarkan data waktu nyata dan pengalaman perjalanan pelanggan sebelumnya.

### Contoh: Metakognisi dalam Layanan Agen Perjalanan

Bayangkan Anda merancang layanan agen perjalanan yang didukung oleh AI. Agen ini, "Agen Perjalanan," membantu pengguna merencanakan liburan mereka. Untuk memasukkan metakognisi, Agen Perjalanan perlu mengevaluasi dan menyesuaikan tindakannya berdasarkan kesadaran diri dan pengalaman masa lalu. Berikut adalah bagaimana metakognisi dapat berperan:

#### Tugas Saat Ini

Tugas saat ini adalah membantu pengguna merencanakan perjalanan ke Paris.

#### Langkah-langkah untuk Menyelesaikan Tugas

1. **Mengumpulkan Preferensi Pengguna**: Tanyakan kepada pengguna tentang tanggal perjalanan, anggaran, minat (misalnya, museum, kuliner, belanja), dan persyaratan khusus.
2. **Mengambil Informasi**: Cari opsi penerbangan, akomodasi, atraksi, dan restoran yang sesuai dengan preferensi pengguna.
3. **Menghasilkan Rekomendasi**: Berikan itinerary yang dipersonalisasi dengan detail penerbangan, reservasi hotel, dan aktivitas yang disarankan.
4. **Menyesuaikan Berdasarkan Umpan Balik**: Tanyakan kepada pengguna tentang umpan balik terhadap rekomendasi dan lakukan penyesuaian yang diperlukan.

#### Sumber Daya yang Dibutuhkan

- Akses ke database pemesanan penerbangan dan hotel.
- Informasi tentang atraksi dan restoran di Paris.
- Data umpan balik pengguna dari interaksi sebelumnya.

#### Pengalaman dan Refleksi Diri

Agen Perjalanan menggunakan metakognisi untuk mengevaluasi kinerjanya dan belajar dari pengalaman masa lalu. Misalnya:

1. **Menganalisis Umpan Balik Pengguna**: Agen Perjalanan meninjau umpan balik pengguna untuk menentukan rekomendasi mana yang diterima dengan baik dan mana yang tidak. Ia menyesuaikan saran masa depannya sesuai kebutuhan.
2. **Adaptabilitas**: Jika pengguna sebelumnya menyebutkan ketidaksukaan terhadap tempat yang ramai, Agen Perjalanan akan menghindari merekomendasikan tempat wisata populer selama jam sibuk di masa depan.
3. **Koreksi Kesalahan**: Jika Agen Perjalanan membuat kesalahan dalam pemesanan sebelumnya, seperti menyarankan hotel yang sudah penuh, ia belajar untuk memeriksa ketersediaan dengan lebih teliti sebelum memberikan rekomendasi.

#### Contoh Pengembang Praktis

Berikut adalah contoh sederhana bagaimana kode Agen Perjalanan mungkin terlihat saat memasukkan metakognisi:

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

#### Mengapa Metakognisi Penting

- **Refleksi Diri**: Agen dapat menganalisis kinerja mereka dan mengidentifikasi area yang perlu diperbaiki.
- **Adaptabilitas**: Agen dapat memodifikasi strategi berdasarkan umpan balik dan kondisi yang berubah.
- **Koreksi Kesalahan**: Agen dapat mendeteksi dan memperbaiki kesalahan secara mandiri.
- **Pengelolaan Sumber Daya**: Agen dapat mengoptimalkan penggunaan sumber daya, seperti waktu dan daya komputasi.

Dengan memasukkan metakognisi, Agen Perjalanan dapat memberikan rekomendasi perjalanan yang lebih personal dan akurat, meningkatkan pengalaman pengguna secara keseluruhan.

---

## 2. Perencanaan pada Agen

Perencanaan adalah komponen penting dari perilaku agen AI. Ini melibatkan penguraian langkah-langkah yang diperlukan untuk mencapai tujuan, dengan mempertimbangkan keadaan saat ini, sumber daya, dan kemungkinan hambatan.

### Elemen Perencanaan

- **Tugas Saat Ini**: Definisikan tugas dengan jelas.
- **Langkah-langkah untuk Menyelesaikan Tugas**: Pecah tugas menjadi langkah-langkah yang dapat dikelola.
- **Sumber Daya yang Dibutuhkan**: Identifikasi sumber daya yang diperlukan.
- **Pengalaman**: Gunakan pengalaman masa lalu untuk menginformasikan perencanaan.

**Contoh**:
Berikut adalah langkah-langkah yang perlu diambil Agen Perjalanan untuk membantu pengguna merencanakan perjalanan mereka secara efektif:

### Langkah-langkah untuk Agen Perjalanan

1. **Mengumpulkan Preferensi Pengguna**
   - Tanyakan kepada pengguna detail tentang tanggal perjalanan, anggaran, minat, dan persyaratan khusus.
   - Contoh: "Kapan Anda berencana untuk bepergian?" "Berapa kisaran anggaran Anda?" "Aktivitas apa yang Anda nikmati saat liburan?"

2. **Mengambil Informasi**
   - Cari opsi perjalanan yang relevan berdasarkan preferensi pengguna.
   - **Penerbangan**: Cari penerbangan yang tersedia dalam anggaran dan tanggal perjalanan yang diinginkan pengguna.
   - **Akomodasi**: Temukan hotel atau properti sewa yang sesuai dengan preferensi pengguna untuk lokasi, harga, dan fasilitas.
   - **Atraksi dan Restoran**: Identifikasi atraksi populer, aktivitas, dan pilihan makan yang sesuai dengan minat pengguna.

3. **Menghasilkan Rekomendasi**
   - Kompilasi informasi yang diambil ke dalam itinerary yang dipersonalisasi.
   - Berikan detail seperti opsi penerbangan, reservasi hotel, dan aktivitas yang disarankan, dengan memastikan rekomendasi disesuaikan dengan preferensi pengguna.

4. **Menyajikan Itinerary kepada Pengguna**
   - Bagikan itinerary yang diusulkan kepada pengguna untuk ditinjau.
   - Contoh: "Berikut adalah itinerary yang disarankan untuk perjalanan Anda ke Paris. Ini mencakup detail penerbangan, pemesanan hotel, dan daftar aktivitas serta restoran yang direkomendasikan. Beri tahu saya pendapat Anda!"

5. **Mengumpulkan Umpan Balik**
   - Tanyakan kepada pengguna tentang umpan balik terhadap itinerary yang diusulkan.
   - Contoh: "Apakah Anda menyukai opsi penerbangan?" "Apakah hotel sesuai dengan kebutuhan Anda?" "Apakah ada aktivitas yang ingin Anda tambahkan atau hapus?"

6. **Menyesuaikan Berdasarkan Umpan Balik**
   - Modifikasi itinerary berdasarkan umpan balik pengguna.
   - Lakukan perubahan yang diperlukan pada rekomendasi penerbangan, akomodasi, dan aktivitas untuk lebih sesuai dengan preferensi pengguna.

7. **Konfirmasi Akhir**
   - Sajikan itinerary yang diperbarui kepada pengguna untuk konfirmasi akhir.
   - Contoh: "Saya telah melakukan penyesuaian berdasarkan umpan balik Anda. Berikut adalah itinerary yang diperbarui. Apakah semuanya terlihat baik bagi Anda?"

8. **Memesan dan Mengonfirmasi Reservasi**
   - Setelah pengguna menyetujui itinerary, lanjutkan dengan pemesanan penerbangan, akomodasi, dan aktivitas yang telah direncanakan.
   - Kirim detail konfirmasi kepada pengguna.

9. **Memberikan Dukungan Berkelanjutan**
   - Tetap tersedia untuk membantu pengguna dengan perubahan atau permintaan tambahan sebelum dan selama perjalanan mereka.
   - Contoh: "Jika Anda membutuhkan bantuan lebih lanjut selama perjalanan Anda, jangan ragu untuk menghubungi saya kapan saja!"

### Contoh Interaksi

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

## 3. Sistem RAG Korektif

Pertama-tama mari kita mulai dengan memahami perbedaan antara Alat RAG dan Pemuatan Konteks Pre-emptive

![RAG vs Pemuatan Konteks](../../../translated_images/rag-vs-context.9eae588520c00921f531e4dc788992e8a7b69b6ff7c9eaa69fb9bc83ad243504.id.png)

### Retrieval-Augmented Generation (RAG)

RAG menggabungkan sistem pengambilan dengan model generatif. Ketika sebuah kueri dibuat, sistem pengambilan mengambil dokumen atau data yang relevan dari sumber eksternal, dan informasi yang diambil ini digunakan untuk meningkatkan input ke model generatif. Ini membantu model menghasilkan respons yang lebih akurat dan relevan secara kontekstual.

Dalam sistem RAG, agen mengambil informasi yang relevan dari basis pengetahuan dan menggunakannya untuk menghasilkan respons atau tindakan yang sesuai.

### Pendekatan RAG Korektif

Pendekatan RAG Korektif berfokus pada penggunaan teknik RAG untuk memperbaiki kesalahan dan meningkatkan akurasi agen AI. Ini melibatkan:

1. **Teknik Prompting**: Menggunakan prompt spesifik untuk memandu agen dalam mengambil informasi yang relevan.
2. **Alat**: Menerapkan algoritma dan mekanisme yang memungkinkan agen mengevaluasi relevansi informasi yang diambil dan menghasilkan respons yang akurat.
3. **Evaluasi**: Secara terus-menerus menilai kinerja agen dan melakukan penyesuaian untuk meningkatkan akurasi dan efisiensi.

#### Contoh: RAG Korektif dalam Agen Pencarian

Pertimbangkan agen pencarian yang mengambil informasi dari web untuk menjawab kueri pengguna. Pendekatan RAG Korektif mungkin melibatkan:

1. **Teknik Prompting**: Merumuskan kueri pencarian berdasarkan input pengguna.
2. **Alat**: Menggunakan pemrosesan bahasa alami dan algoritma pembelajaran mesin untuk memberi peringkat dan menyaring hasil pencarian.
3. **Evaluasi**: Menganalisis umpan balik pengguna untuk mengidentifikasi dan memperbaiki ketidakakuratan dalam informasi yang diambil.

### RAG Korektif dalam Agen Perjalanan

RAG Korektif (Retrieval-Augmented Generation) meningkatkan kemampuan AI untuk mengambil dan menghasilkan informasi sambil memperbaiki ketidakakuratan. Mari kita lihat bagaimana Agen Perjalanan dapat menggunakan pendekatan RAG Korektif untuk memberikan rekomendasi perjalanan yang lebih akurat dan relevan.

Ini melibatkan:

- **Teknik Prompting:** Menggunakan prompt spesifik untuk memandu agen dalam mengambil informasi yang relevan.
- **Alat:** Menerapkan algoritma dan mekanisme yang memungkinkan agen mengevaluasi relevansi informasi yang diambil dan menghasilkan respons yang akurat.
- **Evaluasi:** Secara terus-menerus menilai kinerja agen dan melakukan penyesuaian untuk meningkatkan akurasi dan efisiensi.

#### Langkah-langkah untuk Menerapkan RAG Korektif dalam Agen Perjalanan

1. **Interaksi Awal dengan Pengguna**
   - Agen Perjalanan mengumpulkan preferensi awal dari pengguna, seperti tujuan, tanggal perjalanan, anggaran, dan minat.
   - Contoh:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Pengambilan Informasi**
   - Agen Perjalanan mengambil informasi tentang penerbangan, akomodasi, atraksi, dan restoran berdasarkan preferensi pengguna.
   - Contoh:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Menghasilkan Rekomendasi Awal**
   - Agen Perjalanan menggunakan informasi yang diambil untuk menghasilkan itinerary yang dipersonalisasi.
   - Contoh:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Mengumpulkan Umpan Balik Pengguna**
   - Agen Perjalanan meminta umpan balik dari pengguna tentang rekomendasi awal.
   - Contoh:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Proses RAG Korektif**
   - **Teknik Prompting**: Agen Perjalanan merumuskan kueri pencarian baru berdasarkan umpan balik pengguna.
     - Contoh:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Alat**: Agen Perjalanan menggunakan algoritma untuk memberi peringkat dan menyaring hasil pencarian baru, menekankan relevansi berdasarkan umpan balik pengguna.
     - Contoh:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Evaluasi**: Agen Perjalanan secara terus-menerus menilai relevansi dan akurasi rekomendasinya dengan menganalisis umpan balik pengguna dan melakukan penyesuaian yang diperlukan.
     - Contoh:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Contoh Praktis

Berikut adalah contoh kode Python sederhana yang memasukkan pendekatan RAG Korektif dalam Agen Perjalanan:
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

### Memuat Konteks Secara Pre-emptive

Memuat konteks secara pre-emptive melibatkan pengisian informasi latar belakang atau konteks yang relevan ke dalam model sebelum memproses permintaan. Dengan cara ini, model memiliki akses ke informasi tersebut sejak awal, sehingga dapat memberikan respons yang lebih terinformasi tanpa perlu mengambil data tambahan selama proses berlangsung.

Berikut adalah contoh sederhana bagaimana memuat konteks secara pre-emptive untuk aplikasi agen perjalanan dalam Python:

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

#### Penjelasan

1. **Inisialisasi (metode `__init__`)**: Kelas `TravelAgent` memuat terlebih dahulu sebuah kamus yang berisi informasi tentang destinasi populer seperti Paris, Tokyo, New York, dan Sydney. Kamus ini mencakup detail seperti negara, mata uang, bahasa, dan atraksi utama untuk setiap destinasi.

2. **Mengambil Informasi (metode `get_destination_info`)**: Ketika pengguna bertanya tentang destinasi tertentu, metode `get_destination_info` mengambil informasi yang relevan dari kamus konteks yang telah dimuat sebelumnya.

Dengan memuat konteks terlebih dahulu, aplikasi agen perjalanan dapat merespons pertanyaan pengguna dengan cepat tanpa harus mengambil informasi ini dari sumber eksternal secara real-time. Hal ini membuat aplikasi lebih efisien dan responsif.

### Memulai Rencana dengan Tujuan Sebelum Iterasi

Memulai rencana dengan tujuan berarti memulai dengan menetapkan sasaran atau hasil yang jelas. Dengan mendefinisikan tujuan ini sejak awal, model dapat menggunakannya sebagai prinsip panduan selama proses iterasi. Hal ini membantu memastikan bahwa setiap iterasi bergerak lebih dekat ke pencapaian hasil yang diinginkan, sehingga proses menjadi lebih efisien dan terfokus.

Berikut adalah contoh bagaimana memulai rencana perjalanan dengan tujuan sebelum iterasi untuk agen perjalanan dalam Python:

### Skenario

Seorang agen perjalanan ingin merancang liburan yang disesuaikan untuk klien. Tujuannya adalah membuat rencana perjalanan yang memaksimalkan kepuasan klien berdasarkan preferensi dan anggaran mereka.

### Langkah-langkah

1. Tentukan preferensi dan anggaran klien.
2. Mulai rencana awal berdasarkan preferensi tersebut.
3. Iterasi untuk menyempurnakan rencana, mengoptimalkan kepuasan klien.

#### Kode Python

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

#### Penjelasan Kode

1. **Inisialisasi (metode `__init__`)**: Kelas `TravelAgent` diinisialisasi dengan daftar destinasi potensial, masing-masing memiliki atribut seperti nama, biaya, dan jenis aktivitas.

2. **Memulai Rencana (metode `bootstrap_plan`)**: Metode ini membuat rencana perjalanan awal berdasarkan preferensi dan anggaran klien. Metode ini memeriksa daftar destinasi dan menambahkannya ke rencana jika sesuai dengan preferensi klien dan sesuai dengan anggaran.

3. **Mencocokkan Preferensi (metode `match_preferences`)**: Metode ini memeriksa apakah destinasi sesuai dengan preferensi klien.

4. **Iterasi Rencana (metode `iterate_plan`)**: Metode ini menyempurnakan rencana awal dengan mencoba mengganti setiap destinasi dalam rencana dengan pilihan yang lebih baik, mempertimbangkan preferensi dan batasan anggaran klien.

5. **Menghitung Biaya (metode `calculate_cost`)**: Metode ini menghitung total biaya dari rencana saat ini, termasuk destinasi baru yang potensial.

#### Contoh Penggunaan

- **Rencana Awal**: Agen perjalanan membuat rencana awal berdasarkan preferensi klien untuk wisata dan anggaran sebesar $2000.
- **Rencana yang Disempurnakan**: Agen perjalanan mengiterasi rencana, mengoptimalkan preferensi dan anggaran klien.

Dengan memulai rencana dengan tujuan yang jelas (misalnya, memaksimalkan kepuasan klien) dan mengiterasi untuk menyempurnakan rencana, agen perjalanan dapat menciptakan rencana perjalanan yang disesuaikan dan dioptimalkan untuk klien. Pendekatan ini memastikan bahwa rencana perjalanan sesuai dengan preferensi dan anggaran klien sejak awal dan terus membaik dengan setiap iterasi.

### Memanfaatkan LLM untuk Re-ranking dan Scoring

Model Bahasa Besar (LLM) dapat digunakan untuk re-ranking dan scoring dengan mengevaluasi relevansi dan kualitas dokumen yang diambil atau respons yang dihasilkan. Berikut cara kerjanya:

**Pengambilan**: Langkah pengambilan awal mengambil serangkaian dokumen atau respons kandidat berdasarkan permintaan.

**Re-ranking**: LLM mengevaluasi kandidat ini dan menyusun ulang peringkatnya berdasarkan relevansi dan kualitas. Langkah ini memastikan bahwa informasi yang paling relevan dan berkualitas tinggi disajikan terlebih dahulu.

**Scoring**: LLM memberikan skor pada setiap kandidat, mencerminkan relevansi dan kualitasnya. Hal ini membantu dalam memilih respons atau dokumen terbaik untuk pengguna.

Dengan memanfaatkan LLM untuk re-ranking dan scoring, sistem dapat memberikan informasi yang lebih akurat dan relevan secara kontekstual, meningkatkan pengalaman pengguna secara keseluruhan.

Berikut adalah contoh bagaimana agen perjalanan dapat menggunakan Model Bahasa Besar (LLM) untuk re-ranking dan scoring destinasi perjalanan berdasarkan preferensi pengguna dalam Python:

#### Skenario - Perjalanan Berdasarkan Preferensi

Seorang agen perjalanan ingin merekomendasikan destinasi perjalanan terbaik kepada klien berdasarkan preferensi mereka. LLM akan membantu menyusun ulang peringkat dan memberikan skor pada destinasi untuk memastikan opsi yang paling relevan disajikan.

#### Langkah-langkah:

1. Kumpulkan preferensi pengguna.
2. Ambil daftar destinasi perjalanan potensial.
3. Gunakan LLM untuk menyusun ulang peringkat dan memberikan skor pada destinasi berdasarkan preferensi pengguna.

Berikut cara memperbarui contoh sebelumnya untuk menggunakan Azure OpenAI Services:

#### Persyaratan

1. Anda perlu memiliki langganan Azure.
2. Buat sumber daya Azure OpenAI dan dapatkan kunci API Anda.

#### Contoh Kode Python

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

#### Penjelasan Kode - Preference Booker

1. **Inisialisasi**: Kelas `TravelAgent` diinisialisasi dengan daftar destinasi perjalanan potensial, masing-masing memiliki atribut seperti nama dan deskripsi.

2. **Mendapatkan Rekomendasi (metode `get_recommendations`)**: Metode ini menghasilkan prompt untuk layanan Azure OpenAI berdasarkan preferensi pengguna dan membuat permintaan HTTP POST ke API Azure OpenAI untuk mendapatkan destinasi yang disusun ulang peringkatnya dan diberi skor.

3. **Menghasilkan Prompt (metode `generate_prompt`)**: Metode ini membangun prompt untuk Azure OpenAI, termasuk preferensi pengguna dan daftar destinasi. Prompt ini membimbing model untuk menyusun ulang peringkat dan memberikan skor pada destinasi berdasarkan preferensi yang diberikan.

4. **Panggilan API**: Pustaka `requests` digunakan untuk membuat permintaan HTTP POST ke endpoint API Azure OpenAI. Responsnya berisi destinasi yang disusun ulang peringkatnya dan diberi skor.

5. **Contoh Penggunaan**: Agen perjalanan mengumpulkan preferensi pengguna (misalnya, minat pada wisata dan budaya yang beragam) dan menggunakan layanan Azure OpenAI untuk mendapatkan rekomendasi destinasi perjalanan yang disusun ulang peringkatnya dan diberi skor.

Pastikan untuk mengganti `your_azure_openai_api_key` dengan kunci API Azure OpenAI Anda yang sebenarnya dan `https://your-endpoint.com/...` dengan URL endpoint aktual dari deployment Azure OpenAI Anda.

Dengan memanfaatkan LLM untuk re-ranking dan scoring, agen perjalanan dapat memberikan rekomendasi perjalanan yang lebih personal dan relevan kepada klien, meningkatkan pengalaman mereka secara keseluruhan.

### RAG: Teknik Prompting vs Alat

Retrieval-Augmented Generation (RAG) dapat menjadi teknik prompting maupun alat dalam pengembangan agen AI. Memahami perbedaan antara keduanya dapat membantu Anda memanfaatkan RAG secara lebih efektif dalam proyek Anda.

#### RAG sebagai Teknik Prompting

**Apa itu?**

- Sebagai teknik prompting, RAG melibatkan perumusan kueri atau prompt tertentu untuk memandu pengambilan informasi yang relevan dari korpus besar atau basis data. Informasi ini kemudian digunakan untuk menghasilkan respons atau tindakan.

**Bagaimana cara kerjanya:**

1. **Merumuskan Prompt**: Buat prompt atau kueri yang terstruktur dengan baik berdasarkan tugas yang sedang dilakukan atau input pengguna.
2. **Mengambil Informasi**: Gunakan prompt untuk mencari data yang relevan dari basis pengetahuan atau dataset yang sudah ada.
3. **Menghasilkan Respons**: Gabungkan informasi yang diambil dengan model AI generatif untuk menghasilkan respons yang komprehensif dan koheren.

**Contoh dalam Agen Perjalanan**:

- Input Pengguna: "Saya ingin mengunjungi museum di Paris."
- Prompt: "Temukan museum terbaik di Paris."
- Informasi yang Diambil: Detail tentang Museum Louvre, Musée d'Orsay, dll.
- Respons yang Dihasilkan: "Berikut adalah beberapa museum terbaik di Paris: Museum Louvre, Musée d'Orsay, dan Centre Pompidou."

#### RAG sebagai Alat

**Apa itu?**

- Sebagai alat, RAG adalah sistem terintegrasi yang mengotomatisasi proses pengambilan dan pembuatan, sehingga memudahkan pengembang untuk mengimplementasikan fungsi AI yang kompleks tanpa harus membuat prompt secara manual untuk setiap kueri.

**Bagaimana cara kerjanya:**

1. **Integrasi**: Tanamkan RAG dalam arsitektur agen AI, memungkinkan agen untuk secara otomatis menangani tugas pengambilan dan pembuatan.
2. **Otomatisasi**: Alat ini mengelola seluruh proses, mulai dari menerima input pengguna hingga menghasilkan respons akhir, tanpa memerlukan prompt eksplisit untuk setiap langkah.
3. **Efisiensi**: Meningkatkan kinerja agen dengan merampingkan proses pengambilan dan pembuatan, memungkinkan respons yang lebih cepat dan akurat.

**Contoh dalam Agen Perjalanan**:

- Input Pengguna: "Saya ingin mengunjungi museum di Paris."
- Alat RAG: Secara otomatis mengambil informasi tentang museum dan menghasilkan respons.
- Respons yang Dihasilkan: "Berikut adalah beberapa museum terbaik di Paris: Museum Louvre, Musée d'Orsay, dan Centre Pompidou."

### Perbandingan

| Aspek                 | Teknik Prompting                                         | Alat                                                   |
|-----------------------|----------------------------------------------------------|-------------------------------------------------------|
| **Manual vs Otomatis**| Perumusan prompt secara manual untuk setiap kueri.        | Proses pengambilan dan pembuatan otomatis.            |
| **Kontrol**           | Memberikan lebih banyak kontrol atas proses pengambilan. | Merampingkan dan mengotomatisasi pengambilan dan pembuatan. |
| **Fleksibilitas**     | Memungkinkan prompt yang disesuaikan berdasarkan kebutuhan spesifik. | Lebih efisien untuk implementasi skala besar.         |
| **Kompleksitas**      | Membutuhkan pembuatan dan penyesuaian prompt.            | Lebih mudah diintegrasikan dalam arsitektur agen AI.  |

### Contoh Praktis

**Contoh Teknik Prompting:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Contoh Alat:**

```python
class Travel_Agent:
    def __init__(self):
        self.rag_tool = RAGTool()

    def get_museums_in_paris(self):
        user_input = "I want to visit museums in Paris."
        response = self.rag_tool.retrieve_and_generate(user_input)
        return response

travel_agent = Travel_Agent()
museums = travel_agent.get_museums_in_paris()
print("Top Museums in Paris:", museums)
```

### Mengevaluasi Relevansi

Mengevaluasi relevansi adalah aspek penting dari kinerja agen AI. Hal ini memastikan bahwa informasi yang diambil dan dihasilkan oleh agen sesuai, akurat, dan berguna bagi pengguna. Mari kita eksplorasi bagaimana mengevaluasi relevansi dalam agen AI, termasuk contoh praktis dan teknik.

#### Konsep Utama dalam Mengevaluasi Relevansi

1. **Kesadaran Konteks**:
   - Agen harus memahami konteks kueri pengguna untuk mengambil dan menghasilkan informasi yang relevan.
   - Contoh: Jika pengguna bertanya "restoran terbaik di Paris," agen harus mempertimbangkan preferensi pengguna, seperti jenis masakan dan anggaran.

2. **Akurasi**:
   - Informasi yang diberikan oleh agen harus faktual dan terkini.
   - Contoh: Merekomendasikan restoran yang saat ini buka dengan ulasan bagus daripada opsi yang sudah tutup atau usang.

3. **Niat Pengguna**:
   - Agen harus menyimpulkan niat pengguna di balik kueri untuk memberikan informasi yang paling relevan.
   - Contoh: Jika pengguna bertanya "hotel ramah anggaran," agen harus memprioritaskan opsi yang terjangkau.

4. **Umpan Balik**:
   - Mengumpulkan dan menganalisis umpan balik pengguna secara terus-menerus membantu agen menyempurnakan proses evaluasi relevansi.
   - Contoh: Mengintegrasikan peringkat dan umpan balik pengguna pada rekomendasi sebelumnya untuk meningkatkan respons di masa depan.

#### Teknik Praktis untuk Mengevaluasi Relevansi

1. **Skoring Relevansi**:
   - Berikan skor relevansi pada setiap item yang diambil berdasarkan seberapa baik item tersebut sesuai dengan kueri dan preferensi pengguna.
   - Contoh:

     ```python
     def relevance_score(item, query):
         score = 0
         if item['category'] in query['interests']:
             score += 1
         if item['price'] <= query['budget']:
             score += 1
         if item['location'] == query['destination']:
             score += 1
         return score
     ```

2. **Penyaringan dan Peringkat**:
   - Saring item yang tidak relevan dan beri peringkat pada item yang tersisa berdasarkan skor relevansinya.
   - Contoh:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Return top 10 relevant items
     ```

3. **Pemrosesan Bahasa Alami (NLP)**:
   - Gunakan teknik NLP untuk memahami kueri pengguna dan mengambil informasi yang relevan.
   - Contoh:

     ```python
     def process_query(query):
         # Use NLP to extract key information from the user's query
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integrasi Umpan Balik Pengguna**:
   - Kumpulkan umpan balik pengguna tentang rekomendasi yang diberikan dan gunakan untuk menyesuaikan evaluasi relevansi di masa depan.
   - Contoh:

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### Contoh: Mengevaluasi Relevansi dalam Agen Perjalanan

Berikut adalah contoh praktis bagaimana Agen Perjalanan dapat mengevaluasi relevansi rekomendasi perjalanan:

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
        ranked_hotels = self.filter_and_rank(hotels, self.user_preferences)
        itinerary = create_itinerary(flights, ranked_hotels, attractions)
        return itinerary

    def filter_and_rank(self, items, query):
        ranked_items = sorted(items, key=lambda item: self.relevance_score(item, query), reverse=True)
        return ranked_items[:10]  # Return top 10 relevant items

    def relevance_score(self, item, query):
        score = 0
        if item['category'] in query['interests']:
            score += 1
        if item['price'] <= query['budget']:
            score += 1
        if item['location'] == query['destination']:
            score += 1
        return score

    def adjust_based_on_feedback(self, feedback, items):
        for item in items:
            if item['name'] in feedback['liked']:
                item['relevance'] += 1
            if item['name'] in feedback['disliked']:
                item['relevance'] -= 1
        return items

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
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### Pencarian dengan Niat

Pencarian dengan niat melibatkan pemahaman dan interpretasi tujuan atau sasaran di balik kueri pengguna untuk mengambil dan menghasilkan informasi yang paling relevan dan berguna. Pendekatan ini melampaui sekadar mencocokkan kata kunci dan berfokus pada memahami kebutuhan dan konteks pengguna yang sebenarnya.

#### Konsep Utama dalam Pencarian dengan Niat

1. **Memahami Niat Pengguna**:
   - Niat pengguna dapat dikategorikan menjadi tiga jenis utama: informasional, navigasional, dan transaksional.
     - **Niat Informasional**: Pengguna mencari informasi tentang suatu topik (misalnya, "Apa museum terbaik di Paris?").
     - **Niat Navigasional**: Pengguna ingin menavigasi ke situs web atau halaman tertentu (misalnya, "Situs resmi Museum Louvre").
     - **Niat Transaksional**: Pengguna bertujuan untuk melakukan transaksi, seperti memesan tiket atau melakukan pembelian (misalnya, "Pesan tiket ke Paris").

2. **Kesadaran Konteks**:
   - Menganalisis konteks kueri pengguna membantu dalam mengidentifikasi niat mereka secara akurat. Hal ini mencakup mempertimbangkan interaksi sebelumnya, preferensi pengguna, dan detail spesifik dari kueri saat ini.

3. **Pemrosesan Bahasa Alami (NLP)**:
   - Teknik NLP digunakan untuk memahami dan menginterpretasi kueri bahasa alami yang diberikan oleh pengguna. Hal ini mencakup tugas seperti pengenalan entitas, analisis sentimen, dan parsing kueri.

4. **Personalisasi**:
   - Memersonalisasi hasil pencarian berdasarkan riwayat, preferensi, dan umpan balik pengguna meningkatkan relevansi informasi yang diambil.
#### Contoh Praktis: Pencarian dengan Maksud di Travel Agent

Mari kita ambil Travel Agent sebagai contoh untuk melihat bagaimana pencarian dengan maksud dapat diterapkan.

1. **Mengumpulkan Preferensi Pengguna**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Memahami Maksud Pengguna**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Kesadaran Konteks**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Mencari dan Memersonalisasi Hasil**

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

5. **Contoh Penggunaan**

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

## 4. Menghasilkan Kode sebagai Alat

Agen penghasil kode menggunakan model AI untuk menulis dan menjalankan kode, menyelesaikan masalah kompleks, dan mengotomatisasi tugas.

### Agen Penghasil Kode

Agen penghasil kode menggunakan model AI generatif untuk menulis dan menjalankan kode. Agen ini dapat menyelesaikan masalah kompleks, mengotomatisasi tugas, dan memberikan wawasan berharga dengan menghasilkan dan menjalankan kode dalam berbagai bahasa pemrograman.

#### Aplikasi Praktis

1. **Pembuatan Kode Otomatis**: Menghasilkan potongan kode untuk tugas tertentu, seperti analisis data, web scraping, atau pembelajaran mesin.
2. **SQL sebagai RAG**: Menggunakan kueri SQL untuk mengambil dan memanipulasi data dari basis data.
3. **Pemecahan Masalah**: Membuat dan menjalankan kode untuk menyelesaikan masalah tertentu, seperti mengoptimalkan algoritma atau menganalisis data.

#### Contoh: Agen Penghasil Kode untuk Analisis Data

Bayangkan Anda merancang agen penghasil kode. Berikut cara kerjanya:

1. **Tugas**: Menganalisis dataset untuk mengidentifikasi tren dan pola.
2. **Langkah-langkah**:
   - Memuat dataset ke dalam alat analisis data.
   - Menghasilkan kueri SQL untuk memfilter dan mengagregasi data.
   - Menjalankan kueri dan mengambil hasilnya.
   - Menggunakan hasil untuk menghasilkan visualisasi dan wawasan.
3. **Sumber Daya yang Dibutuhkan**: Akses ke dataset, alat analisis data, dan kemampuan SQL.
4. **Pengalaman**: Menggunakan hasil analisis sebelumnya untuk meningkatkan akurasi dan relevansi analisis di masa depan.

### Contoh: Agen Penghasil Kode untuk Travel Agent

Dalam contoh ini, kita akan merancang agen penghasil kode, Travel Agent, untuk membantu pengguna merencanakan perjalanan mereka dengan menghasilkan dan menjalankan kode. Agen ini dapat menangani tugas seperti mengambil opsi perjalanan, memfilter hasil, dan menyusun rencana perjalanan menggunakan AI generatif.

#### Gambaran Umum Agen Penghasil Kode

1. **Mengumpulkan Preferensi Pengguna**: Mengumpulkan input pengguna seperti tujuan, tanggal perjalanan, anggaran, dan minat.
2. **Menghasilkan Kode untuk Mengambil Data**: Menghasilkan potongan kode untuk mengambil data tentang penerbangan, hotel, dan atraksi.
3. **Menjalankan Kode yang Dihasilkan**: Menjalankan kode yang dihasilkan untuk mengambil informasi secara real-time.
4. **Menyusun Rencana Perjalanan**: Menyusun data yang diambil menjadi rencana perjalanan yang dipersonalisasi.
5. **Menyesuaikan Berdasarkan Umpan Balik**: Menerima umpan balik pengguna dan menghasilkan ulang kode jika diperlukan untuk menyempurnakan hasil.

#### Implementasi Langkah-demi-Langkah

1. **Mengumpulkan Preferensi Pengguna**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Menghasilkan Kode untuk Mengambil Data**

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

3. **Menjalankan Kode yang Dihasilkan**

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

4. **Menyusun Rencana Perjalanan**

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

5. **Menyesuaikan Berdasarkan Umpan Balik**

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

### Memanfaatkan Kesadaran Lingkungan dan Penalaran

Berdasarkan skema tabel, sistem dapat meningkatkan proses pembuatan kueri dengan memanfaatkan kesadaran lingkungan dan penalaran.

Berikut contoh bagaimana hal ini dapat dilakukan:

1. **Memahami Skema**: Sistem akan memahami skema tabel dan menggunakan informasi ini untuk mendasari pembuatan kueri.
2. **Menyesuaikan Berdasarkan Umpan Balik**: Sistem akan menyesuaikan preferensi pengguna berdasarkan umpan balik dan mempertimbangkan bidang mana dalam skema yang perlu diperbarui.
3. **Menghasilkan dan Menjalankan Kueri**: Sistem akan menghasilkan dan menjalankan kueri untuk mengambil data penerbangan dan hotel yang diperbarui berdasarkan preferensi baru.

Berikut adalah contoh kode Python yang diperbarui yang mengintegrasikan konsep ini:

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

#### Penjelasan - Pemesanan Berdasarkan Umpan Balik

1. **Kesadaran Skema**: Kamus `schema` mendefinisikan bagaimana preferensi harus disesuaikan berdasarkan umpan balik. Ini mencakup bidang seperti `favorites` dan `avoid`, dengan penyesuaian yang sesuai.
2. **Menyesuaikan Preferensi (metode `adjust_based_on_feedback`)**: Metode ini menyesuaikan preferensi berdasarkan umpan balik pengguna dan skema.
3. **Penyesuaian Berbasis Lingkungan (metode `adjust_based_on_environment`)**: Metode ini menyesuaikan preferensi berdasarkan skema dan umpan balik.
4. **Menghasilkan dan Menjalankan Kueri**: Sistem menghasilkan kode untuk mengambil data penerbangan dan hotel yang diperbarui berdasarkan preferensi yang disesuaikan dan mensimulasikan eksekusi kueri ini.
5. **Menyusun Rencana Perjalanan**: Sistem membuat rencana perjalanan yang diperbarui berdasarkan data penerbangan, hotel, dan atraksi baru.

Dengan membuat sistem sadar lingkungan dan menggunakan penalaran berdasarkan skema, sistem dapat menghasilkan kueri yang lebih akurat dan relevan, menghasilkan rekomendasi perjalanan yang lebih baik dan pengalaman pengguna yang lebih personal.

### Menggunakan SQL sebagai Teknik Retrieval-Augmented Generation (RAG)

SQL (Structured Query Language) adalah alat yang kuat untuk berinteraksi dengan basis data. Ketika digunakan sebagai bagian dari pendekatan Retrieval-Augmented Generation (RAG), SQL dapat mengambil data relevan dari basis data untuk menginformasikan dan menghasilkan respons atau tindakan dalam agen AI. Mari kita eksplorasi bagaimana SQL dapat digunakan sebagai teknik RAG dalam konteks Travel Agent.

#### Konsep Utama

1. **Interaksi Basis Data**:
   - SQL digunakan untuk mengkueri basis data, mengambil informasi relevan, dan memanipulasi data.
   - Contoh: Mengambil detail penerbangan, informasi hotel, dan atraksi dari basis data perjalanan.

2. **Integrasi dengan RAG**:
   - Kueri SQL dihasilkan berdasarkan input dan preferensi pengguna.
   - Data yang diambil kemudian digunakan untuk menghasilkan rekomendasi atau tindakan yang dipersonalisasi.

3. **Pembuatan Kueri Dinamis**:
   - Agen AI menghasilkan kueri SQL dinamis berdasarkan konteks dan kebutuhan pengguna.
   - Contoh: Menyesuaikan kueri SQL untuk memfilter hasil berdasarkan anggaran, tanggal, dan minat.

#### Aplikasi

- **Pembuatan Kode Otomatis**: Menghasilkan potongan kode untuk tugas tertentu.
- **SQL sebagai RAG**: Menggunakan kueri SQL untuk memanipulasi data.
- **Pemecahan Masalah**: Membuat dan menjalankan kode untuk menyelesaikan masalah.

**Contoh**:
Agen analisis data:

1. **Tugas**: Menganalisis dataset untuk menemukan tren.
2. **Langkah-langkah**:
   - Memuat dataset.
   - Menghasilkan kueri SQL untuk memfilter data.
   - Menjalankan kueri dan mengambil hasil.
   - Menghasilkan visualisasi dan wawasan.
3. **Sumber Daya**: Akses dataset, kemampuan SQL.
4. **Pengalaman**: Menggunakan hasil sebelumnya untuk meningkatkan analisis di masa depan.

#### Contoh Praktis: Menggunakan SQL di Travel Agent

1. **Mengumpulkan Preferensi Pengguna**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Menghasilkan Kueri SQL**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Menjalankan Kueri SQL**

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

4. **Menghasilkan Rekomendasi**

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

#### Contoh Kueri SQL

1. **Kueri Penerbangan**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Kueri Hotel**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Kueri Atraksi**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Dengan memanfaatkan SQL sebagai bagian dari teknik Retrieval-Augmented Generation (RAG), agen AI seperti Travel Agent dapat secara dinamis mengambil dan memanfaatkan data relevan untuk memberikan rekomendasi yang akurat dan dipersonalisasi.

### Contoh Metakognisi

Untuk mendemonstrasikan implementasi metakognisi, mari kita buat agen sederhana yang *merefleksikan proses pengambilan keputusannya* saat menyelesaikan masalah. Dalam contoh ini, kita akan membangun sistem di mana agen mencoba mengoptimalkan pilihan hotel, tetapi kemudian mengevaluasi penalarannya sendiri dan menyesuaikan strateginya ketika membuat kesalahan atau pilihan yang kurang optimal.

#### Bagaimana ini menggambarkan metakognisi:

1. **Keputusan Awal**: Agen akan memilih hotel termurah, tanpa memahami dampak kualitas.
2. **Refleksi dan Evaluasi**: Setelah pilihan awal, agen akan memeriksa apakah hotel tersebut adalah pilihan "buruk" menggunakan umpan balik pengguna. Jika kualitas hotel terlalu rendah, agen merefleksikan penalarannya.
3. **Menyesuaikan Strategi**: Agen menyesuaikan strateginya berdasarkan refleksi, beralih dari "termurah" ke "kualitas_tertinggi", sehingga meningkatkan proses pengambilan keputusan di iterasi berikutnya.

Berikut contohnya:

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

#### Kemampuan Metakognisi Agen

Kunci di sini adalah kemampuan agen untuk:
- Mengevaluasi pilihan dan proses pengambilan keputusan sebelumnya.
- Menyesuaikan strategi berdasarkan refleksi, yaitu metakognisi dalam tindakan.

Ini adalah bentuk sederhana dari metakognisi di mana sistem mampu menyesuaikan proses penalarannya berdasarkan umpan balik internal.

### Kesimpulan

Metakognisi adalah alat yang kuat yang dapat secara signifikan meningkatkan kemampuan agen AI. Dengan mengintegrasikan proses metakognitif, Anda dapat merancang agen yang lebih cerdas, adaptif, dan efisien. Gunakan sumber daya tambahan untuk lebih mengeksplorasi dunia metakognisi dalam agen AI.

### Punya Pertanyaan Lebih Lanjut tentang Pola Desain Metakognisi?

Bergabunglah dengan [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pembelajar lain, menghadiri jam konsultasi, dan mendapatkan jawaban atas pertanyaan Anda tentang Agen AI.

## Pelajaran Sebelumnya

[Pola Desain Multi-Agen](../08-multi-agent/README.md)

## Pelajaran Selanjutnya

[Agen AI dalam Produksi](../10-ai-agents-production/README.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.