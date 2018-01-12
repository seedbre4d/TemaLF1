# imports
import mraa
import time
import datetime
import threading

# consts definition
CONST_LIN = "-"
CONST_TIME = 0.4

# led class definition
class Led:
    bot_right = mraa.Gpio(1)
    bot_right.dir(mraa.DIR_OUT)

    top_right = mraa.Gpio(2)
    top_right.dir(mraa.DIR_OUT)

    bot = mraa.Gpio(3)
    bot.dir(mraa.DIR_OUT)

    mid = mraa.Gpio(4)
    mid.dir(mraa.DIR_OUT)

    top = mraa.Gpio(5)
    top.dir(mraa.DIR_OUT)

    top_left = mraa.Gpio(6)
    top_left.dir(mraa.DIR_OUT)

    bot_left = mraa.Gpio(7)
    bot_left.dir(mraa.DIR_OUT)

# table class definition
class Table:
    def __init__(self):
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            self.write_time()

    def __write_one(self):
        Led.top_right.write(1)
        Led.bot_right.write(1)

    def __write_two(self):
        Led.top.write(1)
        Led.top_right.write(1)
        Led.mid.write(1)
        Led.bot_left.write(1)
        Led.bot.write(1)

    def __write_three(self):
        Led.top.write(1)
        Led.top_right.write(1)
        Led.mid.write(1)
        Led.bot_right.write(1)
        Led.bot.write(1)

    def __write_four(self):
        Led.top_left.write(1)
        Led.mid.write(1)
        Led.bot_right.write(1)
        Led.top_right.write(1)

    def __write_five(self):
        Led.top_left.write(1)
        Led.top.write(1)
        Led.mid.write(1)
        Led.bot_right.write(1)
        Led.bot.write(1)
        
    def __write_six(self):
        Led.top_left.write(1)
        Led.top.write(1)
        Led.mid.write(1)
        Led.bot_right.write(1)
        Led.bot.write(1)
        Led.bot_left.write(1)

    def __write_seven(self):
        Led.top_right.write(1)
        Led.bot_right.write(1)
        Led.top.write(1)

    def __write_eight(self):
        Led.top.write(1)
        Led.top_right.write(1)
        Led.top_left.write(1)
        Led.mid.write(1)
        Led.bot_left.write(1)
        Led.bot_right.write(1)
        Led.bot.write(1)

    def __write_nine(self):
        Led.top.write(1)
        Led.top_right.write(1)
        Led.top_left.write(1)
        Led.mid.write(1)
        Led.bot_right.write(1)
        Led.bot.write(1)

    def __write_zero(self):
        Led.top.write(1)
        Led.top_right.write(1)
        Led.top_left.write(1)
        Led.bot_left.write(1)
        Led.bot_right.write(1)
        Led.bot.write(1)
        
    def __write_line(self):
        Led.mid.write(1)

    def clear(self):
        print "Clearing table."
        Led.top.write(0)
        Led.top_right.write(0)
        Led.top_left.write(0)
        Led.mid.write(0)
        Led.bot_left.write(0)
        Led.bot_right.write(0)
        Led.bot.write(0)

    def write_item(self, item):
        print "Writing {} on table.".format(item)
        if item == 0:
            self.__write_zero()
        elif item == 1:
            self.__write_one()
        elif item == 2:
            self.__write_two()
        elif item == 3:
            self.__write_three()
        elif item == 4:
            self.__write_four()
        elif item == 5:
            self.__write_five()
        elif item == 6:
            self.__write_six()
        elif item == 7:
            self.__write_seven()
        elif item == 8:
            self.__write_eight()
        elif item == 9:
            self.__write_nine()
        elif item == CONST_LIN:
            self.__write_line()

    def write_time(self):
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute

        hour_split = [int(i) for i in str(hour)]
        minute_split = [int(i) for i in str(minute)]

        time.sleep(CONST_TIME)
        self.clear()

        for number in hour_split:
            if len(hour_split) == 1:
                self.write_item(0)
                time.sleep(CONST_TIME + CONST_TIME / 2)
                self.clear()
            
            self.write_item(number)
            time.sleep(CONST_TIME + CONST_TIME / 2)
            self.clear()
        
        self.write_item(CONST_LIN)
        time.sleep(CONST_TIME)
        self.clear()
        
        for number in minute_split:
            if len(minute_split) == 1:
                self.write_item(0)
                time.sleep(CONST_TIME + CONST_TIME / 2)
                self.clear()
            
            self.write_item(number)
            time.sleep(CONST_TIME + CONST_TIME / 2)
            self.clear()
            
        time.sleep(CONST_TIME)
        self.clear()
        

def main():
    try:
        table = Table()
        print "-> Printing now time on table. Press any key and <enter> to exit."
        raw_input()
        print "-> Stopped printing time on table. Clearing table..."
        table.clear()
        print "-> Table cleared. Exiting..."
    except Exception:
        pass



if __name__ == '__main__':  
    main()
    