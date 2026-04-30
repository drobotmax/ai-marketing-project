# Семантика и кластеры запросов (Allex Villas)

16 кластеров коммерческой семантики, всего 926 запросов. Источник — Google Sheet (см. LINKS.md).

## Карта кластеров

| Кластер (родительский) | Объём (запросов) | Подкластеры | Объём подкластера |
|---|---|---|---|
| **bali development** | 8 | — | — |
| **bali investment** | 24 | — | — |
| **buying a property in bali** | 14 | hotel for sales in bali | 17 |
| | | apartments for sale in bali | 19 |
| | | bali villas sale | 254 |
| | | land for sale | 46 |
| | | luxe villa bali | 22 |
| | | cheap bali villas | 22 |
| **rent in bali** | 37 | bali apartment for rent | 91 |
| | | bali villas for rent | 147 |
| **real estate in bali** | 83 | — | — |
| **management in bali** | 43 | — | — |
| **architect firm** | 13 | — | — |
| **bali property legal assistance** | 3 | — | — |
| **freehold bali** | 83 | — | — |

## Топ кластеров по объёму

1. **bali villas sale** — 254 запроса (самый горячий)
2. **bali villas for rent** — 147
3. **bali apartment for rent** — 91
4. **freehold bali** — 83
5. **real estate in bali** — 83
6. **land for sale** — 46
7. **management in bali** — 43
8. **rent in bali** — 37
9. **bali investment** — 24
10. **luxe / cheap villa bali** — 22 каждый

## Маппинг кластеров на структуру сайта

| Кластер | Где приземляем |
|---|---|
| bali villas sale | `/sale/villas` (общий листинг продажи) + `/sale/villas/<location>` (под локацию) |
| bali villas for rent | `/rent/villas` + `/rent/villas/<location>` |
| bali apartment for rent | `/rent/apartments` + `/rent/apartments/<bedrooms>` |
| hotel for sales in bali | `/sale/hotels` |
| apartments for sale in bali | `/sale/apartments` |
| land for sale | `/sale/land` |
| luxe villa bali | `/sale/villas/luxury` |
| cheap bali villas | `/sale/villas/discount` |
| freehold bali | `/sale/freehold` (важно: иностранцы могут владеть только freehold через структуры) |
| real estate in bali | главная + `/about` + `/blog/bali-real-estate-guide` |
| management in bali | `/services/management` + посадочная под управление |
| bali investment | `/invest` + калькулятор рентабельности |
| bali development | `/development` (текущие проекты, что строим) |
| architect firm | `/services/architecture` |
| bali property legal assistance | `/services/legal` |
| buying a property in bali | hub-страница + блог-статья «как купить недвижимость на Бали» |

## Принцип: один кластер = одна посадочная

Если кластер большой (>50 запросов) → отдельная страница с уникальным title, description, текстом, FAQ.

Если кластер малый (<10 запросов) → объединяется с родительским или закрывается блог-статьёй.

## Гайдлайн на любую недвижку

Для нового проекта застройщика — собрать кластеры по той же схеме:
- **Транзакционные:** *<тип объекта> sale / rent / buy в <регион>* + сегменты по бюджету / локации / типу собственности.
- **Информационные:** *invest / management / freehold / legal / regulations / how to* — закрываются блогом (это E-E-A-T-трафик, конвертирует в лиды через формы и калькулятор).
- **Услуги девелопера:** *development / architecture / construction / sale / management* — посадочные под услуги.

Пропорция объёма обычно: транзакционные ~70%, информационные ~25%, услуги ~5%. Маленький объём услуг компенсируется высокой конверсией.

## Расширение под управляющий трек

Если клиент работает с управлением (как Allex Villas), кластер «management in bali» (43 запроса) разворачивается в отдельный микро-сайт внутри сайта:
- `/services/management` — главная управления
- `/services/management/villa` — управление виллами
- `/services/management/apartment` — управление апартами
- `/services/management/calculator` — калькулятор доходности от управления
- блог-статьи под информационные запросы про управление (как сдавать, что входит в услугу, какая комиссия — типичные вопросы инвестора)

Под этот трек берётся вторая когорта конкурентов (см. seo-competitor-analysis.md).
