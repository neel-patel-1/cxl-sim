import sys
from model import cxl_trans

def sum_latencies(trans_list):
    latency = 0 # 0ns
    for trans in trans_list:
        latency += trans.getLatency()
    return latency

def main():
    
    print( "Starting Buffer Simulation...")

    h2dreq = cxl_trans.Trans(100, "H2D", "Request")
    print( sum_latencies([h2dreq]) )


if __name__ == '__main__':
    sys.exit(main())