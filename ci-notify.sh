#!/bin/bash

TIME="10"
URL="https://api.telegram.org/bot7708142308:AAF7Igl56gq9xlB3WyZfKrhLPrWy40BiW3k/sendMessage"
TEXT="Статус деплоя: $1%0A%0AПроект:+$CI_PROJECT_NAME%0AСсылка:+$CI_PROJECT_URL/pipelines/$CI_PIPELINE_ID/%0AВетка:+$CI_COMMIT_REF_SLUG%0A%0AГойда zzz SVO"

curl -s --max-time $TIME -d "chat_id=895942691&disable_web_page_preview=1&text=$TEXT" $URL > /dev/null
