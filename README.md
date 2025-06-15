# Chat Wall — Контейнеризиран full-stack проект с Docker Compose

## Описание

Проектът **Chat Wall** е примерен full-stack уеб проект, който демонстрира работа с няколко свързани услуги чрез Docker Compose. Приложението позволява на потребителя да въвежда съобщения през уеб интерфейс, които се записват в база данни и се визуализират в таблица в реално време.

---

## Структура на проекта

```
chat_wall_project/
├── backend/
│   ├── app.py                 # Flask API
│   ├── requirements.txt       # Python зависимости
│   ├── Dockerfile             # Контейнеризация на backend
│   └── init.sql               # Инициализиране на таблицата
├── frontend/
│   ├── index.html             # Основен HTML интерфейс
│   ├── script.js              # JS логика за fetch и рендиране
│   └── Dockerfile             # Контейнеризация на frontend
├── docker-compose.yml         # Docker Compose конфигурация
└── README.md                  # Документация
```

---

## Как се изграждат и стартират контейнерите

### Изисквания:
- Docker
- Docker Compose

### Стартиране на проекта:

```bash
docker compose up --build
```

Това ще изгради образите и стартира следните услуги:
- `backend` – Flask API, слуша на порт `5000`
- `frontend` – уеб интерфейс, достъпен на порт `8080`
- `db` – PostgreSQL база данни с таблица `messages`

---

## Достъп до услугите

| Компонент | URL |
|-----------|-----|
| Frontend  | http://localhost:8080 |
| API       | http://localhost:5000/api/messages |

---

## Как работи всеки от компонентите

### Frontend:
HTML + JavaScript интерфейс, който позволява на потребителя да въведе съобщение и да го изпрати чрез HTTP POST заявка до backend-а. Използва `fetch()` за комуникация.

### Backend:
Flask API, който приема POST заявки със съобщения и ги записва в базата данни. При GET заявка връща всички записани съобщения като JSON.

### Database:
PostgreSQL контейнер, който съхранява съобщенията в таблица `messages`. Таблицата се създава автоматично чрез SQL скрипт при първо стартиране.

---

## Комуникация между услугите

- `frontend` → комуникира с `backend` през HTTP (`http://backend:5000`)
- `backend` → комуникира с `db` чрез `psycopg2`, използвайки host `db`
- Docker Compose създава изолирана мрежа и осигурява достъп между контейнерите по имена на услугите

---

## Публикувани Docker образи

Образите са качени в Docker Hub и са публично достъпни:

- **Backend:** https://hub.docker.com/r/shwetli/backend
- **Frontend:** https://hub.docker.com/r/shwetli/frontend
