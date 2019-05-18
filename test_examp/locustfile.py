import locust



class UsersTest(locust.TaskSet): #Активный класс, описание задач которыми будем нагружить

    # @locust.task - Задачи выполняются одновременно
    # @locust.seq_task() - Задачи выполняются последовательно


    @locust.seq_task(1)
    def api_get_task(self): # Задача
        self.client.get("/api", name="GET /api") # Самое действие

    @locust.seq_task(2)
    def api_post_task(self): # Задача
        payload = {"username": "user1", "password": "123456"} # Данные для нагрузки
        self.client.post("/api", data=payload, name="POST /api") # Самое действие с нагрузкой

class SituationTest(locust.HttpLocust): # Этот класс описывает условия применения класса с описанием задач (UsersTest)

    task_set = UsersTest # Указатьель на класс с тасками
    min_wait = 1000 # Минимальная пауза между сессиями
    max_wait = 2000 # Максимальная пауза между сессиями
    host = "http://127.0.0.1:3000" # Куда будем применять


"""
MBP-anton:interview anton$ ls
README.md       test_examp            Solutions_P1_P2
MBP-anton:interview anton$ cd test_examp/
MBP-anton:test_examp anton$ ls
__init__.py     __pycache__     fl_server.py    locustfile.py   selen_tests.py  templates       test_unit.py
MBP-anton:test_examp anton$ locust -f locustfile.py
http://127.0.0.1:8089/
"""
