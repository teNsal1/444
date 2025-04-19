class TxtHandler:
    def read_file(self, filepath: str) -> str:
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                return file.read()
        except (FileNotFoundError, PermissionError):
            return ""

    def write_file(self, filepath: str, *data: str) -> None:
        try:
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(" ".join(data))
        except (PermissionError, IsADirectoryError) as e:
            print(f"Ошибка записи: {e}")
    
    def append_file(self, filepath: str, *data: str) -> None:
        try:
            with open(filepath, "a", encoding="utf-8") as file:
                file.write(" ".join(data) + "\n")
        except (PermissionError, IsADirectoryError) as e:
            print(f"Ошибка добавления: {e}")