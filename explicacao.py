from abc import ABC
from abc import abstractmethod

# ----- CONTRATO

class TodoListDataSource(ABC):
    ## Classe de contrato para a fonte de dados de lista de tarefas
    @abstractmethod
    def get_todo_list(self, user_id: str) -> list:
        pass

class TodoListRepository(ABC):
    ## Classe de contrato para a fonte de dados de lista de tarefas
    @abstractmethod
    def get_todo_list(self, user_id: str) -> list:
        pass

# ----- CONCRETE IMPLEMENTATIONS -----

class TodoListMySQLDataSource(TodoListDataSource):
    def __init__(self, connection_mysql):
        self.connection = connection_mysql

    ## Classe de implementacao para a fonte de dados de lista de tarefas pelo MySQL
    def get_todo_list(self, user_id: str) -> list:
        # Simulate a MySQL database call
        return [
            {"id": 1, "task": "Buy groceries", "user_id": user_id},
            {"id": 2, "task": "Walk the dog", "user_id": user_id},
        ]


class TodoListPostgreSQLDataSource(TodoListDataSource):
    def __init__(self, connection_postgresql):
        self.connection = connection_postgresql

    ## Classe de implementacao para a fonte de dados de lista de tarefas pelo PostGreSQL
    def get_todo_list(self, user_id: str) -> list:
        # Simulate a PostgreSQL database call
        return [
            {"id": 1, "task": "Read a book", "user_id": user_id},
            {"id": 2, "task": "Go to the gym", "user_id": user_id},
        ]


class TodoListRepositoryImpl(TodoListRepository):
    def __init__(self, data_source: TodoListDataSource):
        self._data_source = data_source

    def get_todo_list(self, user_id: str) -> list:
        self._data_source.get_todo_list(user_id)


class TodoListUseCase:
    def __init__(self, data_repository: TodoListRepository):
        self._data_repository = data_repository


    def execute(self, user_id: str) -> list:
        self._data_repository.get_todo_list(user_id)

# ----- Exemplo DE USO -----

class TodoListService:

    def get_user_todo_list(self, user_id: str) -> list:
        datasource = TodoListPostgreSQLDataSource()
        repository = TodoListRepositoryImpl(datasource)
        
        list_todo = TodoListUseCase(repository).execute(user_id)