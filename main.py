from collections import deque
from dataclasses import dataclass

@dataclass
class Message:
    message_id: str
    sender: str
    receiver: str
    content: str

class DistributedSimulator:
    def __init__(self):
        self.process_ids = ["P1", "P2", "P3", "P4"]
        self.queues = {pid: deque() for pid in self.process_ids}
        self.events = []
        self.next_id = 1

    def log(self, event, details):
        self.events.append(f"{len(self.events) + 1:02d}. {event}: {details}")

    def send(self, sender, receiver, content):
        if sender not in self.queues or receiver not in self.queues:
            print("Invalid process ID. Choose P1, P2, P3 or P4.")
            return
        if sender == receiver:
            print("Sender and receiver must be different.")
            return
        msg = Message(f"M{self.next_id}", sender, receiver, content)
        self.next_id += 1
        self.queues[receiver].append(msg)
        self.log("SEND/DELIVER", f"{sender} -> {receiver} | {msg.message_id}: {content}")
        print(f"Message {msg.message_id} delivered to {receiver}.")

    def broadcast(self, sender, content):
        if sender not in self.queues:
            print("Invalid process ID.")
            return
        for receiver in self.process_ids:
            if receiver != sender:
                self.send(sender, receiver, content)

    def receive(self, pid):
        if pid not in self.queues:
            print("Invalid process ID.")
            return
        if not self.queues[pid]:
            print(f"{pid}: No messages pending.")
            return
        msg = self.queues[pid].popleft()
        self.log("RECEIVE", f"{pid} received {msg.message_id} from {msg.sender}: {msg.content}")
        print(f"{pid} received {msg.message_id} from {msg.sender}: {msg.content}")

    def show_queues(self):
        print("\n--- MESSAGE QUEUES (FIFO) ---")
        for pid, queue in self.queues.items():
            ids = [msg.message_id for msg in queue]
            print(f"{pid}: {ids if ids else 'Empty'}")

    def show_log(self):
        print("\n--- COMMUNICATION EVENT LOG ---")
        if not self.events:
            print("No events yet.")
        for event in self.events:
            print(event)

    def analysis(self):
        delivered = self.next_id - 1
        pending = sum(len(q) for q in self.queues.values())
        print("\n--- COMMUNICATION ANALYSIS ---")
        print(f"Processes: {len(self.process_ids)}")
        print(f"Message copies delivered: {delivered}")
        print(f"Messages still pending: {pending}")
        for pid, queue in self.queues.items():
            print(f"{pid}: {len(queue)} pending message(s)")

def main():
    sim = DistributedSimulator()
    while True:
        print("\n===== DISTRIBUTED MESSAGE-PASSING SIMULATOR =====")
        print("1. Send unicast message")
        print("2. Broadcast message")
        print("3. Receive next message")
        print("4. View message queues")
        print("5. View event log")
        print("6. Communication analysis")
        print("7. Run sample demonstration")
        print("0. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            sender = input("Sender (P1-P4): ").strip().upper()
            receiver = input("Receiver (P1-P4): ").strip().upper()
            content = input("Message: ").strip()
            if content:
                sim.send(sender, receiver, content)
            else:
                print("Message cannot be empty.")
        elif choice == "2":
            sender = input("Sender (P1-P4): ").strip().upper()
            content = input("Broadcast message: ").strip()
            if content:
                sim.broadcast(sender, content)
            else:
                print("Message cannot be empty.")
        elif choice == "3":
            sim.receive(input("Process to receive (P1-P4): ").strip().upper())
        elif choice == "4":
            sim.show_queues()
        elif choice == "5":
            sim.show_log()
        elif choice == "6":
            sim.analysis()
        elif choice == "7":
            sim.send("P1", "P2", "Request: send status")
            sim.send("P2", "P1", "Reply: system ready")
            sim.broadcast("P3", "Meeting starts at 10 AM")
            sim.show_queues()
            sim.show_log()
        elif choice == "0":
            print("Exiting simulator. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
