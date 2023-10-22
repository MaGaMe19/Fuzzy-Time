from time import sleep;
from datetime import datetime, date;
import os

# Text
HOURS = {
    0: [
        "                                             ",
        " _____ _ _   _                       _   _   ",
        "|     |_| |_| |_ ___ ___ ___ ___ ___| |_| |_ ",
        "| | | | |  _|  _| -_|  _|   | .'|  _|   |  _|",
        "|_|_|_|_|_| |_| |___|_| |_|_|__,|___|_|_|_|  ",
        "                                             "

    ],
    1: [
        "             ",
        " _____ _     ",
        "|   __|_|___ ",
        "|   __| |_ -|",
        "|_____|_|___|",
        "             "

    ],
    2: [
        "             _ _   ",
        " _____      |_|_|_ ",
        "|__   |_ _ _ ___|_|",
        "|   __| | | | . | |",
        "|_____|_____|___|_|",
        "                   "

    ],
    3: [
        "           _ _ ",
        " ____     |_|_|",
        "|    \\ ___ _ _ ",
        "|  |  |  _| | |",
        "|____/|_| |___|",
        "               "

    ],
    4: [
        "                   ",
        " _____ _         _ ",
        "|  |  |_|___ ___|_|",
        "|  |  | | -_|  _| |",
        " \\___/|_|___|_| |_|",
        "                   "

    ],
    5: [
        "       _ _       ",
        " _____|_|_|___ _ ",
        "|   __|_ _|  _|_|",
        "|   __| | |  _| |",
        "|__|  |___|_| |_|",
        "                 "

    ],
    6: [
        "       _ _               ",
        " _____|_|_|    _       _ ",
        "|   __|___ ___| |_ ___|_|",
        "|__   | .'|  _|   |_ -| |",
        "|_____|__,|___|_|_|___|_|",
        "                         "

    ],
    7: [
        "                   ",
        " _____ _ _       _ ",
        "|   __|_| |_ ___|_|",
        "|__   | | . |   | |",
        "|_____|_|___|_|_|_|",
        "                   "

    ],
    8: [
        "                     ",
        " _____     _   _   _ ",
        "|  _  |___| |_| |_|_|",
        "|     |  _|   |  _| |",
        "|__|__|___|_|_|_| |_|",
        "                     "

    ],
    9: [
        "       _ _       ",
        " _____|_|_|    _ ",
        "|   | |_ _ ___|_|",
        "| | | | | |   | |",
        "|_|___|___|_|_|_|",
        "                 "

    ],
    10: [
        "       _ _           ",
        " _____|_|_|_       _ ",
        "|__   |___| |_ ___|_|",
        "|   __| .'|   |   | |",
        "|_____|__,|_|_|_|_|_|",
        "                     "

    ],
    11: [
        "                 ",
        " _____     ___ _ ",
        "|   __|_ _|  _|_|",
        "|   __| | |  _| |",
        "|_____|___|_| |_|",
        "                 "
    ],
    12: [
        "                         ",
        " _____ _ _   _           ",
        "|     |_| |_| |_ ___ ___ ",
        "| | | | |  _|  _| .'| . |",
        "|_|_|_|_|_| |_| |__,|_  |",
        "                    |___|"

    ],
    13: [
        "             ",
        " _____ _     ",
        "|   __|_|___ ",
        "|   __| |_ -|",
        "|_____|_|___|",
        "             "

    ],
    14: [
        "             _ _   ",
        " _____      |_|_|_ ",
        "|__   |_ _ _ ___|_|",
        "|   __| | | | . | |",
        "|_____|_____|___|_|",
        "                   "

    ],
    15: [
        "           _ _ ",
        " ____     |_|_|",
        "|    \\ ___ _ _ ",
        "|  |  |  _| | |",
        "|____/|_| |___|",
        "               "

    ],
    16: [
        "                   ",
        " _____ _         _ ",
        "|  |  |_|___ ___|_|",
        "|  |  | | -_|  _| |",
        " \\___/|_|___|_| |_|",
        "                   "

    ],
    17: [
        "       _ _       ",
        " _____|_|_|___ _ ",
        "|   __|_ _|  _|_|",
        "|   __| | |  _| |",
        "|__|  |___|_| |_|",
        "                 "

    ],
    18: [
        "       _ _               ",
        " _____|_|_|    _       _ ",
        "|   __|___ ___| |_ ___|_|",
        "|__   | .'|  _|   |_ -| |",
        "|_____|__,|___|_|_|___|_|",
        "                         "

    ],
    19: [
        "                   ",
        " _____ _ _       _ ",
        "|   __|_| |_ ___|_|",
        "|__   | | . |   | |",
        "|_____|_|___|_|_|_|",
        "                   "

    ],
    20: [
        "                     ",
        " _____     _   _   _ ",
        "|  _  |___| |_| |_|_|",
        "|     |  _|   |  _| |",
        "|__|__|___|_|_|_| |_|",
        "                     "

    ],
    21: [
        "       _ _       ",
        " _____|_|_|    _ ",
        "|   | |_ _ ___|_|",
        "| | | | | |   | |",
        "|_|___|___|_|_|_|",
        "                 "

    ],
    22: [
        "       _ _           ",
        " _____|_|_|_       _ ",
        "|__   |___| |_ ___|_|",
        "|   __| .'|   |   | |",
        "|_____|__,|_|_|_|_|_|",
        "                     "

    ],
    23: [
        "                 ",
        " _____     ___ _ ",
        "|   __|_ _|  _|_|",
        "|   __| | |  _| |",
        "|_____|___|_| |_|",
        "                 "
    ],
    24: [
        "                                             ",
        " _____ _ _   _                       _   _   ",
        "|     |_| |_| |_ ___ ___ ___ ___ ___| |_| |_ ",
        "| | | | |  _|  _| -_|  _|   | .'|  _|   |  _|",
        "|_|_|_|_|_| |_| |___|_| |_|_|__,|___|_|_|_|  ",
        "                                             "
    ]
}

MINUTES = {
    0: [
        "",
        "",
        "",
        "",
        "",
        ""
    ],
    5: [
        "       _ _                  ",
        " _____|_|_|___        _     ",
        "|   __|_ _|  _|   ___| |_   ",
        "|   __| | |  _|  | .'| . |  ",
        "|__|  |___|_|    |__,|___|  ",
        "                            "

    ],
    10: [
        "       _ _                  ",
        " _____|_|_|_          _     ",
        "|__   |___| |_    ___| |_   ",
        "|   __| .'|   |  | .'| . |  ",
        "|_____|__,|_|_|  |__,|___|  ",
        "                            "

    ],
    15: [
        "                                      ",
        " _____ _         _              _     ",
        "|  |  |_|___ ___| |_ _ _    ___| |_   ",
        "|  |  | | -_|  _|  _| | |  | .'| . |  ",
        " \\___/|_|___|_| |_| |___|  |__,|___|  ",
        "                                       "

    ],
    20: [
        "             _ _                          ",
        " _____      |_|_|                   _     ",
        "|__   |_ _ _ ___ ___ ___ ___    ___| |_   ",
        "|   __| | | | .'|   |- _| . |  | .'| . |  ",
        "|_____|_____|__,|_|_|___|_  |  |__,|___|  ",
        "                        |___|             "

    ],
    25: [
        "       _ _                                           ",
        " _____|_|_|___                   _           _   _   ",
        "|   __|_ _|  _|   _ _ ___ ___   | |_ ___ _ _| |_|_|  ",
        "|   __| | |  _|  | | | . |  _|  |   | .'| | | . | |  ",
        "|__|  |___|_|     \\_/|___|_|    |_|_|__,|___|___|_|  ",
        "                                                     "

    ],
    30: [
        "                       ",
        " _____         _   _   ",
        "|  |  |___ _ _| |_|_|  ",
        "|     | .'| | | . | |  ",
        "|__|__|__,|___|___|_|  ",
        "                       "

    ],
    35: [
        "       _ _                                       ",
        " _____|_|_|___        _      _           _   _   ",
        "|   __|_ _|  _|   ___| |_   | |_ ___ _ _| |_|_|  ",
        "|   __| | |  _|  | .'| . |  |   | .'| | | . | |  ",
        "|__|  |___|_|    |__,|___|  |_|_|__,|___|___|_|  ",
        "                                                 "

    ],
    40: [
        "             _ _                              ",
        " _____      |_|_|                             ",
        "|__   |_ _ _ ___ ___ ___ ___    _ _ ___ ___   ",
        "|   __| | | | .'|   |- _| . |  | | | . |  _|  ",
        "|_____|_____|__,|_|_|___|_  |   \\_/|___|_|    ",
        "                        |___|                 "

    ],
    45: [
        "                                          ",
        " _____ _         _                        ",
        "|  |  |_|___ ___| |_ _ _    _ _ ___ ___   ",
        "|  |  | | -_|  _|  _| | |  | | | . |  _|  ",
        " \\___/|_|___|_| |_| |___|   \\_/|___|_|    ",
        "                                          "

    ],
    50: [
        "       _ _                      ",
        " _____|_|_|_                    ",
        "|__   |___| |_    _ _ ___ ___   ",
        "|   __| .'|   |  | | | . |  _|  ",
        "|_____|__,|_|_|   \\_/|___|_|    ",
        "                                "

    ],
    55: [
        "       _ _                      ",
        " _____|_|_|___                  ",
        "|   __|_ _|  _|   _ _ ___ ___   ",
        "|   __| | |  _|  | | | . |  _|  ",
        "|__|  |___|_|     \\_/|___|_|    ",
        "                                "

    ],
    60: [
        "",
        "",
        "",
        "",
        "",
        ""

    ]
}

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def getFuzzyTime(time: datetime, oldTime: str) -> str:
    currentHour = time.hour
    # round minutes to nearest multiple of 5 with multiple * round(number / multiple)
    currentMinute = 5 * round(time.minute / 5)

    if currentMinute > 20:
        currentHour += 1 # bärndütsch logic

    fuzzyTime = """"""
    for i in range(6):
        fuzzyTime += f"    {MINUTES[currentMinute][i]}{HOURS[currentHour][i]}\n"
    
    return fuzzyTime if oldTime != fuzzyTime else "SAME"            

if __name__ == "__main__":
    previousTime = ""
    while (True):
        fuzzyTime = getFuzzyTime(datetime.now(), previousTime)

        if fuzzyTime != "SAME":
            cls()
            previousTime = fuzzyTime

            print("\n    Es isch öbbe\n")
            print(fuzzyTime)
            print(f"\n    am {date.today().strftime('%d.%m.%y')}.")

        sleep(5)
