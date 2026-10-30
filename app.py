import streamlit as st
from transformers import pipeline
import pandas as pd

# Настройка страницы Streamlit
st.set_page_config(page_title="NLP Sentiment Analysis", page_icon="🧠", layout="centered")

st.title("🧠 Анализ тональности текста (NLP)")
st.markdown("""
Этот сервис использует современную нейросеть (BERT) для определения эмоциональной окраски текста.
Введите текст на русском языке, и модель определит, является ли он **позитивным** или **негативным**.
""")

# Кэшируем загрузку модели, чтобы она не загружалась при каждом клике
@st.cache_resource
def load_model():
    # Используем легковесную русскоязычную модель от SberDevices
    model_name = "blanchefort/rubert-base-cased-sentiment"
    classifier = pipeline("sentiment-analysis", model=model_name, tokenizer=model_name)
    return classifier

try:
    with st.spinner("Загрузка нейросети... Пожалуйста, подождите (это происходит только один раз)..."):
        classifier = load_model()
    st.success("Модель успешно загружена!")
except Exception as e:
    st.error(f"Ошибка при загрузке модели: {e}")
    st.stop()

# Поле для ввода текста
user_input = st.text_area("Введите текст для анализа:", height=150, placeholder="Например: Этот фильм просто ужасен, зря потратил время...")

if st.button("Проанализировать"):
    if user_input.strip() == "":
        st.warning("Пожалуйста, введите текст.")
    else:
        with st.spinner("Анализируем..."):
            # Получаем предсказание
            result = classifier(user_input)[0]
            
            label = result['label']
            score = result['score']
            
            # Маппинг меток модели на понятный язык
            # Модель blanchefort выдает метки POSITIVE и NEGATIVE
            if label == 'POSITIVE':
                emoji = "😊"
                color = "green"
                text_result = "Позитивный"
            else:
                emoji = "😡"
                color = "red"
                text_result = "Негативный"
                
            st.markdown("---")
            st.subheader("Результат анализа:")
            
            # Вывод результата с цветом
            st.markdown(f"<h1 style='text-align: center; color: {color};'>{emoji} {text_result}</h1>", unsafe_allow_html=True)
            
            # Вывод уверенности модели
            st.write(f"**Уверенность модели:** {score * 100:.2f}%")
            
            # Прогресс-бар для наглядности
            st.progress(float(score))

st.markdown("---")
st.caption("Разработано с использованием HuggingFace Transformers и Streamlit.")
