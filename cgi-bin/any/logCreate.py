import logging

logging.basicConfig(filename='logfile\logCreate.log',level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')
print("============================================================================")
print("==================== = = = ==  S u c c e s s  == = = = =====================")
print("============================================================================")

