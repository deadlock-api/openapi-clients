from enum import Enum


class Language(str, Enum):
    BRAZILIAN = "brazilian"
    BULGARIAN = "bulgarian"
    CZECH = "czech"
    DANISH = "danish"
    DUTCH = "dutch"
    ENGLISH = "english"
    FINNISH = "finnish"
    FRENCH = "french"
    GERMAN = "german"
    GREEK = "greek"
    HUNGARIAN = "hungarian"
    INDONESIAN = "indonesian"
    ITALIAN = "italian"
    JAPANESE = "japanese"
    KOREANA = "koreana"
    LATAM = "latam"
    NORWEGIAN = "norwegian"
    POLISH = "polish"
    PORTUGUESE = "portuguese"
    ROMANIAN = "romanian"
    RUSSIAN = "russian"
    SCHINESE = "schinese"
    SPANISH = "spanish"
    SWEDISH = "swedish"
    TCHINESE = "tchinese"
    THAI = "thai"
    TURKISH = "turkish"
    UKRAINIAN = "ukrainian"
    VIETNAMESE = "vietnamese"

    def __str__(self) -> str:
        return str(self.value)
