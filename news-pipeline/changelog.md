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

## 2026-04-06 | yandex deprecation
**Source:** https://yandex.ru/adv/news/ustarevshie-modeli-atribycii
**Classification:** deprecation (confidence: 90%)
**Urgency:** important
**Changes:**
- `knowledge/yandex-direct-course/attribution-models-deprecation-2026.md` - создан файл: устаревшие модели атрибуции Метрики/Директа отключаются 21 апр / 20 мая 2026, таблица миграции
**Agents updated:** none (изменение в аналитике, не в рекламных форматах)
**Commit:** TBD

## 2026-04-06 | yandex new_feature
**Source:** https://yandex.ru/adv/news/v-kartah-poyavilas-vozmozhnost-dlya-prodvizheniya-biznes-centrov
**Classification:** new_feature (confidence: 90%)
**Urgency:** informational
**Changes:**
- `knowledge/yandex-direct-course/yandex-maps-3d-business-centers.md` - создан файл: 3D-макеты в Яндекс Картах теперь доступны для бизнес-центров (коммерческая недвижимость), актуально для клиентов KUBRIK
**Agents updated:** none
**Commit:** TBD

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
