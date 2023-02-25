import psutil
import time


def print_system_stats():
    while True:
        cpu_percent = psutil.cpu_percent()
        memory_stats = psutil.virtual_memory()
        available_memory = round(memory_stats.available / (1024 * 1024), 2)

        print("CPU Usage: {}%".format(cpu_percent))
        print("Available Memory: {} MB".format(available_memory))

        time.sleep(1)


if __name__ == '__main__':
    print_system_stats()
