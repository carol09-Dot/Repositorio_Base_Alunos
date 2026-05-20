import pyautogui as pg


pg. press("win")

pg. sleep(1)

pg.write("chrome", interval=0.4)

pg.press("enter")

pg.write("youtube.com")
pg.press("enter")

pg.sleep(2)

pg.moveTo(799, 167, duration=0.5)
pg.click()

pg.write("overture, Phantom of the opera", interval= 0.5)
pg.sleep(2)
pg.press("enter")

pg.moveTo(701, 669)
pg.sleep(2)
pg.click()