import colorama
from colorama import Fore
from colorama import init
init(autoreset=True)
print(Fore.BLUE + "Инициализация")
print(Fore.LIGHTBLUE_EX + "Приложения должны инициализировать Colorama с помощью:")
print(Fore.GREEN + "from colorama import init\ninit()")
print(Fore.LIGHTBLUE_EX + "В Windows вызов init() отфильтрует управляющие ANSI-последовательности из любого текста, отправленного в stdout или stderr, и заменит их на эквивалентные вызовы Win32.\nНа других платформах вызов init() не имеет никакого эффекта (если только вы не укажете другие дополнительные возможности; \nсм. раздел «Аргументы Init», ниже). По задумке разработчиков такое поведение позволяет приложениям вызывать init() безоговорочно на всех платформах, после чего вывод ANSI должен просто работать. \nЧтобы прекратить использование Colorama до выхода из программы, просто вызовите deinit(). \nДанный метод вернет stdout и stderr к их исходным значениям, так что Colorama будет отключена. Чтобы возобновить ее работу, используйте reinit(); \nэто выгоднее, чем повторный вызов init() (но делает то же самое).")
print(Fore.BLUE + "Цветной вывод")
print(Fore.LIGHTBLUE_EX + "Кроссплатформенное отображение цветного текста может быть упрощено за счет использования константных обозначений для управляющих последовательностей ANSI, предоставляемых библиотекой Colorama:")
print(Fore.GREEN + "from colorama import init\ninit()\nfrom colorama import Fore, Back, Style\nprint(Fore.GREEN + 'зеленый текст')\nprint(Back.YELLOW + 'на желтом фоне')\nprint(Style.BRIGHT + 'стал ярче' + Style.RESET_ALL)\nprint('обычный текст')")
from colorama import init
init()
from colorama import Fore, Back, Style
print(Fore.GREEN + 'зеленый текст')
print(Back.YELLOW + 'на желтом фоне')
print(Style.BRIGHT + 'стал ярче' + Style.RESET_ALL)
print('обычный текст')
print(Fore.LIGHTBLUE_EX +"При этом вы также можете использовать ANSI-последовательности напрямую в своем коде:")
print(Fore.GREEN + "print('\\033[31m' + 'красный текст')\nprint('\\033[39m')")
print('\033[31m' + 'красный текст')
print('\033[39m')  # сброс к цвету по умолчанию
print(Fore.LIGHTBLUE_EX +"Еще одним вариантом является применение Colorama в сочетании с существующими ANSI библиотеками, такими как Termcolor или Blessings. \nТакой подход настоятельно рекомендуется для чего-то большего, чем тривиальное выделение текста:")
print(Fore.GREEN + "from colorama import init\nfrom termcolor import colored\n# используйте Colorama, чтобы Termcolor работал и в Windows\ninit()\n# теперь вы можете применять Termcolor для вывода\n# вашего цветного текста\nprint(colored('Termcolor and Colorama!', 'red', 'on_yellow'))")
print(Fore.LIGHTBLUE_EX +"init() принимает некоторые **kwargs для переопределения поведения по умолчанию. \nЕсли вы постоянно осуществляете сброс указанных вами цветовых настроек после каждого вывода, init(autoreset=True) будет выполнять это по умолчанию:")
print(Fore.GREEN + "from colorama import init, Fore\ninit(autoreset=True)\nprint(Fore.GREEN + 'зеленый текст')\nprint('автоматический возврат к обычному')")
print(Fore.LIGHTBLUE_EX + "init(strip=None): \nПередайте True или False, чтобы определить, должны ли коды ANSI удаляться при выводе. \nПоведение по умолчанию — удаление, если программа запущена на Windows или если вывод перенаправляется (не на tty). \ninit(convert=None): \nПередайте True или False, чтобы определить, следует ли преобразовывать ANSI-коды в выводе в вызовы win32. \nПо умолчанию Colorama будет их конвертировать, если вы работаете под Windows и вывод осуществляется на tty (терминал).\ninit(wrap=True): \nВ Windows Colorama заменяет sys.stdout и sys.stderr прокси-объектами, которые переопределяют метод .write() для выполнения своей работы. \nЕсли эта обертка вызывает у вас проблемы, то ее можно отключить, передав init(wrap=False). \nПоведение по умолчанию — обертывание, если autoreset, strip или convert равны True.\nКогда обертка отключена, цветной вывод на платформах, отличных от Windows, будет продолжать работать как обычно. \nДля кроссплатформенного цветного отображения текста можно использовать AnsiToWin32 прокси, предоставляемый Colorama, напрямую:")
print(Fore.GREEN + "import sys\nfrom colorama import init, Fore, AnsiToWin32(wrap=False)\nstream = AnsiToWin32(sys.stderr).stream\n# Python 2\nprint >>stream, Fore.RED + 'красный текст отправлен в stderr'\n# Python 3\nprint(Fore.RED + 'красный текст отправлен в stderr', file=stream)")
