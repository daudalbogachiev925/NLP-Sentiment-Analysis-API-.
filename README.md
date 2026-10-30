# 🧠 NLP Sentiment Analysis (Анализ тональности)

Проект по обработке естественного языка (NLP). Представляет собой веб-приложение, которое определяет эмоциональную окраску текста (позитив/негатив) на русском языке.

## 🛠 Стек
- **Python 3.10**
- **HuggingFace Transformers** (модель `blanchefort/rubert-base-cased-sentiment`)
- **PyTorch**
- **Streamlit** (UI)
- **Docker**

## 🚀 Как запустить локально

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your-username/sentiment-analysis.git
   cd sentiment-analysis

   Создайте виртуальное окружение и установите зависимости:


python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
pip install -r requirements.txt\
Запустите приложение:

streamlit run app.py

Приложение откроется в браузере (обычно http://localhost:8501).
Примечание: При первом запуске модель будет скачиваться с HuggingFace, это может занять 1-2 минуты.

 Запуск через Docker
docker build -t nlp-sentiment .
docker run -p 8501:8501 nlp-sentiment
