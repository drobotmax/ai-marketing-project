# VK Ads API - справочник (T3)

Техническая справка для интеграций с рекламным кабинетом VK Рекламы (ads.vk.com).
Источник: https://ads.vk.com/help/features/help_api, https://ads.vk.com/doc/api/info/

Используется агентами (targeting, media-buyer, validator) и инфраструктурой для:
- вытягивания статистики кампаний/объявлений
- автоматической загрузки аудиторий (лукалайк, ремаркетинг, пользовательские списки)
- автоматизации запуска/паузы/бюджетов
- отчётности по клиентам

## 1. Получение доступа

1. Заполнить реквизиты в кабинете:
   - юрлица/агентства - раздел «Бюджет» (реквизиты должны пройти модерацию)
   - физлица - раздел «Настройки»
2. «Настройки» → «Доступ к API» → «Запросить доступ к API». Указать ФИО и контакты ответственного.
3. После одобрения в «Настройках» появятся `client_id` и кнопка получения `client_secret`.
   - `client_secret` доступен для копирования **только 10 минут**, повторно не выдаётся. Сохранять сразу.
4. Поддержка API: `ads_api@vk.team`.

## 2. Базовые параметры

- Host: `https://ads.vk.com`
- Префикс: `/api/v2/` (часть ресурсов - `v3`)
- Формат: JSON, `Content-Type: application/json`
- Стиль: REST-like, методы HTTP: GET/POST/DELETE
- Сжатие: `Accept-Encoding: gzip, deflate`
- Временная зона по умолчанию: Europe/Moscow
- Дата: `YYYY-MM-DD`, datetime: `YYYY-MM-DD HH:MM:SS`

## 3. Аутентификация (OAuth 2.0)

Реализованы три схемы:

### 3.1. Client Credentials Grant
Для работы со своим аккаунтом.

```
POST /api/v2/oauth2/token.json HTTP/1.1
Host: ads.vk.com
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}
```

Ответ:
```json
{
  "access_token": "...",
  "token_type": "bearer",
  "scope": "...",
  "expires_in": "86400",
  "refresh_token": "..."
}
```

### 3.2. Agency Client Credentials Grant (нестандартная)
Для агентств/менеджеров - создание токенов клиентов без их подтверждения.

```
POST /api/v2/oauth2/token.json HTTP/1.1
Content-Type: application/x-www-form-urlencoded

grant_type=agency_client_credentials
&client_id={client_id}
&client_secret={client_secret}
&agency_client_name={username}           # или agency_client_id={user_id}
&access_token={agency_access_token}      # если цепочка через токен агентства
```

`username` / `user_id` берутся из ответа `AgencyClients` или `ManagerClients`.

### 3.3. Authorization Code Grant
Для доступа к сторонним аккаунтам. Выдаётся по отдельному запросу.

Шаги:
1. Редирект пользователя:
   ```
   GET /hq/settings/access?action=oauth2
       &response_type=code
       &client_id={client_id}
       &state={csrf_token}
       &scope={scopes}
       &redirect_uri={redirect_uri}
   ```
2. После согласия VK перенаправляет на `redirect_uri?code=...&state=...&user_id=...`.
3. Проверка кода (опционально):
   ```
   POST /api/v2/oauth2/code_info.json
   code={code}&client_id=...&client_secret=...
   ```
4. Обмен кода на токен:
   ```
   POST /api/v2/oauth2/token.json
   grant_type=authorization_code&code={code}&client_id={client_id}
   ```

### 3.4. Подпись запросов

Все запросы к API подписываются:
```
Authorization: Bearer {access_token}
```

Токен одного аккаунта **нельзя** использовать для доступа к данным клиента агентства - нужен отдельный токен, полученный через Agency Client Credentials.

## 4. Scopes (права доступа)

Передаются списком через запятую в параметре `scope` при Authorization Code Grant.

Рекламодатель:
- `read_ads` - чтение статистики и РК
- `read_payments` - чтение транзакций и баланса
- `create_ads` - создание и редактирование РК, баннеров, аудиторий (ставки, статус, таргетинги)

Агентства и представительства:
- `create_clients` - создание клиентов
- `read_clients` - просмотр клиентов и операции от их имени
- `create_agency_payments` - переводы между счетами клиентов

Менеджеры:
- `read_manager_clients` - просмотр клиентов и операции от их имени
- `edit_manager_clients` - изменение параметров клиентов
- `read_payments` - чтение транзакций и баланса

VK Ads автоматически определяет тип аккаунта и отдаёт только подходящие права.

## 5. Ресурсы и методы (примеры)

- `GET /api/v2/ad_plans.json` - список кампаний
- `POST /api/v2/ad_plans.json` - создать кампанию
- `GET /api/v2/ad_plans/{id}.json` - одна кампания
- `/api/v2/remarketing/users_lists/{id}.json` - списки ремаркетинга (v2 и v3)
- `GET /api/v2/throttling.json` - текущие лимиты пользователя

Полный список - в разделе «Методы и ресурсы» документации: https://ads.vk.com/doc/api/

## 6. Общие параметры запроса

| Параметр | Формат | Default | Описание |
|---|---|---|---|
| `fields` | `field1,field2` | зависит от ресурса | Поля объекта верхнего уровня |
| `limit` | integer | 20 | Количество объектов, максимум 50 |
| `offset` | integer | 0 | Сдвиг по выдаче |
| `sorting` | `[-]field1,[-]field2` | - | Сортировка (`-` = DESC) |
| `_<field>=value` | - | - | Фильтр на равенство |
| `_<field>__<lookup>=value` | - | - | Фильтр с lookup'ом |

Field lookups: `ne`, `lt`, `lte`, `gt`, `gte`, `in`, и др. Нельзя фильтровать по полям вложенных объектов.

Примеры:
```
?fields=id,name
?_id__in=1,2,3
?_status__ne=active
?_updated__gt=2025-01-01 00:00:00
?sorting=id,-created&limit=50
```

## 7. Rate limiting

Лимиты действуют на трёх интервалах: секунда / час / день. Индивидуально на пользователя. Привязаны к календарным периодам.

В каждом ответе:
```
X-RateLimit-RPS-Limit / X-RateLimit-RPS-Remaining
X-RateLimit-Hourly-Limit / X-RateLimit-Hourly-Remaining
X-RateLimit-Daily-Limit / X-RateLimit-Daily-Remaining
```

Явный запрос текущих лимитов: `GET /api/v2/throttling.json` - вернёт лимиты и остатки отдельно по ресурсам × версиям × операциям (READ / CREATE).

Лимиты старых версий метода после релиза новой **постепенно уменьшаются** - закладывать миграцию на v3 по мере появления.

## 8. Типы данных

| Тип | JSON |
|---|---|
| String | `"value"` |
| Integer | `"123"` |
| Decimal | `"1.23"` |
| Boolean | `"true"` / `"false"` |
| None | `null` |
| Date | `"2013-08-18"` (YYYY-MM-DD) |
| Datetime | `"2013-08-28 16:49:34"` (Europe/Moscow) |
| List | `["v1", "v2"]` - однородные элементы |
| Object | `{"id": 1, "name": "N"}` |

## 9. Коды ошибок

| Код | Значение |
|---|---|
| 400 | Ошибка валидации тела запроса |
| 401 | Нет `access_token` или он неверный |
| 403 | Операция запрещена для этого аккаунта |
| 404 | Ресурс не найден |
| 405 | Метод не поддерживается ресурсом |
| 413 | Тело запроса слишком велико |
| 429 | Превышен rate limit |
| 500 | Серверная ошибка |

Тело ошибки - JSON (`application/json`) с деталями.

## 10. Документация (ссылки)

- Главная справка: https://ads.vk.com/help/features/help_api
- Устройство API: https://ads.vk.com/doc/api/info/Устройство%20API
- Авторизация: https://ads.vk.com/doc/api/info/Авторизация%20в%20API
- Методы и ресурсы: https://ads.vk.com/doc/api/

## 11. Практика для KUBRIK

- Хранить `client_id` / `client_secret` / `refresh_token` в `~/.config/maxos/vk-ads-*.env` (по аналогии с amoCRM).
- Для клиентских кабинетов, которые ведёт агентство, использовать Agency Client Credentials - не плодить отдельные регистрации.
- Перед интеграцией проверять `GET /api/v2/throttling.json` - лимиты по ремаркетинг-спискам жёсткие (1 создание в минуту на v2).
- Для отчётности использовать статистические ресурсы через v2, но готовиться к миграции на v3 (лимиты v2 будут ужиматься).
- Все времена в ответах - Europe/Moscow, учитывать при сверке с Метрикой/GA.
