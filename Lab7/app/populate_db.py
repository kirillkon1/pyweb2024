# app/populate_db.py

from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine

# Создаём все таблицы перед заполнением
models.Base.metadata.create_all(bind=engine)

# Определяем термины для заполнения
terms = [
    {
        "keyword": "Микросервис",
        "description": "Архитектурный стиль, при котором приложение строится как набор небольших, независимых сервисов, взаимодействующих через четко определенные API."
    },
    {
        "keyword": "Kotlin",
        "description": "Современный статически типизированный язык программирования, работающий на JVM и полностью совместимый с Java."
    },
    {
        "keyword": "Service Discovery",
        "description": "Механизм, позволяющий сервисам находить друг друга в динамически масштабируемой системе."
    },
    {
        "keyword": "API Gateway",
        "description": "Компонент, который выступает единой точкой входа для всех клиентов, маршрутизируя запросы к соответствующим микросервисам."
    },
    {
        "keyword": "Контейнеризация",
        "description": "Технология упаковки приложения и его зависимостей в изолированные контейнеры для обеспечения переносимости и консистентности среды выполнения."
    },
    {
        "keyword": "Docker",
        "description": "Платформа для разработки, доставки и запуска приложений в контейнерах."
    },
    {
        "keyword": "Orchestration",
        "description": "Процесс управления, координации и автоматизации развертывания, масштабирования и управления контейнеризованными приложениями."
    },
    {
        "keyword": "Kubernetes",
        "description": "Система оркестрации контейнеров с открытым исходным кодом для автоматизации развертывания, масштабирования и управления контейнеризованными приложениями."
    },
    {
        "keyword": "Circuit Breaker",
        "description": "Шаблон проектирования, предназначенный для предотвращения каскадных отказов в распределенных системах."
    },
    {
        "keyword": "Continuous Integration",
        "description": "Практика частой интеграции кода в общий репозиторий с автоматическим тестированием для обнаружения ошибок на ранних стадиях."
    }
]

def populate():
    db: Session = SessionLocal()
    try:
        existing_terms = db.query(models.Term).count()
        if existing_terms == 0:
            for term_data in terms:
                term = models.Term(**term_data)
                db.add(term)
            db.commit()
            print("База данных успешно заполнена начальными терминами.")
        else:
            print("База данных уже содержит данные. Пропуск заполнения.")
    except Exception as e:
        db.rollback()
        print(f"Ошибка при заполнении базы данных: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    populate()
