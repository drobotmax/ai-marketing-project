# Client Memory

## Snapshot
- Client: Горизонт Девелопмент (тестовый клиент)
- Project / object: ЖК "Парковый"
- Market: РФ, первичная недвижимость, Краснодар
- Stage: test pipeline / pre-launch
- Owner: KUBRIK team

## Core Facts
- Product: комфорт+ ЖК, 3 корпуса, 280 квартир, сдача Q4 2027
- Geography: Краснодар и край + Москва / СПб для релокантов
- Audience: молодые семьи, инвесторы, релоканты
- Budget: 500К руб/мес
- KPI: 80-120 лидов/мес, CPL до 5000 руб, конверсия в просмотр 20-30%

## Positioning
- Core offer: встроенная маркетинговая команда для системного запуска объекта
- Main differentiator: парк 3 га во дворе + центральная локация + ипотека от 0.1%
- Key message: единственный комплекс в центре Краснодара с парком 3 га во дворе

## Launch Readiness
- Landing page: `https://parkovy.gorizont-dev.test`
- CRM: AmoCRM
- Feed: есть XML-фид по квартирам
- Analytics: Яндекс Метрика не установлена
- Call tracking: отсутствует
- Consent / privacy: чекбокс согласия есть, политику конфиденциальности нужно проверить на лендинге

## Constraints
- Legal: без подтвержденной privacy / consent нельзя считать лид-формы полностью launch-ready
- Budget: 500К руб/мес - hard constraint
- Brand: не продавать "AI-агентов" как abstraction, продавать понятный маркетинговый результат
- Operational: товарные кампании и полноценная оптимизация ограничены до установки Метрики и коллтрекинга

## Decisions Log
- 2026-03-31: тестовый клиент используется как end-to-end проверка pipeline
- 2026-04-04: клиент переведен в новый ops-format с явной operational memory

## Open Questions
- Кто отвечает за установку Метрики и настройку целей?
- Когда подключается коллтрекинг?
- Есть ли подтвержденная privacy policy на лендинге?
- Когда можно передавать офлайн-конверсии из AmoCRM в аналитику?

## Next Step
- Создать launch-readiness session и закрыть blockers по analytics / call tracking / privacy
