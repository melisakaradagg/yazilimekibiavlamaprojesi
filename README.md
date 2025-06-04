<div align="center">
  <img src="https://img.shields.io/github/languages/count/melisakaradagg/yazilimekibiavlamaprojesi?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/melisakaradagg/yazilimekibiavlamaprojesi?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/melisakaradagg/yazilimekibiavlamaprojesi?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/melisakaradagg/yazilimekibiavlamaprojesi?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
</div>

# Software Team Hunting Project
*Yazılım Ekibi Avlama Projesi*

This project was developed to identify some basic protocols and services used by software teams on the network. The aim is to listen to the traffic of services such as FTP, SSH, MySQL and SQL Server over certain ports and to create the necessary infrastructure to analyze and filter this traffic using the Python language.  
*Bu proje, ağdaki yazılım ekipleri tarafından kullanılan bazı temel protokolleri ve servisleri tanımlamak için geliştirilmiştir. Amaç, FTP, SSH, MySQL ve SQL Server gibi servislerin trafiğini belirli portlar üzerinden dinlemek ve bu trafiği Python dili kullanılarak analiz etmek ve filtrelemek için gerekli altyapıyı oluşturmaktır.*

---
Features / Özellikler
Feature 1: List available network interfaces to let the user choose.
Özellik 1: Kullanıcının seçebilmesi için mevcut ağ arayüzlerini listeler.

Feature 2: Capture packets for specific ports (FTP, SSH, MySQL, SQL Server).
Özellik 2: Belirli portlar için (FTP, SSH, MySQL, SQL Server) ağ paketlerini yakalar.

Feature 3: Save captured packet summaries to a text file.
Özellik 3: Yakalanan paket özetlerini bir metin dosyasına kaydeder.

Feature 4: Show live packet capture results on the screen.
Özellik 4: Canlı olarak ağdan gelen paketleri ekranda gösterir.

---

## Team / *Ekip*

-2420191031 - Melisa KARADAĞ: Proje Sahibi / Project Owner 

---

## Roadmap / *Yol Haritası*

See our plans in [ROADMAP.md](ROADMAP.md).  
*Yolculuğu görmek için [ROADMAP.md](ROADMAP.md) dosyasına göz atın.*

---

## Research / *Araştırmalar*

| Topic / *Başlık*        | Link                                    | Description / *Açıklama*                        |
|-------------------------|-----------------------------------------|------------------------------------------------|
| Aircrack Deep Dive      | [researchs/aircrack.md](researchs/aircrack.md) | In-depth analysis of Aircrack-ng suite. / *Aircrack-ng paketinin derinlemesine analizi.* |
| Example Research Topic  | [researchs/your-research-file.md](researchs/your-research-file.md) | Brief overview of this research. / *Bu araştırmanın kısa bir özeti.* |
| Add More Research       | *Link to your other research files*     | *Description of the research*                  |

---

## Installation / *Kurulum*

1. **Clone the Repository / *Depoyu Klonlayın***:  
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
   ```

2. **Set Up Virtual Environment / *Sanal Ortam Kurulumu*** (Recommended):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies / *Bağımlılıkları Yükleyin***:  
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage / *Kullanım*

Run the project:  
*Projeyi çalıştırın:*

```bash
python main.py --input your_file.pcap --output results.txt
```

**Steps**:  
1. Prepare input data (*explain data needed*).  
2. Run the script with arguments (*explain key arguments*).  
3. Check output (*explain where to find results*).  

*Adımlar*:  
1. Giriş verilerini hazırlayın (*ne tür verilere ihtiyaç duyulduğunu açıklayın*).  
2. Betiği argümanlarla çalıştırın (*önemli argümanları açıklayın*).  
3. Çıktıyı kontrol edin (*sonuçları nerede bulacağınızı açıklayın*).

---

## Contributing / *Katkıda Bulunma*

We welcome contributions! To help:  
1. Fork the repository.  
2. Clone your fork (`git clone git@github.com:YOUR_USERNAME/YOUR_REPO.git`).  
3. Create a branch (`git checkout -b feature/your-feature`).  
4. Commit changes with clear messages.  
5. Push to your fork (`git push origin feature/your-feature`).  
6. Open a Pull Request.  

Follow our coding standards (see [CONTRIBUTING.md](CONTRIBUTING.md)).  

*Topluluk katkilerini memnuniyetle karşılıyoruz! Katkıda bulunmak için yukarıdaki adımları izleyin ve kodlama standartlarımıza uyun.*

---

## License / *Lisans*

Licensed under the [MIT License](LICENSE.md).  
*MIT Lisansı altında lisanslanmıştır.*

---

## Acknowledgements / *Teşekkürler* (Optional)

Thanks to:  
- Melisa KARADAĞ (karadagmelisa.mk@gmail.com)
- Istinye University

*Teşekkürler: Harika kütüphaneler ve ilham kaynakları için.*

---

## Contact / *İletişim* (Optional)

Project Maintainer: [Melisa KARADAĞ / Istinye University] - [Melisa KARADAĞ / Istinye University]  
Found a bug? Open an issue.  

*Proje Sorumlusu: [Melisa KARADAĞ / Istinye University] - [Melisa KARADAĞ / Istinye University]. Hata bulursanız bir sorun bildirin.*

---

*Replace placeholders (e.g., YOUR_USERNAME/YOUR_REPO) with your project details.*
