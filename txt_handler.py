# Класс для работы с текстовыми файлами
class TxtFileHandler:


# Прочитать файл
    def read_file(self, filepath: str) -> str:
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                return file.read()
        except (FileNotFoundError, PermissionError):
            return ""


# Записать данные в файл
    def write_file(self, filepath: str, *data: str) -> None:
        try:
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(" ".join(data))
        except (PermissionError, IsADirectoryError) as e:
            print(f"Ошибка записи: {e}")
    

# Добавить данные в файл
    def append_file(self, filepath: str, *data: str) -> None:
        try:
            with open(filepath, "a", encoding="utf-8") as file:
                file.write(" ".join(data) + "\n")
        except (PermissionError, IsADirectoryError) as e:
            print(f"Ошибка добавления: {e}")


# Тест
if __name__ == "__main__":
    handler = TxtFileHandler()
    
    # Тест записи
    handler.write_file("test.txt", "Первая строка", "Вторая строка")
    
    # Тест добавления
    handler.append_file("test.txt", " Третья строка")
    
    # Тест чтения
    content = handler.read_file("test.txt")
    print("Содержимое файла:", content)
    
    # Тест ошибки (чтение несуществующего файла)
    print("Чтение несуществующего файла:", handler.read_file("missing.txt"))