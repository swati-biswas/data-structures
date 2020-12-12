# python 3

packets_start = []

class Packet():
 def __init__(self, arrived_at, time_to_process):
  self.arrived_at = arrived_at
  self.time_to_process = time_to_process
  self.start_time = arrived_at

class Buffer():
 
 def __init__(self, size):
  self.size = size
  self.buffer = [None]* size
  self.w_pntr = 0
  self.total_time = 0
 
 def increment_pntr(self):
  self.w_pntr = self.w_pntr + 1
  if self.w_pntr == self.size: self.w_pntr = 0

 def processPackets(self, packet):
  w_pntr = self.w_pntr
  buffer = self.buffer
  tt = self.total_time
  if buffer[w_pntr] == None:
   buffer[w_pntr] = packet
   self.increment_pntr()
   
   if packet.arrived_at > tt:
    tt = packet.arrived_at + packet.time_to_process
    packets_start.append(packet.arrived_at)
   else:
    packets_start.append(tt)
    packet.start_time = tt
    tt = tt + packet.time_to_process
  else:
   prev_packet = buffer[w_pntr]
   prev_packet_finish = prev_packet.start_time + prev_packet.time_to_process
   if packet.arrived_at >= prev_packet_finish:
    buffer[w_pntr] = packet
    self.increment_pntr()
    if packet.arrived_at > tt:
     tt = packet.arrived_at + packet.time_to_process
     packets_start.append(packet.arrived_at)
    else:
     packets_start.append(tt)
     packet.start_time = tt
     tt = tt + packet.time_to_process
   else:
    packets_start.append(-1)
  self.total_time = tt
  
def main():
 global packets_start
 
 buffer_size, n_requests = map(int, input().split())
 buffer = Buffer(buffer_size)

 for x in range(n_requests):
  arrived_at, time_to_process = map(int, input().split())
  packet = Packet(arrived_at, time_to_process)
  buffer.processPackets(packet)
 #print(packets_start)
 for p in packets_start:
  print(p)
  
if __name__ == "__main__":
 main()
