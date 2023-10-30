import logging

formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")

handler1 = logging.StreamHandler()
handler1.setLevel(logging.DEBUG)
handler1.setFormatter(formatter)

handler2 = logging.FileHandler(filename="../Log/test.log")
handler2.setLevel(logging.DEBUG)
handler2.setFormatter(formatter)

logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler1)
logger.addHandler(handler2)
