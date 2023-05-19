# # Python实用宝典
# # 2019/12/29
#
# import sys
# import time
# import logging
# from watchdog.observers import Observer
# from watchdog.events import LoggingEventHandler
# from pychorus import find_and_output_chorus
#
# class extractor(LoggingEventHandler):
#
#     def on_created(self, event):
#         super(LoggingEventHandler, self).on_created(event)
#         what = 'directory' if event.is_directory else 'file'
#         logging.info("Created %s: %s", what, event.src_path)
#         NameExt = event.src_path.split('.')
#         if NameExt[-1] == 'mp3':
#             logging.info("mp3文件, 提取音乐高潮中...")
#             output_path = "."+"".join(NameExt[:-1])+'_high.wav'
#             find_and_output_chorus(event.src_path, output_path, 30)
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S')
#     path = sys.argv[1] if len(sys.argv) > 1 else '.'
#
#     # 生成事件处理器对象
#     event_handler = extractor()
#
#     # 生成监控器对象
#     observer = Observer()
#     # 注册事件处理器
#     observer.schedule(event_handler, path, recursive=True)
#     # 监控器启动——创建线程
#     observer.start()
#
#     # 以下代码是为了保持主线程运行
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#
#     # 主线程任务结束之后，进入阻塞状态，一直等待其他的子线程执行结束之后，主线程再终止
#     observer.join()





import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    # 生成事件处理器对象
    event_handler = LoggingEventHandler()

    # 生成监控器对象
    observer = Observer()
    # 注册事件处理器，配置监控目录
    observer.schedule(event_handler, path, recursive=True)
    # 监控器启动——创建线程
    observer.start()

    # 以下代码是为了保持主线程运行
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    # 主线程任务结束之后，进入阻塞状态，一直等待其他的子线程执行结束之后，主线程再终止
    observer.join()
