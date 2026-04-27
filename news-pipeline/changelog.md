# KUBRIK News Pipeline - Changelog

Append-only log of all knowledge base changes made by the automated news pipeline.

---

<!-- Entries are prepended (newest first). Format:
## YYYY-MM-DD | [platform] [category]
**Source:** [article URL]
**Classification:** spec_change | policy_update | new_feature | deprecation
**Urgency:** breaking | important | informational
**Changes:**
- `file/path.md` - description of change
**Agents updated:** [list]
**Commit:** [hash]
-->

## 2026-04-27 | yandex new_feature
**Source:** https://yandex.ru/adv/news/knopka-kupit-v-1-klik-teper-v-lente-ritma
**Classification:** new_feature (confidence: 90%)
**Urgency:** informational
**Changes:**
- `knowledge/yandex-direct-course/yandex-commerce-protocol-ycp.md` - добавлена поверхность Яндекс Ритм: кнопка «Купить в 1 клик» теперь доступна в постах ленты на ya.ru (тестовый режим, апрель 2026), конверсия x7 vs обычных постов
**Agents updated:** none
**Commit:** 5e08818

## 2026-04-27 | yandex new_feature
**Source:** https://yandex.ru/adv/news/novye-instrumenty-dlya-sovmestnoy-raboty-nad-tekstom-v-redaktore-promostranits
**Classification:** new_feature (confidence: 90%)
**Urgency:** informational
**Changes:**
- `knowledge/yandex-direct-course/promostranicy-collaboration-tools.md` - создан файл: инструменты совместной работы в редакторе ПромоСтраниц - шеринг черновика по ссылке, ветки комментариев, сравнение версий, AI-переписывание фрагментов
**Agents updated:** none
**Commit:** 5e08818

## 2026-04-27 | google new_feature
**Source:** https://blog.google/products/ads-commerce/ads-advisor-google-ads/
**Classification:** new_feature (confidence: 88%)
**Urgency:** informational
**Changes:**
- `knowledge/google-ads/explore-features/ads-advisor-safety-features.md` - создан файл: 3 новые функции Ads Advisor - Proactive Troubleshooting (Real-Time Policy Reviews), 24/7 Security Monitoring (passkeys, security dashboard), Instant Certifications (Gemini, автосертификация)
- `agents/contextologist/skill.md` - добавлена ссылка на ads-advisor-safety-features.md в раздел источников Google Ads
**Agents updated:** contextologist
**Commit:** 5e08818

## 2026-04-27 | google new_feature
**Source:** https://blog.google/products/ads-commerce/demand-gen-drop-april-2026/
**Classification:** new_feature (confidence: 85%)
**Urgency:** informational
**Changes:**
- `knowledge/google-ads/campaigns/demand-gen-campaigns.md` - добавлен раздел «Новые возможности (апрель 2026)»: Demand Gen в Commerce Media Suite (first-party данные ритейлеров в Google Ads), VTC optimization для YouTube
**Agents updated:** none (contextologist уже имеет ссылку на этот файл)
**Commit:** 5e08818

## 2026-04-20 | google deprecation+new_feature
**Source:** https://blog.google/products/ads-commerce/dsa-upgrade-to-ai-max-2026/
**Classification:** deprecation+new_feature (confidence: 88%)
**Urgency:** important
**Changes:**
- `knowledge/google-ads/campaigns/ai-max-for-search-campaigns.md` - полностью обновлен: AI Max вышел из беты (GA апрель 2026), +7% конверсий при полном suite; таблица DSA vs AI Max; план миграции (добровольный сейчас, автоматический сентябрь 2026)
- `agents/contextologist/skill.md` - обновлена строка AI Max: добавлен статус GA, дата замены DSA (сентябрь 2026), метрика +7%, рекомендация text guidelines для premium
**Agents updated:** contextologist
**Commit:** 3030f1c

## 2026-04-20 | yandex new_feature
**Source:** https://yandex.ru/adv/news/sozdanie-statej-s-ii-generatorom-v-promostranicah
**Classification:** new_feature (confidence: 87%)
**Urgency:** informational
**Changes:**
- `knowledge/yandex-direct-course/promostranicy-ai-article-generator.md` - создан файл: AI-генератор статей в ПромоСтраницах (Alice AI, Ya.Cloud), черновик за 10-20 мин, 5 целей продвижения, применение для недвижимости (TOFU/MOFU, вывод ЖК, конкурентное переключение)
**Agents updated:** none
**Commit:** 3030f1c

## 2026-04-13 | yandex new_feature
**Source:** https://yandex.ru/adv/news/lendingi-v-direct-vyhod-iz-bety
**Classification:** new_feature (confidence: 90%)
**Urgency:** important
**Changes:**
- `knowledge/yandex-direct-course/yandex-direct-landings-2026.md` - создан файл: Лендинги в Директе вышли из беты (апрель 2026) - резервная посадочная в ЕПК, адаптивная структура, AI-подбор изображений, уникальный URL, экспорт заявок в API
- `agents/contextologist/skill.md` - добавлена ссылка на `yandex-direct-landings-2026.md` в раздел источников знаний; добавлено описание резервной посадочной в ЕПК в раздел Яндекс Директ
**Agents updated:** contextologist
**Commit:** 80ac1f1

## 2026-04-06 | yandex deprecation
**Source:** https://yandex.ru/adv/news/ustarevshie-modeli-atribycii
**Classification:** deprecation (confidence: 90%)
**Urgency:** important
**Changes:**
- `knowledge/yandex-direct-course/attribution-models-deprecation-2026.md` - создан файл: устаревшие модели атрибуции Метрики/Директа отключаются 21 апр / 20 мая 2026, таблица миграции
**Agents updated:** none (изменение в аналитике, не в рекламных форматах)
**Commit:** 15f5c9f

## 2026-04-06 | yandex new_feature
**Source:** https://yandex.ru/adv/news/v-kartah-poyavilas-vozmozhnost-dlya-prodvizheniya-biznes-centrov
**Classification:** new_feature (confidence: 90%)
**Urgency:** informational
**Changes:**
- `knowledge/yandex-direct-course/yandex-maps-3d-business-centers.md` - создан файл: 3D-макеты в Яндекс Картах теперь доступны для бизнес-центров (коммерческая недвижимость), актуально для клиентов KUBRIK
**Agents updated:** none
**Commit:** 15f5c9f

## 2026-03-31 | yandex new_feature
**Source:** https://yandex.ru/adv/news/ycp-kak-poluchat-prodazhi-iz-otvetov-v-chate-s-alisoj-ai-i-iz-poiska-yandeksa
**Classification:** new_feature (confidence: 90%)
**Urgency:** important
**Changes:**
- `knowledge/yandex-direct-course/yandex-commerce-protocol-ycp.md` - создан файл: Yandex Commerce Protocol (YCP) - новый стандарт интеграции интернет-магазинов с ИИ, кнопка "Купить в 1 клик" в Алисе AI и Яндекс Поиске
**Agents updated:** none (YCP не является рекламным форматом Директа, агенты не обновлены)
**Commit:** ffb5ab4

## 2026-03-31 | google new_feature
**Source:** https://blog.google/products/ads-commerce/demand-gen-drop-march-2026/
**Classification:** new_feature (confidence: 88%)
**Urgency:** informational
**Changes:**
- `knowledge/google-ads/campaigns/demand-gen-campaigns.md` - создан KB-файл: Demand Gen кампании - новые функции марта 2026: Veo (генерация видео из изображений), YouTube Creator Partnerships boost (+30% конверсий на Shorts), оптимизация под follow-on views
- `agents/contextologist/skill.md` - добавлена ссылка на `demand-gen-campaigns.md` в раздел источников знаний
**Agents updated:** contextologist
**Commit:** 25d3c09
