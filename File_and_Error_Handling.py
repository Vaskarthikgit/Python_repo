import logging as log

log.basicConfig(level=log.DEBUG, 
                format="%(asctime)s - %(levelname)-8s - %(message)s",
                filename="test.log")
log.debug("Debug started for developer")

log.info("File read started")
with open("Sample.txt","r+") as fh:
    fh.write("Hello world11sss\n")
    #print(fh.read())
log.info("File read ended")

try:
    def divide():
        num = 10
        log.warning("Divide value is zero")
        log.error(f"{num} can't divide by zero")
        return num/0
    
    print(divide())
except ZeroDivisionError as e:
    print("You can't divide by zero")
except Exception as e:
    print(e)
else:
    print("No exception occurred")
finally:
    print("Code is executed")