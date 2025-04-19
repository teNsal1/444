class TxtHandler:
    def read_file(self, filepath: str) -> str:
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                return file.read()
        except (FileNotFoundError, PermissionError):
            return ""