import psutil
import time

class SystemMonitor(object):

    def pub_CPU_wide_metric(self):
        cpu_percent = psutil.cpu_percent(interval=0.1)
        with open("../logs/cpu_wide_perc.log", "a+") as f:
            f.write("{}-{}: {}\n".format("CPU_UTILIZATION", time.time(), cpu_percent))
    
    def pub_CPU_per_core_metric(self):
        cpu_percent = psutil.cpu_percent(interval=0.1, percpu=True)
        with open("../logs/cpu_per_core_perc.log", "a+") as f:
            f.write("{}-{}: {}\n".format("CPU_PER_CORE_PERCENTAGE",time.time(), cpu_percent))

    def pub_CPU_stats(self):
        cpu_stats = psutil.cpu_stats()
        curr_time = time.time()
        with open("../logs/cpu_stats.log", "a+") as f:
            for name in cpu_stats._fields:
                value = getattr(cpu_stats, name)
                f.write("{}-{}: {}\n".format(name.upper(), curr_time, value))


    def pub_CPU_wide_freq(self):
        cpu_freq = psutil.cpu_freq()
        curr_time = time.time()
        with open("../logs/cpu_freq.log", "a+") as f:
            for name in cpu_freq._fields:
                value = getattr(cpu_freq, name)
                f.write("{}-{}: {}\n".format(name.upper(), curr_time, value))

    def pub_virt_memory_stats(self):
        mem = psutil.virtual_memory()
        curr_time = time.time()
        with open("../logs/virtual_memory_stats.log", "a+") as f:
            for name in mem._fields:
                value = getattr(mem, name)
                f.write("{}-{}: {}\n".format(name.upper(), curr_time, value))

    # IMPLEMENT SWAP MEMORY STATISTICS

    def pub_disk_usage(self):
        usage = psutil.disk_usage('/')
        curr_time = time.time()
        with open("../logs/disk_usage.log", "a+") as f:
            for name in usage._fields:
                value = getattr(usage, name)
                f.write("{}-{}: {}\n".format(name.upper(), curr_time, value))

    def pub_disk_wide_io_counters(self):
        io_counters = psutil.disk_io_counters()
        curr_time = time.time()
        with open("../logs/disk_io_counters.log", "a+") as f:
            for name in io_counters._fields:
                value = getattr(io_counters, name)
                f.write("{}-{}: {}\n".format(name.upper(), curr_time, value))

    def pub_net_io_counters(self):
        net_io_c = psutil.net_io_counters()
        curr_time = time.time()
        with open("../logs/network_io_counters.log", "a+") as f:
            for name in net_io_c._fields:
                value = getattr(net_io_c, name)
                f.write("{}-{}: {}\n".format(name.upper(), curr_time, value))

    def pub_core_temperature(self):
        sensor_temperature = psutil.sensors_temperatures()
        curr_time = time.time()
        with open("../logs/core_temperature.log", "a+") as f:
            core_temp = sensor_temperature["coretemp"]
            for core in core_temp:
                for name in core._fields:
                    value = getattr(core, name)
                    if isinstance(value, str):
                        if "Package" in value:
                            break
                        else:
                            f.write("{}\n".format(value))
                    else:
                        f.write("{}-{}: {}\n".format(name.upper(), curr_time, value))
    
    def pub_hw_fan_speed(self):
        fans = psutil.sensors_fans()
        curr_time = time.time()
        with open("../logs/fan_speed.log", "a+") as f:
            for k, v in fans.items():
                for fan in v:
                    if fan.label != "":
                        f.write("{}-{}: {}\n".format(fan.label.upper(), curr_time, fan.current))
                    else:
                        f.write("{}-{}: {}\n".format(k.upper(), curr_time, fan.current))

    def publish_all_metrics(self):
        self.pub_CPU_wide_metric()
        self.pub_CPU_per_core_metric()
        self.pub_CPU_stats()
        self.pub_CPU_wide_freq()
        self.pub_virt_memory_stats()
        self.pub_disk_usage()
        self.pub_disk_wide_io_counters()
        self.pub_net_io_counters()
        self.pub_core_temperature()
        self.pub_hw_fan_speed()
        

def main():
    sm = SystemMonitor()
    for x in range(20):
        sm.publish_all_metrics()
        time.sleep(0.1)

if __name__=='__main__':
    main()