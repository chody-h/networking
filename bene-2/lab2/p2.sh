rm -rf outputs/*

python transfer.py -l 0.0 -w 3000 -f "test.txt" > outputs/output1-0.txt
python transfer.py -l 0.1 -w 3000 -f "test.txt" > outputs/output1-1.txt
python transfer.py -l 0.2 -w 3000 -f "test.txt" > outputs/output1-2.txt
python transfer.py -l 0.5 -w 3000 -f "test.txt" > outputs/output1-5.txt
python transfer.py -l 0.0 -w 10000 -f "internet-architecture.pdf" > outputs/output2-0.txt
python transfer.py -l 0.1 -w 10000 -f "internet-architecture.pdf" > outputs/output2-1.txt
python transfer.py -l 0.2 -w 10000 -f "internet-architecture.pdf" > outputs/output2-2.txt
python transfer.py -l 0.5 -w 10000 -f "internet-architecture.pdf" > outputs/output2-5.txt
python transfer.py -w 01000 -f "internet-architecture.pdf" -n "one-hop-100-queue.txt" > outputs/output3-01000.txt
python transfer.py -w 02000 -f "internet-architecture.pdf" -n "one-hop-100-queue.txt" > outputs/output3-02000.txt
python transfer.py -w 05000 -f "internet-architecture.pdf" -n "one-hop-100-queue.txt" > outputs/output3-05000.txt
python transfer.py -w 10000 -f "internet-architecture.pdf" -n "one-hop-100-queue.txt" > outputs/output3-10000.txt
python transfer.py -w 15000 -f "internet-architecture.pdf" -n "one-hop-100-queue.txt" > outputs/output3-15000.txt
python transfer.py -w 20000 -f "internet-architecture.pdf" -n "one-hop-100-queue.txt" > outputs/output3-20000.txt