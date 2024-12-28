import enum
from sys_module import SystemModule
from typing import Callable

@enum.unique
class KeyCode(enum.Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    AR_RIGHT = 5
    AR_LEFT = 6

class Input(SystemModule):

    def __init__(self):
        self.IsRight: bool = False
        self.IsLeft: bool = False
        self.IsUp: bool = False
        self.IsDown: bool = False
        self.IsArRight: bool = False
        self.IsArLeft: bool = False
        self._subscribers: list[Callable[[KeyCode], None]] = []

    def reset(self):
        self.IsRight: bool = False
        self.IsLeft: bool = False
        self.IsUp: bool = False
        self.IsDown: bool = False
        self.IsArRight: bool = False
        self.IsArLeft: bool = False

    def key_down(self, key_code: KeyCode) -> None :
        if isinstance(key_code, KeyCode):
            if key_code == KeyCode.UP: self.IsUp = True
            elif key_code == KeyCode.DOWN: self.IsDown = True
            elif key_code == KeyCode.RIGHT: self.IsRight = True
            elif key_code == KeyCode.LEFT: self.IsLeft = True
            elif key_code == KeyCode.AR_RIGHT: self.IsArRight = True
            elif key_code == KeyCode.AR_LEFT:self.IsArLeft = True

    def key_up(self, key_code: KeyCode) -> None :
        if isinstance(key_code, KeyCode):
            if key_code == KeyCode.UP: self.IsUp = False
            elif key_code == KeyCode.DOWN: self.IsDown = False
            elif key_code == KeyCode.RIGHT: self.IsRight = False
            elif key_code == KeyCode.LEFT: self.IsLeft = False
            elif key_code == KeyCode.AR_RIGHT: self.IsArRight = False
            elif key_code == KeyCode.AR_LEFT:self.IsArLeft = False

    def update(self):
        if self.IsRight: self._notyfy_subs(KeyCode.RIGHT)
        if self.IsLeft: self._notyfy_subs(KeyCode.LEFT)
        if self.IsUp: self._notyfy_subs(KeyCode.UP)
        if self.IsDown: self._notyfy_subs(KeyCode.DOWN)
        if self.IsArRight: self._notyfy_subs(KeyCode.AR_RIGHT)
        if self.IsArLeft: self._notyfy_subs(KeyCode.AR_LEFT)

    def subscribe(self, handler: Callable[[KeyCode], None]) -> None:
        """Подписывает метод или функцию на события нажатия клавиш."""
        self._subscribers.append(handler)

    def _notyfy_subs(self, key_code: KeyCode) -> None:
        for sub in self._subscribers:
            sub(key_code)

    def _notyfy_subs(self, key_code: KeyCode) -> None:
        for sub in self._subscribers:
            sub(key_code)