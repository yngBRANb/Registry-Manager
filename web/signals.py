from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Error, TelegramUser
from django.conf import settings
import logging
import requests
import os

logger = logging.getLogger(__name__)


def send_telegram_message(chat_id, text):
    url = f"https://api.telegram.org/bot7602750998:AAE-6L6T5KyWkTa3kYXQLZhxWS4jHRVDfJo/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'Markdown'
    }
    try:
        logger.info(f"Попытка отправить сообщение в Telegram: {payload}")
        response = requests.post(url, json=payload)
        response.raise_for_status()
        logger.info(f"Сообщение успешно отправлено в Telegram. Ответ: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при отправке сообщения в Telegram: {e}")
        logger.error(f"URL: {url}")
        logger.error(f"Payload: {payload}")

@receiver(post_save, sender=Error)
def notify_new_error(sender, instance, created, **kwargs):
    if created:
        try:
            logger.info(f"📝 Создана новая ошибка: {instance.id}")
            message = f"🚨 *Новая ошибка добавлена!*\n\n" \
                     f"📌 *Название:* {instance.name}\n" \
                     f"📝 *Описание:* {instance.description[:100]}...\n" \
                     f"🏷️ *Категория:* {instance.category}\n\n" \
                     f"🔍 Подробнее: {settings.SITE_URL}/error/{instance.id}"
            
            logger.info(f"Сформировано сообщение: {message}")
            
            # Отправляем сообщение всем подписчикам
            users = TelegramUser.objects.all()
            logger.info(f"Найдено {users.count()} пользователей для отправки")
            
            for user in users:
                logger.info(f"Отправка сообщения на chat_id: {user.chat_id}")
                send_telegram_message(user.chat_id, message)
                        
        except Exception as e:
            logger.error(f"Ошибка при отправке уведомления: {e}", exc_info=True)
