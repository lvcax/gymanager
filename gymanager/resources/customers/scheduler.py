import atexit

from apscheduler.schedulers.background import BackgroundScheduler


def print_date_time():
    print("compre um relógio pra saber a hora")

def customer_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=print_date_time, trigger="interval", seconds=2)
    scheduler.start()

    atexit.register(lambda: scheduler.shutdown())
