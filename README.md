# 🤖 Telegram Historical AI Bot

**Поговори с Наполеоном! Спроси Эйнштейна про E=mc²!**  
Бот превращает ИИ в исторических личностей — отвечают **их голосом**! 🪖⚛️

![Demo GIF](screenshots/demo.gif)

## ✨ **Что умеет**
- 🧠 **15+ персонажей**: Наполеон, Эйнштейн, Цезарь, Екатерина II
- 🗣️ **Помнит разговор** — контекст сохраняется
- ⌨️ **Красивые кнопки** — один клик для выбора
- 🔥 **OpenAI + Gemini** — мощный ИИ


# 🏗️ Архитектура (Middle-level)

TG_bot_AI/
📁 telegram-historical-ai-bot/
│
├── bot.py           🎯 Главный Telebot
├── config.py        🔑 Загрузка .env
│
├── handlers/        📨 Обработчики
│   ├── start.py     /start команда
│   └── chat.py      Диалог с ИИ
│
├── keyboards/       ⌨️ Кнопки
│   └── main.py      Наполеон/Эйнштейн
│
├── data/            🧠 Персонажи
│   └── personas.json
│
├── .env.example     📋 Твои ключи
└── requirements.txt 📦 Зависимости

# 🔥 Стек

Технология	Версия	Назначение
Python	3.11+	Основной язык
Telebot	4.22.1	Telegram API
OpenAI	1.85.0	Генерация текста
dotenv	1.0.1	Конфигурация

# 🌟 Для рекрутеров

✅ Async-ready архитектура (легко мигрировать на aiogram)

✅ Модульность — handlers отделены

✅ Безопасность — .env в gitignore

✅ Документация — README + примеры
