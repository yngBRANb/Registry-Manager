#!/bin/bash

TIME="10"
URL="https://api.telegram.org/bot7708142308:AAF7Igl56gq9xlB3WyZfKrhLPrWy40BiW3k/sendMessage"
TEXT="Deploy status: $1%0A%0AProject:+$CI_PROJECT_NAME%0AURL:+$CI_PROJECT_URL/pipelines/$CI_PIPELINE_ID/%0ABranch:+$CI_COMMIT_REF_SLUG"

curl -s --max-time $TIME -d "chat_id=895942691&disable_web_page_preview=1&text=$TEXT" $URL > /dev/null
