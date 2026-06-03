# Automated Python/Flask Deployment Pipeline (CI/CD & DevOps Showcase)

## 🇹🇷 Türkçe Proje Detayları

Bu proje; modern yazılım geliştirme süreçlerinin en kritik aşamalarından biri olan **DevOps, Konteynerizasyon (Docker) ve Sürekli Entegrasyon/Sürekli Dağıtım (CI/CD)** pratiklerini uygulamalı olarak sergilemek amacıyla geliştirilmiştir. 

Python ve Flask altyapısıyla kurulan mikro uygulama, kodun yazılmasından canlı sunucuya ulaşmasına kadar geçen tüm aşamaları tamamen otomatik bir boru hattı (pipeline) üzerinden yönetmektedir.

### ⚙️ Altyapı ve Süreç Mimarisi
*   **Konteynerizasyon (Docker):** Uygulama, platform bağımsız çalışabilmesi ve üretim ortamı (production) standartlarına uygun olması amacıyla `Dockerfile` ile imaj haline getirilmiş ve izole edilmiştir.
*   **Sürekli Entegrasyon (CI - GitHub Actions):** `.github/workflows` altında kurgulanan otomasyon sayesinde, depoya atılan (push) her yeni kod değişikliğinde `tests/` klasöründeki birim testler (unit tests) otomatik olarak tetiklenir.
*   **Sürekli Dağıtım (CD - Coolify & Azure VM):** Testleri başarıyla geçen kodlar, Azure sanal makinesi (Virtual Machine) üzerinde koşan Coolify platformu aracılığıyla hiçbir kesinti olmaksızın otomatik olarak canlıya (deployment) alınır.

### 🧠 Kazanılan DevOps Yetkinlikleri
*   CI/CD İş Akışı Yönetimi (Workflow Orchestration)
*   Docker ile İmaj Oluşturma ve Konteyner Yönetimi
*   GitHub Actions ile Test Otomasyonu
*   Bulut Altyapısı Yönetimi (Azure & PaaS Deployment)

---


### 🛠️ Teknolojik Stack
*   **Core Backend:** Python, Flask
*   **DevOps & Automation:** Docker, GitHub Actions, Coolify
*   **Cloud Infrastructure:** Microsoft Azure (Virtual Machines)

---

## 🇺🇸 English Project Details

This repository is a production-level demonstration of modern **DevOps practices, Containerization (Docker), and Continuous Integration/Continuous Deployment (CI/CD)** pipelines. 

Built upon a Python/Flask micro-application, this project orchestrates the entire lifecycle of software delivery—from local commits to automated cloud deployment—without manual intervention.

### ⚙️ Pipeline & Infrastructure Engineering
*   **Containerization (Docker):** The application architecture is isolated and standardized using a custom `Dockerfile`, ensuring identical environments across local development and cloud production.
*   **Continuous Integration (CI - GitHub Actions):** Workflows configured inside `.github/workflows` intercept every commit or push event, automatically executing the comprehensive suite located in the `tests/` directory.
*   **Continuous Deployment (CD - Azure & Coolify):** Upon successful validation of all test parameters, the source code undergoes zero-downtime, fully automated redeployment to an Azure Virtual Machine orchestrated via Coolify.

### 🧠 Core Engineering Competencies Demonstrated
*   Automated Workflow & Pipeline Design (GitHub Actions)
*   Infrastructure as Code & Containerized Architectures (Docker)
*   Unit Testing & Automated Quality Assurance (QA)
*   Cloud Deployment Operations (Azure Cloud & PaaS Management)
