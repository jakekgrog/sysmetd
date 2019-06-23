# SysMetD - Distributed System Metrics Monitoring

SysMetD is a distributed system metrics monitoring platform designed to give insight into how a distributed system is performing by analysing and graphing stats on the following parameters:

- Memory
  * Total virtual memory
  * Available virtual memory
  * Virtual memory utilization
  * Virtual memory used
  * Virtual memory free
  * Virtual memory active
  * Virtual memory inactive
  * Virtual memory buffers
  * Virtual memory cached
  * Virtual memory shared
  * Virtual memory slabs
- CPU
  * CPU wide utilization
  * CPU utilization per core
  * CPU wide frequency (current, min, max)
  * CPU temperature per core (current, high, critical)
  * Context switches
  * Interrupts
  * Soft interrupts
  * system calls
- Network
  * Bytes sent
  * bytes received
  * packets sent
  * packets received
  * ERRIN
  * ERROUT
  * DROPIN
  * DROPOUT
- Disk
  * Total disk space
  * Used disk space
  * Free disk space
  * usage percentage
  * Read count
  * Write count
  * Read time
  * Write time
  * Read merged count
  * Write merged count
  * Busy time
- Hardware
  * Fan speed (If H/W sensors are available you will have access to this e.g. CPU fan speed)

__Note:__ Depending on the platform this runs on, you may be restricted on the metrics you have access to.

## Agents & Aggrelyzers

SysMetD agents run on individual machines and log all the above information every 100 milliseconds.

SysMetD aggrelyzers will stream the tail of the log files produced by the agents, aggregate and analyze the data.

You will be able to graph near real-time data.

You will also be able to graph historical data on the following periods:
- 1 second
- 5 seconds
- 30 seconds
- 1 minute
- 5 minute
- 1 hour
- 3 hour
- 12 hour
- 24 hour

# TODO
- [x] Initial agent implementation
- [x] Initial log tail streamer
- [ ] Initial aggrelyzer implementation
- [ ] Initial graphing dashboard
