# Employee Retention Rate Analytics - Human Resource (HR) Department 
Proyek data science tentang studi kasus masalah di Departemen Sumber Daya Manusia (HR).

![Image](https://www.clearpeaks.com/wp-content/uploads/2019/05/Advanced-analytics-Employee-Attrition-1200-630.jpg)

## 🏷️Metodologi 

Metodologi manajemen proyek yang digunakan dalam proyek ini adalah CRISP-DM. Metodologi ini adalah salah satu dari beberapa metodologi yang sering digunakan di dunia industri. Selain CRISP-DM, ada beberapa metodologi manajemen proyek lainnya, yaitu Ad Hoc, Waterfall, Agile Scrum & Kanban. 

CRISP-DM (Cross Industry Standard Process for Data Mining) adalah pendekatan yang menggambarkan proses standar untuk proyek data mining, data science, dan machine learning. Dalam metodologi ini, pekerjaan pada proyek dimulai dengan tahap pemahaman bisnis agar dapat membantu memastikan proyek dilaksanakan sesuai dengan kebutuhan bisnis. Kelebihan lain dari metodologi ini adalah proses kerjanya bersifat iteratif, sehingga proses kerja dapat disesuaikan dengan kebutuhan eksperimen proyek data science. Ini berbeda dengan metodologi waterfall yang hanya berjalan satu arah. 

CRISP-DM terdiri dari 6 fase dan disusun sebagai siklus, yang bertujuan untuk memaksimalkan hasil dari proyek data science. Fase-fase CRISP-DM dapat dilihat pada gambar berikut:

![CRISP-DM](https://dicoding-web-img.sgp1.cdn.digitaloceanspaces.com/original/academy/dos:418b0f7f4b2dc3d25a68e4f10cca803820230908164632.jpeg)


## 🧭Business Understanding 

Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000. Perusahaan ini memiliki lebih dari 1000 karyawan yang tersebar di seluruh negeri. Meskipun telah menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih mengalami kesulitan dalam mengelola karyawan. Hal ini berdampak pada tingginya tingkat attrition (rasio jumlah karyawan yang keluar terhadap total jumlah karyawan) lebih dari 10%.

### Business Problems

Untuk mencegah masalah yang terjadi di perusahaan semakin parah, maka perlu diidentifikasi berbagai faktor yang dapat menyebabkan karyawan meninggalkan perusahaan.

### Project Scope

Berdasarkan masalah bisnis yang telah dijelaskan, untuk menjawab masalah bisnis ini akan dibuat sistem klasifikasi menggunakan Random Forest Classification. Sehingga dapat mengidentifikasi faktor-faktor yang berkontribusi terhadap tingginya tingkat attrition karyawan.

Selain itu, akan dibuat juga sebuah business dashboard yang dapat digunakan oleh Departemen HR untuk membantu memantau berbagai faktor yang menyebabkan tingginya tingkat attrition.

Berikut adalah beberapa pertanyaan yang akan dijawab dalam proyek ini dengan mengikuti konsep SMART-Question:

### SMART Question (Specific - Measurable - Action oriented - relevant - Time bond) :
- **Specific :** Faktor apa saja yang mempengaruhi tingkat attrition di perusahaan?
- **Measurable :** Berapa jumlah atau persentase faktor yang mempengaruhi tingkat attrition?
- **Action oriented:** Tindakan apa yang dapat dilakukan Departemen HR untuk merespons faktor-faktor penyebab karyawan keluar dan mengurangi tingkat attrition?
- **Relevant :** Apakah tindakan atau langkah ini dapat mengurangi tingkat attrition?
- **Time bond :** Berapa lama rencana untuk mengurangi tingkat attrition akan dilaksanakan?

### Project Preparation 
1. **Dataset** 
Proyek ini menggunakan [IBM HR Analytics Employee Attrition & Performance Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

2. **Tech Stack** 	
	 - **Programming Languages** : Python
	- **AI/ML** : Tensorflow, pandas, numpy, scikit-learn, SciPy, matplotlib, seaborn, sqlalchemy, psycopg2-binary, joblib
	- **Database** : PostreSQL
	- **Devops** : Docker image dengan Metabase
	- **Other** : Git

3. **Setup Environment** 

    **Library**
    
	`pip install numpy pandas scipy matplotlib seaborn jupyter sqlalchemy psycopg2-binary scikit-learn==1.2.2 joblib==1.3.1`
    
    **Metabase** <br>
    username : root@gmail.com<br> 
    password : root123

## 📚 Data Understanding 
Dataset yang digunakan dalam proyek machine learning ini adalah [IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset/). Dataset ini terdiri dari 1470 data dengan 35 fitur.

| Field                   | Description                                   |
|-------------------------|-----------------------------------------------|
| EmployeeId              | Identitas Karyawan                            |
| Attrition               | Apakah karyawan attrition? (0=tidak, 1=ya)   |
| Age                     | Usia karyawan                                 |
| BusinessTravel          | Komitmen perjalanan pekerjaan                 |
| DailyRate               | Gaji harian                                   |
| Department              | Departemen karyawan                          |
| DistanceFromHome        | Jarak dari rumah ke tempat kerja (dalam km)  |
| Education               | 1-Below College, 2-College, 3-Bachelor, 4-Master, 5-Doctor |
| EducationField          | Bidang Pendidikan                            |
| EnvironmentSatisfaction | 1-Rendah, 2-Sedang, 3-Tinggi, 4-Sangat Tinggi |
| Gender                  | Jenis kelamin karyawan                        |
| HourlyRate              | Gaji per jam                                  |
| JobInvolvement          | 1-Rendah, 2-Sedang, 3-Tinggi, 4-Sangat Tinggi |
| JobLevel                | Level pekerjaan (1 hingga 5)                 |
| JobRole                 | Peran pekerjaan                               |
| JobSatisfaction         | 1-Rendah, 2-Sedang, 3-Tinggi, 4-Sangat Tinggi |
| MaritalStatus           | Status perkawinan                             |
| MonthlyIncome           | Gaji bulanan                                  |
| MonthlyRate             | Tingkat bulanan                               |
| NumCompaniesWorked      | Jumlah perusahaan yang pernah bekerja         |
| Over18                  | Di atas 18 tahun?                             |
| OverTime                | Lembur?                                       |
| PercentSalaryHike       | Persentase kenaikan gaji tahun lalu          |
| PerformanceRating       | 1-Rendah, 2-Baik, 3-Sangat Baik, 4-Luar Biasa|
| RelationshipSatisfaction| 1-Rendah, 2-Sedang, 3-Tinggi, 4-Sangat Tinggi |
| StandardHours           | Jam Standar                                   |
| StockOptionLevel        | Tingkat Opsi Saham                            |
| TotalWorkingYears       | Total tahun bekerja                           |
| TrainingTimesLastYear   | Jumlah pelatihan yang dihadiri tahun lalu     |
| WorkLifeBalance         | 1-Rendah, 2-Baik, 3-Sangat Baik, 4-Luar Biasa |
| YearsAtCompany          | Tahun bekerja di perusahaan                   |
| YearsInCurrentRole      | Tahun di peran saat ini                       |
| YearsSinceLastPromotion | Tahun sejak terakhir promosi                  |
| YearsWithCurrManager    | Tahun dengan manajer saat ini                 |

## 📚 Data Preparation 
Tahap ini mencakup pengumpulan data, penilaian data, pembersihan data, atau proses rekayasa fitur. Dalam proyek ini dilakukan beberapa teknik seperti penanganan nilai yang hilang, penanganan data duplikat, dan beberapa teknik lainnya.

## 🎯 Modeling 
Dalam proyek ini algoritma machine learning yang digunakan adalah Random Forest.

![image](https://miro.medium.com/v2/resize:fit:1200/1*DvgOxmBc30t9HjDKFYLC0g.jpeg)

Algoritma random forest adalah algoritma pembelajaran terarah yang dapat digunakan untuk menyelesaikan masalah klasifikasi dan regresi. Random forest juga merupakan algoritma yang sering digunakan karena cukup sederhana namun memiliki stabilitas yang besar.

Random forest adalah model machine learning yang termasuk dalam kategori pembelajaran ansambel (grup). Pembelajaran ansambel adalah model prediksi yang terdiri dari beberapa model dan bekerja bersama. Ide di balik model ansambel adalah sekelompok model yang bekerja sama untuk menyelesaikan masalah. Jadi, tingkat keberhasilannya akan lebih tinggi daripada model yang bekerja sendiri. Dalam model ansambel, setiap model harus membuat prediksi secara independen. Kemudian, prediksi dari setiap model ansambel ini digabungkan untuk membuat prediksi akhir.

## Evaluasi dan Deployment

Memahami evaluasi model adalah langkah penting dalam analisis data terstruktur maupun tidak terstruktur. Evaluasi model membantu kita mengetahui seberapa baik model kita dalam memberikan hasil yang tepat. Untuk mengevaluasi sebuah model, kita dapat menggunakan beberapa metode atau ukuran yang dapat memberikan gambaran objektif tentang kinerja model. Beberapa ukuran yang sering digunakan adalah akurasi, presisi, recall, spesifisitas, dan skor F1. Dengan memahami evaluasi model, kita dapat melihat kelebihan dan kekurangan dari model yang kita buat. Sehingga, kita dapat melakukan perbaikan agar model dapat memberikan hasil yang lebih baik.

| Metric   | Definisi                                                                                   |
|----------|--------------------------------------------------------------------------------------------|
| Presisi  | Rasio true positives terhadap jumlah true positives dan false positives.                  |
| Recall   | Rasio true positives terhadap jumlah true positives dan false negatives.                  |
| Skor F1  | Rata-rata harmonik tertimbang dari presisi dan recall. Semakin mendekati 1.0, semakin baik modelnya. |
| Support  | Jumlah kejadian aktual dari kelas dalam dataset.                                           |

## Dashboard Bisnis

Berikut adalah beberapa tahapan yang umumnya ditemukan dalam pengembangan sebuah dashboard bisnis.

1. **Definisikan:** Pada tahap awal, tentu kita perlu memahami audiens untuk dashboard yang akan dibuat. Selain itu, kita juga perlu menentukan tujuan atau output dari dashboard serta pertanyaan bisnis yang ingin kita jawab melalui visualisasi data.

2. **Kumpulkan Data:** Tahap berikutnya adalah menentukan atau mengumpulkan data yang akan digunakan untuk menjawab pertanyaan bisnis. Pada tahap ini, kita perlu mempertimbangkan sumber dan kualitas data yang akan digunakan.

3. **Prototipe:** Setelah mengetahui tujuan dan data yang akan digunakan, tahap berikutnya adalah membuat prototipe/sketsa/mockup dari dashboard yang akan dibuat. Hal ini akan membantu Anda membuat tata letak dashboard yang baik dan efektif. Dalam proses ini, Anda perlu mempertimbangkan ukuran tampilan dan menggunakan sweet spot yang tepat.

4. **Bangun:** Jika prototipe yang Anda buat telah selesai, Anda dapat mulai membuat dan menyusun dashboard sesuai dengan prototipe yang telah Anda buat. Dalam proses ini, Anda perlu menentukan bentuk grafis yang tepat untuk menjawab pertanyaan bisnis.

5. **Evaluasi:** Tahap berikutnya adalah mengevaluasi dashboard yang telah dibuat. Hal ini dilakukan untuk memastikan bahwa grafik dan komponen visual lainnya yang terdapat dalam dashboard efektif dan mudah dipahami.

6. **Umpan Balik:** Terakhir, kita juga perlu meminta umpan balik dari audiens atau pengguna terkait dashboard yang telah dibuat. Hal ini tentu akan sangat membantu kita dalam membuat dashboard bisnis yang lebih baik di masa depan.

### Dashboard Bisnis

Dashboard bisnis yang telah dibuat dapat diakses pada tautan berikut:

- [Demografi karyawan](http://localhost:8000/public/dashboard/398cb3da-c03a-42ae-a20c-376731f7d5c2)
- [Analisis Turnover Karyawan](http://localhost:8000/public/dashboard/9ef77c75-a07e-47ca-bd08-af6aad6837bd)
- [Kesejahteraan Karyawan](http://localhost:8000/public/dashboard/5382b602-4e1d-4c31-a432-d02ba3e00ea9)

## Kesimpulan & Rekomendasi Aksi

**SMART (Specific - Measurable - Action oriented - Relevant - Time bond)**

Berdasarkan KPI & wawasan yang diperoleh dari hasil analisis, dapat disimpulkan bahwa ada beberapa faktor yang mempengaruhi tingkat turnover perusahaan Jaya Jaya Maju. Faktor-faktor tersebut adalah pendapatan bulanan, lembur, usia, total tahun kerja, dan jarak dari rumah (Specific).

Dari dashboard bisnis yang telah dibuat sebelumnya, beberapa wawasan dapat diperoleh, di antaranya adalah:

- Sebanyak 85% (153 karyawan) yang berhenti bekerja mendapatkan pendapatan bulanan yang rendah-menengah. Sementara itu, karyawan dengan pendapatan bulanan yang lebih tinggi (pendapatan tinggi) cenderung bertahan atau bekerja di perusahaan. (Measurable) Dengan mempertimbangkan dampak gaji terhadap tingkat turnover perusahaan, diperlukan kembali atau upaya untuk meninjau dan mengumpulkan informasi untuk mengetahui apakah perusahaan memberikan gaji yang kompetitif sesuai kondisi pasar. Sehingga karyawan merasa dihargai dan termotivasi untuk terus bekerja. (Action oriented & Relevant)

- Karyawan atau pekerja dalam kelompok usia 18-40 tahun memiliki kecenderungan lebih besar untuk berhenti bekerja dibandingkan dengan mereka yang berada dalam kelompok usia yang lebih tua. (Measurable) Oleh karena itu, upaya yang dapat dilakukan adalah menyelaraskan visi jangka panjang dengan karyawan muda, serta memberikan penghargaan, karir, serta promosi yang jelas. (Action oriented & Relevant)

- Jarak antara kantor dan tempat tinggal juga mempengaruhi tingkat turnover perusahaan Jaya Jaya Maju, berdasarkan hasil analisis, 59% (107 karyawan) yang pergi atau berhenti bekerja tinggal sangat jauh dari kantor. (Measurable) Terkait dengan masalah ini, perusahaan dapat memberikan dukungan transportasi bagi karyawan atau memberikan dukungan berupa tunjangan transportasi. Sehingga dapat mengurangi tingkat turnover perusahaan. (Action oriented & Relevant).

- Sebanyak 54% (98 karyawan) berhenti bekerja karena lembur. (Measurable) Oleh karena itu, upaya yang dapat dilakukan perusahaan adalah merencanakan atau merancang proyek-proyek yang dilakukan dengan baik pada awalnya dan dengan tenaga kerja yang memadai, sehingga karyawan tidak bekerja lembur. Alternatif lain adalah memberikan kompensasi kepada karyawan yang telah bekerja lembur, sehingga dapat mengurangi tingkat turnover. (Action oriented & Relevant)

- Sebanyak 65% (117 karyawan) yang berhenti bekerja terkait dengan faktor-faktor perjalanan bisnis pada tingkat langka. Hal ini menunjukkan bahwa perjalanan bisnis berpengaruh pada tingkat turnover. Langkah yang dapat diambil perusahaan adalah meninjau dan mengoptimalkan kebijakan perjalanan bisnis untuk semua karyawan untuk meminimalkan tingkat stres karyawan dan membantu mempertahankan karyawan. (Action oriented & Relevant)

Hasil dari analisis atau wawasan yang diperoleh beserta langkah-langkah yang dapat diambil perusahaan untuk mengurangi tingkat turnover harus dilakukan dalam periode waktu yang jelas. Untuk awalnya, program-program tertentu yang telah dirancang akan diimplementasikan selama enam bulan pertama. Kemudian evaluasi dari program tersebut dilakukan untuk mengetahui apakah terdapat perubahan signifikan terhadap tingkat turnover perusahaan Jaya Jaya Maju. (Time Bond)

Di sisi lain, langkah-langkah juga diperlukan seperti mengadakan pertemuan tatap muka secara berkala dalam jangka waktu tertentu antara manajer SDM dan karyawan yang berisiko tinggi untuk pergi atau berhenti dari pekerjaan mereka. Dengan tujuan untuk mengetahui dan mendiskusikan kondisi kerja yang dialami. Sehingga para pemangku kepentingan dapat menentukan langkah-langkah pencegahan dan solusi yang tepat.

### Tautan

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://syarifulmsth.github.io) [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/syariful-musthofa/) [![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/)

### Umpan Balik

Jika Anda memiliki umpan balik, silakan hubungi saya di syarifulm007@gmail.com
