from apscheduler.schedulers.background import BackgroundScheduler
from sample_function import message_print, job_print

if __name__ == "__main__" : 
    scheduler = BackgroundScheduler()
    scheduler.add_job(message_print, trigger='interval', seconds=2, coalesce=True, max_instances=1) # message_print 와 second 를 바꿔서 쓰면 될듯.
    scheduler.add_job(job_print, trigger='interval', seconds=2, coalesce=True, max_instances=1)
    
    scheduler.start()

    # 무한루프(응답 지속 기다림)
    while True:
        pass